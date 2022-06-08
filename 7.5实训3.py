"""
Time:     2022/6/8 14:55
Author:   LEHOSO
Version:  V 0.1
File:     7.5实训3.py
Describe: Write during the junior at CQUCC, Github link: https://github.com/lehoso
"""
from pyecharts import Pie

pie = Pie('2018年全国上映的电影中“爱情片”比例', "数据来自豆瓣", title_pos="left")
pie.add("", ["爱情", ""], [14, 86], center=[50, 30], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)
pie.show_config()
pie.render('pie.html')
# pie.render()
