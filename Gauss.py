#!/usr/bin/env python
# coding: utf-8

# In[4]:


def mGauss(n,a,b):
    x=b
    det=1#jопределитель
    #прямой метод Гаусса
    for i in range(n):
        if a[i][i] == 0:
            for j in range(i,n):
                if a[j][i]!=0:
                    a[j],a[i]=a[i],a[j]
                    b[j],b[i]=b[i],b[j]
                    break
        l=a[i][i]
        det*=l
        a[i][i]=1
        for j in range(i+1,n):
            a[i][j]/=l
        b[i]/=l
        for j in range(i+1,n):
            l=a[j][i]
            for k in range(i,n):
                a[j][k] =a[j][k] - a[i][k]*l
            b[j]-=b[i]*l
    #определитель
    if (det==0):
        print('Определитель равен нулю')
        return None
    #обратный ход метода Гаусса
    x[n-1]=b[n-1]
    for i in range (n-2,-1,-1):
        x[i] = b[i]
        for j in range(i+1,n):
            x[i]-=a[i][j]*x[j]
    return x


# In[ ]:




