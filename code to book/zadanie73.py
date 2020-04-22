from gi.repository import Gtk


class Okno:

  def __init__(self):
    self.o=Gtk.Window()
    self.h=Gtk.HBox()
    self.v=Gtk.VBox()
    self.pa=Gtk.Button('Wolna pamięć')
    self.sw=Gtk.Button('Wolna przestrzeń wymiany')
    self.cz=Gtk.Button('Czas od restartu')
    self.b=Gtk.TextBuffer()
    self.t=Gtk.TextView()
    self.t.set_buffer(self.b)
    self.o.add(self.v)
    self.v.pack_start(self.t,True,True,0)
    self.v.pack_start(self.h,False,True,0)
    self.h.pack_start(self.pa,True,True,0)
    self.h.pack_start(self.sw,True,True,0)
    self.h.pack_start(self.cz,True,True,0)
    self.o.show_all()
    self.t.set_editable(False)
    self.o.connect('delete_event',Gtk.main_quit)
    self.t.connect('button-press-event',lambda *args:1)
    self.pa.connect('button-press-event',self.pokaz_pa)
    self.sw.connect('button-press-event',self.pokaz_sw)
    self.cz.connect('button-press-event',self.pokaz_cz)

  def pokaz_pa(*args):
    with open('/proc/meminfo') as f:
      d=dict([map(str.strip,i.split(':',1)) for i in f])
    args[0].b.set_text('Wolna pamięć: %s/%s' % (d['MemFree'],d['MemTotal']))

  def pokaz_sw(*args):
    with open('/proc/meminfo') as f:
      d=dict([map(str.strip,i.split(':',1)) for i in f])
    args[0].b.set_text('Wolna przestrzeń wymiany: %s/%s' % (d['SwapFree'],d['SwapTotal']))

  def pokaz_cz(*args):
    with open('/proc/uptime') as f:
      t=int(f.read().split('.',1)[0])
      t,s=divmod(t,60)
      t,m=divmod(t,60)
      t,h=divmod(t,24)
      args[0].b.set_text('Czas od restartu: %dd : %dh : %dm : %ds' % (t,h,m,s))
      

ok=Okno()
Gtk.main()
