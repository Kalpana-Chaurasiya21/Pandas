#importing pandas library

import pandas as pd



#creating dataframe

sales = pd.DataFrame({

    "Date":[

        "2025-01-01",

        "2025-01-02",

        "2025-01-03",

        "2025-01-04",

        "2025-01-05",

        "2025-01-06"

    ],

    "Sales":[

        1200,

        1500,

        1800,

        1600,

        2000,

        2200

    ]

})



print(sales)



#to_datetime()

#definition

#converts string dates

#into datetime format

#syntax

#pd.to_datetime(column)

#uses

#required before performing

#time series operations

sales["Date"] = pd.to_datetime(

    sales["Date"]

)



#set_index()

#definition

#set_index()

#sets date column

#as dataframe index

#syntax

#dataframe.set_index(column_name)

#uses

#required for resampling

#and time based analysis

sales = sales.set_index(

    "Date"

)



print(sales)



#shift()

#definition

#shift() moves values

#up or down

#without changing

#the original data

#syntax

#series.shift(number)

#uses

#used to compare

#current value

#with previous value

sales["Previous_Day_Sales"] = sales["Sales"].shift(

    1

)



print(sales)



#diff()

#definition

#diff() calculates

#difference between

#current value

#and previous value

#syntax

#series.diff()

#uses

#used to calculate

#daily increase

#or decrease

sales["Sales_Difference"] = sales["Sales"].diff()



print(sales)



#pct_change()

#definition

#pct_change() calculates

#percentage change

#between current

#and previous value

#syntax

#series.pct_change()

#uses

#used in stock market

#used in business growth

sales["Growth_Percentage"] = sales["Sales"].pct_change()



print(sales)



#rolling()

#definition

#rolling()

#creates moving window

#for calculations

#syntax

#series.rolling(window)

#uses

#used for moving averages

sales["Moving_Average"] = sales["Sales"].rolling(

    window=3

).mean()



print(sales)



#resample()

#definition

#resample()

#groups time series data

#into different intervals

#syntax

#dataframe.resample(rule)

#uses

#used for weekly reports

#monthly reports

#yearly reports



weekly_sales = sales.resample(

    "W"

).sum()



print(weekly_sales)



monthly_sales = sales.resample(

    "M"

).sum()



print(monthly_sales)



#important interview points

#shift() compares current and previous values

#diff() calculates difference

#pct_change() calculates percentage change

#rolling() calculates moving statistics

#resample() groups time based dataS