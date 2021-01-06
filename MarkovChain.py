#--coding:utf-8--
import numpy as np

p=[[0.65,0.15,0.12],[0.28,0.67,0.36],[0.07,0.18,0.52]]#给定状态转移矩阵
iter1=50#选取50个变量，
for i in range(iter1):
    #模拟每个变量的初始值，矩阵的三个元素分别为位于上层、中层、下层的概率，概率之和为1
    #由于不知道怎么给出这种随机函数，因此选取了这种方法
    a=np.random.dirichlet(np.ones(3),size=1)
    x=a[0]
    iter2=4000#迭代次数
    for j in range(iter2):
        x_tmp=np.matmul(p,x)#马尔可夫链
        if(x==x_tmp).all():
            break#记录到达平稳状态所需的迭代次数
        x=x_tmp
    print 'start with:',a[0],'end with:',x,'need',j,'times'
