import numpy as np
def imageNegative(newImage,x):
    c=0
    
    for f in newImage:
        
        y=(x-1)-f
        newImage[c]=y
        c=c+1
    return newImage
def logtransform(newImage,x):
    c=(x-1)/np.log10(1+np.maxnp.max((newImage)))
    out=c*np.log10(newImage+1)
    return np.round(out)
