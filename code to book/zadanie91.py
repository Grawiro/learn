s="""
<!DOCTYPE html>
  <head><meta charset="UTF-8"></head>
  <body>
    Czas od ostatniego pobrania strony: %s
  </body>
</html>
"""

from time import time


def index():
  with open('/var/www/czas.txt') as f:
    t=f.read()

  with open('/var/www/czas.txt','w') as f:
    f.write(str(time()))

  return s % (str(time()-float(t)) if t else '',)
