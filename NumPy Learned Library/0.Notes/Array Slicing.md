
### For NumPy arrays: Use views
If you're using NumPy, slicing returns a view, not a copy (most of the time):

```python
view = arr[i:j]  # This is a *view*, not a full copy
```
So it's efficient — unless you force a copy with .copy().