
## 实验三  《k-means聚类算法》
#### 一、实验内容：

##### 
用C++实现k-means聚类算法，

1. 对实验二中的z-score归一化的成绩数据进行测试，观察聚类为2类，3类，4类，5类的结果，观察得出什么结论？

2. 由老师给出测试数据，进行测试，并画出可视化出散点图，类中心，类半径，并分析聚为几类合适。

样例数据(x,y)数据对：

3.45	7.08

1.76	7.24

4.29	9.55

3.35	6.65

3.17	6.41

3.68	5.99

2.11	4.08

2.58	7.10

3.45	7.88

6.17	5.40

4.20	6.46

5.87	3.87

5.47	2.21

5.97	3.62

6.24	3.06

6.89	2.41

5.38	2.32

5.13	2.73

7.26	4.19

6.32	3.62

找到聚类中心后，判断(2,6)是属于哪一类？

#### 二、实验环境:

##### 1、文件说明

问题1_K-Means.cpp文件为用C++实现对实验二z-score归一化后的样本数据进行降维和K-Means聚类，聚类后的数据存为数据文件夹中的一系列k=n.csv文件(n为类数)；

问题1_可视化.py文件为用python实现的对上一文件聚类后的数据绘制散点图;

问题2.py为用python实现的对题目给出的样例数据进行K-Means聚类和散点图绘制；

数据文件夹中包括用于问题1的z-score归一化数据、用于问题2的由题目给出的样例数据、问题1聚类后的一系列k=n.csv文件(n为类数)；

实验截图文件夹中包括，问题1、2的代码运行截图（包括数据输出截图和可视化截图），问题1的数据输出截图仅以聚为5类为例；

##### 2、运行环境

C++部分：

#include <iostream>

#include <fstream>
  
#include <string>
  
#include <sstream>
  
#include <stdio.h>

#include <math.h>

#include "Eigen/Dense"

#include <vector>
  
#include <stdlib.h>

#include <random>
  
python部分：

import matplotlib.pyplot as plt

import pandas as pd

import csv

import numpy as np

import random

import copy

##### 3、函数说明

代码中已标明注释

#### 三、困难与总结:


