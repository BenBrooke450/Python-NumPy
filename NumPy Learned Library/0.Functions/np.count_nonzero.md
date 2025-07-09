
```python

import numpy as np

class Solution:

    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        t = 0

        nums = np.array(nums)

        while t + k <= len(nums):

            q = nums[t:t+k+1]

            if any(np.count_nonzero(q == x) > 1 for x in q):

                return True

            t = t + 1

        return False

 

 

 

 

import numpy as np

# Create a NumPy array

arr = np.array([2, 3, 4, 5, 3, 4, 5, 3, 5, 4, 7, 8, 3, 6, 2])

# Count occurrences of the value '3'

count = np.count_nonzero(arr == 3)

print('Total occurrences of "3" in array:', count)

 

 

 

 

# Count values less than 6

count_less_than_6 = np.count_nonzero(arr < 6)

print('Total values less than 6:', count_less_than_6)

 

 

 

 

matrix = np.array([[2, 3, 4], [5, 3, 4], [5, 3, 5], [4, 7, 8], [3, 6, 2]])

# Count occurrences of '3' in each row

count_row_wise = np.count_nonzero(matrix == 3, axis=1)

print('Occurrences of "3" in each row:', count_row_wise)

 




# Count occurrences of '3' in each column

count_column_wise = np.count_nonzero(matrix == 3, axis=0)

print('Occurrences of "3" in each column:', count_column_wise)
```