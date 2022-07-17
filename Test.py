from pandas import *
#read files
data1 = read_csv("./data/daily_sales_data_0.csv")
data2 = read_csv("./data/daily_sales_data_1.csv")
data3 = read_csv("./data/daily_sales_data_2.csv")

#filter pink morsel products
data1 = data1[data1['product'].str.contains('pink morsel')]
data2 = data2[data2['product'].str.contains('pink morsel')]
data3 = data3[data3['product'].str.contains('pink morsel')]

#filtered products
data1.to_csv("./data1.csv")
data2.to_csv("./data2.csv")
data3.to_csv("./data3.csv")

#join files
total = concat(map(read_csv, ['./data1.csv', './data2.csv', './data3.csv']))
trim = total.drop(total.columns[[0]], axis=1)
trim.to_csv('totalData.csv')
data = read_csv("./totalData.csv")

#needed data
price =data['price'].str.replace('$', '').astype(float)
quantity = data['quantity'].astype(float)
product = data['product']
sales = (price * quantity).tolist()
date = data['date'].tolist()
region = data['region'].tolist()

#final output
df = DataFrame({'product': product, 'sales($)': sales, 'date': date, 'region': region} )
df.to_csv("./complete.csv")
