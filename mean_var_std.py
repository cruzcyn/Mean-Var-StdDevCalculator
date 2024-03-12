import numpy as np

# TODO the input of the func should be a list containing 9 digits
# TODO the func should return a dict containing mean, variance, standard deviation, 
#      max, min, and sum along both axes and for the flattened matrix
# TODO the values in the returned dictionary should be lists and not Numpy arrays.

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        a = np.array(list)
        a = np.reshape(a, (3,3))

        # calculations = {
        #     "mean": [axis1, axis2, flattened],
        #     "variance": [axis1, axis2, flattened],
        #     "standard deviation": [axis1, axis2, flattened],
        #     "max": [axis1, axis2, flattened],
        #     "min": [axis1, axis2, flattened],
        #     "sum": [np.sum(a, axis=0), np.sum(a, axis=1), np.sum(a)],
        # }
        # return calculations

        axis1_sum = np.sum(a)
        print(axis1_sum)

test_list = (0, 1, 2, 3, 4, 5, 6, 7, 8)

calculate(test_list)
