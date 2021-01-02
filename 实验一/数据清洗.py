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


#初步去重（去表头）
df=pd.read_csv(r'D:\学习资料\机器学习\实验一\实验结果\result_v1.csv',encoding='gbk',header=None)
df.drop_duplicates(inplace=True)

#保存成新文件
list=df.values.tolist()
file=open(r'D:\学习资料\机器学习\实验一\实验结果\result_v2.csv','w+',encoding='gbk',newline='')
writer=csv.writer(file)
for i in list:
    writer.writerow(i)
file.close()

#读取新文件
df=pd.read_csv(r'D:\学习资料\机器学习\实验一\实验结果\result_v2.csv',encoding='gbk',header=0)

#规范化
df.loc[df['ID']<202000,'ID']+=202000
df.loc[df['Gender']=='boy','Gender']='male'
df.loc[df['Gender']=='girl','Gender']='female'
df.loc[df['Height']<3,'Height']*=100

#规范化后再次去重（重复行）
df.drop_duplicates(inplace=True)
df = df.reset_index(drop=True)

#同一学生缺失值填充
height_list=df[df['Height'].isnull()].index.tolist()
for i in range(len(height_list)):
    for j in range(len(df)):
        if df.Name[j]==df.Name[height_list[i]] and j!=height_list[i]:
            df.loc[df.index[height_list[i]],'Height']=df.Height[j]

C1_list=df[df['C1'].isnull()].index.tolist()
for i in range(len(C1_list)):
    for j in range(len(df)):
        if df.Name[j]==df.Name[C1_list[i]] and j!=C1_list[i]:
            df.loc[df.index[C1_list[i]],'C1']=df.C1[j]

C2_list=df[df['C2'].isnull()].index.tolist()
for i in range(len(C2_list)):
    for j in range(len(df)):
        if df.Name[j]==df.Name[C2_list[i]] and j!=C2_list[i]:
            df.loc[df.index[C2_list[i]],'C2']=df.C2[j]

C3_list=df[df['C3'].isnull()].index.tolist()
for i in range(len(C3_list)):
    for j in range(len(df)):
        if df.Name[j]==df.Name[C3_list[i]] and j!=C3_list[i]:
            df.loc[df.index[C3_list[i]],'C3']=df.C3[j]

C4_list=df[df['C4'].isnull()].index.tolist()
for i in range(len(C4_list)):
    for j in range(len(df)):
        if df.Name[j]==df.Name[C4_list[i]] and j!=C4_list[i]:
            df.loc[df.index[C4_list[i]],'C4']=df.C4[j]

C5_list=df[df['C5'].isnull()].index.tolist()
for i in range(len(C5_list)):
    for j in range(len(df)):
        if df.Name[j]==df.Name[C5_list[i]] and j!=C5_list[i]:
            df.loc[df.index[C5_list[i]],'C5']=df.C5[j]

C6_list=df[df['C6'].isnull()].index.tolist()
for i in range(len(C6_list)):
    for j in range(len(df)):
        if df.Name[j]==df.Name[C6_list[i]] and j!=C6_list[i]:
            df.loc[df.index[C6_list[i]],'C6']=df.C6[j]

C7_list=df[df['C7'].isnull()].index.tolist()
for i in range(len(C7_list)):
    for j in range(len(df)):
        if df.Name[j]==df.Name[C7_list[i]] and j!=C7_list[i]:
            df.loc[df.index[C7_list[i]],'C7']=df.C7[j]

Con_list=df[df['Constitution'].isnull()].index.tolist()
for i in range(len(Con_list)):
    for j in range(len(df)):
        if df.Name[j]==df.Name[Con_list[i]] and j!=Con_list[i]:
            df.loc[df.index[Con_list[i]],'Constitution']=df.Constitution[j]

#再一次去重（填充缺失值后的重复行）
df.drop_duplicates(inplace=True)
df = df.reset_index(drop=True)

#其余缺失值填充
df['C3'].fillna(round(df['C3'].mean(),0),inplace=True)
df['C4'].fillna(round(df['C4'].mean(),0),inplace=True)
df['C5'].fillna(round(df['C5'].mean(),0),inplace=True)
df['Constitution'].fillna(('general'),inplace=True)

#按ID号排序
df.sort_values(by='ID',inplace=True,ascending=True)
#重置行索引
df=df.reset_index(drop=True)

#数据中存在ID相同，其他特征值不同的情况，同ID去重
drop_list=[]#用于存放记录重复行序列
for i in df.index:
    for j in df.index:
        if df.ID[j]==df.ID[i] and j>i :
            drop_list.append(j)
drop_dup_list=sorted(set(drop_list))#列表去重并排序
for line in drop_dup_list:
    df.drop([line],inplace=True)

#去重后重置行索引
df=df.reset_index(drop=True)
print(df)
print('数据清洗完成!')

#保存最终文件
df.to_csv(r'D:\学习资料\机器学习\实验一\实验结果\result_v3.csv',encoding='gbk', mode='a', index=False)

