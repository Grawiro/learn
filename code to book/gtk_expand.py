from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.o.set_title('')
    self.o.resize(400,100)
    self.h=Gtk.HBox()
    self.b=Gtk.Button('1')
    self.e=Gtk.Button('2')
    self.h.pack_start(self.b,True,True,0)
    self.h.pack_start(self.e,True,True,0)
    self.o.add(self.h)
    self.o.show()
    self.b.show()
    self.e.show()
    self.h.show()


ok=Okno()
Gtk.main()
