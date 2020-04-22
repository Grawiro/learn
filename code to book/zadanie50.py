# Kod uzupełniający ciało klasy Wielomian

  def __init__(*args):
    if len(args)==2:
      list.__init__(args[0],args[1])
    else:
      list.__init__(args[0],args[1]*reduce(lambda a,b:a*b, [Wielomian([p,1]) for p in args[2]]))
  
