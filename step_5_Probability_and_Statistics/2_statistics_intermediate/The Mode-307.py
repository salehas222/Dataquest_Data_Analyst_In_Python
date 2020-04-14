## 1. Introduction ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

houses['Land Slope'].unique()
houses['Kitchen AbvGr'].unique()
scale_land = 'ordinal'
scale_roof = 'nominal'
kitchen_variable = 'discrete'

## 2. The Mode for Ordinal Variables ##

houses['Land Slope'].value_counts()

# Defining a Mode function

def mode(array):
    counts = {}
    for a in array:
        if a in counts:
            counts[a] += 1
        else:
            counts[a] = 1
            
    return max(counts, key = counts.get)
mode_function = mode(houses['Land Slope'])
mode_function
mode_method = houses['Land Slope'].mode()
mode_method

same = (mode_function == mode_method)
same

## 3. The Mode for Nominal Variables ##

# The function we wrote (you can copy-paste yours from the previous screen)
def mode(array):
    counts = {}
    
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    return max(counts, key = counts.get)
houses['Roof Style'].value_counts()

# Editing the mode function so it also returns the counts dictionary

def mode(array):
    counts = {}
    for a in array:
        if a in counts:
            counts[a] += 1
        else:
            counts[a] = 1
            
    return (max(counts, key = counts.get), counts)
mode, value_counts = mode(houses['Roof Style'])
mode
value_counts

## 4. The Mode for Discrete Variables ##

houses['Kitchen AbvGr'].value_counts().sort_index()
houses['Bedroom AbvGr'].unique()
bedroom_variable = 'discrete'
bedroom_mode = houses['Bedroom AbvGr'].mode()
bedroom_mode
price_variable = 'continuous'

## 5. Special Cases ##

intervals = pd.interval_range(start = 0, end = 800000, freq = 100000)
gr_freq_table = pd.Series([0,0,0,0,0,0,0,0], index = intervals)

for value in houses['SalePrice']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break

print(gr_freq_table)
midpoint = 150000
mode = midpoint
mean = houses['SalePrice'].mean()
mean
median = houses['SalePrice'].median()
median
sentence_1 = True
sentence_2 = True

## 6. Skewed Distributions ##

distribution_1 = {'mean': 3021 , 'median': 3001, 'mode': 2947}
distribution_2 = {'median': 924 , 'mode': 832, 'mean': 962}
distribution_3 = {'mode': 202, 'mean': 143, 'median': 199}
import matplotlib.pyplot as plt

houses['SalePrice'].plot.kde(xlim = (houses['SalePrice'].min(),houses['SalePrice'].max()))
plt.axvline(150000, color = 'Green')
plt.axvline(houses['SalePrice'].median(), color = 'Black', label = 'Median')
plt.axvline(houses['SalePrice'].mean(), color = 'Orange', label = 'Mean')
plt.legend()
plt.show()
houses['Year Built'].plot.kde(xlim = (houses['Year Built'].min(),houses['Year Built'].max()))
plt.axvline(2005, color = 'Green')
plt.axvline(houses['Year Built'].median(), color = 'Black', label = 'Median')
plt.axvline(houses['Year Built'].mean(), color = 'Orange', label = 'Mean')
plt.legend()
plt.show()
shape_1 = 'right skew'
shape_2 = 'right skew'
shape_3 = 'left skew'

## 7. Symmetrical Distributions ##

houses['Mo Sold'].plot.kde(xlim=(1,12))
plt.axvline(houses['Mo Sold'].mode()[0], color='Green', label='Mode')
plt.axvline(houses['Mo Sold'].median(), color='Orange', label='Median')
plt.axvline(houses['Mo Sold'].mean(), color='Black', label='Mean')
plt.legend()
plt.show()