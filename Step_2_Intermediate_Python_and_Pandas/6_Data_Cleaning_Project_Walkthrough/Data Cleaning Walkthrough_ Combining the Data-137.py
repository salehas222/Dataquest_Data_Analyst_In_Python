## 3. Condensing the Class Size Data Set ##

class_size=data["class_size"]
class_size=class_size[class_size["GRADE "]=="09-12"]
class_size=class_size[class_size["PROGRAM TYPE"]=="GEN ED"]
class_size.head()

## 5. Computing Average Class Sizes ##

import numpy
class_size=class_size.groupby('DBN').agg(numpy.mean)
class_size.reset_index(inplace=True)
data['class_size']=class_size
print(data['class_size'].head())

## 7. Condensing the Demographics Data Set ##

data1=data['demographics']
data1=data1[data['demographics']['schoolyear']==20112012]
data['demographics']=data1
print(data['demographics'].head())

## 9. Condensing the Graduation Data Set ##

data1=data['graduation']
data1=data1[data1['Cohort']=='2006']
data1=data1[data1['Demographic']=='Total Cohort']
data['graduation']=data1
print(data['graduation'].head())

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
for i in cols:
    data['ap_2010'][i]=pd.to_numeric(data['ap_2010'][i], errors='coerce')
    
print(data['ap_2010'].dtypes)   

## 12. Performing the Left Joins ##

combined = data["sat_results"]
combined = combined.merge(data["ap_2010"],how="left",on="DBN")
combined = combined.merge(data["graduation"],how="left",on="DBN")
print(combined.head())
print("---------------")
print("---------------")
print(combined.shape)

## 13. Performing the Inner Joins ##

combined = combined.merge(data["class_size"],how="inner", on="DBN")
combined = combined.merge(data["demographics"],how="inner", on="DBN")
combined = combined.merge(data["survey"],how="inner", on="DBN")
combined = combined.merge(data["hs_directory"],how="inner", on="DBN")
print(combined.head())
print("---------------")
print("---------------")
print(combined.shape)

## 15. Filling in Missing Values ##

means = combined.mean()
combined = combined.fillna(means)
print(combined.head())
print("---------------")
print("---------------")
combined = combined.fillna(value=0)
print(combined.head())

## 16. Adding a School District Column for Mapping ##

def extracts21thchar(str):
    extract = str[0:2]
    return extract

combined["school_dist"] = combined["DBN"].apply(extracts21thchar)
print(combined.head())