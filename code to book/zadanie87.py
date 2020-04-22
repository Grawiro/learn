#!/usr/bin/python3
from datetime import datetime


print("Content-type: text/html\n\n")
with open('/var/www-stud/log.txt','a') as f:
  f.write(str(datetime.now())+'\n')
with open('/var/www-stud/log.txt') as f:
  print("<!DOCTYPE html><html><body>%s</body></html>" % '<br>\n'.join(f.readlines()))
