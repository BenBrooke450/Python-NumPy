
```python
def canThreePartsEqualSum(arr: list[int]) -> bool:

    arr = np.array(arr)

    cumsum = np.cumsum(arr)

    print(cumsum)

 

print(canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))

#[ 0  2  3 -3  3 -4  5  6  8  8  9]
```