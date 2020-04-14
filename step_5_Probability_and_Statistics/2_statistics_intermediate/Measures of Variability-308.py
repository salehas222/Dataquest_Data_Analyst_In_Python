## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')
houses.head()
def find_range(array):
    return max(array) - min(array)
years = houses['Yr Sold'].unique()
years

range_by_year = {}

for year in years:
    range_by_year[year] = find_range(houses[houses['Yr Sold'] == year]['SalePrice'])
    
range_by_year
two = True
one = False

## 2. The Average Distance ##

def avg_dist(array):
    mean = sum(array)/len(array)
    distances = []
    for element in array:
        distance = element - mean
        distances.append(distance)
        
    return sum(distances)/len(distances)
C = [1,1,1,1,1,1,1,1,1,21]

C_average_distance = avg_dist(C)
avg_distance = C_average_distance

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]
def mean_abs_dist(array):
    mean = sum(array)/len(array)
    distances = []
    for element in array:
        distance = abs(element-mean)
        distances.append(distance)
        
    return sum(distances)/len(distances)
mad = mean_abs_dist(C)
mad

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]

def variance(array):
    mean = sum(array)/len(array)
    distances = []
    for element in array:
        distance = (element-mean) ** 2
        distances.append(distance)
        
    return sum(distances)/len(distances)
variance_C = variance(C)
variance_C

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]

def sd(array):
    mean = sum(array)/len(array)
    distances=[]
    for element in array:
        distance = (element-mean) ** 2
        distances.append(distance)
        
    return sqrt(sum(distances)/len(distances))

standard_deviation_C = sd(C)
standard_deviation_C

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
mean = houses['SalePrice'].mean()
st_dev = sd(houses['SalePrice'])

houses['SalePrice'].plot.hist()
plt.axvline(mean, color = 'Black', label = 'Mean')
plt.axvline(mean - st_dev, color = 'Red', label = 'Below')
plt.axvline(mean + st_dev, color = 'Violet', label = 'Above')
plt.legend()
plt.show()

years = {}

for year in houses['Yr Sold'].unique():
    years[year] = sd(houses[houses['Yr Sold'] == year]['SalePrice'])

greatest_variability = max(years, key = years.get)
greatest_variability

lowest_variability = min(years, key = years.get)
lowest_variability

## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

for i in range(1,5):
    sample = houses['SalePrice'].sample(50, random_state = i)
    st_dev = sd(sample)
    print('Sample ' + str(i) + ': ' + str(st_dev))
 
sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

st_dev1 = sd(sample1)
print(st_dev1)
st_dev2 = sd(sample2)
print(st_dev2)
bigger_spread = 'sample 2'

## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt

s_d = []
for i in range(5000):
    s = houses['SalePrice'].sample(10,random_state=i)
    s_d.append(sd(s))
    
plt.hist(s_d)
plt.axvline(sd(houses['SalePrice']), color = 'r')
plt.show()
sum(s_d) / 5000
sd(houses['SalePrice'])

## 9. Bessel's Correction ##

from math import sqrt
def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances)/(len(distances)-1)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)

plt.hist(st_devs)
plt.axvline(pop_stdev)  # pop_stdev is pre-saved from the last screen



## 10. Standard Notation ##

from numpy import std, var
sample = houses.sample(100, random_state = 1)
from numpy import std, var
pandas_std = sample['SalePrice'].std(ddof=1)
numpy_std = std(sample['SalePrice'],ddof=1)
equal_stdevs = (pandas_std == numpy_std)
equal_stdevs

pandas_var = sample['SalePrice'].var(ddof=1)
numpy_var = var(sample['SalePrice'],ddof=1)
equal_vars = pandas_var == numpy_var

numpy_stdev = 76469.14464354333
pandas_stdev = 76469.14464354333

## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]


pop_var = var(population, ddof = 0)
pop_std = std(population, ddof = 0)
stds = []
variances = []

for s in samples:
    stds.append(std(s, ddof = 1))
    variances.append(var(s, ddof = 1))
    
mean_std = sum(stds) / len(stds)
mean_var = sum(variances) / len(variances)
equal_stdev = (pop_std == mean_std)
equal_var = (pop_var == mean_var)
