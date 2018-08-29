# _*_ coding:utf-8 _*_
import sympy
'''
for i in range(1, 8):    
    n = (1 << i) - 1                #注释
    print n
print '---------end-----------'

 if __name__ == '__main__':
     unittest.main()
'''
#with open('secret.txt','r') as secret_file:
#    secret_byte=secret_file.read()

x=sympy.Symbol('x')
y=sympy.Symbol('y')
expreArray=[x+y-1,3*x+2*y-5]
result=sympy.solve(expreArray,[x,y])
print(result)