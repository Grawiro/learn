from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.b=Gtk.Button('Zajrzyj pod okno')
    self.o.add(self.b)
    self.o.show_all()
    self.b.connect("button-press-event",lambda *args:self.o.set_opacity(0))
    self.b.connect("button-release-event",lambda *args:self.o.set_opacity(1))

    
ok=Okno()
Gtk.main()
