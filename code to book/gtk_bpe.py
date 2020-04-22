from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.o.set_title('')
    self.o.resize(400,100)
    self.h=Gtk.HBox()
    self.b=Gtk.Button('Pierwszy')
    self.e=Gtk.Button('Drugi')
    self.h.pack_start(self.b,True,True,0)
    self.h.pack_start(self.e,True,True,0)
    self.o.add(self.h)
    self.o.show_all()
    self.b.connect("button-press-event",self.b_press)
    self.e.connect("button-press-event",self.b_press)

  def b_press(*args):
    print(args)

    
ok=Okno()
Gtk.main()
