from requests import get
    
    
class Response_cm:

  def __init__(self,adres):
    self.adres=adres

  def __enter__(self):
    self.f = get(self.adres)
    return self.f

  def __exit__(self,t,e,tb):
    self.f.close()


with Response_cm('https://docs.python.org') as f:
  print(f.text)
