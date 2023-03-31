#!/usr/bin/python
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super(AppWindow, self).__init__(application=app)
        self.init_ui()
    
    def init_ui(self):
        self.set_title('Biswajit Rajaguru: Image')
        self.set_default_size(500, 500)
        
        vbox = Gtk.Box.new(Gtk.Orientation.VERTICAL,8)
        hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL,8)
        vbox.set_margin_start(5)
        vbox.set_margin_top(5)
        self.entry = Gtk.Entry()
        hbox.append(self.entry)
        
        keycont = Gtk.EventControllerKey()
        keycont.connect('key-released', self.on_key_released)
        keycont.connect('key-pressed', self.on_key_pressed)
        self.add_controller(keycont)
        
        self.label = Gtk.Label.new('...')
        hbox.append(self.label)
        vbox.append(hbox)
        self.set_child(vbox)
    
    
    
    #     image = Gtk.Image.new_from_file('bhagwa.png')
       
        
    #     box = Gtk.Box.new(Gtk.Orientation.VERTICAL,2)
    #     box.set_margin_start(5)
    #     box.set_margin_top(5)
        
    #     btn = Gtk.Button(label='Quit')
    #     btn.connect('clicked', lambda _:self.close())
    #     btn.set_halign(Gtk.Align.START)
        
    #     cbtn = Gtk.CheckButton.new_with_label('Show Title')
    #     cbtn.set_active(True)
    #     cbtn.connect('toggled', self.on_toggle)
        
    #     box.append(cbtn)
    #     box.append(btn)
    #     box.append(image)
    #     self.set_child(box)
    #     # self.set_child(image)
        
        
        
        
    def on_key_pressed(self, *_):
        self.set_title('keycont_q')
        if '1'=='q':
            self.close()
    
    def on_key_released(self, *_):
        self.label.set_text(self.entry.get_text())
    
    
    # def on_toggle(self, wid):
    #     if wid.get_active():
    #         self.set_title('CheckButton')
    #     else:
    #         self.set_title('')
    
            
        

def on_activate(app):
    win = AppWindow(app)
    win.present()
    
app = Gtk.Application(application_id='com.biswajit.Image')
app.connect('activate', on_activate)
app.run(None)