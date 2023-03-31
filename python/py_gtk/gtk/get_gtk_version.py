#!/usr/bin/python

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

print(f'{Gtk.MAJOR_VERSION}.{Gtk.MINOR_VERSION}.{Gtk.MICRO_VERSION}')

