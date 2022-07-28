from pandas import *

data1 ="./data/daily_sales_data_0.csv"
data2 = "./data/daily_sales_data_1.csv"
data3 = "./data/daily_sales_data_2.csv"

#join files
totalRaw = concat(map(read_csv, [data1, data2, data3]))
totalRaw = totalRaw[totalRaw['product'].str.contains('pink morsel')]
totalRaw.to_csv()

#needed data
price =totalRaw['price'].str.replace('$', '').astype(float)
quantity = totalRaw['quantity'].astype(float)
product = totalRaw['product']
sales = (price * quantity).tolist()
date = totalRaw['date'].tolist()
region = totalRaw['region'].tolist()

#final output
df = DataFrame({'product': product, 'sales($)': sales, 'date': date, 'region': region} )
df.to_csv("./complete.csv")