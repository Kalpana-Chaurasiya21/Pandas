#importing pandas library

import pandas as pd



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,104,105,106],

    "Employee_Name":["Rahul","Priya","Aman","Neha","Riya","Karan"],

    "Department":["IT","IT","HR","HR","Finance","Finance"],

    "Salary":[50000,70000,45000,60000,80000,65000]

})



print(employees)



#rank()

#definition

#rank() assigns a rank

#to values in a column

#higher values receive higher ranks

#syntax

#series.rank()

#uses

#used for ranking employees

#used for leaderboard generation

employees["Salary_Rank"] = employees["Salary"].rank(

    ascending=False

)

print(employees)



#dense_rank()

#definition

#dense rank assigns ranks

#without leaving gaps

#when duplicate values exist

#syntax

#series.rank(method="dense")

#uses

#used in reports

#used in SQL like ranking

employees["Dense_Rank"] = employees["Salary"].rank(

    method="dense",

    ascending=False

)

print(employees)



#group wise ranking

#definition

#ranking inside each group

#instead of the whole dataframe

#syntax

#groupby(column)[target].rank()

#uses

#used for department wise ranking

employees["Department_Rank"] = employees.groupby(

    "Department"

)["Salary"].rank(

    ascending=False

)

print(employees)



#rolling()

#definition

#rolling() creates

#a moving window

#for calculations

#syntax

#series.rolling(window)

#uses

#used in stock market analysis

#used in sales trends

employees["Rolling_Average"] = employees["Salary"].rolling(

    window=2

).mean()

print(employees)



#rolling sum

#definition

#calculates moving total

employees["Rolling_Sum"] = employees["Salary"].rolling(

    window=3

).sum()

print(employees)



#cumsum()

#definition

#returns cumulative sum

#syntax

#series.cumsum()

#uses

#used for running totals

employees["Cumulative_Salary"] = employees["Salary"].cumsum()

print(employees)



#cummax()

#definition

#returns cumulative maximum

employees["Highest_Salary"] = employees["Salary"].cummax()

print(employees)



#cummin()

#definition

#returns cumulative minimum

employees["Lowest_Salary"] = employees["Salary"].cummin()

print(employees)



#cumprod()

#definition

#returns cumulative product

numbers = pd.Series([2,3,4,5])

print(numbers.cumprod())



#important interview points

#rank() assigns ranking

#dense rank removes ranking gaps

#groupby().rank() performs group wise ranking

#rolling() performs moving calculations

#cumsum() returns running total

#cummax() returns cumulative maximum

#cummin() returns cumulative minimum

#cumprod() returns cumulative product