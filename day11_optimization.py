#importing pandas library

import pandas as pd



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,104,105],

    "Employee_Name":["Rahul","Priya","Aman","Neha","Riya"],

    "Department":["IT","HR","IT","Finance","HR"],

    "Salary":[50000,65000,70000,80000,60000],

    "Experience":[2,4,3,5,2]

})



print(employees)



#query()

#definition

#query() filters rows

#using a string expression

#it is an alternative

#to boolean indexing

#syntax

#dataframe.query("condition")

#uses

#used to write clean code

#used for filtering multiple conditions

it_employees = employees.query(

    "Department == 'IT'"

)

print(it_employees)



experienced_employees = employees.query(

    "Salary > 60000 and Experience >= 3"

)

print(experienced_employees)



#eval()

#definition

#eval() evaluates

#expressions directly

#on dataframe columns

#syntax

#dataframe.eval("expression")

#uses

#used for creating new columns

#used for mathematical calculations

employees = employees.eval(

    "Bonus = Salary * 0.10"

)

print(employees)



employees = employees.eval(

    "Total_Salary = Salary + Bonus"

)

print(employees)



#astype()

#definition

#astype() changes

#the data type

#of one or more columns

#syntax

#dataframe.astype(datatype)

#uses

#used for type conversion

#used before analysis

employees["Employee_ID"] = employees["Employee_ID"].astype(

    "string"

)

print(employees.dtypes)



employees["Department"] = employees["Department"].astype(

    "category"

)

print(employees.dtypes)



#memory_usage()

#definition

#memory_usage()

#shows memory

#used by each column

#syntax

#dataframe.memory_usage()

#uses

#used to optimize

#large datasets

print(

    employees.memory_usage()

)



print(

    employees.memory_usage(

        deep=True

    )

)



#select_dtypes()

#definition

#select_dtypes()

#selects columns

#based on datatype

#syntax

#dataframe.select_dtypes(include=datatype)

#uses

#used to separate

#numeric and text columns

numeric_columns = employees.select_dtypes(

    include="number"

)

print(numeric_columns)



text_columns = employees.select_dtypes(

    include="object"

)

print(text_columns)



category_columns = employees.select_dtypes(

    include="category"

)

print(category_columns)



#important interview points

#query() filters rows using expressions

#eval() evaluates dataframe expressions

#astype() changes column datatype

#category datatype saves memory

#memory_usage() checks memory consumption

#select_dtypes() filters columns by datatype