nowa_ankieta=b"""
<!DOCTYPE html>
  <head>
    <meta charset="UTF-8">
    <style>
      table
      {{
        border-collapse: collapse;
      }}
      table th
      {{
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: center;
        background-color: LimeGreen;
        width: 150px;
        color: white;
        border: 1px solid #ddd;
      }}
      table td
      {{
        border: 1px solid #ddd;
        text-align: center;
      }}
      .godzina
      {{
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: center;
        background-color: LimeGreen;
        width: 50px;
        color: white;
        border: 1px solid #ddd;
      }}
      .belka
      {{
        display:flex;
        align-items: center;
        background-color:LimeGreen;
        width:818px;
        color:white;
      
      }}
      input[type=submit]
      {{
        background-color:Green;
        border:none;
        color:white;
        font-weight:bold;
        margin:5px;
        padding:10px;
      }}
    </style>
  </head>
  <body>
    <form>
      <div class="belka">
        <b>Nazwa ankiety:</b><input style="flex:2" type="text" name="nazwa">
        <b>Autor ankiety:</b><input style="flex:2" type="text" name="autor">
      </div>
      <h3>Proponowane terminy:</h3>
      <table>
        <tr><th style="background-color:white;border:none;width:50px;"></th><th>Poniedzia\xc5\x82ek</th><th>Wtorek</th><th>\xc5\x9aroda</th><th>Czwartek</th><th>Pi\xc4\x85tek</th></tr>
        <tr><td class="godzina">8-10</td><td><input type="checkbox" name="termin" value="00"></td><td><input type="checkbox" name="termin" value="10"></td><td><input type="checkbox" name="termin" value="20"></td><td><input type="checkbox" name="termin" value="30"></td><td><input type="checkbox" name="termin" value="40"></td></tr>
        <tr><td class="godzina">10-12</td><td><input type="checkbox" name="termin" value="01"></td><td><input type="checkbox" name="termin" value="11"></td><td><input type="checkbox" name="termin" value="21"></td><td><input type="checkbox" name="termin" value="31"></td><td><input type="checkbox" name="termin" value="41"></td></tr>
        <tr><td class="godzina">12-14</td><td><input type="checkbox" name="termin" value="02"></td><td><input type="checkbox" name="termin" value="12"></td><td><input type="checkbox" name="termin" value="22"></td><td><input type="checkbox" name="termin" value="32"></td><td><input type="checkbox" name="termin" value="42"></td></tr>
        <tr><td class="godzina">14-16</td><td><input type="checkbox" name="termin" value="03"></td><td><input type="checkbox" name="termin" value="13"></td><td><input type="checkbox" name="termin" value="23"></td><td><input type="checkbox" name="termin" value="33"></td><td><input type="checkbox" name="termin" value="43"></td></tr>
      </table>
      <div class="belka" style="flex-flow: row-reverse;">
        <input type="submit" value="Stw\xc3\xb3rz ankiet\xc4\x99">
      </div>
      {0}
    </form>
  </body>
</html>
""".decode('utf8')

stworzono=b"""
<!DOCTYPE html>
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
    <h3>Stworzono now\xc4\x85 ankiet\xc4\x99<h3>
    <h3>Link do ankiety: localhost/ankiety.py?klucz={0}</h3>
  </body>
</html>
""".decode('utf8')

ankieta=b"""
<!DOCTYPE html>
  <head>
    <meta charset="UTF-8">
  </head>
  <style>
    table {{ border-collapse: collapse; }}
    table th
    {{
      padding-top: 12px;
      padding-bottom: 12px;
      text-align: center;
      background-color: LimeGreen;
      width: 180px;
      color: white;
      border: 1px solid #ddd;
    }}
    table td
    {{
      border: 1px solid #ddd;
      text-align: center;
    }}
    .godzina
    {{
      padding-top: 12px;
      padding-bottom: 12px;
      text-align: center;
      background-color: LimeGreen;
      width: 45px;
      color: white;
      border: 1px solid #ddd;
    }}
    .belka
    {{
      display:flex;
      align-items: center;
      background-color:LimeGreen;
      width:100vw;
      color:white;
    }}
    input[type=submit]
    {{
      background-color:Green;
      border:none;
      color:white;
      font-weight:bold;
      margin:5px;
      padding:10px;
    }}
    .nakt
    {{
      background-color:Grey;
    }}
    .dobry
    {{
      background-color:Yellow;
    }}
    .form
    {{
      background-color:LightGreen;
    }}
  </style>
  <body>
    <form>
      <h3>Ankieta: {0}, autor: {1}</h3>
      <h3>Proponowane terminy:</h3>
      <table>
        <tr><th rowspan=2>Uczestnik</th><th colspan=4>Poniedzia\xc5\x82ek</th><th colspan=4>Wtorek</th><th colspan=4>\xc5\x9aroda</th><th colspan=4>Czwartek</th><th colspan=4>Pi\xc4\x85tek</th></tr>
        {2}
      </table>
      <input type="submit" value="Dodaj propozycj\xc4\x99">
      <input type="hidden" name="klucz" value="{3}">
    </form>
  </body>
</html>""".decode('utf8')

godziny = ['8-10','10-12','12-14','14-16']

def naglowek(terminy_ankiety):
  terminy_ank=['nakt' if i=='0' else '' for i in terminy_ankiety]
  naglowek = zip(list(terminy_ank), 5*godziny)
  return '<tr>'+''.join(['<th class="%s">%s</th>' % i for i in naglowek])+'</tr>\n'

def form(terminy_ankiety):
  cl = ['nakt' if i=='0' else 'form' for i in terminy_ankiety]
  dis = ['disabled=true' if i=='0' else '' for i in terminy_ankiety]
  val = [str(i)+str(j) for i in range(5) for j in range(4)]
  return '<tr><td class="form"><input type="text" name="uczestnik"></td>' + ''.join(['<td class="%s"><input type="checkbox" %s name="termin" value="%s"></td>' % i for i in zip(cl,dis,val)])
  
def wiersz(kto,terminy,terminy_ank):
  terminy=['nakt' if terminy_ank[i]=='0' else ('dobry' if terminy[i]=='1' else '') for i in range(20)]
  return '<tr>'+'<td>%s</td>' % kto +''.join(['<td class="%s"></td>' % i for i in terminy])+'</tr>\n'
  

