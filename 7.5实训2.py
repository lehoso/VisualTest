"""
Time:     2022/6/8 14:45
Author:   LEHOSO
Version:  V 0.1
File:     7.5实训2.py
Describe: Write during the junior at CQUCC, Github link: https://github.com/lehoso
"""
from pyecharts import Line

line = Line("折线图", "每周销售图", width=800, height=400)
attr = ['8.3-8.9', '8.10-8.16', '8.16-8.22', '8.23-8.29',
        '8.30-9.5', '9.6-9.12', '9.13-9.19', '9.20-9.26']
data = [15000, 22000, 24000, 29000, 31000, 34000, 27000,2000]
line.add("销售量", attr, data, is_label_show=True,
         legend_orient='vertical',legend_pos='center',
         is_smooth=True, xaxis_rotate='50')
line.render()
