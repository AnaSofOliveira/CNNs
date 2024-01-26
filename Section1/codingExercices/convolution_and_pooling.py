# Importing needed libraries
import numpy as np
from custom_functions import convolution_2d, range_0_255, pooling


# Defining input matrix
input_matrix = np.ones((15, 20))


# Defining filters
filter_1 = np.ones((3, 3))
filter_2 = np.ones((3, 3))
filter_3 = np.ones((3, 3))


'''
(!) Your task is here
Replace '?' marks by needed variables

Input to c1: (?, filter_1, pad=1, step=1)
Input to c1_p1: (?, f_pooling=2, step=2)

Input to c2: (?, filter_2, pad=1, step=1)
Input to c2_p2: (?, f_pooling=2, step=2)

Input to c3: (?, filter_3, pad=1, step=1)
Input to c3_p3: (?, f_pooling=2, step=2)
'''

# Implement architecture: [C1, P1]-->[C2, P2]-->[C3, P3]

# [C1, P1]
# Applying 2D convolution
c1 = convolution_2d(input_matrix, filter_1, pad=1, step=1)
# Excluding non-needed values
c1 = range_0_255(c1)
# Applying pooling
c1_p1 = pooling(c1, f_pooling=2, step=2)


# [C2, P2]
# Applying 2D convolution
c2 = convolution_2d(c1_p1, filter_2, pad=1, step=1)
# Excluding non-needed values
c2 = range_0_255(c2)
# Applying pooling
c2_p2 = pooling(c2, f_pooling=2, step=2)


# [C3, P3]
# Applying 2D convolution
c3 = convolution_2d(c2_p2, filter_3, pad=1, step=1)
# Excluding non-needed values
c3 = range_0_255(c3)
# Applying pooling
c3_p3 = pooling(c3, f_pooling=2, step=2)


# Printing final, resulted matrix
print(c3_p3)
