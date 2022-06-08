"""
Time:     2022/6/8 15:16
Author:   LEHOSO
Version:  V 0.1
File:     1.py
Describe: Write during the junior at CQUCC, Github link: https://github.com/lehoso
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
data = [30, 20, 15, 10, 10, 15]
plt.figure(num=1, FigureClass=(5, 5))  # 设置图的宽度和高度
plt.title('机械系2019招生专业人数对比图', size=18)
plt.pie(data, labels=('机电一体化技术', '数控技术', '汽车电子技术', '飞行器制造', '飞机维修技术', '应用电子技术'))
plt.show()
