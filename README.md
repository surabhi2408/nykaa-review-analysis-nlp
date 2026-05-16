# 💄 Nykaa Review Analysis NLP

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FF9D00?style=for-the-badge&logo=huggingface&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

An **End-to-End Natural Language Processing (NLP)** pipeline built to intelligently analyze cosmetic product reviews from Indian consumers on Nykaa. This project goes beyond basic sentiment by extracting deep, actionable insights such as aspect-based opinion mining and review usefulness prediction.

## ✨ Key Features
- **Sentiment Analysis**: Evaluates customer reviews to determine whether the sentiment is positive, negative, or neutral using fine-tuned models.
- **Aspect-Based Opinion Mining**: Breaks down reviews to identify specific aspects of products (e.g., *fragrance, texture, packaging, price*) and determines the sentiment for each individual aspect.
- **Review Usefulness Prediction**: Predicts whether a review will be helpful to other consumers, filtering out spam or low-quality feedback.
- **Web Scraping**: Built-in Selenium scripts to autonomously gather large datasets of real consumer reviews.
- **Interactive Dashboard**: A beautiful frontend built with Streamlit to visualize the insights and explore the NLP model's predictions in real-time.

---

## 🧠 Tech Stack & Models
- **Core ML Frameworks**: PyTorch, Scikit-Learn
- **Deep Learning / Transformers**: HuggingFace `transformers` (BERT) for contextual embeddings and sequence classification.
- **Lexicon-Based NLP**: `vaderSentiment` and `nltk` for rule-based sentiment scoring.
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency) for traditional ML baseline models.
- **Web App**: Streamlit
- **Data Gathering**: Selenium, Pandas

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed. 

### 2. Installation
Clone the repository:
```bash
git clone https://github.com/surabhi2408/nykaa-review-analysis-nlp.git
cd nykaa-review-analysis-nlp
```

Install the required Python packages:
```bash
pip install -r nykaa-review-analysis-nlp/requirements.txt
```

### 3. Usage
*(Note: Instructions will vary depending on your specific scripts inside the `src/` and `notebooks/` folders).*
To run the interactive Streamlit dashboard:
```bash
streamlit run nykaa-review-analysis-nlp/src/app.py 
```

---

## 📂 Project Structure
- `nykaa-review-analysis-nlp/notebooks/`: Contains Jupyter notebooks for EDA, model training, and experimentation.
- `nykaa-review-analysis-nlp/src/`: Contains the production-ready source code, scraping scripts, and Streamlit app.
- `nykaa-review-analysis-nlp/requirements.txt`: Python dependencies.

---
*Developed for deep NLP research into consumer behavior in the Indian cosmetics market.*
