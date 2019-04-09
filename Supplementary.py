import pandas as pd
df = pd.read_csv ('SupplementaryTable.csv', index_col=0)

# block 1 - simple stats
mean1 = df['customers'].mean()
sum1 = df['customers'].sum()
max1 = df['customers'].max()
min1 = df['customers'].min()
count1 = df['customers'].count()
median1 = df['customers'].median()
std1 = df['customers'].std()
var1 = df['customers'].var()

# block 2 - group by
groupby_sum1 = df.groupby(['Country']).sum()
groupby_count1 = df.groupby(['Country']).count()

# print block 1
print ('Mean customers: ' + str(mean1))
print ('Sum of customers: ' + str(sum1))
print ('Max customers: ' + str(max1))
print ('Min customers: ' + str(min1))
print ('Count of customers: ' + str(count1))
print ('Median customers: ' + str(median1))
print ('Standard Deviation of customers: ' + str(std1))
print ('Variance of customers: ' + str(var1))

# print block 2
print ('Sum of values, grouped by the Country: ' + str(groupby_sum1))
