import pandas as pd
import numpy as np

number = pd.Series([50,14,15,7,8])
r = np.diff(np.sign(np.diff(number)))#Calculate the n-th discrete
results = np.where(r==-2)[0]+1
print(results)

my_str = 'dbc deb abed gade'
list = pd.Series(list(my_str))
count  = list.value_counts()#containing counts of unique values
least_count = count.dropna().index[-1]#Remove missing values.
print("".join(list.replace(" ",least_count)))

ser = pd.Series(np.arange(20) + np.random.normal(1, 10, 20))#Return evenly spaced values within a given interval.
autocorrelations = [ser.autocorr(i).round(2) for i in range(11)]
print(autocorrelations[1:])

L = pd.Series(range(15))
