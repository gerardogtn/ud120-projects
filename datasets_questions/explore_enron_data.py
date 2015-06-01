#!/usr/bin/python

"""
    starter code for exploring the Enron dataset (emails + finances)
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

## Load data
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


## Dictionary -> void
## Prints the length of the dictionary.
def peopleInDataset():
    print "The amount of people in the dataset is: ", len(enron_data)

## Dictionary -> void
## Prints the amount of keys in the dataset.
def featuresInDataSet():
    print "The amount of features in the dataset is: ", len(enron_data.values()[0])

## Dictionary -> void
## Prints the amount of people in enron_data that have a positive value for the
## 'poi' field.
def peopleOfInterest():
    numberPOI = 0
    for k, v in enron_data.iteritems():
        if v['poi']:
            numberPOI = numberPOI + 1
    print "The amount of people of interest is: ", numberPOI

## String -> void
## Prints the total amount of stock for name. If not found, notifies user.
## TotalStock = restrictedStock + exercisedStockOptions
def stockValue(user):
    try:
        totalStock = enron_data[user]["restricted_stock"]
        totalStock = totalStock + enron_data[user]["exercised_stock_options"]
        print "The total stock value of ", user, "is: ", totalStock
    except KeyError:
        print "The user:", user, " was not found in the dataset"



## String -> void
## Prints the amount of emails from the user to a poi
def emailsToPOI(user):
    try:
        amountOfEmails = enron_data[user]["from_this_person_to_poi"]
        print "The amount of emails sent from: ", user, "to POIs is: ", amountOfEmails
    except KeyError:
        print "The user:", user, " was not found in the dataset"


## String -> void
## Prints the amount of exercised stock options by user
def exercisedStockOptions(user):
    try:
        eso = enron_data[user]["exercised_stock_options"]
        print "The amount of stock options exercised by: ", user, "is: ", eso
    except KeyError:
        print "The user:", user, " was not found in the dataset"

## void -> void
## Prints the keys of enron_data in alphabetical order
def printKeys():
    for k, v in sorted(enron_data.iteritems()):
        print k

## Main function.
if __name__ == '__main__':
    ##printKeys()
    peopleInDataset()
    featuresInDataSet()
    peopleOfInterest()
    stockValue("PRENTICE JAMES")
    emailsToPOI("COLWELL WESLEY")
    exercisedStockOptions("SKILLING JEFFREY K")
