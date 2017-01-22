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


len(enron_data)

len(enron_data["CAUSEY RICHARD A"]))

count = 0
for i in enron_data:
    if enron_data[i]['poi'] == True:
        count += 1
print 'count is ' , count

print(enron_data["PRENTICE JAMES"]['total_stock_value'])

print(enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])

print(enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])

print(enron_data["SKILLING JEFFREY K"]['total_payments'])
print(enron_data["LAY KENNETH L"]['total_payments'])
print(enron_data["FASTOW ANDREW S"]['total_payments'])

count = 0
for i in enron_data:
    if enron_data[i]['salary'] != 'NaN':
        count += 1
print 'count is ' , count

count = 0
for i in enron_data:
    if enron_data[i]['email_address'] != 'NaN':
        count += 1
print 'count is ' , count

count = 0
for i in enron_data:
    if enron_data[i]['total_payments'] == 'NaN':
        if enron_data[i]['poi'] == True:
            count += 1
print 'count is ' , count

count = 0
for i in enron_data:
    if enron_data[i]['total_payments'] == 'NaN':
        count += 1
print 'count is ' , count
