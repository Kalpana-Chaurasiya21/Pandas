#importing pandas library

import pandas as pd

import numpy as np



#Data Cleaning

#definition

#data cleaning means finding and fixing

#incorrect

#missing

#duplicate

#or inconsistent data

#before performing analysis



#creating dataframe

students = pd.DataFrame({

    "Student_ID":[101,102,103,104,105,105],

    "Name":["Rahul","Priya","Aman","Neha",None,"Riya"],

    "Marks":[85,np.nan,76,88,95,95],

    "City":["Delhi","Mumbai","Delhi",None,"Lucknow","Lucknow"]

})



print(students)



#isnull()

#definition

#returns True for missing values

print(students.isnull())



#counting missing values

print(students.isnull().sum())



#notnull()

#definition

#returns True for available values

print(students.notnull())



#dropna()

#definition

#removes rows containing missing values

print(students.dropna())



#dropna() with axis=1

#definition

#removes columns containing missing values

print(students.dropna(axis=1))



#fillna()

#definition

#replaces missing values

filled_data = students.fillna("Unknown")

print(filled_data)



#replacing only marks column

students["Marks"] = students["Marks"].fillna(0)

print(students)



#replace()

#definition

#replaces existing values with new values

students["City"] = students["City"].replace("Delhi","New Delhi")

print(students)



#duplicated()

#definition

#returns True for duplicate rows

print(students.duplicated())



#count duplicate rows

print(students.duplicated().sum())



#drop_duplicates()

#definition

#removes duplicate rows

students = students.drop_duplicates()

print(students)



#rename()

#definition

#changes column names

students = students.rename(columns={

    "Marks":"Score",

    "City":"Location"

})

print(students)



#astype()

#definition

#changes the data type of columns

students["Student_ID"] = students["Student_ID"].astype(str)

print(students.dtypes)



#real world example

employees = pd.DataFrame({

    "Employee":["Amit","Riya",None,"Neha"],

    "Salary":[25000,30000,np.nan,45000]

})



print(employees)



employees = employees.fillna({

    "Employee":"Unknown",

    "Salary":0

})



print(employees)



#important interview points

#isnull() checks missing values

#notnull() checks available values

#dropna() removes missing values

#fillna() fills missing values

#replace() replaces values

#duplicated() finds duplicate rows

#drop_duplicates() removes duplicate rows

#rename() changes column names

#astype() changes data types