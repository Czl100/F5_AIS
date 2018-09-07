#_*_ coding:utf-8 _*_
import logging
import json
import matplotlib.pyplot as plt
import numpy as np
from math import ceil
import Image


def pro_draw(array):
	coef_set=set(array)
	coef_set=list(coef_set)
	coef_set.sort()
	count_ori=[]
	for i in coef_set:
		count_ori.append(array.count(i))
	
	return coef_set,count_ori

with open('unpro_ais.json') as unprocess_f:
    coef_origin=json.load(unprocess_f)

with open('embeded.json') as embed_f:
    coef_embeded=json.load(embed_f)

with open('aised.json') as ais_f:
   coef_ais=json.load(ais_f)

with open('embeded_ais.json') as embeded_ais_f:
   coef_embeded_ais=json.load(embeded_ais_f)

ori,count_ori=pro_draw(coef_origin)
embeded,count_embeded=pro_draw(coef_embeded)
aised,count_ais=pro_draw(coef_ais)
embed_ais,count_embed_ais=pro_draw(coef_embeded_ais)

if max(count_ori)>max(count_embeded):
	y_max=max(count_ori)
else:
	y_max=max(count_embeded)

index_ori=ori.index(0)
index_embeded=embeded.index(0)
index_aised=aised.index(0)
index_embed_ais=embed_ais.index(0)

print('numble of 0 in origin: %d' % count_ori[index_ori])
print('numble of 0 in embeded: %d' % count_embeded[index_embeded])

#直方图
'''
	QDCT=[-2,-2,-1,-1,-1,0,0,0,0,1,1,1,2,2,3,8,-6]
	bin_s=max(QDCT)-min(QDCT)+1
	hist=np.histogram(QDCT,bin_s)
	#n, bins, patches = plt.hist(QDCT, bins=bin_s, normed=0, facecolor='black', edgecolor='black',alpha=1,histtype='bar')
	ycount=hist[0]
	xindex=[ceil(value) for value in hist[1]]
	xindex=list(set(xindex))
	xindex.sort()
'''

#fig = plt.figure()
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
width=0.2
_w=width/2
plt.bar([i-(width/2) for i in ori],count_ori,width,color="black",label=u'载体图像')
plt.bar([i+(width/2) for i in embeded],count_embeded,width,color="b",label=u'载密图像')
plt.bar([i-1.5*width for i in aised],count_ais,width,color="r",label=u'处理后载体图像')
plt.bar([i+1.5*width for i in embed_ais],count_embed_ais,width,color="g",label=u'处理后载密图像')

#plt.xticks(np.arange(-10,10,1))
plt.text(0,count_ori[index_ori],count_ori[index_ori],ha='left', va='bottom', fontsize=10)
plt.text(0,count_embeded[index_embeded],count_embeded[index_embeded],ha='left', va='bottom', fontsize=10)
plt.text(0,count_ais[index_aised],count_ais[index_aised],ha='left', va='bottom', fontsize=10)
plt.text(0,count_embed_ais[index_embed_ais],count_embed_ais[index_embed_ais],ha='left', va='bottom', fontsize=10)

plt.title(u"总统计直方图")
plt.xlabel(u'量化后DCT系数')
plt.ylabel(u'频数')
plt.xticks(np.linspace(-10,10,21))
plt.axis([-5,5, 0,1.05*max(count_embeded)])
plt.legend()
plt.savefig(u"总统计直方图.tif")



width=0.4
plt.figure()
plt.bar([i-(width/2) for i in ori],count_ori,width,color="black",label=u'载体图像')
plt.bar([i+(width/2) for i in embeded],count_embeded,width,color="b",label=u'载密图像')
plt.text(0,count_ori[index_ori],count_ori[index_ori],ha='left', va='bottom', fontsize=10)
plt.text(0,count_embeded[index_embeded],count_embeded[index_embeded],ha='left', va='bottom', fontsize=10)
plt.title(u"未预处理载体\载密直方图")
plt.xlabel(u'量化后DCT系数')
plt.ylabel(u'频数')
plt.xticks(np.linspace(-10,10,21))
plt.axis([-5,5, 0,1.05*max(count_embeded)])
plt.legend()
plt.savefig(u"未处理嵌入前后.tif")

plt.figure()
plt.bar([i-(width/2) for i in ori],count_ori,width,color="black",label=u'载体图像')
plt.bar([i+(width/2) for i in aised],count_ais,width,color="r",label=u'处理后载体图像')
plt.text(0,count_ori[index_ori],count_ori[index_ori],ha='left', va='bottom', fontsize=10)
plt.text(0,count_ais[index_aised],count_ais[index_aised],ha='left', va='bottom', fontsize=10)
plt.title(u"预处理前后载体直方图")
plt.xlabel(u'量化后DCT系数')
plt.ylabel(u'频数')
plt.xticks(np.linspace(-10,10,21))
plt.axis([-5,5, 0,1.05*max(count_embeded)])
plt.legend()
plt.savefig(u"预处理前后载体直方图.tif")

plt.figure()
plt.bar([i+(width/2) for i in embeded],count_embeded,width,color="b",label=u'载密图像')
plt.bar([i-(width/2) for i in embed_ais],count_embed_ais,width,color="g",label=u'处理后载密图像')
plt.text(0,count_embeded[index_embeded],count_embeded[index_embeded],ha='left', va='bottom', fontsize=10)
plt.text(0,count_embed_ais[index_embed_ais],count_embed_ais[index_embed_ais],ha='left', va='bottom', fontsize=10)
plt.title(u"预处理前后载密直方图")
plt.xlabel(u'量化后DCT系数')
plt.ylabel(u'频数')
plt.xticks(np.linspace(-10,10,21))
plt.axis([-5,5, 0,1.05*max(count_embeded)])
plt.legend()
plt.savefig(u"预处理前后载密直方图.tif")
#plt.show()

#折线图
'''
	#plt.plot(ori,count_ori,'-k',ais,count_ais,'-r',embeded,count_embeded,'-g' ,ex,count_ex,'-b')
	plt.subplot(1,2,1)
	plt.plot(ori,count_ori,'-k',label='ori',linewidth=1.0)
	plt.plot(aised,count_ais,'--r',label='aised',linewidth=1.0)
	plt.legend()
	plt.axis([-5,5, 0,max(count_embeded)])
	plt.title('imagname')
	plt.xlabel('Quantized DCT coefficient')
	plt.ylabel('Frequency')  

	plt.subplot(1,2,2)
	plt.plot(embeded,count_embeded,'-k',label='em',linewidth=1.0)
	plt.plot(embed_ais,count_embed_ais,'--r',label='embed_ais',linewidth=1.0)

	# plt.text(0,count_ori[index_ori],count_ori[index_ori],ha='left', va='bottom', fontsize=10)
	# plt.text(0,count_embeded[index_embeded],count_embeded[index_embeded],ha='left', va='bottom', fontsize=10)
	# plt.text(0,count_ais[index_aised],count_ais[index_aised],ha='left', va='bottom', fontsize=10)
	# plt.text(0,count_embed_ais[index_embed_ais],count_embed_ais[index_embed_ais],ha='left', va='bottom', fontsize=10)

	plt.legend()
	plt.axis([-5,5, 0,max(count_embeded)])
	plt.title('imagname')
	plt.xlabel('Quantized DCT coefficient')
	plt.ylabel('Frequency')  
	plt.show()
'''