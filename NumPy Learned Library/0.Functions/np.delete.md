
Does NOT change arr in-place — it returns a new array.

Original arr stays the same.

 
```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

 

# Remove index 2 → 30

arr_new = np.delete(arr, 2)

 

print(arr_new)

# [10 20 40 50]
```

```python

 

# Remove multiple indices

arr = np.array([10, 20, 30, 40, 50, 60])

arr_new = np.delete(arr, [1, 4])  # Remove index 1 and 4

print(arr_new)

# [10 30 40 60]

 

 

 

 

 

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