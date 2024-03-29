import numpy as np

def calculate(list):
    """Takes a list of 9 int, turns it into a 3x3 numpy array and calculates the mean, variance, standard
    deviation, max, min and sum of the rows, columns and the flattened matrix. Returns a dictionary with lists
    of all the results."""

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        a = np.array(list)
        a = np.reshape(a, (3,3))

        mean_calcs = [np.mean(a, axis=0), np.mean(a, axis=1), np.mean(a)]
        var_calcs = [np.var(a, axis=0), np.var(a, axis=1), np.var(a)]
        std_calcs = [np.std(a, axis=0), np.std(a, axis=1), np.std(a)]
        max_calcs = [np.max(a, axis=0), np.max(a, axis=1), np.max(a)]
        min_calcs = [np.min(a, axis=0), np.min(a, axis=1), np.min(a)]
        sum_calcs = [np.sum(a, axis=0), np.sum(a, axis=1), np.sum(a)]

        calculations = {
            "mean": [result.tolist() for result in mean_calcs],
            "variance": [result.tolist() for result in var_calcs],
            "standard deviation": [result.tolist() for result in std_calcs],
            "max": [result.tolist() for result in max_calcs],
            "min": [result.tolist() for result in min_calcs],
            "sum": [result.tolist() for result in sum_calcs],
        }

        return calculations
