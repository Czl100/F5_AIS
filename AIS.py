#_*_ coding:utf-8 _*_
import random
#对QDCT系数进行一次预处理
class Ais(object):
    def __init(self)__:
        self.one_num=0
        self.zero_num=0
        self.two_num=0

        self.pa=0
        self.pb=0
        self.r=0
def ais(a,b,r,coef):
    
    for i, cc in enumerate(coef):
        pa=random.uniform(1,10)     #[1,10]
        pb=random.uniform(1,10)     #[1,10]
        if i % 64 == 0:                  #AC系数
            continue
        if cc == 1 or cc == -1:
            one_num += 1
            if pa<a:
                if cc==1:
                    coef[i]+=1
                elif cc==-1
                    coef[i]-=-1  
        elif cc == 0:
            zero_num += 1
            if pb<b/2:
                coef[i]-=1
            elif pb<b:
                coef[i]-=1

def statistic(coef):
    index=[i for i in range(0,len(coef)) if i%64==0]
    coef[index]=100                 #跳过AC系数
    num_zero=coef.count(0)
    num_one=coef.count(1)
    num_none=coef.count(-1)
    num_two=coef.count(2)
    num_ntwo=coef.count(-2)