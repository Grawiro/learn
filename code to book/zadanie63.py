from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.o.show()
    self.o.connect("configure-event",lambda *args:self.o.set_title('szerokość: {0.width}, wysokość: {0.height}'.format(args[-1])))

    
ok=Okno()
Gtk.main()
