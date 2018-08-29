#_*_ coding:utf-8 _*_
import random
import sympy

class Ais(object):
    #对QDCT系数进行一次预处理
    def __init__(self,QDCT,size_secret):        
        self.pa,self.pb,self.r,self.T=0,0,0,0             #T>1        
        self.secret_byte=size_secret                                  #密码信息大小(byte)
        self.expected=0
        self.k_matrix=0

        self.coef=QDCT
        self.ac_buf=[]                                               #暂存AC系数的位置、值
        index=[index for index in range(0,len(QDCT),64)]             #ac系数下标    
        for i in index:            
            self.ac_buf.append((i,QDCT[i]))
            self.coef[i]=100                                #跳过AC系数
        
        print 'end'
            
    def findindex(self,aim):
        #查找值为0\1\-1的元素的全部下标(位置)
        count=self.coef.count(aim)
        indexlist=[]
        index=0
        first=True
        for i in range(count):
            if first:
                index=self.coef.index(aim,index)
            else:
                index=self.coef.index(aim,index+1)
            indexlist.append(index)
            first=False
        return indexlist

    def fix(self):
        #查找指定元素的全部下标
        indexlist0=findindex(0)                                    #验证:len(indexlist0)==H0    
        lenlist0=len(indexlist0)
        #按比例将0改为1
        numfix0=int(lenlist0*pa)
        randnum=random.sample(indexlist0,numfix0)                       #randnum是coef的下标    
        ishalf=True
        le=len(randnum)    
        for i in range(le):
            if ishalf:              #将前一半改为1
                coef[randnum[i]]=1
            else:
                coef[randnum[i]]=-1
            if i>(len(randnum)/2):
                ishalf=False

        indexlist1=findindex(1)                                   #可以用random.shuffle混洗indexlist
        indexlist_1=findindex(-1)
        numfix_one=int(pb*len(indexlist1))
        numfix_none=int(pb*len(indexlist_1))
        randindex_one=random.sample(indexlist1,numfix_one)
        randindex_none=random.sample(indexlist_1,numfix_one)
        #1改为2
        _modifone(randindex_one)
        _modifone(randindex_none)

        #复原ac系数
        for i in range(len(self.ac_buf)):
            index=self.ac_buf[i][0]
            value=self.ac_buf[i][1]
            self.coef[index]=value

    def _modifone(self,randindex):
        le=len(randindex)
        if coef[randindex[1]]==1:
            ispositive=True
        elif coef[randindex[1]]==-1:
            ispositive=False
        else:
            print '\nthe coef not 1 or -1\nerrorin _modifone\n'
            answer = raw_input('y/n: ')
            if answer != 'y':
                print 'exit'
                sys.exit(0)

        if ispositive:
            for i in range(le):
                coef[randindex[i]]=2
        else:
            for i in range(le):
                coef[randindex[i]]=-2

    def statistic(self):
        #统计H(0)、H(1)\H(-1)\H(2)\H(-2):原始统计数据
        #确定参数pb:1->2的概率,只考虑正数                
        #统计正数的个数
        H0,H1,H2,H3=self.coef.count(0),self.coef.count(1),self.coef.count(2),self.coef.count(3)
        zero_origin=H0
        one_origin=H1+self.coef.count(-1)                
        
        _large = coeff_count - zero_origin - one_origin-coeff_count / 64            #有效载体系数的个数
        self.expected = _large + int(0.49 * one_origin)                             #预期容量,shrinkage效应无法确定

    def cal_k_r(self):
        for i in range(1, 8):
            self.n = (1 << i) - 1
            usable = (self.expected * i / self.n - self.expected * i / self.n % self.n) / 8
            if usable < self.secret_byte + 4:
                break
        k=i-1
        self.k_matrix=k
        logger.info('\nk:%d' % k)    
                    
        self.r=float(1)/((1<<k)-1)          #每个像素被修改的概率,待定?
        
        #AIS处理、计算修改0、1、概率a,b,r    
        #expression:ax+by=c
        a1,b1,c1=0.5*(1-r)*H1,(2*r-2+r)*H1,r*H3-(2*r-1)*H2-(1-r)*H1             #H(1)'>H(2)'  > 
        a2,b2,c2=0.5*(3*r-1)*H0-H0,-((3*r-1)*H1+r*H1),r*H2-H0-H1*(3*r-1)        # >
        a3,b3,c3=(r-1)*H0,-2*r*H1,self.T*H0-H0-2*r*H1                                #<
        a4,b4,c4=1.5*H0,-H1,H0-H1           #<
        a5,b5,c5=-0.5*H0,2*H1,H1-H2         #<

        #解一元二次方程
        '''
        x=sympy.Symbol('x')                 #x:pa  y:pb
        y=sympy.Symbol('y')
        expreArray=[x+y-1,3*x+2*y-5]
        result=sympy.solve(expreArray,[x,y])
        print(result)
        '''