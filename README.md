# Automated_News_Classification_System

Overview
This project aims to build a news classification system using Natural Language Processing (NLP) techniques. The system extracts news articles from selected websites, preprocesses the data, and employs machine learning models to classify articles into various topics such as sports, business, politics, and weather.

Project Structure
Web Scraping: Utilizes web scraping tools like BeautifulSoup and Selenium to collect news articles from diverse sources, including BBC, The Hindu, Times Now, and CNN.

Data Cleaning and Preprocessing: Cleans and preprocesses the data by removing irrelevant information, tokenizing text, removing stop words, and applying lemmatization or stemming.

Text Representation: Converts the text data into a numerical format suitable for machine learning models, using techniques like TF-IDF or word embeddings such as Word2Vec and GloVe.

Topic Clustering: Applies clustering algorithms like K-means and hierarchical clustering to group similar articles together.

Topic Labeling: Manually inspects a sample of articles in each cluster to assign meaningful topic labels.

Classification Model: Trains a supervised machine learning model (Naive Bayes, Support Vector Machines, LSTM, or BERT) to predict the topic of a news article, using labeled clusters as ground truth labels.

Evaluation: Assesses the performance of the classification model on a testing set using metrics such as accuracy, precision, recall, and F1-score.

Deployment: Deploys a classification application using Streamlit to allow users to input news text and receive predictions on the topic category.
