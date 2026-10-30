# Sentiment Analysis

A Streamlit app that classifies product reviews as Positive, Neutral, or Negative
using the saved scikit-learn model.

## Run locally

From this directory, install the dependencies and start the app:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Then open `http://localhost:8501`.

## Deploy to Streamlit Community Cloud

1. Push this project to a GitHub repository. Include `app.py`,
   `requirements.txt`, and `sentiment_analysis_model.pkl`.
2. Sign in at [share.streamlit.io](https://share.streamlit.io/) and connect
   your GitHub account.
3. Choose **Create app**, select the repository and branch, and set the main
   file path to `app.py`.
4. Choose **Deploy**. Streamlit Community Cloud will build the app and provide
   a public URL in the form `https://<app-name>.streamlit.app`.

Keep the model file in the repository root beside `app.py`; the app loads it
relative to its own file location.
