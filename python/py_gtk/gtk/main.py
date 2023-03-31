#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import os
from os.path import exists, expanduser
from pathlib import Path

import shutil
import subprocess

home = expanduser('~')
user = os.getlogin()
pwd = subprocess.run('pwd',encoding='utf-8',text=True).strip()
dest = pwd+'my_app.desktop'
source = dest

bash = '/usr/bin/bash'
zsh = '/usr/bin/zsh'

if Path(bash).is_file():
    print(f'Bash exists')
else:
    print('Bash is not installed')

if Path(zsh).is_file():
    print(f'zsh exists')
else:
    print('zsh is not installed')
    
class MyWindow1(Gtk.Window):
    def __init__(self):
        super().__init__(title='My Gtk App')
        
        self.set_border_width(10)
        self.set_default_size(640, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)
        
        frame1 = Gtk.Frame(label='My App')
        
        grid1 = Gtk.Grid(row_spacing = 10,
                         column_spacing = 10,
                         column_homogenous = True)
        
        image1 = Gtk.Image()
        image1.set_from_file('image1.png')
        label1 = Gtk.Label(label="Welcome User")
        label1.set_hexpand(True)
        
        label2 = Gtk.Label(label="How are you doing")
        label2.set_hexpand(True)
        
        label3 = Gtk.Label()
        label4 = Gtk.Label()
        
        button1 = Gtk.Button(label='Biswajit Rajaguru')
        button1.set_hexpand(True)
        button1.connect('clicked', self.on_button1_clicked)
        
        button2 = Gtk.Button(label='Exit')
        button2.set_hexpand(True)
        button2.connect('clicked', Gtk.main_quit)
        
        check = Gtk.CheckButton(label = 'Toggle')
        check.connect('toggled', self.toggle_func)
        check.set_active(eval(self.toggle_check()))
        
        


