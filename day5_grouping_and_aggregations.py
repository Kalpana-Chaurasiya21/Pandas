#importing pandas library

import pandas as pd



#Grouping and Aggregation

#definition

#grouping means dividing data into groups

#based on one or more columns

#aggregation means performing calculations

#on each group



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,104,105,106,107,108],

    "Employee":["Rahul","Priya","Aman","Neha","Riya","Karan","Mohit","Anjali"],

    "Department":["IT","HR","IT","Finance","HR","Finance","IT","HR"],

    "Salary":[50000,35000,60000,45000,40000,55000,70000,42000],

    "Experience":[2,3,5,4,2,6,8,1]

})



print(employees)



#--------------------------------------------------

#groupby()

#definition

#groupby() divides the dataframe

#into groups based on a column



department_groups = employees.groupby("Department")



print(department_groups)



#--------------------------------------------------

#sum()

#definition

#returns the sum of numeric columns

print(

    employees.groupby("Department").sum(numeric_only=True)

)



#--------------------------------------------------

#mean()

#definition

#returns average values

print(

    employees.groupby("Department").mean(numeric_only=True)

)



#--------------------------------------------------

#count()

#definition

#counts non-null values

print(

    employees.groupby("Department").count()

)



#--------------------------------------------------

#max()

#definition

#returns maximum value

print(

    employees.groupby("Department").max()

)



#--------------------------------------------------

#min()

#definition

#returns minimum value

print(

    employees.groupby("Department").min()

)



#--------------------------------------------------

#agg()

#definition

#performs multiple aggregations together

print(

    employees.groupby("Department").agg({

        "Salary":["sum","mean","max","min"],

        "Experience":["mean","max"]

    })

)



#--------------------------------------------------

#value_counts()

#definition

#counts frequency of unique values

print(

    employees["Department"].value_counts()

)



#--------------------------------------------------

#unique()

#definition

#returns all unique values

print(

    employees["Department"].unique()

)



#--------------------------------------------------

#nunique()

#definition

#returns the number of unique values

print(

    employees["Department"].nunique()

)



#--------------------------------------------------

#size()

#definition

#returns the number of rows in each group

print(

    employees.groupby("Department").size()

)



#--------------------------------------------------

#real world example

sales = pd.DataFrame({

    "Product":["Laptop","Laptop","Mouse","Keyboard","Mouse","Laptop"],

    "Sales":[65000,70000,900,1500,1000,68000]

})



print(sales)



print(

    sales.groupby("Product").sum(numeric_only=True)

)



print(

    sales.groupby("Product").mean(numeric_only=True)

)



#important interview points

#groupby() creates groups

#sum() calculates total

#mean() calculates average

#count() counts values

#max() finds maximum

#min() finds minimum

#agg() performs multiple operations together

#value_counts() counts frequency

#unique() returns unique values

#nunique() returns number of unique values

#size() returns number of rows