#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
clf = svm.SVC(kernel="rbf", C=10000)
#Smaller training set for faster training/predicting times
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 
t0=time()
clf.fit(features_train,labels_train)
print "training time: ", round(time()-t0, 3)
t0=time()
print clf.score(features_test,labels_test)
print "scoring time: ", round(time()-t0, 3)
pred = clf.predict(features_test)
counter = 0
for x in pred:
    if x == 1: #if chris wrote email
        counter+=1
print counter
#printing out predictions below
"""print "10: " + str(pred[10]) + ", 26: " + str(pred[26]) + ", 50: " + str(pred[50])
predictions = ""
for prediction in pred:
    predictions+=str(prediction) + ", "
print "Predictions:" + predictions"""
#########################################################


