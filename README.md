# 💼 Sentiment-Based Product Recommendation System

A Machine Learning-powered web application that recommends products to users based on sentiment analysis of product reviews. This project integrates Natural Language Processing (NLP) techniques to understand user feedback and leverages collaborative filtering for personalized recommendations.

![Heroku](https://img.shields.io/badge/Deployed-Heroku-7952B3?logo=heroku\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📌 Problem Statement

E-commerce allows businesses to sell products online without the need for face-to-face customer interaction. Popular platforms like Amazon, Flipkart, Myntra, Paytm, and Snapdeal have set strong examples in this space. Ebuss is a growing e-commerce company offering a wide range of products, including household essentials, books, healthcare items, and electronics. With its expanding market presence, Ebuss aims to compete with these established players. To do so, it must leverage advanced technology and grow rapidly to become a major industry leader.

---

## 📌 Features

* 📊 **Sentiment Analysis** using TextBlob
* 🤝 **Collaborative Filtering** using cosine similarity
* 🧠 NLP preprocessing (stopword removal, lemmatization, etc.)
* 🔍 Review-based product rating analysis
* 🌐 Flask-based Web Interface
* 🚀 Deployed on **Heroku** using **Gunicorn**

---

## 📌 Solution

* **Github:** https://github.com/RavishankarDuMCA10/Sentiment-Based-Product-Recommendation-System
* **Heroku (Live Application):** https://sentimentbasedproductrecommend-4d986cccbd68.herokuapp.com/

---

## 📂 Project Structure

```
├── app/
│   ├── static/
│   ├── templates/
│   ├── main.py             # Flask routes and app logic
│   ├── model.pkl           # Pretrained recommendation model
│   └── utils.py            # Preprocessing and sentiment logic
├── Sentiment Based Product Recommendation System.ipynb
├── requirements.txt
├── runtime.txt
├── Procfile
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 🔧 Prerequisites

* Python 3.11+
* `pip`
* `virtualenv` (optional but recommended)

### 🧪 Create a Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 How It Works

1. The system analyzes product reviews using **TextBlob** for polarity scoring.
2. Reviews with high polarity are given more weight in recommendation.
3. A **cosine similarity matrix** is used to identify similar products.
4. Recommendations are tailored using **user sentiment trends**.

---

## 🚀 Run Locally

```bash
gunicorn app:app
```

Then open your browser at `http://localhost:8000`.

---

## ☁️ Deploying to Heroku

### Step-by-step

1. **Login to Heroku**:

   ```bash
   heroku login
   ```

2. **Create a Heroku app**:

   ```bash
   heroku create sentiment-based-recommender
   ```

3. **Add a buildpack (if needed)**:

   ```bash
   heroku buildpacks:set heroku/python
   ```

4. **Deploy your app**:

   ```bash
   git add .
   git commit -m "Initial deploy"
   git push heroku main
   ```

5. **Open the app**:

   ```bash
   heroku open
   ```

> Make sure you have `Procfile` and `runtime.txt` in the root directory for Heroku to detect it as a Python app.

---

## 📝 Example

> Search top 5 recommended products using username like `"08dallas"` and get real-time recommendations based on positively reviewed items.

---

## 📟 Requirements

```txt
Flask
nltk
numpy==1.24.4
pandas==1.5.3
gunicorn
scikit-learn
xgboost==1.7.6
```
(Ensure these are listed in your `requirements.txt`.)

---
## Technologies Used
- Numpy - version '1.24.4'
- Pandas - version '1.5.3'
- Seaborn version: 0.12.2
- Matplotlib version: 3.7.1
- Imbalanced-learn (imblearn) version: 0.12.3
- NLTK version: 3.9.1
- PIL (Pillow) version: 9.4.0
- WordCloud version: 1.9.4
- Scikit-learn (sklearn) version: 1.3.0
- Python version (for pprint, pickle, pathlib): 3.11.4
- Scipy version: 1.15.3
- XGBoost version: 1.7.6



---

## 🧠 Notebook Preview

The Jupyter Notebook (`Sentiment Based Product Recommendation System.ipynb`) provides an end-to-end demonstration of:

* Dataset loading
* Text preprocessing
* Sentiment scoring
* Similarity matrix generation
* Recommendation output

Useful for experiments and understanding the model pipeline.

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 🙌 Acknowledgments

* [TextBlob](https://textblob.readthedocs.io/)
* [Heroku](https://www.heroku.com/)
* [Flask](https://flask.palletsprojects.com/)

---

## 📬 Contact

For issues or suggestions, feel free to reach out on [LinkedIn](https://www.linkedin.com/in/ravi-shankar-k-45a77224/).
