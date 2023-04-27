import numpy as np
import matplotlib.pyplot as plt

######  EE-381 Final Project ##########
# load text file
fname = 'Sales_01_20.csv' # comma separated values
data = np.loadtxt(fname, delimiter=',', skiprows=1)

df = pd.DataFrame(data, columns=['year', 'amount'])
print(df.head())

df_yearly_avg = df.groupby('year')['amount'].mean().round(2)
df_yearly_std = df.groupby('year')['amount'].std().round(2)

print(df_yearly_avg.head())
print(df_yearly_std.head())

df_yearly_avg.plot(kind='bar', xlabel='Year', ylabel='Mean Price', title='Mean Price by Year')
plt.show()

df_yearly_std.plot(kind='bar', xlabel='Year', ylabel='STD', title='STD by Year')
plt.show()

# fig, ax = plt.subplots(1, 2)   # Create a figure containing a single axes
# ax[0].hist(data1, ec='black')
# ax[0].set_title("Equal width bins")
#
# ax[1].hist(data1, ec='black', bins=[2, 4, 6, 8, 12, 20, 30])
# ax[1].set_title("Unequal width")
#
# ax[0].set_xlabel('Bond strength')
# ax[1].set_xlabel('Bond strength')
# ax[0].set_ylabel('')
# plt.show()
