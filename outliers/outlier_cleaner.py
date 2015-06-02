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
        cleaned_data.append((age, net_worth, abs(predict-net_worth)))

    i = 0
    for entry in sorted(cleaned_data, key=lambda tup: tup[2], reverse = True):
        if (i < len(predictions)/10):
            cleaned_data.remove(entry)
            i = i + 1

    return cleaned_data
