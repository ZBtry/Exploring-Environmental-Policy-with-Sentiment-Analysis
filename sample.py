"""
From Google.
"""

from textblob import TextBlob

text = "TextBlob is an amazing library for sentiment analysis, it's so easy to use!"
blob = TextBlob(text)

# Get polarity and subjectivity
sentiment_polarity = blob.sentiment.polarity
sentiment_subjectivity = blob.sentiment.subjectivity

print(f"Polarity: {sentiment_polarity}")
print(f"Subjectivity: {sentiment_subjectivity}")

# Interpret the polarity score
if sentiment_polarity > 0:
    print("Sentiment: Positive")
elif sentiment_polarity < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")