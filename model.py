from flask import Flask , redirect , url_for , request , render_template , jsonify , json
import pandas as pd 
import tensorflow as tf
import nltk
import os
import random
from collections import Counter
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, classify
import pandas as pd
import json
stoplist = stopwords.words('english')
app = Flask(__name__)


@app.route("/predict" , methods=['POST'])

def hello():
    json = json.request
    query = str(json)

    def preprocess(sentence):
            lemmatizer = WordNetLemmatizer()
            return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(sentence)]

    def get_features(text, setting):
            if setting=='bow':
                return {word: count for word, count in Counter(preprocess(text)).items() if not word in stoplist}
            else:
                return {word: True for word in preprocess(text) if not word in stoplist}

    def train(features, samples_proportion):
            train_size = int(len(features) * samples_proportion)
            # initialise the training and test sets
            train_set, test_set = features[:train_size], features[train_size:]
            #print ('Training set size = ' + str(len(train_set)) + ' emails')
            #print ('Test set size = ' + str(len(test_set)) + ' emails')
            # train the classifier
            classifier = NaiveBayesClassifier.train(train_set)

            #print (get_features('offer for u,please claim',''))
            return train_set, test_set, classifier

    def evaluate(train_set, test_set, classifier):
            # check how the classifier performs on the training and test sets
            print ('Accuracy on the training set = ' + str(classify.accuracy(classifier, train_set)))
            print ('Accuracy of the test set = ' + str(classify.accuracy(classifier, test_set)))
            # check which words are most informative for the classifier
            classifier.show_most_informative_features(20)

            #if _name_ == &amp;amp;quot;_main_&amp;amp;quot;:
            # initialise the data
            #spam = init_lists('enron1/spam/')
            #ham = init_lists('enron1/ham/')
            a_list = []
            '''f = open('SMSSpamCollection', 'r')
            a_list.append(f.read())
            #x = init_lists('SMSSpamCollection')'''
            df= pd.read_csv('SMSSpamCollection', sep='\t',names=["label", "message"])
            spam=df.loc[df['label'] == 'spam', 'message']
            ham=df.loc[df['label'] == 'ham', 'message']

            a=[]
            for i in range(0,747):
                tup=(spam.iloc[i])
                #print tup
                a.append(tup)
            spam=a
            a=[]
            for i in range(0,4825):
                tup=(ham.iloc[i])
                #print tup
                a.append(tup)
            ham=a
            all_emails = [(email, 'spam') for email in spam]
            all_emails += [(email, 'ham') for email in ham]
            random.shuffle(all_emails)
            #print (all_emails)
            #print ('Corpus size = ' + str(len(all_emails)) + ' emails')
            # extract the features
            all_features = [(get_features(email, ''), label) for (email, label) in all_emails]
            #print ('Collected ' + str(len(all_features)) + ' feature sets')

            # train the classifier
            train_set, test_set, classifier = train(all_features, 0.8)
            #print (classifier.classify("here is an offer for you"))
            # evaluate its performance
            evaluate(train_set, test_set, classifier)
            print (classifier.classify(get_features('offer for u,please claim','')))
            print (classifier.classify(get_features("Nah I don't think he goes to usf, he lives around here though",'')))




if __name__ == '__main__':
    import pickle
    app.run('127.0.0.1' , 5000 , debug = True)