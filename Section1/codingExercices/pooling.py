# Importing needed library
import numpy as np


# Defining input matrix
input_matrix = np.array([[9, 7, 6, 1],
                         [5, 1, 4, 5],
                         [1, 4, 8, 3],
                         [6, 5, 7, 1]])


# Hyperparameters are as following:
# filter size for pooling (width and height are equal)
f_pooling = 2
# stride (step) for sliding
step = 2


'''
(!) Your task is here
Replace '?' marks by needed numbers
Size of the filter for pooling
Step for sliding
'''
# Calculating dimension of output matrix after pooling:
height_out = int((input_matrix.shape[0] - 2) / 2 + 1)
width_out = int((input_matrix.shape[1] - 2) / 2 + 1)


# Preparing zero valued output array after pooling
output_matrix = np.zeros((height_out, width_out))


'''
(!) Your task is here
Replace '?' marks by needed numbers or variables
Initialize indexes for output matrix: ii = ? and jj = ?
Extract 2x2 patch: [i:i+?, j:j+?]
Apply max pooling: np.max(?)
'''
# Implementing pooling operation
# Preparing indexes for rows of output array
ii = 0

# Sliding through entire input matrix
for i in range(0, input_matrix.shape[0] - f_pooling + 1, step):
    # Preparing indexes for columns of output array
    jj = 0

    for j in range(0, input_matrix.shape[1] - f_pooling + 1, step):
        # Extracting (slicing) a 2x2 patch
        # (the same size with filter)
        # from input matrix
        patch = input_matrix[i:i+f_pooling, j:j+f_pooling]

        # Applying max pooling operation -
        # choosing maximum element
        output_matrix[ii, jj] = np.max(patch)

        # Increasing indexes for rows of output array
        jj += 1

    # Increasing indexes for columns of output array
    ii += 1


# Printing final, resulted matrix
print(output_matrix)
