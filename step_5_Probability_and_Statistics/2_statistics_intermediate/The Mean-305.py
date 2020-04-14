## 2. The Mean ##

distribution = [0,2,3,3,3,4,13]
mean = sum(distribution)/len(distribution)
mean

below = []
above = []

for value in distribution:
    if value < mean:
        below.append(mean - value)
    if value > mean:
        above.append(value - mean)

equal_distances = (sum(above) == sum(below))
equal_distances
center=False

## 3. The Mean as a Balance Point ##

from numpy.random import randint, seed

equal_distances = 0

for i in range(5000):
    seed(i) # Seed the generator
    
    distribution = randint(0,1000,10)
    mean = sum(distribution) / len(distribution)
    
    below = []
    above = []
    
    for value in distribution:
        if value == mean:
            continue
        if value < mean:
            below.append(mean - value)
        if value > mean:
            above.append(value - mean)
    
    sum_above = round(sum(above),1)
    sum_below = round(sum(below),1)
    
    if (sum_above == sum_below):
        equal_distances += 1

print(equal_distances)

## 4. Defining the Mean Algebraically ##

def mean_func(distribution):
    sum_dist = 0
    for d in distribution:
        sum_dist = sum_dist + d
        
    return sum_dist / len(distribution)

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

one=False
two=False
three=False

## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

def meanfunc(array):
    sum=0
    for each in array:
        sum=sum+each
        
    return sum/len(array)
        
    
mean_1=meanfunc(distribution_1)
mean_2=meanfunc(distribution_2)
mean_3=meanfunc(distribution_3)

## 6. Introducing the Data ##

import pandas as pd
houses=pd.read_table('AmesHousing_1.txt')
houses.head()
one=True
two=False
three=True

## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)
function_mean=mean(houses['SalePrice'])
pandas_mean=houses['SalePrice'].mean()
means_are_equal=(function_mean==pandas_mean)


## 8. Estimating the Population Mean ##

salesmean=houses['SalePrice'].mean()
size=5
samp_err=[]
sample_sizes=[]
for each in range(101):
    dist=houses['SalePrice'].sample(size,random_state=each)
    mean=sum(dist)/len(dist)
    samp_err.append(salesmean-mean)
    sample_sizes.append(size)
    size=size+29
    
import matplotlib.pyplot as plt
plt.scatter(sample_sizes, samp_err)
plt.axhline(0)
plt.axvline(2930)
plt.xlabel('Sample size')
plt.ylabel('Sampling error')

## 9. Estimates from Low-Sized Samples ##

means=[]
for i in range(10000):
    samp=houses['SalePrice'].sample(100,random_state=i)
    means.append(sum(samp)/len(samp))
    
plt.hist(means)
plt.axvline(houses['SalePrice'].mean())
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.xlim(0,500000)

## 11. The Sample Mean as an Unbiased Estimator ##

population = [3, 7, 2]
samples = [[3, 7], [3, 2],
           [7, 2], [7, 3],
           [2, 3], [2, 7]
          ]

sample_means = []
for sample in samples:
    sample_means.append(sum(sample) / len(sample))
    
population_mean = sum(population) / len(population)
mean_of_sample_means = sum(sample_means) / len(sample_means)

unbiased = (population_mean == mean_of_sample_means)