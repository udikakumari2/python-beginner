import test as t4
import numpy as np
img=[12,23,34,45]
neImge=np.array(img)
print(neImge)
out=t4.imageNegative(neImge,256)
print(out)
out=t4.logtransform(neImge,256)
print(out)
