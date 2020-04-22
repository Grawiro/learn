#!/usr/bin/python3
from subprocess import check_output


print("Content-type: text/html\n\n")
print("<!DOCTYPE html><html><body>%s</body></html>" % check_output('who').decode('utf8').replace('\n','<br>\n'))

  
