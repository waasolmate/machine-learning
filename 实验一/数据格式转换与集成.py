import pandas as pd
import random
import glob
import csv
import xlrd

##数据格式转换
def Return():
    #数据源一xlsx文件转成csv文件
    data_xls = pd.read_excel(r'D:\学习资料\机器学习\实验一\样本数据集\一.数据源1.xlsx', index_col=0)
    data_xls.to_csv(r'D:\学习资料\机器学习\实验一\实验结果\数据源1.csv', encoding='utf-8')

    # 数据源二txt文件转成csv文件
    csvFile = open(r"D:\学习资料\机器学习\实验一\实验结果\数据源2.csv",'w+',newline='',encoding='utf-8')
    writer = csv.writer(csvFile,dialect='excel')
    f = open(r"D:\学习资料\机器学习\实验一\样本数据集\一.数据源2-逗号间隔.txt",'r',encoding='GB2312')
    data=f.read()
    data=data.split()
    for line in data:
        line=line.split(',')
        writer.writerow(line)
    f.close()
    csvFile.close()

##合并数据源
def Merge(csv_list, output_csv_path):
    for inputfile in csv_list:
        f = open(inputfile)
        data = pd.read_csv(f)
        data.to_csv(output_csv_path,encoding='gbk', mode='a', index=False)
    print('完成合并')

if __name__=='__main__':
    Return() #将两个数据集转换为csv格式
    csv_list = glob.glob(r'D:\学习资料\机器学习\实验一\实验结果\*.csv') #找到路径下所有csv文件
    output_csv_path = r'D:\学习资料\机器学习\实验一\实验结果\result_v1.csv' #将合并结果存入该路径
    print(csv_list) #输出找到的csv文件路径
    Merge(csv_list, output_csv_path) #将找到的两个csv文件合并
