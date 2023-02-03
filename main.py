#this will be the run file
#file created on 2/2/23
#first commit from replit
#testing to see if it works
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
#from nltk.tokenize import word_tokenize - not needed bc of array? Does 'tokenize' mean to create a an array of the stings given as inputs?

strings = [
    "This tool is awesome. it totally works",
    "This tool sucks. It's a lot of work to build.",
    "This tool is meh."
]

# Create a sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

# Process the data in the strings array. Processing one string at a time.
for string in strings:
    # Get the sentiment score of the string
    sentiment_score = sentiment_analyzer.polarity_scores(string)["compound"]

    # Determine the sentiment label based on the score
    if sentiment_score >= 0.05:
        sentiment = "Positive"
    elif sentiment_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Print the sentiment score and label
    print("String:", string)
    print("Sentiment score:", sentiment_score)
    print("Sentiment:", sentiment)
    print("")