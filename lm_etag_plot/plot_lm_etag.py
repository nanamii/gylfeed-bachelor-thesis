# usr/bin/env python3
# encoding:utf8

from gi.repository import GLib
from gi.repository import GObject
import sys
import pygal
from pygal.style import LightGreenStyle



pie_chart = pygal.Pie(style=LightGreenStyle, truncate_legend=30)
#pie_chart.title = 'Anteil an last-modified und ETag in HTTP-Header von Feeds'
pie_chart.add('mit Attribut: 83,88%', 83.88)
pie_chart.add('ohne Attribut: 16,12%', 16.12 )
pie_chart.render_to_file('pie_chart.svg')
