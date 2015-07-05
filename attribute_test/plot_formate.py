# usr/bin/env python3
# encoding:utf8

from gi.repository import GLib
from gi.repository import GObject
import sys
import pygal
from pygal.style import LightGreenStyle



pie_chart = pygal.HorizontalBar(style=LightGreenStyle, truncate_legend=30)
#pie_chart.title = 'Anteil an last-modified und ETag in HTTP-Header von Feeds'
pie_chart.add('RSS 2.0', 3559)
pie_chart.add('Atom 1.0', 971)
pie_chart.add('RSS 1.0', 63)
pie_chart.add('RSS 0.91', 7)
pie_chart.add('RSS 0.92', 5)
pie_chart.add('RSS 0.90', 1)
pie_chart.add('Ohne Feed-Format', 483)
pie_chart.render_to_file('plot_formate.svg')
