szukaj_form = """
<form>
  <div style="display:flex;width:800px;background-color:LimeGreen;border:5px solid white;">
    <input style="flex:2;    background-color:Yellow;  border:none;  margin:5px;" type="text" name="szukaj">
    <input style="float:right;  background-color:Green;    border:none;  margin:5px;  color:white;" type="submit" name="akc" value="Wyszukaj pytania">
    <input style="float:right;  background-color:Green;    border:none;  margin:5px;  color:white;" type="submit" name="akc" value="Nowe pytanie">
  </div>
</form>"""

p_form = """
<form>
<div style="width:800px;background-color:LimeGreen;border:5px solid white;">
  <div style="margin:-20px 0px -20px 0px"><h3>Pytanie:</h3></div>
  <div style="padding:5px;height:20px;">
    <div style="float:left;"> <b>Autor</b>: {2}</div>
    <div style="float:right;"> <b>Czas</b>: {3}</div>
  </div>
  <div style="background-color:Lime;">{1}</div>
  <div align="right" style="padding:5px;height:20px;">
    <input style="background-color:Green;border:none;color:white;margin:2px;" type="submit" name="akc" value="Poka\xc5\xbc odpowiedzi">
  </div>
</div>
</form>""".decode('utf8')

np_form = """
<form>
  <div style="display:flex;flex-direction:column;width:790px;background-color:LimeGreen;border:5px solid white;padding:5px">
    <div style="margin:-20px 0px -20px 0px"><h3>Nowe pytanie:</h3></div>
    <textarea style="flex:1;background-color:Yellow;" name = "np"></textarea><br>
    <div style="display:flex;">
      <b>Autor: </b>
      <input style="flex:2;background-color:Yellow;border:none;margin:5px;" type="text" name="autor">
      <input style="background-color:Green;border:none;margin:5px;color:white;" type="submit" name="akc" value="Dodaj pytanie">
      <input style="background-color:Green;border:none;margin:5px;color:white;" type="submit" name="akc" value="Powr\xc3\xb3t">
    </div>
  </div>
</form>""".decode('utf8')

odp_temp = """
<div style="background-color:LimeGreen;border:5px solid white;padding:10px;">
  <div style="padding:5px;height:20px;">
    <div style="float:left;"> <b>Autor</b>: {1}</div>
    <div style="float:right;"> <b>Czas</b>: {2}</div>
  </div>
  <div style="background-color:Lime;">{0}</div>
</div>"""

po_form = """
<div style="display:flex;flex-direction:column;width:800px;height:95vh;background-color:LimeGreen;border:5px solid white;">
  <div style="margin:-20px 0px -20px 0px"><h3>Pytanie:</h3></div>
  <div style="padding:5px;height:20px;">
    <div style="float:left;"> <b>Autor</b>: {2}</div>
    <div style="float:right;"> <b>Czas</b>: {3}</div>
  </div>
  <div style="background-color:Lime;">{1}</div>
  <form>
    <div style="display:flex;width:800px;">
      <input style="float:right;  background-color:Green;    border:none;  margin:5px;  color:white;" type="submit" name="akc" value="Powr\xc3\xb3t">
      <span style="flex:2"></span>
      <input style="float:right;  background-color:Green;    border:none;  margin:5px;  color:white;" type="submit" name="akc" value="Dodaj odpowied\xc5\xba">
    </div>
  </form>
  <div style="margin:-20px 0px -20px 0px"><h3>Odpowiedzi:</h3></div>
  <div style="flex:1;background-color:white;border:5px solid LimeGreen;overflow-y:scroll;align=center">
    {4}
  </div>
</div>""".decode('utf8')

do_form = """
<form>
  <div style="display:flex;flex-direction:column;width:790px;background-color:LimeGreen;border:5px solid white;padding:5px">
    <div style="margin:-20px 0px -20px 0px"><h3>Pytanie:</h3></div>
    <div style="padding:5px;height:20px;">
      <div style="float:left;"> <b>Autor</b>: {2}</div>
      <div style="float:right;"> <b>Czas</b>: {3}</div>
    </div>
    <div style="background-color:Lime;">{1}</div>
    <div style="margin:-10px 0px -10px 0px"><h3>Nowa odpowied\xc5\xba:</h3></div>
    <textarea style="flex:1;background-color:Yellow;" name = "no"></textarea><br>
    <div style="display:flex;">
      <b>Autor: </b>
      <input style="flex:2;background-color:Yellow;border:none;margin:5px;" type="text" name="autor">
      <input style="background-color:Green;border:none;margin:5px;color:white;" type="submit" name="akc" value="Dodaj odpowied\xc5\xba">
      <input style="background-color:Green;border:none;margin:5px;color:white;" type="submit" name="akc" value="Powr\xc3\xb3t">
    </div>
  </div>
</form>""".decode('utf8')

main = """
<!DOCTYPE html>
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
    {0}
  </body>
</html>
"""
