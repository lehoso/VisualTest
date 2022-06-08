"""
Time:     2022/6/8 20:05
Author:   LEHOSO
Version:  V 0.1
File:     bar.py
Describe: Write during the junior at CQUCC, Github link: https://github.com/lehoso
"""
# -*- coding: utf-8 -*-

from pyecharts import bar

'''
柱形图
'''

bar = bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        [5, 20, 36, 10, 75, 90])
bar.show_config()
bar.render()
