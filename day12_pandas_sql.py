#importing pandas library

import pandas as pd

import sqlite3



#creating database connection

#definition

#sqlite3.connect()

#creates a connection

#to a SQLite database

#syntax

#sqlite3.connect(database_name)

#uses

#used to connect pandas

#with SQL databases

connection = sqlite3.connect(

    "company.db"

)



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,104],

    "Employee_Name":["Rahul","Priya","Aman","Neha"],

    "Department":["IT","HR","Finance","IT"],

    "Salary":[50000,65000,70000,60000]

})



print(employees)



#to_sql()

#definition

#to_sql() writes

#a dataframe

#into a SQL table

#syntax

#dataframe.to_sql(table_name,connection)

#uses

#used to store cleaned data

#inside a database

employees.to_sql(

    "Employees",

    connection,

    if_exists="replace",

    index=False

)



#read_sql()

#definition

#read_sql()

#reads SQL query results

#into a dataframe

#syntax

#pd.read_sql(query,connection)

#uses

#used to analyze SQL data

all_employees = pd.read_sql(

    "SELECT * FROM Employees",

    connection

)



print(all_employees)



#reading selected columns

selected_columns = pd.read_sql(

    """

    SELECT Employee_Name,

           Salary

    FROM Employees

    """,

    connection

)



print(selected_columns)



#reading filtered records

high_salary = pd.read_sql(

    """

    SELECT *

    FROM Employees

    WHERE Salary > 60000

    """,

    connection

)



print(high_salary)



#reading sorted data

sorted_data = pd.read_sql(

    """

    SELECT *

    FROM Employees

    ORDER BY Salary DESC

    """,

    connection

)



print(sorted_data)



#reading aggregated data

department_summary = pd.read_sql(

    """

    SELECT Department,

           AVG(Salary) AS Average_Salary

    FROM Employees

    GROUP BY Department

    """,

    connection

)



print(department_summary)



#closing database connection

connection.close()



#important interview points

#to_sql() writes dataframe to database

#read_sql() reads SQL query results

#sqlite3.connect() creates database connection

#if_exists="replace" replaces existing table

#index=False prevents dataframe index from becoming a SQL column