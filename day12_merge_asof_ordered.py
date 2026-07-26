#importing pandas library

import pandas as pd



#creating first dataframe

orders = pd.DataFrame({

    "Time":[

        "2025-01-01 09:00",

        "2025-01-01 10:00",

        "2025-01-01 11:00",

        "2025-01-01 12:00"

    ],

    "Order_ID":[101,102,103,104]

})



#creating second dataframe

prices = pd.DataFrame({

    "Time":[

        "2025-01-01 08:30",

        "2025-01-01 09:30",

        "2025-01-01 11:30"

    ],

    "Price":[500,550,600]

})



#converting string to datetime

orders["Time"] = pd.to_datetime(

    orders["Time"]

)

prices["Time"] = pd.to_datetime(

    prices["Time"]

)



#sorting dataframes

#merge_asof() requires

#both dataframes

#to be sorted

orders = orders.sort_values(

    "Time"

)

prices = prices.sort_values(

    "Time"

)



print(orders)

print(prices)



#merge_asof()

#definition

#merge_asof()

#matches each row

#with the nearest value

#instead of an exact match

#syntax

#pd.merge_asof(left,right,on="column")

#uses

#used in stock market

#used in sensor data

#used in transaction logs

nearest_price = pd.merge_asof(

    orders,

    prices,

    on="Time"

)



print(nearest_price)



#forward direction

#definition

#matches next

#available value

forward_merge = pd.merge_asof(

    orders,

    prices,

    on="Time",

    direction="forward"

)



print(forward_merge)



#nearest direction

#definition

#matches closest

#previous or next value

nearest_merge = pd.merge_asof(

    orders,

    prices,

    on="Time",

    direction="nearest"

)



print(nearest_merge)



#creating ordered dataframes

sales_2024 = pd.DataFrame({

    "Month":["Jan","Feb","Mar"],

    "Sales":[1200,1400,1600]

})



sales_2025 = pd.DataFrame({

    "Month":["Apr","May","Jun"],

    "Sales":[1800,2000,2200]

})



#merge_ordered()

#definition

#merge_ordered()

#merges ordered data

#while preserving order

#syntax

#pd.merge_ordered(left,right,on="column")

#uses

#used for time series

#used for ordered reports

merged_sales = pd.merge_ordered(

    sales_2024,

    sales_2025,

    on="Month",

    fill_method=None

)



print(merged_sales)



#important interview points

#merge_asof() matches nearest values

#requires sorted data

#works on ordered columns

#merge_ordered() preserves order

#used in time series analysis