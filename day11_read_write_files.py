#importing pandas library

import pandas as pd



#read_csv()

#definition

#read_csv() reads data

#from a CSV file

#and converts it into a DataFrame

#syntax

#pd.read_csv("file_name.csv")

#uses

#used for datasets from Kaggle

#used for Excel exported CSV files

#used in almost every data analysis project

students = pd.read_csv("students.csv")

print(students)



#head()

#definition

#head() displays

#the first rows

#of a dataframe

#syntax

#dataframe.head(number)

#uses

#used to quickly inspect data

print(students.head())



#tail()

#definition

#tail() displays

#the last rows

#of a dataframe

#syntax

#dataframe.tail(number)

#uses

#used to inspect the ending records

print(students.tail())



#sample()

#definition

#sample() returns

#random rows

#from a dataframe

#syntax

#dataframe.sample(number)

#uses

#used to inspect random records

print(

    students.sample(3)

)



#to_csv()

#definition

#to_csv() saves

#a dataframe

#as a CSV file

#syntax

#dataframe.to_csv("file.csv",index=False)

#uses

#used to export cleaned data

students.to_csv(

    "clean_students.csv",

    index=False

)



#read_excel()

#definition

#read_excel() reads

#an Excel file

#syntax

#pd.read_excel("file.xlsx")

#uses

#used for business reports

#used for HR and finance data

employee_data = pd.read_excel(

    "employees.xlsx"

)

print(employee_data)



#to_excel()

#definition

#to_excel() exports

#a dataframe

#to an Excel file

#syntax

#dataframe.to_excel("file.xlsx",index=False)

#uses

#used for sharing reports

employee_data.to_excel(

    "employee_report.xlsx",

    index=False

)



#read_json()

#definition

#read_json() reads

#JSON data

#into a dataframe

#syntax

#pd.read_json("file.json")

#uses

#used for API data

json_data = pd.read_json(

    "students.json"

)

print(json_data)



#to_json()

#definition

#to_json() exports

#dataframe

#to JSON format

#syntax

#dataframe.to_json("file.json")

#uses

#used while working with APIs

json_data.to_json(

    "new_students.json"

)



#important interview points

#read_csv() reads CSV files

#to_csv() exports CSV files

#read_excel() reads Excel files

#to_excel() exports Excel files

#read_json() reads JSON files

#to_json() exports JSON files

#head() displays first rows

#tail() displays last rows

#sample() displays random rows