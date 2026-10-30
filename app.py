from pathlib import Path

import streamlit as st
import joblib


MODEL_PATH = Path(__file__).resolve().parent / "sentiment_analysis_model.pkl"


st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="📱",
    layout="centered",
)


@st.cache_resource
def load_model():
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}. "
            "Include sentiment_analysis_model.pkl in the deployed app."
        )
    return joblib.load(MODEL_PATH)


model = load_model()


def predict_sentiment(text):
    return model.predict([text])[0]


st.title("📱 Product Review Sentiment Analyzer")

st.write(
    "Enter a product review below and the machine learning "
    "model will classify its sentiment as Positive, Neutral, or Negative."
)

st.divider()

review = st.text_area(
    "Enter your review:",
    placeholder="Example: The phone has excellent battery life and a great camera...",
    height=180,
)

if st.button("🔍 Analyze Sentiment", use_container_width=True):
    if not review.strip():
        st.warning("⚠️ Please enter a review before analyzing.")
    else:
        prediction = predict_sentiment(review)

        st.subheader("Prediction")

        if prediction == "Positive":
            st.success("😊 Positive Sentiment")
        elif prediction == "Negative":
            st.error("😞 Negative Sentiment")
        else:
            st.info("😐 Neutral Sentiment")

        st.subheader("Your Review")
        st.write(review)

st.divider()

st.subheader("About the Model")

st.write(
    """
This sentiment analysis system uses a machine learning pipeline
consisting of:

• Word-level TF-IDF features  
• Character-level TF-IDF features  
• Linear Support Vector Machine (SVM)

The model was trained on product reviews and classifies reviews
into three sentiment categories: Negative, Neutral, and Positive.
"""
)

st.caption("NLP Sentiment Analysis Project | Word + Character TF-IDF + Linear SVM")
