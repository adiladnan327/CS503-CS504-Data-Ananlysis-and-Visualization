#define the tools both the pandas and matplotlib
import pandas
import numpy
import matplotlib.pyplot as plt

#reading the csv file with index value=o
table= pandas.read_csv('NumberofCustomer.csv', index_col=0)

df=table.head(20)
plt.plot(table)
plt.axis([2000,2019, 1,300000])
print(table)
plt.legend()
plt.grid()
plt.xlabel('Number of years')
plt.ylabel('Number of Customers')
plt.title('Store DataSets')
plt.show()
