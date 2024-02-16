# Importing needed library
from sklearn.metrics import confusion_matrix


# Defining True Vector
y_true = [1, 0, 1, 0, 2, 2, 1, 0, 0, 1, 2, 2, 0, 2, 2, 0, 0, 0, 2, 2, 2, 2, 1, 0, 2]

# Defining Predicted Vector
y_predicted = [0, 2, 1, 0, 2, 0, 1, 1, 0, 1, 2, 2, 0, 1, 2, 0, 0, 0, 2, 0, 0, 1, 1, 0, 1]


'''
(!) Your task is here
Replace '?' marks by variables
Compute Confusion Matrix
'''
# Computing Confusion Matrix to evaluate accuracy of classification
c_m = confusion_matrix(y_true, y_predicted)


# Printing Confusion Matrix in form of Numpy array
print(c_m)
