#!/usr/bin/python

"""
    this is the code to accompany the Lesson 3 (decision tree) mini-project

    use an DT to identify emails from the Enron corpus by their authors

    Sara has label 0
    Chris has label 1

"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score
from sklearn import tree

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print len(features_train[0])


#########################################################
### your code goes here ###
##clfr = tree.DecisionTreeClassifier(min_samples_split=40)

##t0 = time()
##clfr.fit(features_train, labels_train)
##print "The training time is: ", round(time() - t0, 4), "s"

##t1 = time()
##pred = clfr.predict(features_test)
##print "The predicting time is: ", round(time() - t1, 4), "s"

##acc = accuracy_score(pred, labels_test)
##print "The accuracy is: ", round(acc, 4)
#########################################################
