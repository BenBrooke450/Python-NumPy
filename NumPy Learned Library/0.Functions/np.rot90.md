
In NumPy, you can rotate a matrix (a 2D array) using various approaches depending on the type of rotation you need. Common rotations include 90-degree rotations, 180-degree rotations, and transpositions. Here are some methods to achieve these rotations:

### 1. Rotate a Matrix by 90 Degrees

To rotate a matrix by 90 degrees clockwise or counterclockwise, you can use the `numpy.rot90` function.

#### Example

```python
import numpy as np

# Example matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Rotate 90 degrees clockwise
rotated_90_clockwise = np.rot90(matrix, k=-1)
print("Rotated 90 degrees clockwise:\n", rotated_90_clockwise)

# Rotate 90 degrees counterclockwise
rotated_90_counterclockwise = np.rot90(matrix)
print("Rotated 90 degrees counterclockwise:\n", rotated_90_counterclockwise)
```

<br><br><br>

### 2. Rotate a Matrix by 180 Degrees

You can rotate a matrix by 180 degrees by applying `numpy.rot90` twice or using array indexing.

#### Example

```python
# Rotate 180 degrees
rotated_180 = np.rot90(matrix, k=2)
print("Rotated 180 degrees:\n", rotated_180)
```

<br><br><br>

### 3. Transpose a Matrix

Transposing a matrix swaps its rows and columns. This is not a rotation but is often used in matrix operations.

#### Example

```python
# Transpose the matrix
transposed_matrix = matrix.T
print("Transposed Matrix:\n", transposed_matrix)
```


### Explanation

- **`numpy.rot90`:** This function is specifically designed for rotating arrays by 90 degrees. The `k` parameter specifies the number of times the array is rotated by 90 degrees. A positive `k` rotates counterclockwise, while a negative `k` rotates clockwise.

- **Transposition:** Swaps rows and columns, which can be useful for certain types of matrix operations.

- **Custom Rotation:** For arbitrary angles, you need to define a rotation matrix and apply it using matrix multiplication. This example is simplified and works for 2D vectors; rotating larger matrices requires more complex handling.

These methods provide flexibility in rotating matrices for various applications in data processing and analysis.