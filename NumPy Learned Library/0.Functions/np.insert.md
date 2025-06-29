
👉 No — numpy.insert and numpy.append do NOT operate in-place.

They return a new array. Your original array is unchanged unless you reassign the result.



```python


import numpy as np

class Solution:

    def check(self, nums: List[int]) -> bool:

        nums = np.array(nums)

        for n in nums:

            if all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):

                return True

            else:

                nums = np.insert(nums,values=nums[-1],obj=0)

                nums = nums[:-1]

        return False

 

 

 

 

 

####################################################################

 

 

def processQueries(self, queries: List[int], m: int) -> List[int]:

        list1 = []

        perm = np.arange(1,m+1)

        i = 0

        while i < len(queries):

            x = np.where(perm == queries[i])

            list1.append(int(x[0][0]))

            perm = np.insert(perm,values=perm[x[0][0]],obj=0)

            perm = np.delete(perm,x[0][0]+1)

            i = i + 1

        return list1

 

```

 