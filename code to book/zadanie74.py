from gi.repository import Gtk, GdkPixbuf


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.o.resize(200,200)
    self.pixbuf = GdkPixbuf.Pixbuf.new_from_file("/usr/share/backgrounds/linuxmint-maya/storm.jpg")
    self.pixbuf = self.pixbuf.scale_simple(1600,900,GdkPixbuf.InterpType.HYPER)
    self.image = Gtk.Image()
    self.o.add(self.image)
    self.o.show_all()
    self.o.connect('delete-event',Gtk.main_quit)
    self.o.connect('configure-event',self.configure)

  def configure(*args):
    args[0].image.set_from_pixbuf(args[0].pixbuf.new_subpixbuf(args[2].x,args[2].y,args[2].width,args[2].height))
    
    
ok=Okno()
Gtk.main()
