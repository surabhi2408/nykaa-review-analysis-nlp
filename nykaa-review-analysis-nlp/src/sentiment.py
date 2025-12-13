from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline

vader = SentimentIntensityAnalyzer()
bert = pipeline("sentiment-analysis",
                model="distilbert-base-uncased-finetuned-sst-2-english")

def vader_sentiment(text):
    return vader.polarity_scores(text)["compound"]

def bert_sentiment(text):
    return bert(text)[0]["label"]
