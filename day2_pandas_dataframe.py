#importing pandas library

import pandas as pd

#importing numpy because we will also create dataframe from numpy arrays

import numpy as np



#DataFrame

#definition

#a dataframe is a two dimensional labeled data structure

#it consists of rows and columns

#each column is actually a pandas series

#it can store multiple data types

#such as integers

#floating point numbers

#strings

#boolean values

#missing values



#real world examples

#employee database

#student records

#sales reports

#excel sheets

#customer information



#creating dataframe using dictionary

#keys become column names

#values become column data

student_data = {

    "Student_ID":[101,102,103,104],

    "Name":["Rahul","Priya","Aman","Neha"],

    "Marks":[85,92,76,88],

    "City":["Delhi","Mumbai","Pune","Lucknow"]

}

students = pd.DataFrame(student_data)

print(students)



#creating dataframe using list of lists

employee_data = [

    [101,"Amit",25000],

    [102,"Riya",32000],

    [103,"Karan",41000]

]

employees = pd.DataFrame(

    employee_data,

    columns=["Employee_ID","Name","Salary"]

)

print(employees)



#creating dataframe from numpy array

numbers = np.array([

    [10,20,30],

    [40,50,60],

    [70,80,90]

])

matrix = pd.DataFrame(

    numbers,

    columns=["Column1","Column2","Column3"]

)

print(matrix)



#shape

#definition

#returns the number of rows and columns

#return type

#tuple

print(students.shape)



#size

#definition

#returns the total number of elements

#formula

#rows × columns

#return type

#integer

print(students.size)



#columns

#definition

#returns all column names

#return type

#Index object

print(students.columns)



#index

#definition

#returns row labels

print(students.index)



#dtypes

#definition

#returns the data type of every column

print(students.dtypes)



#head()

#definition

#returns the first rows

#default is first 5 rows

print(students.head())



print(students.head(2))



#tail()

#definition

#returns the last rows

print(students.tail())



print(students.tail(2))



#info()

#definition

#displays dataframe summary

#it includes

#number of rows

#column names

#data types

#non null values

#memory usage

students.info()



#describe()

#definition

#returns statistical summary

#works mainly on numerical columns

print(students.describe())



#important interview points

#dataframe is two dimensional

#each column is a series

#rows represent records

#columns represent features

#shape returns rows and columns

#size returns total elements

#info gives complete dataframe summary

#describe gives statistical information