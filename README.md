🛡️ Cyberbullying Tweet Detection

Detecting cyberbullying is essential in today's digital age where social media platforms are frequently used for harassment and abuse. This project leverages Natural Language Processing (NLP) and Machine Learning (ML) to automatically classify tweets as cyberbullying or non-cyberbullying, based on their textual content.

📌 Features
Preprocessing of tweet text (stopword removal, stemming, lemmatization)

Feature extraction using TF-IDF

Model training using:

Decision Tree (achieved 97.92% accuracy)

Random Forest

K-Nearest Neighbors

Support Vector Machine

Performance evaluation (confusion matrix, accuracy, precision, recall, F1-score)

Model serialization using joblib for deployment-ready predictions

🧠 Technologies Used
Python 3.x

Libraries: pandas, numpy, sklearn, nltk, matplotlib, seaborn

Jupyter Notebook for EDA and model training

joblib for saving trained models

📊 Dataset
Source: Kaggle – Cyberbullying Tweets Dataset

Content: ~47,000 labeled tweets

Labels: cyberbullying, non-cyberbullying

🚀 Getting Started

Clone the repository
git clone https://github.com/rsiliveri14/Cyberbullying-tweet-detection.git
cd Cyberbullying-tweet-detection

Install dependencies
pip install -r requirements.txt

Run the Jupyter Notebook
jupyter notebook Notebooks/Cyberbullying_Detection.ipynb

Run prediction via script
python main.py


🧪 Model Performance

| Model         | Accuracy   | Precision | Recall | F1-Score |
| ------------- | ---------- | --------- | ------ | -------- |
| Decision Tree | **97.92%** | 97%       | 98%    | 97%      |
| Random Forest | 96.41%     | 95%       | 96%    | 95%      |
| SVM           | 93.85%     | 92%       | 94%    | 93%      |
| KNN           | 91.26%     | 90%       | 91%    | 90%      |

