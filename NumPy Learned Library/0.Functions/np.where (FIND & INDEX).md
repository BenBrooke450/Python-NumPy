
### Using numpy.where():

The numpy.where() function is useful for finding the indices of elements that satisfy a certain condition.



```python
import numpy as np

# Example array
arr = np.array([10, 20, 30, 40, 50])

# Find the index of elements greater than 25
indices = np.where(arr > 25)
print(indices)  # Output: (array([2, 3, 4]),)
```