# Importing needed library
import pandas as pd


'''
(!) Your task is here
Replace '?' marks by needed Boolean value
The data in the file is separated by gap
'''
# Getting Pandas dataFrame from annotation txt file
a = pd.read_csv('annotation.txt',
                header=None,
                delim_whitespace=True)


'''
(!) Your task is here
Replace '?' mark by needed integer number
'''
# Getting number of columns from Pandas dataFrame
a_columns = a.shape[1]


# Defining variable to collect complex class's name
class_name = ''


'''
(!) Your task is here
Replace '?' marks by needed integer numbers
The last four numbers are coordinates
Extract class's name from the first row
'''
# Getting class's name from loaded Pandas dataFrame
# Assembling complex name if it consists of few words
# Placing gap between words
for i in range(a_columns - 4):
    class_name += a.loc[0, i]

    # Adding space at the end
    class_name += ' '

# Deleting space at the end
class_name = class_name.rstrip(' ')


# Printing final, resulted matrix
print(class_name)
