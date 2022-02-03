#%%
from env import host, user, password, get_db_url
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns


# %%
#
petal_data = pd.read_sql('SELECT * FROM measurements', get_db_url('iris_db'))
petal_data
# %% 
#1
sns.relplot(x='species_id', y='petal_length', data=petal_data)

#%%
#2 Yes wider the with longer the leaf
sns.relplot(x='petal_width', y='petal_length', data=petal_data)
# %%
#3 Yes you can id the plant species by 
# sepal length and width. species_1 is the 
# smallest length with an average with of 3
# .5 in. Species 2 length is average a 6 
# with an average width of 3.5 in. Species_3 
# has the longest length average at 7 with a width of 3.2
sns.relplot(x='sepal_width', y='sepal_length', 
col='species_id', data=petal_data
)
plt.show()
# %%
#4 
#scatterplot with species_id as col and x=sepal_width and y sepal_length w/size=petal_length 
sns.relplot(x='sepal_width', y='sepal_length', 
col='species_id', size='petal_length', data=petal_data
)
# %%
anscombe = sns.load_dataset('anscombe')
anscombe
# %%
#Exercise 2 
#1 that the x count is 11, mean, std is all the same
anscombe.groupby(['dataset']).describe().T

#%%
#1 scatterplots
sns.relplot(x='x', y='y', col='dataset', data=anscombe)
# %%
insect = data('InsectSprays')
data('InsectSprays', show_doc=True)

# %%
#2
sns.boxenplot(x='count', y='spray', data=insect)
# %%
swiss_db = data('swiss')
swiss_db
# %%
is_catholic = 
# %%
