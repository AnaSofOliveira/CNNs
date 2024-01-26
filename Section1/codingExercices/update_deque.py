# Importing needed library
from collections import deque


# Initializing a deque object to store custom coordinates
custom_points = deque()


# Preparing custom coordinate to update deque object with
coordinate = (540, 860)


'''
(!) Your task is here
Replace '?' marks by variables/numbers
Update deque object
'''
# Appending coordinate to the deque object from the left side
custom_points.appendleft(coordinate)


# Printing custom coordinate
print(custom_points[0])
