# Comedy Similarity Detection

This a project that uses semantic similarity detection for jokes across various stand-up comedians to spot potential
cases of joke stealing. Each joke shows who said it, where they said, and when they said it. If there are jokes that are similar
we can look at when they said to determine who originally came up with the joke. It uses embeddings and cosine similarity and can generalize to any creative written content.

## Current Status

- Dataset: 100 jokes from 7 comedians
- Similarity threshold: 0.40
- Top similarity pairs identified

## Dataset

100 jokes from 7 comedians:

- Mitch Hedberg: 10 jokes
- Rodney Dangerfield: 10 jokes
- Jim Gaffigan: 10 jokes
- Chris Rock: 10 jokes
- Dave Chappelle: 10 jokes
- Mark Normand: 25 jokes
- Jerry Seinfeld: 25 jokes

## Key Findings

### Topic vs Style Weight

- Similar one-liner comedians styles clustered together for like Hedberg and Dangerfield. Similar story-telling clustered together like Rock and Chappelle. Although, topics by these comedians were also somewhat similar.
- The highest similarity score was from two completely different styles with Hedberg and Chappelle, but because their joke was centered around bananas, they ranked higher in similarity.
- Topics and tone seems to make jokes similar. For low similarity, it's usually just a similar word.

### Optimal Threshold

When testing different thresholds, `0.40` is optimal, because there's a clear gap between 0.40 and 0.44. Above 0.44, the topics were more similar regardless of style while the ones below 0.40 were had topics that could be related, but otherwise different jokes. For example, two jokes that had the word "mother" in it, but one was a one-liner and the other was a long story. Or another pair that similar words like "lady" and "woman", but were otherwise different jokes altogether.

## Dataset Evolution

### Initial Dataset (50 jokes, Week 1)

- Mitch Hedberg: 10 jokes
- Rodney Dangerfield: 10 jokes
- Jim Gaffigan: 10 jokes
- Chris Rock: 10 jokes
- Dave Chappelle: 10 jokes

#### Highest Cross-Comedian Similarities

1. Score: 0.46 - Mitch Hedberg vs Dave Chappelle
   - Why similar: The jokes had the same topic of bananas

2. Score: 0.45 - Mitch Hedberg vs Rodney Dangerfield
   - Why similar: The jokes had the same initial opening words and general topic of family.

3. Score: 0.365 - Mitch Hedberg vs Jim Gaffigan
   - Why similar: Seems to be centered around the bananas, cereal, and monkeypox

4. Score: 0.365 - Jim Gaffigan vs Chris Rock
   - Why similar: The topic of parenthood

#### Top 2 Pairs Analysis

**1. Score: 0.46 - Hedberg vs Chappelle**

**Jokes:**

- Hedberg (1999): "My friend asked me if I wanted a frozen banana, I said 'No, but I want a regular banana later, so...yeah'."
- Chappelle (2017): "You know, I was in Santa Fe the other night, and a motherfucker threw a banana peel at me. Yeah, that didn't feel so good. Of course, it was a white person. Not to indict the whites, I'm just saying. Not to profile. And then, not only did he throw a banana peel at me, but, uh, it was premeditated. You could tell. You could tell, the peel was too brown. You know what I mean? You didn't eat that banana recently, motherfucker. You had that shit waiting on me."

**Analysis:**

Totally different banana jokes. Hedberg talks about wanting bananas. Chappelle talks about getting a banana peel thrown at him. I believe the focus on bananas is what drove the high similarity, even though they have completely different styles.

**2. Score: 0.45 - Hedberg vs Dangerfield (0.45)**

**Jokes:**

- Hedberg (2003): "When I was a boy, I laid in my twin-sized bed and wondered where my brother was."
- Dangerfield (1980): "When I was a kid my parents moved a lot, but I always found them."

**Analysis:**

Both jokes have the same setup. They both say, "When I was a boy/kid" and they are both one-liners. I would say this is a class of jokes about childhood, but both these jokes are a play on words. The entirety of the joke revolves around the topic of family probably drove up the similarity.

### False Positive

An interesting false positive appeared when comparing a banana joke and a monkeypox joke. The similarity may have come from monkeys eating bananas, or cereal and bananas, but otherwise, it was a completely unrelated joke and shouldn't have had that high of similarity score even though it was on the low side.

## Overall Insights

1. Embeddings do look at structure, but rank higher with same topics or word usage to indicate similar topics.
2. Comedy similarity is hard, because of word play that's sometimes involved, so if you get a similar topic, the joke can still be completely different.

## Technical Details

- Embedding model: sentence-transformers (all-MiniLM-L6-v2)
- Similarity metric: Cosine similarity
- Threshold: 0.3+ for reporting

## Next Steps

- Expand dataset to 100+ jokes

## Limitations & Future Work

- Simple similarity threshold won't work for all cases
- May need to combine topic similarity + structural similarity for better detection
- Need more joke variation to get a clearly picture of performance and some examples of actual stolen jokes

## How to Run

Install Python 3.3 or later, create your virtual environment then run the following:

```bash
source venv/Scripts/activate
pip install -r requirements.txt
python src/similarity_detector.py
```
