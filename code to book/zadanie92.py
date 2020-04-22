s=b"""
<!DOCTYPE html>
  <head><meta charset="UTF-8"></head>
  <body>
      wolna pami\xc4\x99\xc4\x87 / pami\xc4\x99\xc4\x87 ca\xc5\x82kowita: {1} / {0} <br>
      wolna przestrze\xc5\x84 wymiany / ca\xc5\x82kowita przestrze\xc5\x84 wymiany: {3} / {2} <br>
      czas od restartu: {4} <br>
  </body>
</html>
""".decode('utf8')

def index():
  with open('/proc/meminfo') as f:
    l = f.readlines()
  l = l[0:2]+l[13:15]
  l = [i.rsplit(':')[1].strip() for i in l]
  with open('/proc/uptime') as f:
    t=f.read()
  t=t.split()[0]
  t=float(t)
  t=int(t)
  t,ts = divmod(t,60)
  t,tm = divmod(t,60)
  td, th = divmod(t,24)
  l.append('%sd %sh:%smin:%ss' % (td,th,tm,ts))  
  return s.format(*l)
  
