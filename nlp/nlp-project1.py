import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Step 1: Download necessary NLTK resources
nltk.download('vader_lexicon')

# Step 2: Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Step 3: Analyze sentiment of example text
text = "I love programming in Python! It's amazing and fun."
scores = sia.polarity_scores(text)
print(scores)
