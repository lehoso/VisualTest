"""
Time:     2022/6/8 20:01
Author:   LEHOSO
Version:  V 0.1
File:     2.py
Describe: Write during the junior at CQUCC, Github link: https://github.com/lehoso
"""
from bokeh.plotting import figure, output_file, show

output_file("patch.html")
p = figure(plot_width=400, plot_height=400)
p.patch([1, 3, 5], [5, 8, 5], alpha=0.5, line_width=2)
p.patch([1, 3, 5], [5.5, 7, 5.5], alpha=0.3, line_width=2)
show(p)
