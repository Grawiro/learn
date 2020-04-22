from gi.repository import Gtk


def zamykanie(c):
  stary_init = c.__init__
  def nowy_init(*args):
    stary_init(*args)
    for i in args[0].__dict__.values():
      if type(i)==Gtk.Window:
        i.connect('delete_event',zamknij)
  def zamknij(*args):
    Gtk.main_quit()
  c.__init__ = nowy_init
  c.zamknij = zamknij
  return c


@zamykanie
class Okno:
  def __init__(self):
    self.o=Gtk.Window()
    self.o.show_all()


Okno()
Gtk.main()

