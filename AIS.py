#_*_ coding:utf-8 _*_
import random
import sympy
#对QDCT系数进行一次预处理
class Ais(object):
    def __init(self)__:
        self.one_num=0
        self.zero_num=0
        self.two_num=0

        self.pa=0
        self.pb=0
        self.r=0
def fix(a,b,r,coef):    
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
    #统计H(0)、H(1)\H(-1)\H(2)\H(-2):原始统计数据
    #确定参数pb:1->2的概率,只考虑正数
    coef_origin=coeff[:]
    index=[i for i in range(0,len(coef_origin)) if i%64==0]
    for i in index:
        coef_origin[i]=100                 #跳过AC系数
    
    #统计正数的个数
    H0,H1,H2,H3=coef_origin.count(0),coef_origin.count(1),coef_origin.count(2),coef_origin.count(3)
    zero_origin=H0
    one_origin=H1+coef_origin.count(-1)        
    two_origin=H2+coef_origin.count(-2)            
    three_origin=H3+coef_origin.count(-3)
    #有效系数的个数
    _large = coeff_count - zero_origin - one_origin-coeff_count / 64
    _expected = _large + int(0.49 * one_origin)                               #预期容量,shrinkage效应无法确定



def cal_k_r():
    for k in range(1,8):
        n=(1<<k)-1
        changed = _large - _large % (n + 1)
        changed = (changed + one_origin + one_origin / 2 - one_origin / (n + 1)) / (n + 1)
        usable = (_expected * k / n - _expected * k / n % n) / 8
        if usable == 0:
            break
    logger.info('\nk:%d' % k)
    k-=1
        
        
    r=float(1)/((1<<k)-1)                 #每个像素被修改的概率,待定?
    #AIS处理
    #计算概率a,b,r:修改0、1、
    T=1.002                              #T>1
    #ax+by=c
    a1,b1,c1=0.5*(1-r)*H1,(2*r-2+r)*H1,r*H3-(2*r-1)*H2-(1-r)*H1     #H(1)'>H(2)'   
    a2,b2,c2=0.5*(3*r-1)*H0-H0,-((3*r-1)*H1+r*H1),r*H2-H0-H1*(3*r-1)
    a3,b3,c3=(r-1)*H0,-2*r*H1,T*H0-H0-2*r*H1
    a4,b4,c4=1.5*H0,-H1,H0-H1
    a5,b5,c5=-0.5*H0,2*H1,H1-H2

    #解一元二次方程
    x=sympy.Symbol('x')                 #x:pa  y:pb
    y=sympy.Symbol('y')
    expreArray=[x+y-1,3*x+2*y-5]
    result=sympy.solve(expreArray,[x,y])
    print(result)