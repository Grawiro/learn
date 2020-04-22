from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.h=Gtk.HBox()
    self.b1=Gtk.Button('OK')
    self.b2=Gtk.Button('Cancel')
    self.h.pack_start(self.b1,True,True,0)
    self.h.pack_start(self.b2,True,True,0)
    self.o.add(self.h)
    self.o.show_all()
    self.b1.connect('button-press-event',self.bpe)
    self.b2.connect('button-press-event',self.bpe)
    
  def bpe(*args):
    if args[1]==args[0].b1:
      print('OK')
    if args[1]==args[0].b2:
      print('Cancel')

      
Okno()
Gtk.main()
