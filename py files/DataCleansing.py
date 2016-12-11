
# coding: utf-8

# # Reading CSV file and removing columns that are not necessary
# 

# In[ ]:

# Ask user to enter file in which columns have to be removed
import pandas as pd
import numpy as np

file_name = input("Please enter a csv file destination")
print("File that has columns which are to be removed: \n",file_name)

num_str = input("Please enter the number of columns that you want to delete")
col_names = []
num = int(num_str)

# add user input to a list
while len(col_names) < num:
    name = input("Column name: ")
    col_names.append(name)
print(col_names)

#read csv file into a data frame
df = pd.read_csv(file_name)
#drop columns
data = df.drop(col_names,axis=1)

#save as new file
new_file_name = input("Please enter the new filename in which modified CSV has to be written")
print("The new file name is: ", new_file_name)

data.to_csv(new_file_name, sep=',', index=None, encoding='utf-8')



# In[ ]:



