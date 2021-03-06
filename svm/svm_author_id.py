#!/usr/bin/python

"""
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors

    Sara has label 0
    Chris has label 1

"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

## Smaller data fit.
## features_train = features_train[:len(features_train)/100]
## labels_train = labels_train[:len(labels_train)/100]


#########################################################
### your code goes here ###
clfr = SVC(C= 10000.0, kernel= "rbf")

t0 = time()
clfr.fit(features_train, labels_train)
print "training time: ", round(time() - t0, 3), "s"

t1 = time()
pred = clfr.predict(features_test)
print "predicting time: ", round(time() - t1, 3), "s"

acc = accuracy_score(pred, labels_test)
print "The accuracy is", round(acc, 5)

chrisCount = 0
for entry in pred:
    if (entry == 1):
        chrisCount = chrisCount + 1


print "The number of Chris' emails is: ", chrisCount

#########################################################
