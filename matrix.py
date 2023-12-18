#!/usr/bin/env python
# coding: utf-8

# In[276]:


from math import sqrt
class matrices:
    shape=(0,0)
    matrix=[]
    
##конструктор класса
    def __init__(self,n,m,l=None):
        self.shape=(n,m)
        if l=='ones':
            c=[]
            for i in range(self.shape[0]):
                c.append([])
                for j in range(self.shape[1]):
                    c[i].append(float(i==j))
            self.matrix=c
        else:
            self.matrix=l
            
##перегрузка вывода            
    def __str__(self):
        a=str()
        for l in range(self.shape[0]):
            a+=str(self.matrix[l])+'\n'
        return a
    
##Перегрузка сложения
    def __add__(self,a):
        c=[]
        ##для матриц
        if type(a)==matrices:
            if self.shape!=a.shape:
                print('Error! Dimensions mismatch!')
            else:
                for i in range(self.shape[0]):
                    c.append([])
                    for j in range(self.shape[1]):
                        c[i].append(self.matrix[i][j]+a.matrix[i][j])                    
        ##для скаляров
        else:
            for i in range(self.shape[0]):
                c.append([])
                for j in range(self.shape[1]):
                    c[i].append(self.matrix[i][j]+a)
        return(matrices(self.shape[0],self.shape[1],c))
    
##Перегрузка вычтания
    def __sub__(self,a):
        c=[]
        ##для матриц
        if type(a)==matrices:
            if self.shape!=a.shape:
                print('Error! Dimensions mismatch!')
            else:
                for i in range(self.shape[0]):
                    c.append([])
                    for j in range(self.shape[1]):
                        c[i].append(self.matrix[i][j]-a.matrix[i][j])   
        ##для скаляров
        else:
            for i in range(self.shape[0]):
                c.append([])
                for j in range(self.shape[1]):
                    c[i].append(self.matrix[i][j]-a)
        return(matrices(self.shape[0],self.shape[1],c))
    
##Перегрузка домножения на скаляр
    def __mul__(self, a):
        c=[]
        for i in range(self.shape[0]):
                c.append([])
                for j in range(self.shape[1]):
                    c[i].append(self.matrix[i][j]*a)
        return(matrices(self.shape[0],self.shape[1],c))
    
##Матричное умножение
    def matmul(self,B):
        c=[]
        if self.shape[1]!=B.shape[0]:
            print('Incorrect matrices! Shape mismatch!')
        else:
            for i in range(self.shape[0]):
                c.append([])
                for j in range(B.shape[1]):
                    x=0
                    for k in range (B.shape[0]):
                        x+=self.matrix[i][k]*B.matrix[k][j]
                    c[i].append(x)
        if self.shape[0]==1 and B.shape[1]==1:
            return (c[0][0])
        else:
            return(matrices(self.shape[0],B.shape[1],c))
    
##Транспонирование
    def transpose(self):
        c=[]
        for i in range(self.shape[1]):
            c.append([])
            for j in range(self.shape[0]):
                c[i].append(self.matrix[j][i])
        self.shape=(self.shape[1],self.shape[0])
        self.matrix=c
        
##Транспонирование с возвращением        
    def getT(self):
        c=[]
        for i in range(self.shape[1]):
            c.append([])
            for j in range(self.shape[0]):
                c[i].append(self.matrix[j][i])
        return(matrices(self.shape[1],self.shape[0],c))
    
##Взятие нормы
    def norm(self):
        if (self.shape[0]==1) or (self.shape[1]==1):
            a=0
            for i in range(self.shape[0]):
                for j in range (self.shape[1]):
                    a+=(self.matrix[i][j])**2
            return(sqrt(a))
        else:
            c=[]
            for i in range(self.shape[0]):
                a=0
                for j in range(self.shape[1]):
                    a+=abs(self.matrix[i][j])
                c.append(a)
            return(max(c))

