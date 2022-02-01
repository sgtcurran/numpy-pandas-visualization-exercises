#%%
from env import host, user, password, get_db_url
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pydataset import data

url = f'mysql+pymysql://{user}:{password}@{host}/employees'
#%%
url = f'mysql+pymysql://{user}:{password}@{host}/employees'

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)
#%%
sql = '''
SELECT
    emp_no,
    first_name,
    last_name
FROM employees
WHERE gender = 'F'
LIMIT 100
'''

employees = pd.read_sql(sql, url)
employees.head()


# %%
pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', get_db_url('employees'))


# %%
#must list a select and from what database
pd.read_sql(('SELECT *'), get_db_url(employee))
# %%
pd.read_sql('SELECT * FROM employees'), get_db_url('employees')
# %%
# 4. funtion to employees database
sql = '''
SELECT
    emp_no,
    first_name,
    last_name
FROM employees
WHERE gender = 'F'
LIMIT 100
'''

employees = pd.read_sql(sql, get_db_url('employees'))
employees.head()

# %%
query = '''
SELECT
    t.title as title,
    d.dept_name as dept_name
FROM titles t
JOIN dept_emp USING (emp_no)
JOIN departments d USING (dept_no)
LIMIT 100
'''

title_dept = pd.read_sql(query, url)
title_dept.head()



# %%
query = '''
SELECT * 
FROM employees
'''
employees = pd.read_sql(query, get_db_url('employees'))
employees
# %%
# Create the users DataFrame.

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users
#%%
# Create the roles DataFrame

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles
#%%
# Perform an outer join specifying the left and right DataFrame keys.

users.merge(roles, left_on='role_id', right_on='id', how='outer', indicator=True)


# %% 
# exercises 2
#1
from pydataset import data

(users.merge(roles, 
            left_on='role_id', 
            right_on='id', 
            how='outer')
    .drop(columns='role_id')
    .rename(columns={'id_x': 'id', 
                     'name_x': 'employee',
                     'id_y': 'role_id',
                     'name_y': 'role'}
            )
)

# %%
#2 
# Join left preserves the key role_id and merges 
# a new table 
#%%
#3 
#join right preserves the key id and merges it in 
# a new table
#%%
#4 
# merge otter perserves the keys from both dataframes
#%%
#5, 6, 
#7 there are 234 rows and 11 columns
mpg = data('mpg', show_doc=True)
[print(thing) for thing in mpg[]]
# %%
#
mpg = data('mpg')

# %%
#8 
mpg
# %%
#9 
mpg.describe()
#
# %%
mpg
# %%
#10
#There are 15 unique manufacturers 
mpg[['manufacturer']].describe()
mpg.manufacturer.nunique()
# %%
#10
mpg.manufacturer.unique()
#['audi', 'chevrolet', 'dodge', 'ford', 'honda', 'hyundai', 'jeep',
# 'land rover', 'lincoln', 'mercury', 'nissan', 'pontiac', 'subaru',
# toyota', 'volkswagen']
# %%
#11
#there are 38 unique models 
mpg[['model']].describe()
# %%
#11
mpg.model.unique()
#['a4', 'a4 quattro', 'a6 quattro', 'c1500 suburban 2wd', 'corvette',
#'k1500 tahoe 4wd', 'malibu', 'caravan 2wd', 'dakota pickup 4wd',
#'durango 4wd', 'ram 1500 pickup 4wd', 'expedition 2wd',
#'explorer 4wd', 'f150 pickup 4wd', 'mustang', 'civic', 'sonata',
#'tiburon', 'grand cherokee 4wd', 'range rover', 'navigator 2wd',
#'mountaineer 4wd', 'altima', 'maxima', 'pathfinder 4wd',
#'grand prix', 'forester awd', 'impreza awd', '4runner 4wd',
#'camry', 'camry solara', 'corolla', 'land cruiser wagon 4wd',
#'toyota tacoma 4wd', 'gti', 'jetta', 'new beetle', 'passat']
# %%
#12
mpg['mileage_difference'] = mpg[['cty', 'hwy']].std(axis = 1)
mpg.head()
# %%
#13
mpg['average_milage'] = mpg[['cty', 'hwy']].mean(axis = 1)
mpg
#%%
mpg.reindex()
# %%
#14
mpg['is_automatic'] = mpg[['trans']]
mpg[mpg['is_automatic'].str.contains('auto', regex=False)]
#%%
mpg.reindex()
# %%
#15 
# honda has the best average per gallon
mpg.groupby('manufacturer').average_milage.mean().idxmax()
# %%
#16
#manual has the best average mile per gallon 
mpg.groupby('trans').average_milage.mean().idxmax()
mpg

# %%
#Excercises 3 
#2
chipotle = pd.read_sql('SELECT * FROM orders',get_db_url('chipotle'))
chipotle
#%%
def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('$', '').replace(',', ''))
    return(x)
# %%
chipotle['item_price'] = chipotle['item_price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
#%%
chipotle['quantity'] = chipotle['quantity'].astype(float)
#%%
chipotle
#%%
chipotle['total_price'] = chipotle[['quantity','item_price']].sum(axis= 1)
#chipotle['total_price'] = chipotle['quantity']*['item_price']

#%%
chipotle.reindex()
# %%
chipotle
# %%

# %%
