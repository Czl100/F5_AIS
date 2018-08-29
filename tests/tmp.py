# _*_ coding:utf-8 _*_
import sympy
import random
'''
for i in range(1, 8):    
    n = (1 << i) - 1                #注释
    print n
print '---------end-----------'

 if __name__ == '__main__':
     unittest.main()
'''
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