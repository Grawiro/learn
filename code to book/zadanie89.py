#!/usr/bin/python3
from cgi import FieldStorage


print("Content-type: text/html\n\n")
f=FieldStorage()
x=f.getfirst('x','')
y=f.getfirst('y','')
dz=f.getfirst('dz','0')
s=['']*4
s[int(dz)]='selected="selected"'
try:
  d={'0':float.__add__,'1':float.__sub__,'2':float.__mul__,'3':float.__truediv__}
  z=d[dz](float(x),float(y))
except:
  z=''
print("""<!DOCTYPE html><html><head></head><body>
<form method="get">
<input type="text" name="x" value="{0}">
<select name="dz">
<option value=0 {1[0]}>+</option>
<option value=1 {1[1]}>-</option>
<option value=2 {1[2]}>*</option>
<option value=3 {1[3]}>/</option>
</select>
<input type="text" name="y" value="{2}">
<input type="submit" value="="> {3}
</form>
</body></html>
""".format(x,s,y,z))
