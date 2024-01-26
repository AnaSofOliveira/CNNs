# Importing needed library
import numpy as np

# Defining input matrix
input_matrix = np.array([[1, 2, 3, 4],
                         [4, 3, 2, 1],
                         [1, 2, 3, 4],
                         [4, 3, 2, 1]])

'''
(!) Your task is here
Replace '?' marks by needed numbers
Size of the pad frame: (?, ?)
Values to fill pad frame with: constant_values=?
'''
# Applying 1 by 1 pad frame around input matrix
# filled with zeros
input_matrix_pad = np.pad(input_matrix, (1, 1),
                          mode='constant',
                          constant_values=0)


# Defining filter to convolve with
f = np.array([[1, 0, 1],
              [0, 1, 0],
              [1, 0, 1]])

# Calculating dimension of convolved matrix:
# height_out = (height_in - f_size + 2 * pad) / step + 1
# width_out = (width_in - f_size + 2 * pad) / step + 1

# Hyperparameters are as following:
# filter size = 3 (width and height are equal)
# stride (step for sliding) = 1
# pad (0-valued frame around image) = 1

# For given input matrix and set hyperparameters,
# dimension of convolved output matrix is:
# height_out = (4 - 3 + 2 * 1) / 1 + 1 = 4
# width_out = (4 - 3 + 2 * 1) / 1 + 1 = 4


# Preparing zero valued array for convolved matrix
# According to the hyperparameters,
# dimension is the same with input matrix
# Passing as argument tuple with needed shape
output_matrix = np.zeros(input_matrix.shape)

'''
(!) Your task is here
Replace '?' marks by needed numbers or variables
Extract 3x3 patch: [i:i+?, j:j+?]
Apply convolution of patch and filter: np.sum(? * ?)
'''
# Implementing convolution operation
# Sliding through entire input matrix with pad frame
for i in range(input_matrix_pad.shape[0] - 2):
    for j in range(input_matrix_pad.shape[1] - 2):
        # Extracting (slicing) a 3x3 patch
        # (the same size with filter)
        # from input matrix with pad frame
        patch = input_matrix_pad[i:i+3, j: j+3]

        # Applying elementwise multiplication and
        # summation - this is convolution operation
        # When we use '*' with matrices,
        # then elementwise multiplication will be applied
        output_matrix[i, j] = np.sum(patch * f)


        # Printing final, resulted matrix
        print(output_matrix)
