import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np
#读取文件数据
df=pd.read_csv(r'D:\学习资料\机器学习\实验三 K-Means\k=3.csv',encoding='gbk',header=None)

#聚为几类d_type即为类数
d_type=3

#生成散点图
fig=plt.figure(0)
color=['red','blue','green','orange','purple']
for i in range(d_type):
    x=df[0][i]
    y=df[1][i]
    plt.scatter(x,y,c=color[i],s=40,alpha=1,marker='*')
x=df[0][d_type:len(df)]
y=df[1][d_type:len(df)]
c=df[2][d_type:len(df)]
for i in range(d_type,len(df)):
    plt.scatter(x[i],y[i],c=color[int(c[i])],s=10,alpha=1,marker='.')
    print(x[i],y[i],int(c[i]))

plt.grid(True)
plt.legend(loc='best')
plt.show()
