#!/usr/bin/python

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_title('Biswajit R')
    win.present()

app = Gtk.Application(application_id='com.biswajit.Simple')
app.connect('activate', on_activate)
app.run(None)

            
