import  pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean

style.use('fivethirtyeight')

#reading the csv file
country=pd.read_csv('BargrapghSale.csv', index_col=0)
#reading only first five file
df= country.head(5)
#setting the index value with country code
df=df.set_index(["Country Code"])
#reading only last five file
dc=country.tail(5)
dc=dc.set_index(["Country Code"])
print(country)
sd=df.reindex(columns=['2010','2011'])
sc=dc.reindex(columns=['2015','2018'],)
print(sd)
print(sc)
de=sc.diff(axis=1)
db=sd.diff(axis=1)
db.plot(kind='bar')
de.plot(kind='bar')
plt.show()
