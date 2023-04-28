import numpy as np
import matplotlib.pyplot as plt

#######################################################
###             EE-381 Final Project                ###
###                Name: Twan Tran                  ###
###                @ID : 029136612                  ###
#######################################################

# load text file
fname = 'Sales_01_20.csv'  # comma separated values

data = np.loadtxt(fname, delimiter=',', skiprows=1)

# make an array for the unique year as x-axis
years = np.unique(data[:, 0])

# make a dictionary to store the amount via year as key, ex: {2020 : [a, b , c, ...] }
amount = {}
for year in years:
    amount[year] = list(data[data[:, 0] == year, 1])
    
# make an array to store and calculate the average amount by year
avg_byYear = np.zeros(len(years))
for i, year in enumerate(years):
    avg_byYear[i] = np.mean(amount[year]).round(2)

# create the an array acting for x-axis
x = [2000, 2005, 2010, 2015, 2020]

# set figure size to hold the graph
fig = plt.figure(figsize=(7, 5))

# create Yearly Mean the bar graph with title, axis labels, and modified tick
plt.bar(years, avg_byYear)
plt.xticks(x, x)
plt.xlabel('Year')
plt.ylabel('Mean Price')
plt.title('Yearly Mean')
plt.show()
    
# make an array to store and calulate the STD by year 
std_byYear = np.zeros(len(years))
for i, year in enumerate(years):
    std_byYear[i] = np.std(amount[year]).round(2)

# create Yearly STD the bar graph with title, axis labels, and modified tick
plt.bar(years, std_byYear)
plt.xticks(x, x)
plt.xlabel('Year')
plt.ylabel('STD')
plt.title('Yearly STD')
plt.show()

# init a count to count values in between $200,000 - $300,000 (inclusive), 
# then store and calculate the Probability (count/total amound by year)
c = 0
prb_byYear = np.zeros(len(years))
for i, year in enumerate (years):
    for val in amount[year]:
        if val >=200000 and val <= 300000:
            c += 1
    prb_byYear[i] = round((c/len(amount[year])), 4)
    c = 0
    
# create Yearly Probability the bar graph with title, axis labels, and modified tick
plt.bar(years, prb_byYear)
plt.xticks(x, x)
plt.xlabel('Year')
plt.ylabel('PRB')
plt.title('Yearly Probability')
plt.show()