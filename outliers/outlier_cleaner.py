#!/usr/bin/python
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error)
    """
    cleaned_data = []
    for predict, age, net_worth in zip(predictions, ages, net_worths):
        cleaned_data.append((age, net_worth, abs(predict-net_worth)))

    i = 0
    for entry in sorted(cleaned_data, key=lambda tup: tup[2], reverse = True):
        if (i < len(predictions)/2):
            cleaned_data.remove(entry)
            i = i + 1

    return cleaned_data

## Works if algorithm deletes 50% of data.
def test_outlierCleaner():
    predictionA = np.array([4, 8, 10])
    predictionB = np.array([])

    agesA = np.array([10, 20, 30])
    agesB = np.array([])

    netWorthA = np.array([4, 8, 10])
    netWorthB = np.array([])
    netWorthC = np.array([7, 9, 11])

    ## Verify that some points are removed
    assert len(outlierCleaner(predictionA, agesA, netWorthA)) < len(predictionA)

    ## Verify that it works for empty arrays
    assert len(outlierCleaner(predictionB, agesA, netWorthA)) == 0
    assert len(outlierCleaner(predictionA, agesB, netWorthA)) == 0
    assert len(outlierCleaner(predictionA, agesA, netWorthB)) == 0
    assert len(outlierCleaner(predictionB, agesB, netWorthB)) == 0

    ## Verify appropiate behaviour
    assert outlierCleaner(predictionA, agesA, netWorthC).__contains__((20, 9, 1)) == True
    assert outlierCleaner(predictionA, agesA, netWorthC).__contains__((30, 11, 1)) == True
    assert outlierCleaner(predictionA, agesA, netWorthC).__contains__((10, 4, 3)) == False
