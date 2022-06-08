"""
Time:     2022/6/8 15:22
Author:   LEHOSO
Version:  V 0.1
File:     2.py
Describe: Write during the junior at CQUCC, Github link: https://github.com/lehoso
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)  # 取值依次欸0-9的等差数列
y = np.sin(x)
z = np.cos(x)
w = np.tan(x)
plt.plot(x, y, marker="*", linewidth=3, linestyle="-", color="red")  # marker设置
plt.plot(x, z)
plt.plot(x, w)
plt.title("matplotlib")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Y", "Z", "W"], loc="upper right")  # 设置图例
plt.grid(True)
plt.show()
