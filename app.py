import boto3
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# AWS Comprehend Client initialize karo
comprehend = boto3.client('comprehend', region_name='us-east-1',
                          aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

# Function to get sentiment
def analyze_sentiment(text):
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    return response['Sentiment']

# Streamlit frontend setup
st.title("Sentiment Analysis Web App")
user_input = st.text_area("Enter text for sentiment analysis:")

if st.button("Analyze Sentiment"):
    sentiment = analyze_sentiment(user_input)
    st.write(f"Sentiment: {sentiment}")
