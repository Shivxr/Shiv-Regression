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

l1=[6.2,6.5,5.48,6.54,7.18,7.93]
l2=[26.3,26.65,25.03,26.01,27.9,30.47]
pred=7.5
print(sreg(l1,l2,pred))
    
