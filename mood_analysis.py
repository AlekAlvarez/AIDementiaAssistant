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

def read_file(file_path):
    """
    Reads text from a file.
    """
    with open(file_path, 'r') as file:
        return file.read()

def save_to_json(data, file_name):
    """
    Saves data to a JSON file.
    """
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage
file_path = 'transcribed_text.txt'  # Change this to your text file path
json_output_path = 'mood_analysis.json'  # Output JSON file

# Read text from the file
text_from_file = read_file(file_path)

# Get sentiment polarity and category
polarity, sentiment_category = analyze_sentiment(text_from_file)

# Save to JSON
mood_data = {
    "polarity": polarity,
    "sentiment": sentiment_category
}
save_to_json(mood_data, json_output_path)

print(f"Sentiment analysis saved to {json_output_path}")
