#importing pandas library

import pandas as pd



#creating dataframe

students = pd.DataFrame({

    "Student_ID":[101,102,103,104],

    "Name":["Rahul","Priya","Aman","Neha"],

    "Marks":[85,92,76,88],

    "City":["Delhi","Mumbai","Pune","Lucknow"]

})



print(students)



#applymap()

#definition

#applymap() applies a function

#to every element of a dataframe

#it is mainly used for element wise operations

#note

#in newer versions of pandas

#DataFrame.map() is preferred for element wise operations

#applymap() may be deprecated in future versions

#syntax

#dataframe.applymap(function)

#uses

#used for formatting

#used for converting text

#used for modifying every value



text = pd.DataFrame({

    "A":["python","sql"],

    "B":["pandas","numpy"]

})



uppercase = text.applymap(

    lambda value:value.upper()

)



print(uppercase)



#assign()

#definition

#assign() creates one or more new columns

#without modifying the original dataframe

#it returns a new dataframe

#syntax

#dataframe.assign(column=value)

#uses

#used in method chaining

#used to create calculated columns



new_students = students.assign(

    Percentage=students["Marks"]

)



print(new_students)



#insert()

#definition

#insert() adds a new column

#at a specific position

#syntax

#dataframe.insert(location,column_name,values)

#uses

#used when column order matters

#used while preparing reports



students.insert(

    2,

    "Age",

    [20,21,22,23]

)



print(students)



#pop()

#definition

#pop() removes a column

#and returns it

#syntax

#dataframe.pop(column_name)

#uses

#used when the removed column

#is still required separately



removed_column = students.pop("Age")



print(removed_column)



print(students)



#drop()

#definition

#drop() removes rows or columns

#from a dataframe

#syntax

#dataframe.drop(labels,axis)

#axis=0 removes rows

#axis=1 removes columns

#uses

#used for removing unwanted data



without_city = students.drop(

    columns=["City"]

)



print(without_city)



without_first_row = students.drop(

    index=0

)



print(without_first_row)



#important interview points

#applymap() applies function to every dataframe element

#assign() creates new columns without modifying original dataframe

#insert() adds column at a specific position

#pop() removes and returns a column

#drop() removes rows or columns