from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.o.show()
    self.o.connect("delete-event",print)


ok=Okno()
Gtk.main()
