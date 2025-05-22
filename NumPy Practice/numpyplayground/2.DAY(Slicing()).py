

import numpy as np

M = np.arange(0, 30, 3)

M = M.reshape((2, 5))

print(M)
"""
[[ 0  3  6  9 12]
 [15 18 21 24 27]]
"""

#M[ROWS:COLUMNS]
print(M[:,0])
#[ 0 15]

print(M[:,1:])
"""
[[ 3  6  9 12]
 [18 21 24 27]]
 """

print(M[0,:])
"""
[ 0  3  6  9 12]
 """





