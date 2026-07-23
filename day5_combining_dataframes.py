#importing pandas library

import pandas as pd



#Combining DataFrames

#definition

#combining dataframes means joining two or more dataframes

#to create a single dataframe

#this is useful when data is stored in different tables

#similar to SQL joins



#creating first dataframe

students = pd.DataFrame({

    "Student_ID":[101,102,103,104],

    "Name":["Rahul","Priya","Aman","Neha"]

})



#creating second dataframe

marks = pd.DataFrame({

    "Student_ID":[101,102,103,105],

    "Marks":[85,92,76,88]

})



print("Students DataFrame")

print(students)



print("Marks DataFrame")

print(marks)



#concat()

#definition

#concat() combines two or more dataframes

#it can combine rows or columns

#it does not match values using common columns

#syntax

#pd.concat([dataframe1,dataframe2],axis=0)

#axis=0 means row wise combination

#axis=1 means column wise combination

#uses

#used to combine monthly reports

#used to combine yearly sales data

#used to stack multiple datasets



semester1 = pd.DataFrame({

    "Student":["Rahul","Priya"],

    "Marks":[85,90]

})



semester2 = pd.DataFrame({

    "Student":["Aman","Neha"],

    "Marks":[78,95]

})



#combining rows

combined_rows = pd.concat(

    [semester1,semester2],

    ignore_index=True

)



print(combined_rows)



#creating dataframes for column wise concatenation

student_names = pd.DataFrame({

    "Name":["Rahul","Priya","Aman"]

})



student_cities = pd.DataFrame({

    "City":["Delhi","Mumbai","Pune"]

})



#combining columns

combined_columns = pd.concat(

    [student_names,student_cities],

    axis=1

)



print(combined_columns)



#merge()

#definition

#merge() combines dataframes

#using one or more common columns

#works exactly like SQL JOIN

#syntax

#pd.merge(left_dataframe,right_dataframe,on="column_name",how="join_type")

#how specifies the type of join

#uses

#used to combine employee and salary tables

#used to combine customer and order tables

#used in almost every data analysis project



#inner join

#returns only matching rows

inner_join = pd.merge(

    students,

    marks,

    on="Student_ID",

    how="inner"

)

print(inner_join)



#left join

#returns all rows from left dataframe

left_join = pd.merge(

    students,

    marks,

    on="Student_ID",

    how="left"

)

print(left_join)



#right join

#returns all rows from right dataframe

right_join = pd.merge(

    students,

    marks,

    on="Student_ID",

    how="right"

)

print(right_join)



#outer join

#returns all rows from both dataframes

outer_join = pd.merge(

    students,

    marks,

    on="Student_ID",

    how="outer"

)

print(outer_join)



#join()

#definition

#join() combines dataframes

#using their indexes

#by default it performs a left join

#syntax

#dataframe1.join(dataframe2)

#uses

#used when indexes are related

#faster than merge in some index based operations



student_information = pd.DataFrame({

    "Name":["Rahul","Priya","Aman"]

},

index=[101,102,103])



student_marks = pd.DataFrame({

    "Marks":[85,92,76]

},

index=[101,102,103])



joined_dataframe = student_information.join(student_marks)



print(joined_dataframe)



#append()

#definition

#append() was previously used

#to add one dataframe below another

#it has been removed in newer versions of pandas

#always use concat() instead



appended_dataframe = pd.concat(

    [semester1,semester2],

    ignore_index=True

)



print(appended_dataframe)



#real world example

#employee basic details

employees = pd.DataFrame({

    "Employee_ID":[1,2,3],

    "Employee":["Amit","Riya","Neha"]

})



#employee salary details

salary = pd.DataFrame({

    "Employee_ID":[1,2,3],

    "Salary":[35000,50000,45000]

})



#merging employee details with salary

employee_details = pd.merge(

    employees,

    salary,

    on="Employee_ID",

    how="inner"

)



print(employee_details)



#important interview points

#concat() combines dataframes row wise or column wise

#merge() combines dataframes using common columns

#join() combines dataframes using indexes

#append() is deprecated

#inner join returns matching rows only

#left join returns all rows from left dataframe

#right join returns all rows from right dataframe

#outer join returns all rows from both dataframes