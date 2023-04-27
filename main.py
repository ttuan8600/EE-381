import numpy as np
import matplotlib.pyplot as plt

######  EE-381 Final Project ##########
# load text file
fname = 'Sales_01_20.csv' # comma separated values
data = np.loadtxt(fname, delimiter=',', skiprows=1)
print(data[:5])
years = np.unique(data[:, 0])

avg_byYear = np.zeros(len(years))

for i, year in enumerate(years):
    avg_byYear[i] = np.mean(data[data[:, 0] == year, 1]).round(2)

fig = plt.figure(figsize=(10, 7))
x = [2000, 2005, 2010, 2015, 2020]

plt.bar(years, avg_byYear)
plt.xticks(x, x)
plt.xlabel('Year')
plt.ylabel('Mean Price')
plt.title('Yearly Mean')
plt.show()
