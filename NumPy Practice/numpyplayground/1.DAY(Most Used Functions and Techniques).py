

import numpy as np

np.array([1, 2, 3])            # From list

a = np.zeros((2, 3))                # Array of zeros
print(a)
"""
[[0. 0. 0.]
 [0. 0. 0.]]
"""

np.ones((3, 2))                 # Array of ones


np.full((2, 2), 7)              # Filled with 7


np.arange(0, 10, 2)
# [0 2 4 6 8]


np.linspace(0, 1, 5)
# Evenly spaced: [0.  0.25 0.5 0.75 1.]


np.random.rand(3, 2)            # Uniform random


np.random.randn(3, 2)           # Normal distribution


np.random.randint(0, 10, 5)     # Random ints [0, 10)






#2. Array Inspection
arr.shape            # Dimensions
arr.ndim             # Number of axes
arr.size             # Total number of elements
arr.dtype            # Data type
arr.itemsize         # Size (in bytes) of each element




#3. Indexing and Slicing
arr[1]               # Single index
arr[1:4]             # Slice (1 to 3)
arr[:, 1]            # All rows, column 1
arr[1, :]            # Row 1, all columns
arr[::2]             # Every other element




#4. Reshaping
arr.reshape((3, 2))  # New shape
arr.flatten()        # 1D copy
arr.T                # Transpose



#5. Mathematical Operations
arr + 5              # Add 5 to each element
arr1 + arr2          # Element-wise add
arr1 * arr2          # Element-wise multiply
np.dot(arr1, arr2)   # Matrix multiplication
np.sum(arr)          # Sum of elements
np.mean(arr)         # Mean
np.median(arr)       # Median
np.std(arr)          # Standard deviation
np.max(arr), np.min(arr)
np.argmax(arr), np.argmin(arr)



#6. Boolean Masking / Filtering
arr[arr > 5]               # Elements > 5
mask = arr % 2 == 0        # Even elements
arr[mask]                  # Apply mask
np.where(arr > 3, 1, 0)    # Replace based on condition







#7. Set Operations
np.unique(arr)                  # Unique values
np.intersect1d(arr1, arr2)      # Intersection
np.union1d(arr1, arr2)          # Union
np.setdiff1d(arr1, arr2)        # In arr1 not arr2





#8. Sorting and Searching
np.sort(arr)                    # Sort array
np.argsort(arr)                 # Indices of sorted elements
np.searchsorted(arr, 5)         # Index where 5 should go



#9. NaN and Inf Handling
np.isnan(arr)                   # Detect NaN
np.isinf(arr)                   # Detect Inf
np.nan_to_num(arr)              # Replace NaN/Inf with numbers
np.nansum(arr)                  # Sum ignoring NaN





