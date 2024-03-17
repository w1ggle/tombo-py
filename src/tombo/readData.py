import numpy as np
import os

data = np.load(os.path.join( os.getcwd(), '..', '..', 'output\data\wake\wake_0.npz' ))
lst = data.files
for item in lst:
    print(item)
    print(data[item])
print(data)