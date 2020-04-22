def index(x='',y=''):
  try:
    z=int(x)+int(y)
  except:
    z=''
  return """<!DOCTYPE html><html><head></head><body>
<form method="get">
<input type="text" name="x">+<input type="text" name="y">
<input type="submit" value="="> %s
</form>
</body></html>
""" % (z,)
