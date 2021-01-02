import pandas as pd
import numpy as np
import random
import glob
import csv
import xlrd
import math
import matplotlib.pyplot as plt
import re
import seaborn
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
np.set_printoptions(threshold=np.inf)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 10000)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

#体能成绩量化
def rand(c_list):
    for i in range(len(c_list)):
        if c_list[i] == 'bad':
            c_list[i]=random.randint(40,60)
        if c_list[i]=='general':
            c_list[i]=random.randint(60,75)
        if c_list[i]=='good':
            c_list[i]=random.randint(75,85)
        if c_list[i]=='excellent':
            c_list[i]=random.randint(85,100)

#读取数据
df=pd.read_csv(r'D:\学习资料\机器学习\实验一\实验结果\result_v3.csv',encoding='gbk',header=0)


#问题1
print('问题1：')
grade=df.loc[df.City=='Beijing']
con=grade.Constitution
con_list=list(con)
rand(con_list)
print('C1:',round(grade['C1'].mean(),1))
print('C2:',round(grade['C2'].mean(),1))
print('C3:',round(grade['C3'].mean(),1))
print('C4:',round(grade['C4'].mean(),1))
print('C5:',round(grade['C5'].mean(),1))
print('C6:',round(grade['C6'].mean(),1))
print('C7:',round(grade['C7'].mean(),1))
print('C8:',round(grade['C8'].mean(),1))
print('C9:',round(grade['C9'].mean(),1))
print('Constitution:',round(np.mean(con_list),1))

#问题2
print('问题2：')
g1=df.loc[df.City=='Guangzhou']
g2=g1.loc[g1.Gender=='male']
g3=g2.loc[g2.C1>80]
g4=g3.loc[g3.C9>9]
print('Number is ',len(g4))

#问题3
print('问题3：')
#计算广州女生的平均体能成绩
g=df.loc[df.City=='Guangzhou'] #定位广州
gg=g.loc[g.Gender=='female'] #定位女生
gg_con=gg.Constitution #获取体能成绩
gg_con=list(gg_con)
rand(gg_con) #体能成绩量化
ggc_avg=round(np.mean(gg_con),1) #计算平均值并保存一位小数
#计算上海女生的平均体能成绩
print('The Constitution mean of girls from Guangzhou is ',ggc_avg)
s=df.loc[df.City=='Shanghai']
sg=s.loc[s.Gender=='female']
sg_con=sg.Constitution
sg_con=list(sg_con)
rand(sg_con)
sgc_avg=round(np.mean(sg_con),1)
print('The Constitution mean of girls from Guangzhou is ',sgc_avg)
#作比较
if ggc_avg>sgc_avg:
    print('Girls from Guangzhou are better.')
else:print('Girls from Shanghai are better.')

#问题4
print('问题4：',)
con_list=list(df.Constitution)
rand(con_list) #体能成绩量化
r_df=df[['C1','C2','C3','C4','C5','C6','C7','C8','C9']].values #提取前九门成绩
array_df=np.c_[r_df,con_list] #体能成绩和其他成绩拼接矩阵
m=array_df.shape[0] #获取矩阵行数
n=array_df.shape[1] #获取矩阵列数
array_z = np.zeros((m, n), dtype=np.float) #创建一个空矩阵
for i in range(array_df.shape[1]):
    avg=sum(array_df[:, i]) / len(array_df[:, i]) #列平均值
    variance = sum([(x - avg) ** 2 for x in array_df[:, i]]) / len(array_df[:, i]) #列方差
    stan = math.sqrt(variance) #列标准差
    for j in range(array_df.shape[0]):
        array_z[j,i]=(array_df[j,i]-avg)/stan
cor=[] #创建空列表存放相关系数
for i in range(array_z.shape[1]-1):
    sum=0
    for j in range(array_z.shape[0]):
        sum+=array_z[j,i]*array_z[j,array_z.shape[1]-1]
    cor.append(round(sum/array_z.shape[0],3))
print('相关性：',cor)