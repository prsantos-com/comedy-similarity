# Comedy Similarity Detection

This is a project that uses semantic similarity detection for jokes across various stand-up comedians to spot potential
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

### Topic vs Style Weight (50 jokes)

- Similar one-liner comedians styles clustered together for like Hedberg and Dangerfield. Similar story-telling clustered together like Rock and Chappelle. Although, topics by these comedians were also somewhat similar.
- The highest similarity score was from two completely different styles with Hedberg and Chappelle, but because their joke was centered around bananas, they ranked higher in similarity.
- Topics and tone seems to make jokes similar. For low similarity, it's usually just a similar word.

### Topic vs Style Weight (100 jokes)

- As similarity ranking got higher with a larger joke set, it became clear that structure doesn't matter that much, since higher rankings could be a one-liner vs story telling or observational humor.

### Optimal Threshold (50 jokes)

When testing different thresholds, `0.40` is optimal, because there's a clear gap between 0.40 and 0.44. Above 0.44, the topics were more similar regardless of style while the ones below 0.40 were had topics that could be related, but otherwise different jokes. For example, two jokes that had the word "mother" in it, but one was a one-liner and the other was a long story. Or another pair that similar words like "lady" and "woman", but were otherwise different jokes altogether.

### Optimal Threshold (100 jokes)

Reviewing the `0.40` threshold and the similarity of the 17 joke pairs below are definitely noise. They're jokes with one similar word or words that might be together in the same sentence. The 12 joke pairs above the `0.40` threshold have topics that are more similar and not just based on words. As the dataset grew it became more apparent that a threshold of `0.45` makes more sense for a closer look, since the jokes become closer in that the joke topics are more similar and the semantic meaning of the joke is closer. With a smaller set, `0.40` makes more sense and it is definitely a decent baseline threshold. I would recommend `0.45` for higher value detection, and `0.40` for starting similarity exploration.

## Dataset Evolution

### Initial Dataset (50 jokes, Week 1)

- Mitch Hedberg: 10 jokes
- Rodney Dangerfield: 10 jokes
- Jim Gaffigan: 10 jokes
- Chris Rock: 10 jokes
- Dave Chappelle: 10 jokes

#### Highest Cross-Comedian Similarities

1. Score: 0.462 - Mitch Hedberg vs Dave Chappelle
   - Why similar: The jokes had the same topic of bananas

2. Score: 0.454 - Mitch Hedberg vs Rodney Dangerfield
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

**2. Score: 0.45 - Hedberg vs Dangerfield**

**Jokes:**

- Hedberg (2003): "When I was a boy, I laid in my twin-sized bed and wondered where my brother was."
- Dangerfield (1980): "When I was a kid my parents moved a lot, but I always found them."

**Analysis:**

Both jokes have the same setup. They both say, "When I was a boy/kid" and they are both one-liners. I would say this is a class of jokes about childhood, but both these jokes are a play on words. The entirety of the joke revolves around the topic of family probably drove up the similarity.

### Expanded Dataset (100 jokes, week 2)

- Added Mark Normand and Jerry Seinfeld with 25 jokes each

#### Highest Cross-Comedian Similarities

1. Score: 0.592 - Dave Chappelle vs Jerry Seinfeld
   - Why similar: The jokes talk about commercials. Once again Chappelle mentions the word commercial multiple times.

2. Score: 0.521 - Mitch Hedberg vs Mark Normand
   - Why similar: Both jokes are talk about drugs and use it in the past tense.

3. Score: 0.469 - Rodney Dangerfield vs Mark Normand
   - Why similar: Seems to be similar around talking about themselves and being self-deprecating.

4. Score: 0.462 - Mitch Hedberg vs Dave Chappelle
   - Why similar: The jokes had the same topic of bananas

#### Top 2 Pairs Analysis

**1. Score: 0.592 - Chappelle vs Seinfeld**

**Jokes:**

- Chappelle (1998): "Is it me, or do commercials have nothing to do with the products anymore? You dig? I don't even know what a fucking commercial is about until the end. Every one is a surprise nowadays. You seen that commercial where the lady got the black eye? This lady comes on TV with a black eye, she's crying, she's like, 'I smoke crack. And my husband beats me.' And then a voice came on and said, 'Got milk?'"
- Seinfeld (1985): "They have the 'new and improved' commercials. If it was so new and improved, why wasn't it that way in the first place?"

**Analysis:**

These jokes are completely different styles. The similarity is driven by the topic of commercials and probably drawn close due to both jokes having questions in them.
The ranking shouldn't have been that high.

**2. Score: 0.521 - Hedberg vs Normand**

**Jokes:**

- Hedberg (1999): "I used to do drugs. I still do, but I used to, too."
- Normand (2023): "When I was younger, everybody smoked cigarettes when they drank. That's over. Anybody still rippin' butts? ... Now smoking's kinda shameful. Weed used to be a drug, used to put you in jail. Now weed got its medical degree and turned its life around. Those two completely traded places."

**Analysis:**

Once again, a different style, one-liner versus observational. The topic of drugs overlaps and both sentences use the phrase "used to" repeatedly, which drives up the similarity,
even though they're both completely different jokes. One is word play and the other is anthropomorphizing marijuana.

#### Mark Normand Analysis

- Mark Normand appeared in the 6 of the top 10 similarity rankings.
- He did have more overall jokes, and half of his jokes in the top 10 were with Chapelle. The other were with Seinfield, Hedberg, and Dangerfield.
- You might be able to make an argument that Normand is well rounded in his joke topics

### False Positive

An interesting false positive appeared when comparing a banana joke and a monkeypox joke. The similarity may have come from monkeys eating bananas, or cereal and bananas, but otherwise, it was a completely unrelated joke and shouldn't have had that high of similarity score even though it was on the low side.

## Overall Insights

1. Embeddings do look at structure, but rank much higher with same topics or word usage to indicate similar topics. We see this when a one-liner can rank high with observational humor.
2. Comedy similarity is hard, because of word play that's sometimes involved, so if you get a similar topic, the joke can still be completely different.
3. For comedy, we want at least a `0.40` threshold, but `0.45` would most likely be better to find jokes that might actually be similar
4. Given the Mark Normand frequency in the top 10, it's possible that given enough data, you could put in a set of jokes of a comedian to determine how well-rounded they are in the topic diversification based on how many different comedians they match with a high similarity.

## How to Use

Install Python 3.8 or later, create your virtual environment then run the following:

```bash
source venv/Scripts/activate
pip install -r requirements.txt
```

### Run Full Analysis

Analyze the complete 100 joke set and see cross-comedian similarities:

```bash
python src/similarity_detector.py
```

### Check a Single Joke

Check if a joke you provide is similar to any jokes in the dataset:

```bash
python src/similarity_detector.py "What's red and bad for your teeth? A brick."
```

Jokes scoring `≥0.45` are flagged as suspicious (potential plagiarism).

## Technical Details

- Embedding model: sentence-transformers (all-MiniLM-L6-v2)
- Similarity metric: Cosine similarity
- Threshold: **0.45 (recommended)** for plagiarism detection
  - 0.40: Baseline filtering (12 pairs, topic-based similarity)
  - 0.30: Initial reporting (all similarities)

## Limitations

- Simple similarity threshold won't work for all cases
- May need to combine topic similarity + structural similarity for better detection
- Need more joke variation to get a clearly picture of performance and some examples of actual stolen jokes

## Next Steps

- Test with AI-generated jokes
- Add structural similarity analysis (beyond semantic embeddings)
