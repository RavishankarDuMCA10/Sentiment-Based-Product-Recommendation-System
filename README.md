```markdown
# 🛍️ Sentiment-Based Product Recommendation System

A Machine Learning-powered web application that recommends products to users based on sentiment analysis of product reviews. This project integrates Natural Language Processing (NLP) techniques to understand user feedback and leverages collaborative filtering for personalized recommendations.

![Heroku](https://img.shields.io/badge/Deployed-Heroku-7952B3?logo=heroku&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📌 Features

- 📊 **Sentiment Analysis** using TextBlob
- 🤝 **Collaborative Filtering** using cosine similarity
- 🧠 NLP preprocessing (stopword removal, lemmatization, etc.)
- 🔍 Review-based product rating analysis
- 🌐 Flask-based Web Interface
- 🚀 Deployed on **Heroku** using **Gunicorn**

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

````

---

## ⚙️ Installation & Setup

### 🔧 Prerequisites

- Python 3.11+
- `pip`
- `virtualenv` (optional but recommended)

### 🧪 Create a Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
````

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
python app/main.py
```

Then open your browser at `http://localhost:5000`.

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

> Search for a product like `"Fitbit Charge 3"` and get real-time recommendations based on positively reviewed items.

---

## 🧾 Requirements

```txt
flask
gunicorn
pandas
numpy
scikit-learn
textblob
```

(Ensure these are listed in your `requirements.txt`.)

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

For issues or suggestions, feel free to open an [issue](https://github.com/yourusername/repo-name/issues) or reach out on [LinkedIn](https://linkedin.com/in/your-profile).

```

---

Would you like this to be tailored with:

- Your actual Heroku app URL?
- GitHub repo name and link?
- Your name or organization in the footer?

I can personalize that for you too.
```
