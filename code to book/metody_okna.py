from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.o.show()

    
ok=Okno()

ok.o.set_title("Moje okno")
ok.o.move(500,500)
ok.o.resize(400,400)
ok.o.set_opacity(0.5)

input()

print(ok.o.get_title())
print(ok.o.get_position())
print(ok.o.get_size())
print(ok.o.get_opacity())

Gtk.main()
