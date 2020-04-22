#!/usr/bin/python3
from cgi import FieldStorage

f=FieldStorage()
x=f.getfirst('x')
y=f.getfirst('y')
dz=f.getfirst('dz')
try:
  if dz=="0":
    z=float(x)+float(y)
  elif dz=="1":
    z=float(x)-float(y)
  elif dz=="2":
    z=float(x)*float(y)
  elif dz=="3":
    z=float(x)/float(y)
  else:
    z=''
except:
  z=''
print("Content-type: text/html\n\n")
print("""<!DOCTYPE html><html><head></head><body>
<form method="get">
<input type="text" name="x">
<select name="dz">
<option value=0>+</option>
<option value=1>-</option>
<option value=2>*</option>
<option value=3>/</option>
</select>
<input type="text" name="y">
<input type="submit" value="="> %s
</form>
</body></html>
""" % (z,))
