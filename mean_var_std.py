import numpy as np

# TODO the input of the func should be a list containing 9 digits
# TODO the func should return a dict containing, 
#      max, min, and along both axes and for the flattened matrix
# TODO the values in the returned dictionary should be lists and not Numpy arrays.

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        a = np.array(list)
        a = np.reshape(a, (3,3))

        mean_calcs = [np.mean(a, axis=0), np.mean(a, axis=1), np.mean(a)]

        calculations = {
            "mean": [result.tolist() for result in mean_calcs],
            "variance": [np.var(a, axis=0), np.var(a, axis=1), np.var(a)],
            "standard deviation": [np.std(a, axis=0), np.std(a, axis=1), np.std(a)],
            "max": [np.max(a, axis=0), np.max(a, axis=1), np.max(a)],
            "min": [np.min(a, axis=0), np.min(a, axis=1), np.min(a)],
            "sum": [np.sum(a, axis=0), np.sum(a, axis=1), np.sum(a)],
        }

        return calculations

test_list = (0, 1, 2, 3, 4, 5, 6, 7, 8)

results = calculate(test_list)
print(results)