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
        totalStock = totalStock + (0 if enron_data[user]["exercised_stock_options"] == "NaN" else enron_data[user]["exercised_stock_options"])
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

## void -> void
## Prints the amount of people in the dataset with a quantified salary
def numberPeopleWithSalaryData():
    npwsd = 0
    for k, v in enron_data.iteritems():
        if (v["salary"] != "NaN"):
            npwsd = npwsd + 1

    print "The amount of people that we have salary data of is: ", npwsd

## void -> void
## Prints the amount of people with a known e-mail address
def numberPeopleWithEmailData():
    npwed = 0
    for k, v in enron_data.iteritems():
        if (v["email_address"] != "NaN"):
            npwed = npwed + 1

    print "The amount of people that we have email data of is: ", npwed

## void -> void
## Prints the percent of people without financial data:
def percentPeopleWithoutFinancialData():
    npwfd = 0
    for k, v in enron_data.iteritems():
        if (v["total_payments"] == "NaN"):
            npwfd = npwfd + 1

    npwfd = float(npwfd) / len(enron_data)

    print "The percent of people without financial data is: ", npwfd

def percentPeopleWithoutFinancialDataAndPOI():
    npwfdap = 0
    for k, v in enron_data.iteritems():
        if (v["total_payments"] == "NaN" and v["poi"]):
            npwfd = npwfd + 1

    print "The amount of people of interest without financial data is: ", npwfdap
    npwfdap = float(npwfdap) / len(enron_data)

    print "The percent of people of interest without financial data is: ", npwfdap

def largestBonus():
    maxBonus = 0
    person = ""

    for k, v in enron_data.iteritems():
        currentBonus = v["bonus"]
        if (currentBonus > maxBonus and currentBonus != "NaN" and k != "TOTAL"):
            maxBonus = currentBonus
            person = k

    print "The person with the largest bonus is: ", person, "with a bonus of: ", maxBonus

def printKeysItems():
    for k, v in enron_data.iteritems():
        print k, "exercised stock options: ", v["exercised_stock_options"]

def printBandits():
    print "The bandits are: "
    for k, v in enron_data.iteritems():
        currentBonus = v["bonus"]
        currentSalary = v["salary"]
        if (k != "TOTAL" and currentBonus != "NaN" and currentSalary != "NaN" and (currentBonus >6000000 or currentSalary > 1000000)):
            print k, "with bonus: ", currentBonus, "and salary: ", currentSalary

def maxExercisedStock():
    maxOrMin(lambda a, b: a>b, "exercised_stock_options", 0, True)

def minExercisedStock():
    maxOrMin(lambda a, b: a<b, "exercised_stock_options", 10000000, False)

## (Number, Number -> Bool) String Number Bool-> void
def maxOrMin(fn, feature, start, isMax):
    output = start
    p = ""

    try:
        for k, v in enron_data.iteritems():
            currentValue = v[feature]
            if currentValue != "NaN" and fn(currentValue, output):
                output = currentValue
                p = k
        print "The ", ("maximum " if isMax else "minimum"), feature, "is: ", output, "by: ", p
    except KeyError:
        print "The key was not found"

def removeTotal():
    enron_data.pop("TOTAL", 0)

def upper(a, b):
    return a > b

def lower(a, b):
    return a < b
## Main function.
if __name__ == '__main__':
    removeTotal()
    maxOrMin(upper, "salary", 0, True)
    maxOrMin(lower, "salary", 1000000, False)
