#%%
from env import host, user, password, get_db_url
import pandas as pd



url = f'mysql+pymysql://{user}:{password}@{host}/employees'
#%%
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
