from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.o.show()
    self.o.connect('key-press-event',self.kpe)

  def kpe(*args):
    c=args[-1].hardware_keycode
    if c==9:
      Gtk.main_quit()
    p=args[0].o.get_position()
    if c==111:
      args[0].o.move(p[0],p[1]-10)
    elif c==116:
      args[0].o.move(p[0],p[1]+10)
    elif c==114:
      args[0].o.move(p[0]+10,p[1])
    elif c==113:
      args[0].o.move(p[0]-10,p[1])

      
ok=Okno()
Gtk.main()
