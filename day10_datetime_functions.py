#importing pandas library

import pandas as pd



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,104,105],

    "Employee_Name":["Rahul","Priya","Aman","Neha","Riya"],

    "Joining_Date":[

        "2022-01-15",

        "2021-06-10",

        "2023-03-25",

        "2020-09-18",

        "2022-12-05"

    ]

})



print(employees)



#to_datetime()

#definition

#to_datetime() converts a string

#into datetime format

#datetime makes it easy

#to perform date calculations

#syntax

#pd.to_datetime(column_name)

#uses

#used before extracting year month day

#used before calculating date differences

employees["Joining_Date"] = pd.to_datetime(

    employees["Joining_Date"]

)



print(employees.dtypes)



#dt.year

#definition

#extracts only the year

#from a datetime column

#syntax

#series.dt.year

#uses

#used for yearly reports

#used for filtering records

employees["Year"] = employees["Joining_Date"].dt.year

print(employees)



#dt.month

#definition

#extracts month number

#syntax

#series.dt.month

employees["Month"] = employees["Joining_Date"].dt.month

print(employees)



#dt.day

#definition

#extracts day

#syntax

#series.dt.day

employees["Day"] = employees["Joining_Date"].dt.day

print(employees)



#dt.day_name()

#definition

#returns the weekday name

#syntax

#series.dt.day_name()

employees["Weekday"] = employees["Joining_Date"].dt.day_name()

print(employees)



#dt.month_name()

#definition

#returns the month name

#syntax

#series.dt.month_name()

employees["Month_Name"] = employees["Joining_Date"].dt.month_name()

print(employees)



#date filtering

#definition

#filtering records

#using datetime values

recent_employees = employees[

    employees["Joining_Date"] > "2022-01-01"

]



print(recent_employees)



#current date

#definition

#Timestamp.now()

#returns current system date and time

current_date = pd.Timestamp.now()

print(current_date)



#calculating experience

#definition

#subtracting two dates

#returns time difference

employees["Experience_Days"] = (

    current_date - employees["Joining_Date"]

).dt.days



print(employees)



#sorting by joining date

#definition

#sorts records

#based on dates

sorted_data = employees.sort_values(

    by="Joining_Date"

)



print(sorted_data)



#important interview points

#to_datetime() converts strings into datetime

#dt.year extracts year

#dt.month extracts month

#dt.day extracts day

#dt.day_name() returns weekday

#dt.month_name() returns month name

#Timestamp.now() returns current date and time

#datetime columns can be filtered

#date subtraction gives time difference