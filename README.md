# SMS Spam Classification (Streamlit)

A simple SMS/Email spam classifier using NLTK preprocessing and a scikit-learn model, served with Streamlit.

## Project structure
- `app.py` – Streamlit app
- `modle.pkl` – trained classifier
- `vectorizer.pkl` – TF-IDF vectorizer
- `requirements.txt` – runtime dependencies
- `.gitignore` – ignores venv/IDE/caches

## Run locally
```bash
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
streamlit run app.py
```

## Deploy to Streamlit Community Cloud
1. Push this repo to GitHub.
2. Go to https://share.streamlit.io → New app → Select this repo.
3. Main file path: `app.py`.
4. Deploy. The app will auto-download NLTK `punkt` and `stopwords` on first run.

## Notes
- If you change model/vectorizer filenames, update the paths in `app.py`.
- Keep large datasets out of the repo or use Git LFS.
