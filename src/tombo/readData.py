import numpy as np
import os

data = np.load(os.path.join( os.getcwd(), '..', '..', 'output\data\wake\wake_0.npz' ))
lst = data.files
with open("output.txt", "a") as f:
    for item in lst:
        print(item, file=f)
        print(data[item], file=f)
#print(data)