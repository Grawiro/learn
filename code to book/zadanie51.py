# Kod uzupełniający ciało klasy Wielomian

  def __getitem__(self,i):
    return list.__getitem__(self,i) if i<len(self) else 0
  
