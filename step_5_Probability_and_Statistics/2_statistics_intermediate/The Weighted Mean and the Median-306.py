## 1. Introduction ##

mean_new=houses_per_year['Mean Price'].mean()

mean_original = houses['SalePrice'].mean()

difference = mean_original - mean_new
difference

## 2. Different Weights ##

houses_per_year['sum_per_year'] = houses_per_year['Mean Price'] * houses_per_year['Houses Sold']

all_sums_together = houses_per_year['sum_per_year'].sum()

total_n_houses = houses_per_year['Houses Sold'].sum()

weighted_mean = all_sums_together / total_n_houses

mean_original = houses['SalePrice'].mean()

difference = round(mean_original, 10) - round(weighted_mean, 10)
difference

## 3. The Weighted Mean ##


from numpy import average

weighted_mean_numpy = average(houses_per_year['Mean Price'], weights = houses_per_year['Houses Sold'])
weighted_mean_numpy
equal = round(weighted_mean_function, 10) == round(weighted_mean_numpy, 10)
equal

## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']
median1 = 23
median2 = 55
median3 = 32

## 5. Distributions with Even Number of Values ##

rooms_above_ground = houses['TotRms AbvGrd'].copy()
rooms_above_ground = rooms_above_ground.replace({'10 or more':'10'})
rooms_above_ground = rooms_above_ground.astype(int)
rooms_above_ground = rooms_above_ground.sort_values()

middle_indices = [int((len(rooms_above_ground) / 2)), int((len(rooms_above_ground) / 2 + 1))]

middle_values = rooms_above_ground.iloc[middle_indices] 

median = middle_values.mean()
median

## 6. The Median as a Resistant Statistic ##

import matplotlib.pyplot as plt
houses['Lot Area'].plot.box()
houses['SalePrice'].plot.box()
lot_mean = houses['Lot Area'].mean()
lot_mean
sale_mean = houses['SalePrice'].mean()
sale_mean
lot_med = houses['Lot Area'].median()
lot_med
sale_med = houses['SalePrice'].median()
sale_med
lotarea_difference = lot_mean - lot_med
lotarea_difference
saleprice_difference = sale_mean-sale_med
saleprice_difference

## 7. The Median for Ordinal Scales ##

houses['Overall Cond'].value_counts().sort_index()
mean = houses['Overall Cond'].mean()
mean
median = houses['Overall Cond'].median()
median
houses['Overall Cond'].plot.hist() 
plt.axvline(mean, c = 'red')
plt.axvline(median, c = 'black')
plt.show()
more_representative = 'mean'