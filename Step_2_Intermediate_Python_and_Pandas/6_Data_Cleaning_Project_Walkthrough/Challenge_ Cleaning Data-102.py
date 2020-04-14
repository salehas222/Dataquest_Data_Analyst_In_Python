## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

#avengers['Year'].hist()

true_avengers = avengers[avengers["Year"] > 1960]
true_avengers['Year'].hist()

## 5. Consolidating Deaths ##

col_death = ["Death1","Death2","Death3","Death4","Death5"]

#for col in col_death:
#    true_avengers[col] = true_avengers[col].fillna("NO")

#print("----------------")
#print(true_avengers[["Death1","Death2","Death3","Death4","Death5"]].head())

def convdeath(str):
    if str == "YES":
        return int(1)
    else:
        return int(0)
    
#for col in col_death:
#    true_avengers[col] = true_avengers[col].apply(convdeath)

#print("----------------")
#print(true_avengers[["Death1","Death2","Death3","Death4","Death5"]].head())

def sumdeath(df):
    res = 0
    for col in col_death:
        if df[col] == 'YES':
            res += 1
    return res

true_avengers["Deaths"] = true_avengers.apply(sumdeath,axis=1)

print("----------------")
print(true_avengers[["Deaths","Death1","Death2","Death3","Death4","Death5"]].head())

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()

print("----------------")
print(true_avengers.info())
print("----------------")

print(true_avengers[["Year","Years since joining"]].head())

def testyearssincecol(df):
    if 2015 - df["Years since joining"] == df["Year"]:
        return 1
    else:
        return 0

true_avengers["test"] = true_avengers.apply(testyearssincecol,axis=1)

joined_accuracy_count = true_avengers["test"].sum()
print(joined_accuracy_count)
print(true_avengers[["Year","Years since joining","test"]].head())

# more simple ...
joined_accuracy_count  = int()
correct_joined_years = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]
joined_accuracy_count = len(correct_joined_years)
