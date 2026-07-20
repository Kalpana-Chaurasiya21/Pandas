#importing pandas library

import pandas as pd



#Pandas

#definition

#pandas is an open source python library

#used for data manipulation

#data cleaning

#data analysis

#data transformation

#and handling structured data



#why do we use pandas?

#numpy is excellent for numerical arrays

#but real world datasets contain

#numbers

#text

#dates

#missing values

#mixed data types

#pandas is specially designed to work with such datasets



#real world uses

#data analyst

#business intelligence

#machine learning

#financial analysis

#report generation

#excel automation



#Series

#definition

#a series is a one dimensional labeled array

#it can store

#integers

#floats

#strings

#boolean values

#or mixed data types



#syntax

#pd.Series(data)



#creating a series from a list

students = pd.Series(["Rahul","Priya","Aman","Neha"])

print(students)



#creating a series of marks

marks = pd.Series([85,92,76,88])

print(marks)



#creating a series using custom index

salary = pd.Series(

    [25000,32000,41000],

    index=["Rahul","Priya","Aman"]

)

print(salary)



#accessing values

print(salary["Rahul"])

print(salary["Priya"])



#accessing multiple values

print(salary[["Rahul","Aman"]])



#creating series from dictionary

employee_salary = {

    "Rahul":25000,

    "Priya":32000,

    "Aman":41000

}



salary_series = pd.Series(employee_salary)

print(salary_series)



#series attributes

print(salary_series.index)

print(salary_series.values)

print(salary_series.dtype)

print(salary_series.shape)

print(salary_series.size)



#performing arithmetic operations

bonus_salary = salary_series + 5000

print(bonus_salary)



#comparison operation

print(salary_series > 30000)



#boolean indexing

print(salary_series[salary_series > 30000])



#important interview points

#series is one dimensional

#series has labels called index

#series can store any data type

#series supports vectorized operations

#series is faster than normal python loops