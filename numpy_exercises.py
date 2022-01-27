#%%
from itertools import product
import itertools
from statistics import mean
from scipy import stats
import numpy as np
import math
from numpy.lib import scimath

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
np_sqrt = np.emath.sqrt([a]) 
np_sqrt
print('the square root of array', np_sqrt)
np_mean = np.mean(np_sqrt)
print('mean of array', np_mean)
np_std = np.std(np_sqrt)
np_std
print('standard deviation of array', np_std)
#print(np.std(np_sqrt))
#np.std(square_a)

# %%
#6 
#centering your dataset (array) you need to find the mean
#then use lambda function to subract the mean from each datapoint 
print('mean of array', a.mean())
#lambda function to subtract the mean from dataset (array)
center_function = lambda x: x - x.mean()
# link data center to the center function 
data_centered = center_function(a)
print('centering of array', data_centered)
#to verify centering has accured the mean must equal 0
print('the mean of centered data must equal 0 ==', data_centered.mean())
# %%
# 7 
#Zscore using smypy 
print('z score with sympy', stats.zscore(a))
#zcore with numpy
np_zscore = (a-np.mean(a))/np.std(a)
print('zscore uing numpy', np_zscore)

# %%
# Life w/o numpy to life with numpy
#%%
## Setup 1
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a 
# to hold the sum of all the numbers in above list
sum_of_a = sum(list_a)
print(sum_of_a)
#%%
# Exercise 2 - Make a variable named min_of_a to 
# hold the minimum of all the numbers in the above list
min_of_a = min(list_a)
print(min_of_a)
#%%
# Exercise 3 - Make a variable named max_of_a to 
# hold the max number of all the numbers in the above list
max_of_a = max(list_a)
print(max_of_a)
#%%
# Exercise 4 - Make a variable named mean_of_a to 
# hold the average of all the numbers in the 
# above list
mean_of_a = mean(list_a)
print(mean_of_a)
#%%
# Exercise 5 - Make a variable named product_of_a 
# to hold the product of multiplying all the numbers in the above list together
product_of_a = math.prod()
print(product_of_a(list_a))
#%%
# Exercise 6 - Make a variable named squares_of_a. 
# should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = sum([x**2 for x in list_a])
print(math.sqrt(squares_of_a/len(list_a)))
#%%
# Exercise 7 - Make a variable named odds_in_a. It 
# hold only he odd numbers
odds_in_a = [x for x in list_a if x % 2 != 0]
print(odds_in_a)
    
#%%
# Exercise 8 - Make a variable named evens_in_a. 
# It should hold only the evens.
evens_in_a = [x for x in list_a if x % 2 == 0]
print(evens_in_a)
#%%
## What about life in two dimensions? A list of 
# lists is matrix, a table, a spreadsheet, a chessboard...

## Setup 2: Consider what it would take to find the sum, 
# min, max, average, sum, product, and list of squares 
# for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
#%%
# Exercise 1 - refactor the following to use numpy. 
# Use sum_of_b as the variable. **Hint, you'll first 
# need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
#%%
# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
#%%
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

#%%
# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
#%%
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
#%%
# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
#%%

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

#%%
# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
#%%
# Exercise 9 - print out the shape of the array b.

# Exercise 10 - transpose the array b.

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

# Exercise 2 - Determine the standard deviation of c.

# Exercise 3 - Determine the variance of c.

# Exercise 4 - Print out the shape of the array c

# Exercise 5 - Transpose c and print out transposed result.

# Exercise 6 - Get the dot product of the array c with c. 

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

# Exercise 2 - Find the cosine of all the numbers in d

# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2

# %%
