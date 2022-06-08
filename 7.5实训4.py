"""
Time:     2022/6/8 14:55
Author:   LEHOSO
Version:  V 0.1
File:     7.5实训3.py
Describe: Write during the junior at CQUCC, Github link: https://github.com/lehoso
"""
from pyecharts import Radar

radar = Radar("雷达图", "学生学习情况")
radar_data1 = [[80, 67, 89, 80, 90, 70, 55, 77, 79, 81, 61, 70]]
radar_data2 = [[62, 90, 89, 56, 84, 81, 79, 63, 69, 75, 60, 80]]
schema = [
    ("语文", 100), ("数学", 100), ("化学", 100),
    ("外语", 100), ("物理", 100), ("历史", 100),
    ("地理", 100), ("生物", 100), ("计算机", 100),
    ("美术", 100), ("音乐", 100), ("政治", 100)
]
radar.config(schema)
radar.add("张明", radar_data1)
radar.add("范阳", radar_data2, item_color="#1C86EE")
radar.render("Rader1.html")
