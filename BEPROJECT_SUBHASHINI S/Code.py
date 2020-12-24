
try:

    from urlparse import urlparse
except:
    from urllib.parse import urlparse

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False
val = input("Enter Any Url: ")  
print(uri_validator(val))  
 
import numpy as np 
import pandas as pd 
import os
import seaborn as sns
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
dataset = pd.read_csv("~/Desktop/data.csv")
dataset.head()
y = data["label"]  
 url_list = data["url"]
vectorizer = TfidfVectorizer()  
 X = vectorizer.fit_transform(url_list)
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  
 logit = LogisticRegression() 
logit.fit(X_train, y_train)         
print("Accuracy of our model is: ",logit.score(X_test, y_test))
