# Importing needed library
import numpy as np


# Initializing zero-valued Numpy array for images
# Shape: image number, height, width, number of channels
x_train = np.zeros((10000, 64, 64, 3))


# Initializing zero-valued Numpy array for classes' numbers
# Shape: class's number
y_train = np.zeros(10000)


'''
(!) Your task is here
Replace '?' marks by needed float numbers
'''
# Slicing first 30% of elements
# Assigning sliced elements to temp Numpy arrays
x_temp = x_train[:int(x_train.shape[0] * 0.3), :, :, :]
y_temp = y_train[:int(y_train.shape[0] * 0.3)]


'''
(!) Your task is here
Replace '?' marks by needed float numbers
'''
# Slicing last 70% of elements
# Re-assigning sliced elements to train Numpy arrays
x_train = x_train[int(x_train.shape[0] * 0.3):, :, :, :]
y_train = y_train[int(y_train.shape[0] * 0.3):]


'''
(!) Your task is here
Replace '?' marks by needed float numbers
'''
# Slicing first 67% of elements from temp Numpy arrays
# That is 20% from initial Numpy arrays
# Assigning sliced elements to validation Numpy arrays
x_validation = x_temp[:int(x_temp.shape[0] * 0.67), :, :, :]
y_validation = y_temp[:int(y_temp.shape[0] * 0.67)]


'''
(!) Your task is here
Replace '?' marks by needed float numbers
'''
# Slicing last 33% of elements from temp Numpy arrays
# That is 10% from initial Numpy arrays
# Assigning sliced elements to test Numpy arrays
x_test = x_temp[int(x_temp.shape[0] * 0.67):, :, :, :]
y_test = y_temp[int(y_temp.shape[0] * 0.67):]


# Printing shapes of obtained sub-datasets
print(x_train.shape, x_validation.shape, x_test.shape)
