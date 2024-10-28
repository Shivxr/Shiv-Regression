import numpy as np
def sreg(x,y,p):
    xq=[]
    xy=[]
    n=len(x)
    for i in range(len(x)):
        xq.append(x[i]*x[i])
        xy.append(x[i]*y[i])
    sx,sy,sxq,sxy=np.sum(x),np.sum(y),np.sum(xq),np.sum(xy)
    den=(n*sxq)-(sx*sx)
    a=((sy*sxq)-(sx*sxy))/den
    b=((n*sxy)-(sx*sy))/den
    eq1=a+(b*p)
    return eq


    
