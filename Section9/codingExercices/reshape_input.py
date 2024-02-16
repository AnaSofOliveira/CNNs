# Importing needed library
import numpy as np


# Defining Numpy array as 1-channeled GRAY input
x_input_GRAY = np.zeros((853, 1280))


'''
(!) Your task is here
Replace '?' marks by variables/numbers
Reshape a given input
'''
# Reshaping a given input to get following: (batch size, rows, columns, channels)
x_input_GRAY = x_input_GRAY.reshape(1, x_input_GRAY.shape[0], x_input_GRAY.shape[1], 1)


# Printing shape of the resulted Numpy array
print(x_input_GRAY.shape)
