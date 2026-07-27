#importing pandas library

import pandas as pd



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,104,105,106,107,108],

    "Employee_Name":["Rahul","Priya","Aman","Neha","Riya","Karan","Ankit","Simran"],

    "Department":["IT","HR","IT","Finance","HR","Finance","IT","Marketing"],

    "Salary":[50000,60000,65000,70000,72000,68000,75000,55000],

    "Experience":[2,5,3,7,4,6,5,2]

})



print(employees)



#mean()

#definition

#mean() returns

#the average value

#syntax

#series.mean()

#uses

#used to calculate

#average salary

average_salary = employees["Salary"].mean()

print("Average Salary :",average_salary)



#median()

#definition

#median() returns

#the middle value

#after sorting

#syntax

#series.median()

#uses

#used when outliers exist

median_salary = employees["Salary"].median()

print("Median Salary :",median_salary)



#mode()

#definition

#mode() returns

#the most frequent value

#syntax

#series.mode()

#uses

#used for categorical columns

department_mode = employees["Department"].mode()

print(department_mode)



#min()

#definition

#returns minimum value

print(

    employees["Salary"].min()

)



#max()

#definition

#returns maximum value

print(

    employees["Salary"].max()

)



#std()

#definition

#std() returns

#standard deviation

#it measures

#how spread out

#the data is

#syntax

#series.std()

#uses

#used to measure

#data variability

print(

    employees["Salary"].std()

)



#var()

#definition

#var() returns

#variance

#syntax

#series.var()

#uses

#used in statistics

print(

    employees["Salary"].var()

)



#value_counts()

#definition

#counts frequency

#of each value

print(

    employees["Department"].value_counts()

)



#important interview points

#mean calculates average

#median gives middle value

#mode gives most frequent value

#std measures spread

#variance is square of standard deviation

#value_counts counts category frequency