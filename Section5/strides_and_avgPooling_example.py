# If you're using Nvidia GPU and 'cnngpu' environment, there might be an issue like:
'''dnn PoolForward launch failed [Op:MaxPool] name: max_pooling2d/MaxPool/'''
# In this case, switch to environment 'cnncpu', that is without GPU, and run again


# Importing needed libraries
import numpy as np
import tensorflow as tf


# Defining array with random values
x_train = np.random.randint(50, size=(4, 4)).astype(np.float32)

# Reshaping to get following: (batch size, rows, columns, channels)
x_train_input = x_train.reshape(1, 4, 4, 1)

# Showing initial array
print(x_train)
print()



# Initializing MaxPool2D layer
layer = tf.keras.layers.MaxPool2D()

# Passing array to the layer
output = layer(x_train_input)

# Showing array after MaxPool2D layer
print('MaxPool2D:', output.numpy().flatten())
print()



# Initializing AvgPool2D layer
layer = tf.keras.layers.AvgPool2D()

# Passing array to the layer
output = layer(x_train_input)

# Showing array after AvgPool2D layer
print('AvgPool2D:', output.numpy().flatten())
print()



# Initializing Conv2D layer
layer = tf.keras.layers.Conv2D(1, kernel_size=2, strides=2, kernel_initializer='ones')

# Passing array to the layer
output = layer(x_train_input)

# Showing array after Conv2D layer
print('Conv2D with stride 2:', output.numpy().flatten())
print()

# Showing kernels values
print('Kernels values:', layer.weights[0].numpy().flatten())
print()
