import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np
import random
import copy

def K_Means(k):
    df = pd.read_csv(r'C:\Users\16920\Desktop\样例数据.csv', encoding='gbk', header=None)
    df = np.array(df)
    print(df)
    # 随机选择类中心
    center_array = np.zeros((k,df.shape[1]),dtype=np.float)
    for i in range(k):
        for j in range(df.shape[1]):
            minJ = min(df[:, j])
            maxJ = max(df[:, j])
            center_array[i, j] = random.uniform(minJ, maxJ)

    z=True #设置循环判断条件
    while(z):
        # 判断每个样本点归属哪一类
        clf = []  # 用于存放各个类中心包含的样本点
        for i in range(k):
            clf.append([])
        for i in range(df.shape[0]):
            temp = []  # 创建临时列表存放每个样本点到各个类中心的欧氏距离
            for j in range(k):
                # 计算欧氏距离
                distance = np.sqrt(np.sum((df[i] - center_array[j]) ** 2))
                temp.append(distance)

            # 取欧氏距离最小的索引即为所归属类
            clfc = temp.index(min(temp))
            clf[clfc].append(df[i])

        #存储旧的类中心矩阵，由于接下来会更新类中心矩阵，所以必须用深拷贝
        pre_center_array=copy.deepcopy(center_array)

        #用均值等方法更新类中心
        for i in range(len(clf)):
            sum = 0
            for j in range(len(clf[i])):
                sum+=clf[i][j]
            center_array[i]=sum/len(clf[i])

        #判断误差范围
        opt=0  #设置误差判定条件
        for i in range(len(center_array)):
            org_center=pre_center_array[i]
            cur_center=center_array[i]
            for j in range(len(center_array[i])):
                if cur_center[j]==org_center[j]:
                    opt+=1

        if opt>=k*df.shape[1]: #满足所有类中心不再移动则计算类半径并终止循环
            c_r = [] #存放类半径
            for i in range(len(center_array)):
                c_r.append(0)
                #将每个类中所有样本点到类中心最远的距离作为类半径
                for j in range(len(clf[i])):
                    c_distance=np.sqrt(np.sum((clf[i][j] - center_array[i]) ** 2))
                    if c_r[i]<c_distance:
                        c_r[i]=c_distance
            print(c_r)
            print(center_array)
            z=False

    #可视化
    color = [ 'deepskyblue', 'limegreen', 'orange', 'deeppink','darkred']
    plt.xlabel('评分')
    plt.ylabel('月份')
    for i in range(len(clf)):
        for j in range(len(clf[i])):
            plt.scatter(clf[i][j][0], clf[i][j][1], c=color[i], marker='o', s=10)

    for i in range(len(center_array)):
        plt.scatter(center_array[i][0], center_array[i][1], c=color[i],marker='*', s=80,label=round(c_r[i],3))
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()

if __name__=="__main__":
    k=2 #类数
    K_Means(k)