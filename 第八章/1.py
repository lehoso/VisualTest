"""
Time:     2022/6/8 19:24
Author:   LEHOSO
Version:  V 0.1
File:     1.py
Describe: Write during the junior at CQUCC, Github link: https://github.com/lehoso
"""
from bokeh.plotting import figure, output_file, show
import numpy as np

output_file("sincos.html")
x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)
z = np.cos(x)
p = figure(plot_width=400, plot_height=400)
p.line(x, y)
p.line(x, z)
show(p)
