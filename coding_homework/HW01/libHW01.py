from matplotlib import pyplot as plt
import numpy as np

def drawfunction(f, imsize=300):
    arr = np.zeros([imsize,imsize])
    for i in range(imsize):
        for j in range(imsize):
            xx = ((i - 0.5*imsize) / float(imsize)) * 2
            yy = ((-j + 0.5*imsize) / float(imsize)) * 2
            arr[j,i] = f(xx,yy) 
            
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111)
    ax.tick_params(labelsize=16)
            
    plt.imshow(arr, interpolation='nearest', cmap='gray', vmin=0, vmax=1, extent=[-1,1,-1,1])
    plt.show()


def graphfunction(f, precision=300, x1=-1, x2=1, y1=-1, y2=1):
    arx = np.fromfunction(lambda i: ((i-precision/2)/precision*2), (precision, ))
    ary = np.vectorize(f)(arx) 

    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111)
    ax.tick_params(labelsize=16)

    plt.axis((x1,x2,y1,y2))
    plt.plot(arx, ary)
    plt.show()
    
