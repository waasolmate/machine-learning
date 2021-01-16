## 实验一    《数据统计与可视化》

#### 一、实验内容
##### 
基于实验一中清洗后的数据练习统计和视化操作，100个同学（样本），每个同学有11门课程的成绩（11维的向量）；那么构成了一个100x11的数据矩阵。以你擅长的语言C/C++/Java/Python/Matlab，编程计算：

1. 请以课程1成绩为x轴，体能成绩为y轴，画出散点图。
<img src="https://github.com/waasoulmate/machine-learning/raw/main/%E5%AE%9E%E9%AA%8C%E4%BA%8C/%E5%AE%9E%E9%AA%8C%E7%BB%93%E6%9E%9C/%E9%97%AE%E9%A2%981%E6%95%A3%E7%82%B9%E5%9B%BE.png" />

2. 以5分为间隔，画出课程1的成绩直方图。
<img src="https://raw.githubusercontent.com/waasoulmate/machine-learning/main/%E5%AE%9E%E9%AA%8C%E4%BA%8C/%E5%AE%9E%E9%AA%8C%E7%BB%93%E6%9E%9C/%E9%97%AE%E9%A2%982%E7%9B%B4%E6%96%B9%E5%9B%BE.png" />

3. 对每门成绩进行z-score归一化，得到归一化的数据矩阵。

4. 计算出100x100的相关矩阵，并可视化出混淆矩阵。（为避免歧义，这里“协相关矩阵”进一步细化更正为100x100的相关矩阵，100为学生样本数目，视实际情况而定）
<img src="https://raw.githubusercontent.com/waasoulmate/machine-learning/main/%E5%AE%9E%E9%AA%8C%E4%BA%8C/%E5%AE%9E%E9%AA%8C%E7%BB%93%E6%9E%9C/%E9%97%AE%E9%A2%984%E6%B7%B7%E6%B7%86%E7%9F%A9%E9%98%B5.png" />

5. 根据相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔。

#### 二、实验环境:

##### 1、文件说明
**实验二.py**为对实验要求的五个问题的代码实现；

**样本数据集文件夹**中为实验一中清洗后的样本数据；

**实验结果文件夹**中包括：问题1、2、3、4的运行截图、z-score_array.csv为问题3得到的归一化矩阵、相关矩阵.csv为问题4得到的相关矩阵、ID.txt为问题5得到的结果。

##### 2、运行环境

import pandas as pd //用于读取csv数据

import random //用于体能成绩量化

import numpy as np //用于进行矩阵操作

import math //用于计算相关系数和归一化操作

import matplotlib.pyplot as plt //用于可视化

##### 3、函数说明

代码中已标明注释

#### 三、困难与总结:

#####
本次实验难点较多，可视化是从网上查阅资料一点一点学的；归一化矩阵的计算和相关矩阵的计算代码实现较为麻烦，但根据公式最终也得以完成；根据相关矩阵找到距离每个样本最近的三个样本之后将其映射到样本数据中找到对应ID，采用的方法是对相关矩阵的每一行进行排序后记录下其索引值，根据索引值在样本数据中找到其对应ID。

总结本次实验，学会了各种图例的可视化，对数据进行归一化和求相关矩阵可以更方便找到数据间的联系。
