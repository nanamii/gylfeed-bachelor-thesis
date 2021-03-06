# usr/bin/env python3
# encoding:utf8

from gi.repository import GLib
from gi.repository import GObject
import sys
import pygal
from pygal.style import LightGreenStyle
from pygal.style import LightSolarizedStyle
from pygal.style import LightStyle
from pygal.style import RedBlueStyle

pie_chart = pygal.Pie(style=RedBlueStyle, truncate_legend=30)
#pie_chart.title = 'Anteil an last-modified und ETag in HTTP-Header von Feeds'
pie_chart.add('RSS', [3559, 63, 7, 5, 1])
pie_chart.add('Atom', [971, 1] )
pie_chart.add('Ohne Feed-Format', 483)
pie_chart.render_to_file('plot_formate.svg')
