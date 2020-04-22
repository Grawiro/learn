from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.h=Gtk.HBox()
    self.v=Gtk.VBox()
    self.l=Gtk.Button('Lewy')
    self.p=Gtk.Button('Prawy')
    self.b=Gtk.TextBuffer()
    self.t=Gtk.TextView()
    self.t.set_buffer(self.b)
    self.o.add(self.v)
    self.v.pack_start(self.t,True,True,0)
    self.v.pack_start(self.h,False,True,0)
    self.h.pack_start(self.l,True,True,0)
    self.h.pack_start(self.p,True,True,0)
    self.o.show_all()
    self.t.set_editable(False)
    self.t.connect('button-press-event',lambda *args:1)
    self.o.connect('delete_event',Gtk.main_quit)
    self.il=0
    self.ip=0
    self.napisz()
    self.l.connect('button-press-event',self.lewy)
    self.p.connect('button-press-event',self.prawy)

  def napisz(self):
    self.b.set_text('Lewy: {0.il}, Prawy: {0.ip}'.format(self))

  def lewy(*args):
    args[0].il+=1
    args[0].napisz()

  def prawy(*args):
    args[0].ip+=1
    args[0].napisz()
    

ok=Okno()
Gtk.main()
