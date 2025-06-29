
np.nonzero() returns the indices of non-zero elements in a NumPy array.

It's very useful for:

Finding locations of non-zero values
Filtering arrays
Working with sparse data
 

 
```python
arr2 = np.array([0, 2, 0, 4])

non_zero_indices = np.nonzero(arr2)

 

print(non_zero_indices)     # (array([1, 3]),)

 

print(arr2[non_zero_indices])  # [2 4]


 

 

 

 

 

import numpy as np

class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        list1 = []

 

        groupSizes = np.array(groupSizes)

 

        for x in set(groupSizes):

            list1.append([x,((np.nonzero(groupSizes == x))[0]).tolist()])

 

        list2 = []

 

        for x in list1:

            y = len(x[1])/x[0]

            list2.append(np.split(np.array(x[1]),y))

 

        flat = [item.tolist() for sublist in list2 for item in sublist]

 

        return flat

```