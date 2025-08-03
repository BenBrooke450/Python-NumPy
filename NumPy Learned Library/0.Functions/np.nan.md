
```python
import numpy as np

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Place a NaN value at a specific index, e.g., index 2
array[2] = np.nan

print(array)
```

<br><br><br>


```python
import numpy as np

# Example array
trainers = np.array([1, 2, 3, 4, 5], dtype=float)
p = 3  # Example threshold

# Use np.where to replace elements greater than or equal to p with np.nan
trainers = np.where(p <= trainers, np.nan, trainers)

print(trainers)
#[ 1.  2. nan nan nan]
```