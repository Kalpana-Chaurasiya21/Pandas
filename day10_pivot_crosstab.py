#importing pandas library

import pandas as pd



#creating dataframe

sales = pd.DataFrame({

    "Salesperson":["Rahul","Rahul","Priya","Priya","Aman","Aman"],

    "City":["Delhi","Mumbai","Delhi","Mumbai","Delhi","Mumbai"],

    "Product":["Laptop","Mouse","Laptop","Keyboard","Mouse","Laptop"],

    "Sales":[65000,1500,70000,2500,1800,68000]

})



print(sales)



#pivot_table()

#definition

#pivot_table() summarizes data

#by grouping rows and columns

#and applying aggregate functions

#it is similar to Excel Pivot Table

#syntax

#pd.pivot_table(data,index,columns,values,aggfunc)

#uses

#used for sales reports

#used for business dashboards

#used in data analysis



sales_summary = pd.pivot_table(

    sales,

    index="Salesperson",

    values="Sales",

    aggfunc="sum"

)



print(sales_summary)



#pivot table using rows and columns

city_summary = pd.pivot_table(

    sales,

    index="Salesperson",

    columns="City",

    values="Sales",

    aggfunc="sum",

    fill_value=0

)



print(city_summary)



#multiple aggregation functions

multiple_summary = pd.pivot_table(

    sales,

    index="Salesperson",

    values="Sales",

    aggfunc=["sum","mean","max"]

)



print(multiple_summary)



#crosstab()

#definition

#crosstab() calculates

#frequency between two columns

#syntax

#pd.crosstab(row,column)

#uses

#used for frequency analysis

#used in survey analysis

#used in categorical data analysis



city_frequency = pd.crosstab(

    sales["Salesperson"],

    sales["City"]

)



print(city_frequency)



#sort_index()

#definition

#sort_index() sorts dataframe

#using row or column indexes

#syntax

#dataframe.sort_index()

#uses

#used after groupby

#used after pivot table



sorted_rows = city_summary.sort_index()

print(sorted_rows)



sorted_columns = city_summary.sort_index(

    axis=1

)

print(sorted_columns)



#reset_index()

#definition

#reset_index() converts

#index into a normal column

#syntax

#dataframe.reset_index()

#uses

#used after groupby

#used after pivot tables



reset_dataframe = city_summary.reset_index()

print(reset_dataframe)



#set_index()

#definition

#set_index() converts

#a column into dataframe index

#syntax

#dataframe.set_index(column_name)

#uses

#used for faster lookup

#used before joining dataframes



indexed_dataframe = sales.set_index(

    "Salesperson"

)



print(indexed_dataframe)



#important interview points

#pivot_table() summarizes data

#crosstab() counts frequencies

#sort_index() sorts indexes

#reset_index() converts index into a column

#set_index() converts a column into index