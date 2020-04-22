from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.o.show_all()
    self.o.connect("enter_notify_event",lambda *args:args[0].set_opacity(0))
    self.o.connect("leave_notify_event",lambda *args:args[0].set_opacity(1))


Okno()
Gtk.main()
