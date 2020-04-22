from gi.repository import Gtk, GdkPixbuf


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    pixbuf = GdkPixbuf.Pixbuf.new_from_file("./test.png")
    pixbuf = pixbuf.scale_simple(500,500,GdkPixbuf.InterpType.HYPER)
    pixbuf = pixbuf.new_subpixbuf(100,100,300,300)
    image = Gtk.Image()
    image.set_from_pixbuf(pixbuf)
    self.o.add(image)
    self.o.show_all()

    
Okno()
Gtk.main()
