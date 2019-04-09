import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

piechart= pd.read_csv('customerpie.csv')

print(piechart)
colors = ['darkorange', 'sandybrown', 'darksalmon', 'orangered','chocolate']


plt.pie(piechart['Percentage'],
        labels=piechart['Sector'],
        colors=colors,
        autopct='%.2f')

plt.axis('equal')

plt.show()