## np.hstack (Horizontal Stack)

 - Stacks arrays side by side (along axis 1).
 - Requires arrays to have the same number of rows (i.e., matching dimensions except axis 1).

```python
import numpy as np

a = np.array([[1], [2]])
b = np.array([[3], [4]])

np.hstack((a, b))
# Output:
# array([[1, 3],
#        [2, 4]])
```




## np.vstack (Vertical Stack)
 - Stacks arrays on top of each other (along axis 0).
 - Requires arrays to have the same number of columns.


```python
a = np.array([[1, 2]])
b = np.array([[3, 4]])

np.vstack((a, b))
# Output:
# array([[1, 2],
#        [3, 4]])
```


Use **np.hstack** if you want to combine columns.

Use **np.vstack** if you want to combine rows.