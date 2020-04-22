from requests import get
from contextlib import contextmanager
    
    
@contextmanager
def response_cm(adres):
  f=get(adres)
  yield f
  f.close()


with response_cm('https://docs.python.org') as f:
  print(f.text)
