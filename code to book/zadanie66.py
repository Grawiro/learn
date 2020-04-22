from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.o.show_all()
    self.o.connect("enter_notify_event",self.enter)
  
  def enter(*args):
    w,h=args[0].o.get_size()
    x=int(args[2].x)
    y=int(args[2].y)
    w=w-x
    h=h-y
    m=min([x,y,w,h])
    x0,y0=args[0].o.get_position()
    if x==m:
      args[0].o.move(x0+50+10*m,y0)
    elif w==m:
      args[0].o.move(x0-50-10*m,y0)
    elif y==m:
      args[0].o.move(x0,y0+50+10*m)
    else:
      args[0].o.move(x0,y0-50-10*m)


Okno()
Gtk.main()
