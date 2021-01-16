import pandas as pd
import numpy as np
import random
import math
import matplotlib.pyplot as plt

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
df=pd.read_csv(r'D:\学习资料\机器学习\实验二\样本数据集\data.csv',encoding='gbk',header=0)

##问题1 散点图
x=df.C1 #获取C1成绩
y=df.Constitution #获取体能成绩
x_list=list(x)
y_list=list(y)
rand(y_list) #体能成绩量化
fig=plt.figure(0)
plt.xlabel('x')
plt.ylabel('y')
plt.title('C1 and Constitution散点图')
plt.scatter(x_list,y_list,c='red',alpha=1,marker='.',label='散点')
plt.grid(True)
plt.legend(loc='best')
plt.show()

##问题2 直方图
x=df.C1
x_list=list(x)
bins=[60,65,70,75,80,85,90,95,100]
plt.hist(x_list, bins=bins, histtype='bar',edgecolor = 'k', rwidth=1,label='C1')
plt.xlabel('scores')
plt.ylabel('count')
plt.title('C1成绩直方图')
plt.grid(True)
plt.legend(loc='best')
plt.show()

#生成原始数据矩阵
y_list=list(df.Constitution) #提取体能成绩
rand(y_list) #体能成绩量化
r_df=df[['C1','C2','C3','C4','C5','C6','C7','C8','C9']].values #提取前九门成绩
array_df=np.c_[r_df,y_list] #体能成绩和其他成绩拼接矩阵
m=array_df.shape[0] #获取矩阵行数
n=array_df.shape[1] #获取矩阵列数
print("源数据矩阵：\n",array_df)

##问题3 z-score归一化
array_z = np.zeros((m, n), dtype=np.float) #创建一个空矩阵存放归一化结果
for i in range(array_df.shape[1]):
    avg=sum(array_df[:, i]) / len(array_df[:, i]) #列平均值
    variance = sum([(x - avg) ** 2 for x in array_df[:, i]]) / len(array_df[:, i]) #列方差
    stan = math.sqrt(variance) #列标准差
    for j in range(array_df.shape[0]):
        array_z[j,i]=round((array_df[j,i]-avg)/stan,2) #z-score标准化
print("z-score归一化矩阵：\n",array_z)
#z-score归一化矩阵写入文件
array_z=pd.DataFrame(array_z)
array_z.to_csv(r'D:\学习资料\机器学习\实验二\实验结果\z-score_array.csv',encoding='gbk', mode='a', index=False,header=None)

##问题4 计算相关矩阵并绘制热力图
#十分制成绩量化成百分制
for i in range(5,9):
    for j in range(array_df.shape[0]):
        array_df[j,i]=(array_df[j,i]-1)*10+random.randint(0,10)
array_z_r = np.zeros((m, n), dtype=np.float) #创建空矩阵存放行规范化结果
#计算行规范化
for i in range(array_df.shape[0]):
    avg=np.sum(array_df[i:i+1]) / array_df.shape[1] #行平均值
    variance = np.sum([(x - avg) ** 2 for x in array_df[i:i+1]]) / array_df.shape[1] #行方差
    stan = math.sqrt(variance) #行标准差
    for j in range(array_df.shape[1]):
        array_z_r[i,j]=(array_df[i,j]-avg)/stan #行规范化
array_corr = np.zeros((m, m), dtype=np.float) #创建空矩阵存放相关系数
#计算相关系数矩阵
for k in range(array_z_r.shape[0]):
    for i in range(array_z_r.shape[0]):
        sum=0
        for j in range(array_z_r.shape[1]):
            sum+=array_z_r[k,j]*array_z_r[i,j] #点乘累加
        array_corr[k,i]=round(sum/array_z_r.shape[1],2)
print("相关矩阵：\n",array_corr)
#相关系数矩阵热力图显示
plt.subplots(figsize=(106, 106))
seaborn.heatmap(array_corr, annot=False, vmax=1, square=True, cmap="Blues")
plt.axis('off') #关闭坐标轴刻度
plt.show()

##问题5 找出最近的三个样本
df_array_corr=pd.DataFrame(data=array_corr)
array_sort = np.zeros((m, 3), dtype=np.int) #创建106*3矩阵存放排序后的前三个系数
for i in range(array_corr.shape[0]):
    sort=df_array_corr[i].sort_values(ascending=False) #对相关矩阵每一行进行排序且不改变索引
    for j in range(3):
        array_sort[i,j]=sort.index[j+1] #获取除去自身后的最大的三个相关系数的索引，用于之后从源数据矩阵中按索引定位ID
array_ID=np.zeros((m, 3), dtype=np.int) #创建106*3矩阵存放ID
for i in range(array_sort.shape[0]):
    for j in range(3):
        array_ID[i,j]=df.ID[array_sort[i,j]] #按索引从源数据定位ID
print("相关性最高的ID矩阵：\n",array_ID)
array_ID=pd.DataFrame(data=array_ID)
#ID数据写入文件
array_ID.to_csv(r'D:\学习资料\机器学习\实验二\实验结果\ID.txt',sep='\t',index=None,header=None)
#相关矩阵写入文件
df_array_corr.to_csv(r'D:\学习资料\机器学习\实验二\实验结果\相关矩阵.csv',encoding='gbk', mode='a', index=False,header=None)
