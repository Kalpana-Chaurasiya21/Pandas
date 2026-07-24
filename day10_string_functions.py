#importing pandas library

import pandas as pd



#creating dataframe

students = pd.DataFrame({

    "Student_ID":[101,102,103,104,105],

    "Name":["rahul","PRIYA","Aman","  Neha  ","Riya Sharma"],

    "Email":[

        "rahul@gmail.com",

        "priya@yahoo.com",

        "aman@gmail.com",

        "neha@gmail.com",

        "riya@hotmail.com"

    ],

    "City":["delhi","MUMBAI","Pune","lucknow","DELHI"]

})



print(students)



#str.lower()

#definition

#converts all characters

#into lowercase

#syntax

#series.str.lower()

#uses

#used to standardize text

#used before comparison

students["Name"] = students["Name"].str.lower()

print(students)



#str.upper()

#definition

#converts all characters

#into uppercase

#syntax

#series.str.upper()

#uses

#used in reports

#used for formatting

students["City"] = students["City"].str.upper()

print(students)



#str.title()

#definition

#converts first letter

#of every word into uppercase

#syntax

#series.str.title()

#uses

#used for names

#used for addresses

students["Name"] = students["Name"].str.title()

print(students)



#str.strip()

#definition

#removes spaces

#from beginning and end

#syntax

#series.str.strip()

#uses

#used for cleaning data

students["Name"] = students["Name"].str.strip()

print(students)



#str.replace()

#definition

#replaces old text

#with new text

#syntax

#series.str.replace(old,new)

#uses

#used to correct spelling

#used to replace words

students["City"] = students["City"].str.replace(

    "DELHI",

    "NEW DELHI"

)

print(students)



#str.contains()

#definition

#checks whether

#a string contains

#a specific word

#syntax

#series.str.contains("text")

#uses

#used for searching

#used for filtering

gmail_users = students[

    students["Email"].str.contains("gmail")

]

print(gmail_users)



#str.startswith()

#definition

#checks whether

#a string starts

#with a specific value

print(

    students["Email"].str.startswith("rahul")

)



#str.endswith()

#definition

#checks whether

#a string ends

#with a specific value

print(

    students["Email"].str.endswith(".com")

)



#str.split()

#definition

#splits string

#into a list

#syntax

#series.str.split(separator)

#uses

#used for extracting values

print(

    students["Email"].str.split("@")

)



#str.len()

#definition

#returns length

#of every string

#syntax

#series.str.len()

print(

    students["Name"].str.len()

)



#important interview points

#str.lower() converts text to lowercase

#str.upper() converts text to uppercase

#str.title() capitalizes every word

#str.strip() removes extra spaces

#str.replace() replaces text

#str.contains() searches text

#str.startswith() checks beginning

#str.endswith() checks ending

#str.split() splits text

#str.len() returns string length