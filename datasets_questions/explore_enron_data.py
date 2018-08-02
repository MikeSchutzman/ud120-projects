#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print len(enron_data)
print len(enron_data.values()[0])
counter=0
poiTotalPayCounter = 0
for i in enron_data.values():
    if i["poi"]==1:
        counter+=1
        if i["total_payments"]!="NaN":
            poiTotalPayCounter+=1
print counter
print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]
salCount=0
emailCount=0
totalPayCount=0
for i in enron_data.values():
    if i["salary"]!="NaN":
        salCount+=1
    if i["email_address"]!="NaN":
        emailCount+=1
    if i["total_payments"]!="NaN":
        totalPayCount+=1
print salCount
print emailCount
print totalPayCount
print float(totalPayCount)/len(enron_data)
print poiTotalPayCounter
print float(poiTotalPayCounter)/counter
