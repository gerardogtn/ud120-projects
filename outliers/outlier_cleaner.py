#!/usr/bin/python


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
        cleaned_data.append((predict, age, net_worth, (predict-net_worth)**2))

    sorted_cleaned_data =  sorted(cleaned_data, key=lambda tup: tup[3])

    i = len(predictions) - 1
    lastComparison = i - (i / 10)
    cleaned_data = []
    for entry in sorted_cleaned_data:
        if (i < lastComparison):
            cleaned_data.append(entry[0:3])
        i = i - 1

    return cleaned_data
