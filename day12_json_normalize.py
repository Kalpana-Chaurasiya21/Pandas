#importing pandas library

import pandas as pd



#creating nested json data

students = [

    {

        "Student_ID":101,

        "Name":"Rahul",

        "Address":{

            "City":"Delhi",

            "State":"Delhi"

        },

        "Marks":{

            "Math":90,

            "Science":95

        }

    },

    {

        "Student_ID":102,

        "Name":"Priya",

        "Address":{

            "City":"Mumbai",

            "State":"Maharashtra"

        },

        "Marks":{

            "Math":85,

            "Science":88

        }

    },

    {

        "Student_ID":103,

        "Name":"Aman",

        "Address":{

            "City":"Lucknow",

            "State":"Uttar Pradesh"

        },

        "Marks":{

            "Math":92,

            "Science":90

        }

    }

]



print(students)



#json_normalize()

#definition

#json_normalize()

#converts nested json

#into a flat dataframe

#syntax

#pd.json_normalize(json_data)

#uses

#used for api responses

#used for nested json files

#used for web scraping projects

student_dataframe = pd.json_normalize(

    students

)



print(student_dataframe)



#using separator

#definition

#sep changes

#nested column names

#syntax

#pd.json_normalize(data,sep="_")

student_dataframe = pd.json_normalize(

    students,

    sep="_"

)



print(student_dataframe)



#accessing nested columns

print(

    student_dataframe[

        [

            "Address_City",

            "Marks_Math"

        ]

    ]

)



#adding calculated column

student_dataframe["Total_Marks"] = (

    student_dataframe["Marks_Math"]

    +

    student_dataframe["Marks_Science"]

)



print(student_dataframe)



#sorting students

sorted_students = student_dataframe.sort_values(

    by="Total_Marks",

    ascending=False

)



print(sorted_students)



#important interview points

#json_normalize() flattens nested json

#commonly used with api data

#creates dataframe from nested objects

#sep changes nested column names

#works well with web service responses