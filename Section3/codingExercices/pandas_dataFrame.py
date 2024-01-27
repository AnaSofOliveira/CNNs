# Importing needed library
import pandas as pd


'''
(!) Your task is here
Replace '?' mark by needed separator
The data in the file is separated by coma
'''
# Getting Pandas dataFrame from csv file
labels = pd.read_csv('../classes_names.csv', sep=',')
print(labels.head())
'''
(!) Your task is here
Replace '?' mark by needed integer number
Replace '?' mark by needed string value
'''
# Getting class's name of the 11th index
class_name = labels.loc[11, 'SignName']


# Printing extracted class's name
print(class_name)
