# Importing needed library
import numpy as np

# Initializing NumPy array
x_train = np.array([[[[10, 15, 20], [5, 10, 15], [3, 5, 10]],
                     [[12, 5, 25], [51, 17, 35], [11, 6, 7]],
                     [[10, 15, 20], [5, 1, 2], [18, 9, 8]]],

                    [[[12, 25, 30], [5, 10, 15], [3, 5, 10]],
                     [[2, 5, 25], [51, 17, 35], [11, 6, 7]],
                     [[1, 12, 20], [5, 1, 2], [18, 9, 8]]]])

'''
(!) Your task is here
Replace '?' marks by needed variable/key/number
'''
# Calculating Standard Deviation from a given NumPy array
std = np.std(x_train, axis=0)


# Printing calculated Standard Deviation
print(std)
