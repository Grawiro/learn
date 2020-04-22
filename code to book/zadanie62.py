from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.o.show()
    self.o.connect("configure-event",lambda *args:self.o.set_title(str((args[-1].x,args[-1].y))))

    
ok=Okno()
Gtk.main()
