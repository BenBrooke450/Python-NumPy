👉 No — numpy.insert and numpy.append do NOT operate in-place.

They return a new array. Your original array is unchanged unless you reassign the result.

 


```python
"""

Certainly! In Python, you can use NumPy to append elements to an array. Here are three different ways to do this:

 

Method 1: Using np.append()

"""

import numpy as np

# Create an initial array

 

arr = np.array([1, 2, 3])

# Append elements to the array

 

new_arr = np.append(arr, [4, 5, 6])

 

print(new_arr)

#[1, 2, 3, 4, 5, 6]

 

 ```

 

❗ Problem:

np.append() does not modify the array in place — it returns a new array.

So when you write:


np.append(array1, curr.val)

 
You're ignoring the new array returned by np.append, and array1 remains empty.