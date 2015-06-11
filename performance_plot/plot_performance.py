# usr/bin/env python3
# encoding:utf8

from gi.repository import GLib
from gi.repository import GObject
import sys
import pygal
from pygal.style import LightGreenStyle


def read_data(filename):
    with open(filename, 'r') as fd:
        data = fd.read().splitlines()
        data = [tuple(x.split(',')) for x in data]
        return [(float(x), float(y)) for y, x in data]

if __name__ == '__main__':

    sync_data = read_data('sync_data.txt')
    async_data = read_data('async_data.txt')

    chart = pygal.XY(fill=True, style=LightGreenStyle)
    chart.title = "Download Performance"
    chart.add('Synchron', sync_data)
    chart.add('Asynchron', async_data)
    chart.render_to_file('chart.svg')


