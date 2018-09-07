#-*-coding:utf-8-*-
import sys
import sympy
import random
import symbol
import json
from matplotlib import pyplot as plt
import numpy

x=numpy.linspace(0,5,10)
y=[i for i in x]

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False


plt.plot(x,y)
plt.text(1,1,'(%.2f,%.3f)' % (0.212,12.2342),ha='left', va='bottom', fontsize=10)
plt.title(u"显示中文")
plt.show()

#with open('secret.txt','r') as secret_file:
#    secret_bindexte=secret_file.read()

# x=sindexmpindex.Sindexmbol('x')
# index=sindexmpindex.Sindexmbol('index')
# expreArraindex=[x+index-1,3*x+2*index-5]
# result=sindexmpindex.solve(expreArraindex,[x,index])
# print(result)

'''
    ac_coef=[i for i in range(2,64*3+2)]
    ac_dict=[]
    ac_index=[index for index in range(0,len(ac_coef),64)]
    for index in ac_index:
        ac_dict.append((index,ac_coef[index]))

    print ac_dict
    ac_coef[53]=2
    index2=ac_coef.find(2)
    print index2

    index=[1,3]
    array=[11,22,33,44,55]
    for i in range(len(index)):
        print array[index[i]]
    lenlist=10
    pa=0.5
    array=[1,2,3,4,5,6,7,8,9]
    randnum=random.sample(array,5)
    randnum=random.sample(array,5)
    aim=2
    array=[2,2,3,4,2,1,3,2]
    count=array.count(aim)
    indexlist=[]
    index=0
    first=False
    for i in range(count):    
        if first:
            index=array.index(aim,index)
        else:
            index=array.index(array,index+1)
        indexlist.append(index)
        first=False
    print indexlist
'''

'''
    import numpy as np
    import matplotlib.pyplot as plt

    x=[i for i in range(-10,11)]
    x_1=[i for i in range(-5,6)]
    for i in x_1:
        x.append(i)

    print x

'''

'''
    n, bins, patches = plt.hist(x, int(max(x)-min(x)),normed=1, facecolor='g', alpha=0.75)

    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    #添加标题
    plt.title('Histogram of IQ')
    #添加文字
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([min(x),max(x), 0, 1])
    plt.grid(True)
    plt.show()
    data=np.arange(-1,1,0.1)
    print data
'''