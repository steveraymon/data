#!/usr/bin/python
from gi.repository import Gtk, Gdk
import os, urllib, subprocess, ftplib 
class MyWindow(Gtk.Window):

	def __init__(self):
		global ftpServer
		global ftpUsername
		global ftpPasswd
		ftpServer = ""
		ftpUsername = ""
		ftpPasswd = ""
		Gtk.Window.__init__(self, title="Menu")
		self.set_size_request(350, 170)
		self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(self.box)

		self.button1 = Gtk.Button(label="INSTALL")
		self.button1.connect("clicked", self.on_button1_clicked)
		self.box.pack_start(self.button1, False, False, 0)
		self.button1.set_size_request(100,50)

		self.button2 = Gtk.Button(label="PURGE")
		self.button2.connect("clicked", self.on_button2_clicked)
		self.box.pack_start(self.button2, False, False, 0)

		self.button3 = Gtk.Button(label="TERMINAL")
		self.button3.connect("clicked", self.on_button3_clicked)
		self.box.pack_start(self.button3, False, False, 0)
        
		self.button4 = Gtk.Button(label="apt-get clean")
		self.button4.connect("clicked", self.on_button4_clicked)
		self.box.pack_start(self.button4, False, False, 0)

		self.button5 = Gtk.Button(label="Archives")
		self.button5.connect("clicked", self.on_button5_clicked)
		self.box.pack_start(self.button5, False, False, 0)
		
		
		self.entry = Gtk.Entry()
		self.entry.set_text("")		
		self.box.pack_start(self.entry, False, False, 0)

	def on_button1_clicked(self, widget):
		myVar = self.entry.get_text()
		os.system("echo 'unseen' | sudo -S gnome-terminal -e 'apt-get install ' + myVar")

		print myVar
	def on_button2_clicked(self, widget):
		subprocess.Popen(["python", "./cherrytree/usr/bin/cherrytree"])
		
	def on_button3_clicked(self, widget):
		os.system("echo 'unseen' | sudo -S gnome-terminal")

	def on_button4_clicked(self, widget):
		os.system("echo 'unseen' | sudo -S apt-get clean")

	def on_button5_clicked(self, widget):
		os.system("echo 'unseen' | sudo -S thunar /var/cache/apt/archives/")
		#subprocess.Popen(["./midori/AppRun"])
              
win = MyWindow()
win.set_position(Gtk.WindowPosition.CENTER)
win.connect("delete-event", Gtk.main_quit)
win.show_all()

Gtk.main()
