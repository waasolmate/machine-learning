// 实验三 K-Means.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
#include <stdio.h>
#include <math.h>
#include "Eigen/Dense"
#include <vector>
#include <stdlib.h>
#include <random>
using namespace std;
using namespace Eigen;
using Eigen::MatrixXd;

//求协方差矩阵
vector<vector<float>> Cov(vector<vector<float>> z_array)
{
	int z_row = z_array.size();
	const int z_col = z_array[0].size();
	float avg[10];//均值数组
	vector<vector<float>> cov;//协方差矩阵
	//求列均值
	for (int i = 0; i < z_col; i++)
	{
		float sum = 0;
		for (int j = 0; j < z_row; j++)
			sum += z_array[j][i];
		avg[i] = sum / (z_row);
	}
	//求协方差矩阵
	for (int i = 0; i < z_col; i++)
	{
		cov.push_back(vector<float>());
		for (int p = 0; p < z_col; p++)
		{
			cov[i].push_back(i + p);
			float temp = 0;
			for (int j = 0; j < z_row; j++)
			{
				temp += ((z_array[j][i] - avg[i])*(z_array[j][p] - avg[p]));
			}
			cov[i][p] = temp / z_row;
		}
	}
	return cov;
}
//K-Means聚类
MatrixXd K_Means(MatrixXd dimension,int k)
{
	MatrixXd result(dimension.rows() + k, dimension.cols() + 1);//聚类矩阵
	MatrixXd center(k, dimension.cols());//类中心矩阵
	//将每个样本点赋值给聚类矩阵
	for (int i = 0; i < dimension.rows(); i++)
	{
		for (int j = 0; j < dimension.cols(); j++)
			result(i + k, j) = dimension(i, j);
	}
	//设置随机类中心
	for (int i = 0; i < k; i++)
	{
		for (int j = 0; j < dimension.cols(); j++)
		{
			float max = dimension(0, j);
			float min = dimension(0, j);
			for (int p = 0; p < dimension.rows(); p++)
			{
				if (dimension(p, j) > max)
					max = dimension(p, j);
				if (dimension(p, j) < min)
					min = dimension(p, j);
			}
			result(i, j) = min + rand() / float(RAND_MAX / (max - min));
			center(i, j) = result(i, j);
		}
		result(i, result.cols()-1) = i;
	}
	bool z = true;//设置循环判断条件
	while (z)
	{
		//判断每个样本点属于哪一类	
		for (int i = 0; i < dimension.rows(); i++)
		{
			vector<float> euclidean(k);//存放每个样本点到各个类中心的欧氏距离
			for (int j = 0; j < k; j++)
			{
				float temp = 0;
				for (int p = 0; p < dimension.cols(); p++)
				{
					temp += ((dimension(i, p) - center(j, p))*(dimension(i, p) - center(j, p)));
				}
				float distance = sqrt(temp);//计算欧氏距离
				euclidean[j]=distance;
			}
			//取欧氏距离最小的索引即为所属类
			float min_dst = euclidean[0];
			int clfc = 0;//最小欧氏距离的索引值
			for (int q = 0; q < k; q++)
			{
				if (euclidean[q] < min_dst)
				{
					min_dst = euclidean[q];
					clfc = q;
				}
			}
			result(i + k, result.cols()-1) = clfc;//记录每个样本点所属类
		}
		//用均值等方法更新类中心
		for (int i = 0; i < k; i++)
		{
			vector<float> sum(dimension.cols());
			int len = 0;
			for (int j = 0; j < dimension.rows(); j++)
			{
				if (result(j+k, result.cols()-1) == i)
				{
					for (int p = 0; p < dimension.cols(); p++)
					{
						sum[p] += result(j+k, p);
					}
					len++;
				}
			}
			for (int q = 0; q < dimension.cols(); q++)
			{
				result(i, q) = sum[q] / len;
			}
			result(i, result.cols()-1) = i;
		}
		//判断误差范围
		int opt = 0;
		for (int i = 0; i < k; i++)
		{
			for (int j = 0; j < dimension.cols(); j++)
			{
				if (result(i, j) == center(i, j))
					opt++;
			}
		}
		if (opt >= k * dimension.cols())
			z = false;
		else
		{
			for (int i = 0; i < k; i++)
			{
				for (int j = 0; j < dimension.cols(); j++)				
					center(i, j) = result(i, j);										
			}
		}
	}
	return result;
}
//写入文件
void Write(MatrixXd result,int k)
{
	if (k == 2)
	{
		ofstream csv("D:\\学习资料\\机器学习\\实验三 K-Means\\k=2.csv");
		for (int i = 0; i < result.rows(); i++)
		{
			for (int j = 0; j < result.cols(); j++)
				csv << result(i, j) << ',';
			csv << '\n';
		}
		csv.close();
	}
	if (k == 3)
	{
		ofstream csv("D:\\学习资料\\机器学习\\实验三 K-Means\\k=3.csv");
		for (int i = 0; i < result.rows(); i++)
		{
			for (int j = 0; j < result.cols(); j++)
				csv << result(i, j) << ',';
			csv << '\n';
		}
		csv.close();
	}
	if (k == 4)
	{
		ofstream csv("D:\\学习资料\\机器学习\\实验三 K-Means\\k=4.csv");
		for (int i = 0; i < result.rows(); i++)
		{
			for (int j = 0; j < result.cols(); j++)
				csv << result(i, j) << ',';
			csv << '\n';
		}
		csv.close();
	}
	if (k == 5)
	{
		ofstream csv("D:\\学习资料\\机器学习\\实验三 K-Means\\k=5.csv");
		for (int i = 0; i < result.rows(); i++)
		{
			for (int j = 0; j < result.cols(); j++)
				csv << result(i, j) << ',';
			csv << '\n';
		}
		csv.close();
	}
}

int main()
{
	vector<vector<float>> z_array;
	MatrixXd mat_z();
	ifstream fp("D:\\学习资料\\机器学习\\实验三 K-Means\\z-score_array.csv"); //定义声明一个ifstream对象，指定文件路径
	string line;
	while (getline(fp, line))
	{ //循环读取每行数据
		vector<float> data_line;
		string number;
		istringstream readstr(line); //string数据流化
		/*将一行数据按'，'分割*/
		for (int j = 0; j < 10; j++) 
		{ //可根据数据的实际情况取循环获取
			getline(readstr, number, ','); //循环读取数据
			data_line.push_back(atof(number.c_str())); //字符串传float
		}
		z_array.push_back(data_line); //插入到vector中
	}
	fp.close();
	vector<vector<float>> cov = Cov(z_array);//求协方差矩阵
	//协方差矩阵
	MatrixXd mat_cov(cov.size(), cov[0].size());
	for (int i = 0; i < cov.size(); i++)
	{
		for (int j = 0; j < cov[0].size(); j++)
			mat_cov(i, j) = cov[i][j];
	}
	EigenSolver<MatrixXd> es(mat_cov);
	MatrixXd D = es.pseudoEigenvalueMatrix();//特征值
	MatrixXd V = es.pseudoEigenvectors();//特征向量
	//找出第一和第二主成分
	float max = 0, max_2 = 0;
	int index = 0, index_2 = 0;
	for (int i = 0; i < D.rows(); i++)
	{
		if (D(i, i) > max)
		{
			max = D(i, i);
			index = i;
		}
	}
	for (int i = 0; i < D.rows(); i++)
	{
		if ((D(i, i) > max_2) && (i!=index))
		{
			max_2 = D(i, i);
			index_2 = i;
		}
	}
	MatrixXd P(mat_cov.rows(), 2);//转换矩阵
	for (int j = 0; j < P.rows(); j++)
	{
		P(j, 0) = V(j, index);
		P(j, 1) = V(j, index_2);
	}
	MatrixXd T(z_array.size(),z_array[0].size());//原数据转成矩阵形式
	for (int i = 0; i < T.rows(); i++)
	{
		for (int j = 0; j < T.cols(); j++)
			T(i, j) = z_array[i][j];
	}
	MatrixXd dimension(T.rows(),P.cols());
	dimension = T * P;//降维矩阵：原数据矩阵与转换矩阵相乘，实现降维
	int k;//类数
	cout << "请输入聚类个数: ";
	cin >> k;
	MatrixXd result = K_Means(dimension, k);//实现聚类
	Write(result, k);//写入文件
	cout << result << endl;
	cout << "聚类完成!";
	return 0;
}





