import json
from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text and categorizes it.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Extract only polarity

    # Categorizing sentiment based on polarity range
    if -1 <= polarity < -0.3:
        sentiment_category = "Disturbed"
    elif -0.3 <= polarity <= 0.3:
        sentiment_category = "Neutral"
    elif 0.3 < polarity <= 1:
        sentiment_category = "Cheerful"

    return polarity, sentiment_category  # Return both polarity and category
