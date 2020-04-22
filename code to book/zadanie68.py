from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.v=Gtk.VBox()
    self.h=Gtk.HBox()
    self.tb=Gtk.TextBuffer()
    self.t=Gtk.TextView()
    self.t.set_buffer(self.tb)
    self.e=Gtk.Entry()
    self.b=Gtk.Button('OK')
    self.h.pack_start(self.e,True,True,0)
    self.h.pack_start(self.b,False,True,0)
    self.v.pack_start(self.t,True,True,0)
    self.v.pack_start(self.h,False,True,0)
    self.o.add(self.v)
    self.o.show_all()
    self.b.connect('button-press-event',self.bpe)
    self.text=''
    self.t.set_editable(False)
    self.e.grab_focus()

  def bpe(*args):
    args[0].text+=args[0].e.get_text()+'\n'
    args[0].e.set_text('')
    args[0].tb.set_text(args[0].text)

    
ok=Okno()
Gtk.main()
