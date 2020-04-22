from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.shift=False
    self.o=Gtk.Window()
    self.o.show()
    self.o.connect('key-press-event',self.kpe)
    self.o.connect('key-release-event',self.kre)

  def kpe(*args):
    c=args[-1].hardware_keycode
    if c==9:
      Gtk.main_quit()
    elif c==62:
      args[0].shift=True
      return
    if args[0].shift:
      s=args[0].o.get_size()
      if c==111:
        args[0].o.resize(s[0],s[1]-10)
      elif c==116:
        args[0].o.resize(s[0],s[1]+10)
      elif c==114:
        args[0].o.resize(s[0]+10,s[1])
      elif c==113:
        args[0].o.resize(s[0]-10,s[1])
    else:
      p=args[0].o.get_position()
      if c==111:
        args[0].o.move(p[0],p[1]-10)
      elif c==116:
        args[0].o.move(p[0],p[1]+10)
      elif c==114:
        args[0].o.move(p[0]+10,p[1])
      elif c==113:
        args[0].o.move(p[0]-10,p[1])

  def kre(*args):
    if args[-1].hardware_keycode==62:
      args[0].shift=False

      
ok=Okno()
Gtk.main()
