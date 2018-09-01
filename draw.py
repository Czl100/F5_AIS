#_*_ coding:utf-8 _*_
import json
import matplotlib.pyplot as plt
import numpy as np

with open('unprocess.json') as unprocess_f:
    coef_origin=json.load(unprocess_f)

with open('embeded.json') as embed_f:
    embeded_data=json.load(embed_f)

with open('aised.json') as ais_f:
   coef_ais=json.load(ais_f)

with open('excoef.json') as excoef_f:
   coef_ex=json.load(excoef_f)





#QDCT=[-2,-2,-1,-1,-1,0,0,0,0,1,1,1,2,2,3,8,-6]
def pro_draw(array):
	coef_set=set(array)
	coef_set=list(coef_set)
	coef_set.sort()
	count=[]
	for i in coef_set:
		count.append(array.count(i))
	
	return coef_set,count


coef_ori,count=pro_draw(coef_origin)
embeded,count_embeded=pro_draw(embeded_data)
ais,count_ais=pro_draw(coef_ais)
ex,count_ex=pro_draw(coef_ex)

if max(count)>max(count_embeded):
	y_max=max(count)
else:
	y_max=max(count_embeded)

#,embeded,count_embeded,'g--' ,ex,count_ex,'b--'
plt.plot(coef_ori,count,'go',ais,count_ais,'r--',embeded,count_embeded,'g--' ,ex,count_ex,'b--')
plt.axis([-10,10, 0,max(count_embeded)])
plt.show()