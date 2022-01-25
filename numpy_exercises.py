#%%
import numpy as np
import math
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# %%
#1 There are 4 negitive numbers 
a[a < 0]
# %%
#2 There are 5 positive numbers 
a[a > 0]
# %% 3
#3 boolian array 
is_pos = a > 0
is_even = a % 2 == 0
a[is_pos & is_even]
#non boolean array 
a[(a>0)&(a%2==0)]

# %% 12 
#4 boolian array
plus_3 = a
plus_3 + 3
is_pos = a > 0
a[plus_3 & is_pos]
# non boolean array
a[(a + 3) & (a > 0)]
# %%
#5
arr = np.sqrt([a]) 
arr
print(arr)
np.sum(arr)
#np.std(square_a)

# %%
