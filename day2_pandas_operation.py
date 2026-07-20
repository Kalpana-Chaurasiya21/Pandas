#importing pandas library

import pandas as pd



#creating a series

salary = pd.Series(

    [25000,32000,41000,28000,50000],

    index=["Rahul","Priya","Aman","Neha","Riya"]

)

print(salary)



#accessing elements

#definition

#we can access values using their index labels

#or integer positions

print(salary["Rahul"])

print(salary["Neha"])

print(salary[0])

print(salary[3])



#accessing multiple values

#definition

#pass a list of labels

print(salary[["Rahul","Aman","Riya"]])



#slicing

#definition

#slicing returns a part of the series

#syntax

#series[start:end]

print(salary[1:4])



#boolean indexing

#definition

#returns only values that satisfy the condition

print(salary[salary > 30000])



#updating a value

#definition

#assign a new value using the index label

salary["Rahul"] = 27000

print(salary)



#adding a new value

salary["Karan"] = 35000

print(salary)



#deleting a value

#definition

#drop() removes elements using index labels

#it returns a new series

updated_salary = salary.drop("Neha")

print(updated_salary)



#head()

#definition

#returns the first n values

#default is 5

print(salary.head())

print(salary.head(3))



#tail()

#definition

#returns the last n values

print(salary.tail())

print(salary.tail(2))



#sort_values()

#definition

#sorts values

print(salary.sort_values())



print(salary.sort_values(ascending=False))



#sort_index()

#definition

#sorts according to index labels

print(salary.sort_index())



#unique()

#definition

#returns unique values

marks = pd.Series([80,90,80,95,90,100])

print(marks.unique())



#nunique()

#definition

#returns the number of unique values

print(marks.nunique())



#value_counts()

#definition

#counts how many times each value appears

print(marks.value_counts())



#isnull()

#definition

#returns True where values are missing

data = pd.Series([10,20,None,40,None])

print(data.isnull())



#notnull()

#definition

#returns True where values are present

print(data.notnull())



#fillna()

#definition

#replaces missing values

filled = data.fillna(0)

print(filled)



#important interview points

#series is mutable

#head() returns first rows

#tail() returns last rows

#sort_values() sorts values

#sort_index() sorts index labels

#unique() returns unique values

#nunique() returns count of unique values

#value_counts() counts frequency

#isnull() finds missing values

#fillna() replaces missing values