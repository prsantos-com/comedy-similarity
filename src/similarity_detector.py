import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the model
print("Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load jokes
print("Loading jokes...")
with open('data/jokes.json', 'r') as f:
    jokes = json.load(f)

# Extract jokes texts
joke_texts = [j['joke'] for j in jokes]

# Generate embeddings
print("Generating embeddings...")
embeddings = model.encode(joke_texts)

# Compute similarity matrix
print("Computing similarities...")
similarity_matrix = cosine_similarity(embeddings)

# Find similar jokes
print("\n=== Similar Jokes ===\n")
for i, joke in enumerate(jokes):
    print(f"Joke: {joke['joke']}")
    print(f"By: {joke['comedian']} ({joke['year']})")

    # Get similarity scores
    scores = similarity_matrix[i]

    # Get top 3 most similar (excluding itself)
    similar_indices = np.argsort(scores)[::-1][1:4]

    print("\nMost similar jokes (different comedians only):")
    for idx in similar_indices:
        similar_joke = jokes[idx]
        # Only show if different comedian AND similarity > 0.3
        if scores[idx] > 0.3 and similar_joke['comedian'] != joke['comedian']:
            similar_joke = jokes[idx]
            print(f"  - Similarity: {scores[idx]:.2f}")
            print(f"    {similar_joke['joke']}")
            print(f"    By: {similar_joke['comedian']} ({similar_joke['year']})")

    print("\n" + "="*80 + "\n")

# Find top cross-comedian similarities
print("\n" + "="*80)
print("=== TOP CROSS-COMEDIAN SIMILARITIES ===")
print("="*80 + "\n")

cross_similarities = []
for i in range(len(jokes)):
    for j in range(i+1, len(jokes)):
        if jokes[i]['comedian'] != jokes[j]['comedian']:
            score = similarity_matrix[i][j]
            if score > 0.3:
                cross_similarities.append({
                    'score': score,
                    'joke1': jokes[i],
                    'joke2': jokes[j]
                })

# Sort by similarity score (highest first)
cross_similarities.sort(key=lambda x: x['score'], reverse=True)

# Show top 10
print(f"Found {len(cross_similarities)} cross-comedian similarities above 0.3\n")
print("TOP 10:\n")

for i, item in enumerate(cross_similarities[:10], 1):
    print(f"{i}. Similarity: {item['score']:.3f}")
    print(f"   Joke 1: {item['joke1']['comedian']} ({item['joke1']['year']}): \"{item['joke1']['joke'][:80]}...\"")
    print(f"   Joke 2: {item['joke2']['comedian']} ({item['joke2']['year']}): \"{item['joke2']['joke'][:80]}...\"")
    print()

print(f"=== THRESHOLD ANALYSIS ===\n")

thresholds = [0.35, 0.40, 0.42, 0.45, 0.48, 0.50]

for threshold in thresholds:
    matches = [x for x in cross_similarities if x['score'] >= threshold]
    print(f"Threshold {threshold}: {len(matches)} pairs")

    if len(matches) > 0 and len(matches) <= 5:
        for item in matches:
            print(f"  {item['score']:.3f}: {item['joke1']['comedian']} vs {item['joke2']['comedian']}")
        print()

print("\n=== OBSERVATION ===")
print("Clear gap between 0.40-0.44 (no pairs)")
print("Top 2 pairs: 0.45-0.46")
print("Next cluster: 0.35-0.39 (5 pairs)")
print("\nRecommend threshold: 0.40 (captures top 2, filters rest)")

print("\n=== TEMPORAL ANALYSIS: HIGH SIMILARITY PAIRS ===")

# Focus on top 2 pairs (0.45+)
high_pairs = [x for x in cross_similarities if x['score'] >= 0.40]

for item in high_pairs:
    joke1 = item['joke1']
    joke2 = item['joke2']
    score = item['score']

    # Who performed first?
    if joke1['year'] < joke2['year']:
        earlier, later = joke1, joke2
    else:
        earlier, later = joke2, joke1

    years_apart = abs(joke1['year'] - joke2['year'])

    print(f"Score: {score:.3f}")
    print(f"  Earlier: {earlier['comedian']} ({earlier['year']})")
    print(f"  Later:   {later['comedian']} ({later['year']})")
    print(f"  Time gap: {years_apart} years")

    # Flag if suspicious
    if score >= 0.45 and years_apart >= 5:
        print(f"  ⚠️  INVESTIGATE: Later comedian ({later['comedian']}) "
              f"has high similarity to earlier comedian ({earlier['comedian']})")
    
    print()