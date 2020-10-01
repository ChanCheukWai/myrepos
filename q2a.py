import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('GOOGL.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots, None)
    for row in plots:
        y.append(float(row[4]))
    x = range(0, len(y))

plt.plot(x,y)
plt.xlabel('Days started from 11/13/2017 and end on 11/12/2018')
plt.ylabel('Stock price of GOOGL at closing')
plt.title('Stock price of GOOGL at closing for 11/13/2017-11/12/2018')
#plt.legend()
plt.show()