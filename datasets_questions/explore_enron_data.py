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

#How many points?
#print(len(enron_data))

#How many features are available?
#print(len(enron_data[enron_data.keys()[0]]))

#How many POIs are in the data set?
#total = 0
#or names in enron_data.keys():
#    if enron_data[names]["poi"]==1:
#        total += 1
#    else:
#        continue
#
#print(total)

#Total value of stock belonging to James Prentice
#print(enron_data["PRENTICE JAMES"]['total_stock_value'])

#Total number of emails Wesley Colwell sent to POIs
#print(enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])

#Total value of options exercised accessed by Jeffer K SKILLING
#print(enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])

##WHo took home the largest total_payments
#print("FASTOW:",enron_data["FASTOW ANDREW S"]['total_payments'])
#print("SKILLING:",enron_data["SKILLING JEFFREY K"]['total_payments'])
#print("LAY:", enron_data["LAY KENNETH L"]['total_payments'])

#Quantiable salaries and emails
#salary = 0
#email = 0
#for names in enron_data.keys():
#    if enron_data[names]['salary'] != 'NaN':
#        salary += 1
#    if enron_data[names]['email_address'] != 'NaN':
#        email += 1
#print("Salary", salary)
#print("Email", email)

count = 0
total = 0
for finance in enron_data.keys():
    if enron_data[finance]['poi'] ==1:
        if enron_data[finance]['total_payments'] == 'NaN':
            count += 1
    total +=1
print(count, ":", total)
