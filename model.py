from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import pickle
import pandas as pd
import numpy as np
import re
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')
# nltk.download('omw-1.4')

class SentimentRecommenderModel:

    ROOT_PATH = "Pickles/"
    MODEL_NAME = "xgb.pkl"
    VECTORIZER = "tfidf.pkl"
    RECOMMENDER = "user_final_rating.pkl"
    MAIN_DATA = "data.pkl"

    def __init__(self):
        self.model = pickle.load(open(
            SentimentRecommenderModel.ROOT_PATH + SentimentRecommenderModel.MODEL_NAME, 'rb'
        ))
        self.vectorizer = pd.read_pickle(
            SentimentRecommenderModel.ROOT_PATH + SentimentRecommenderModel.VECTORIZER
        )
        self.user_final_rating = pickle.load(open(
            SentimentRecommenderModel.ROOT_PATH + SentimentRecommenderModel.RECOMMENDER, 'rb'
        ))
        self.clean_data = pickle.load(open(
            SentimentRecommenderModel.ROOT_PATH + SentimentRecommenderModel.MAIN_DATA, 'rb'
        ))
        self.data = pd.read_csv("Dataset/sample30.csv")
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    """
    function to get top 20 product recommendations for the user
    """
    def getRecommendationByUser(self, user):
        recommendations = []
        return list(self.user_final_rating.loc[user].sort_values(ascending=False)[0:20].index)
    
    """
    function to filter the product recommendations using the sentiment model and get 
    the top 5 recommendations
    """
    def getSentimentRecommendations(self, user):
        if(user in self.user_final_rating.index):
            # get the product recommendation using the trained ML model
            recommendations = list(
                self.user_final_rating.loc[user].sort_values(ascending=False)[0:20].index
            )
            filtered_data = self.clean_data[self.clean_data.id.isin(recommendations)]
            X = self.vectorizer.transform(
                filtered_data["Review"].values.astype(str)
            )
            filtered_data["predicted_sentiment"] = self.model.predict(X)
            temp = filtered_data[['id', 'predicted_sentiment']]
            temp_grouped = temp.groupby('id', as_index=False).count()
            temp_grouped['pos_review_count'] = temp_grouped.id.apply(lambda x: temp[(
                temp.id == x) & (temp.predicted_sentiment == 1)
                ]['predicted_sentiment'].count())
            temp_grouped['total_review_count'] = temp_grouped['predicted_sentiment']
            temp_grouped['pos_sentiment_percent'] = np.round(temp_grouped['pos_review_count']/temp_grouped['pos_review_count']*100, 2)
            sorted_products = temp_grouped.sort_values('pos_sentiment_percent', ascending=False)[0:5]
            return pd.merge(self.data, sorted_products, on='id')[['name', 'brand', 'manufacturer', 'pos_sentiment_percent']].drop_duplicates().sort_values(['pos_sentiment_percent', 'name'], ascending=[False, True])
        else:
            print(f"User name {user} doesn't exist")
            return None
        
    """
    function to preprocess the text before it's sent to ML model
    """
    def preprocess_text(self, text):

        # cleaning the review text (lower, remove punctuation, numericals and whitespaces)
        text = text.lower().strip()
        text = re.sub("\[\s*\w*\s*]", "", text)
        dictionary = "abc".maketrans('', '', string.punctuation)
        text = text.translate(dictionary)
        text = re.sub("\S*\d\S*", "", text)

        # remove stop-words and convert it to lemma
        text = self.lemma_text(text)
        return text
    
    """
    function to get the pos tag to derive the lemma form
    """
    def get_wordnet_pos(self, tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV    
        else:
            return wordnet.NOUN
        
    """
    function to remove the stop words from the text
    """
    def remove_stopword(self, text):
        words = [word for word in text.split() if word.isalpha() and word not in self.stop_words]
        return " ".join(words)
    
    """
    function to derive the base lemma form of the text using the pos tag
    """
    def lemma_text(self, text):
        word_pos_tags = nltk.pos_tag(word_tokenize(
            self.remove_stopword(text)
        ))
        # Map the position tag and lemmatize the word/token
        words = [self.lemmatizer.lemmatize(tag[0], self.get_wordnet_pos(tag[1])) for idx, tag in enumerate(word_pos_tags)]
        return " ".join(words)
    
    """
    function to classify the sentiment to 1/0 - positive or nagative - using the trained ML model
    """
    def classify_sentiment(self, review_text):
        review_text = self.preprocess_text(review_text)
        X = self.vectorizer.transform([review_text])
        y_pred = self.model.predict(X)
        return y_pred
    
