
np.unique() is a very useful function in NumPy that finds the unique elements of an array. It can also return the indices of the unique elements and counts of occurrences. Below are a few examples of how to use np.unique() in different scenarios:

 

1. Basic Usage: Get Unique Elements

This is the most straightforward usage, where you simply get the unique values in an array.

 

 
```python
# Create an array with some repeated elements

arr = np.array([1, 2, 2, 3, 4, 4, 5])

 

# Get unique elements

unique_elements = np.unique(arr)

 

print(unique_elements)

#[1 2 3 4 5]
```
 

 

 

2. Return Indices of Unique Elements

You can use the return_index=True argument to return the indices of the unique values in the original array.

 
```python
arr = np.array([10, 20, 10, 30, 40, 30, 50])

# Get unique elements and their indices

 

unique_elements, indices = np.unique(arr, return_index=True)

 

print("Unique elements:", unique_elements)

#Unique elements: [10 20 30 40 50]

 

print("Indices:", indices)

#Indices: [0 1 3 4 6]
```