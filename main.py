import numpy as np
import matplotlib.pyplot as plt

######  EE-381 Final Project ##########

# load text file
fname = 'Sales_01_20.csv'  # comma separated values

data = np.loadtxt(fname, delimiter=',', skiprows=1)

# make an array for the unique year as x-axis
years = np.unique(data[:, 0])

# make an zeros array with the len as years
avg_byYear = np.zeros(len(years))

# iterate through the data, get an array of value for each matching year, then avg them, round by 2 decimal
for i, year in enumerate(years):
    avg_byYear[i] = np.mean(data[data[:, 0] == year, 1]).round(2)

# set the size for the figure contain the bar graph
fig = plt.figure(figsize=(10, 7))

# create the an array acting for x-axis
x = [2000, 2005, 2010, 2015, 2020]

# create the bar graph with title, axis labels, and modified tick
plt.bar(years, avg_byYear)
plt.xticks(x, x)
plt.xlabel('Year')
plt.ylabel('Mean Price')
plt.title('Yearly Mean')
plt.show()
