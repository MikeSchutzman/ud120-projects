#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#features_train is training emails
#features_test is test emails
#labels_train is training answers
#labels_test is test answers



#########################################################
### your code goes here ###
clf = GaussianNB()
t0 = time()
clf.fit(features_train,labels_train) #fits data and makes model
print "training time:", round(time()-t0, 3), "s" #outputs how long training took
t1 = time()
clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s" #outputs how long predicting took
print(clf.score(features_test,labels_test)) #test points on model and sees how accurate
#########################################################


