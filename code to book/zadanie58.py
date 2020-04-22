from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.v=Gtk.VBox()
    self.h=Gtk.HBox()
    self.t=Gtk.TextView()
    self.e=Gtk.Entry()
    self.b=Gtk.Button('OK')
    self.h.pack_start(self.e,True,True,0)
    self.h.pack_start(self.b,False,True,0)
    self.v.pack_start(self.t,True,True,0)
    self.v.pack_start(self.h,False,True,0)
    self.o.add(self.v)
    self.o.show_all()

    
ok=Okno()
Gtk.main()
