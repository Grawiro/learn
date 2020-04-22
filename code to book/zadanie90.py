s=b"""
<!DOCTYPE html>
  <head><meta charset="UTF-8"></head>
  <body>
    <form>
      Czas mi\xc4\x99dzy prze\xc5\x82adowaniami: %s
      <input type="hidden" name="t" value="%s">
      <input type="submit" value="Prze\xc5\x82aduj">
    </form>
  </body>
</html>
""".decode('utf8')

from time import time


def index(t=''):
  tn = time()
  if t:
    return s % (tn - float(t), tn)
  return s % ('', tn)
