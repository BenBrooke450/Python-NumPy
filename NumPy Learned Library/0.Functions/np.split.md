
```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

parts = np.split(arr, 3)

 

print(parts)

# [array([10, 20]), array([30, 40]), array([50, 60])]

 

 

 

 

arr = np.array([10, 20, 30, 40, 50, 60])

parts = np.split(arr, [2, 4])

 

print(parts)

# [array([10, 20]), array([30, 40]), array([50, 60])]

 

 

 

 

 

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
