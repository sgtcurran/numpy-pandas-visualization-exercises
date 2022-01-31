#%%
import pandas as pd
import numpy as np
#notes to make a new column use the bracket quote syntax
#df["min"]
#%%

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))
index_labels=[students]
df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)
#%%
df.index


# %%
print(df)
# %%
df.info
# %%
df.describe()
# %%
df.dtypes

# %%
df.shape

# %%
#Exercise 1 

from pydataset import data

# %%
#A)
df.english > 70
df['passing english'] = df.english > 70
print(df)

#%%
#B & C & D
df.sort_values(by = 'passing english', ascending = True)
#%%
df.sort_values(by = ['passing english', 'name'], ascending = True)
#%%
df.sort_values(by = ['passing english', 'english'], ascending = False)

#%%
#final Grade mean 
df['final_grade'] = round(df[['math','english','reading']].mean(axis = 1))
df
# %%

mpg = data('mpg', show_doc=True)
# there are 234 rows and 11 columns 
#manufacturer     object
#model            object
#displ           float64
#year              int64
#cyl               int64
#trans            object
#drv              object
#cty               int64
#hwy               int64
#fl               object
#class            object
#
# %%
mpg = data('mpg')
 
# %%
mpg.info()
mpg.describe()
mpg.dtypes
# %%
mpg.rename(columns = {'cty': 'city' , 'hwy' : 'highway'}, inplace = True)
# %%
mpg[mpg.city > mpg.highway].sort_values(by = 'model')
mpg
#%%
mpg.reindex()
#%%%
mpg
# %%
mpg['mileage_difference'] = mpg[['city', 'highway']].std(axis = 1)
#%%
#
mpg.sort_values(by = ['mileage_difference'], ascending = False).head()
#%%
mpg.mileage_difference.max()
mpg
#%%
mpg['average_milage'] = mpg[['city', 'highway']].mean(axis = 1)
mpg

# %%
