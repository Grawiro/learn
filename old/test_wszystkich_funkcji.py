#    UWAGA! https://docs.python.org/3/library - spis bibliotek
import time #zaimportuj biblioteke time (do manipulacji czasem)
import datetime #do poznania dokladnej daty
import test_wszystkich_funkcji_import as import_pliku
#from test_wszystkich_funkcji_import import test_funkcji_z_importu, inna #importuj tylko te podane funkcje z pliku, podawane po przecinku
#from test_wszystkich_funkcji_import import test_funkcji_z_importu as inna_nazwa # zaimportuj tylko jedna funkcje i zmien jej nazwa na inna_nazwa
#from time import * #zaimportuj wszysko z pliku, jak sie tak zrobi to nie pisze sie np. time.sleep(1) tylko sleep(1)
import os
import random
import math
import pickle # tak, pickle importujemy
from functools import reduce
#jak importowany plik mialby byc w innym katalogu to sie pisze import nazwa_katalogu.nazwa_pliku_do_importu


pokarz_petle = False
pokarz_if = False
pokarz_zmienne = False
pokarz_czas = False
pokarz_funkcje = False
pokarz_import_i_operacje_na_plikach = False
pokarz_operacje_na_systemie = False
pokarz_inne_bibloiteki_i_funkcje = False
pokarz_wyjatki = False
pokarz_klasy = True

if pokarz_petle == True:
    for i in range(0,3): #petla for od 0 do 3 i jest zwiekszana o 1
        print(i) #Wypisz na ekranie wartosc zmienna i
       
    for i in range(0,4,2): #petla for od 0 do 4 i jest zwiekszana o 2
        print(i, end='') #end nie przechodz do nowej linijki domyslnie \n
    
    lista = [1,34,6,4,7,1,8]
    for liczba in lista: #for przechodzi po wszystkich elementach listy
        if liczba == 7:
            continue
        print(liczba) #wyswietl kolejne elementy tabeli
    
    for i,liczba in enumerate(lista): #pokaz indeks kazdego elementu z tablicy
        print(i, liczba)
        if i == 3:
            break
        
    suma = 0
    while suma < 10:
        suma += 3
        print(suma)
    
if pokarz_if == True:
    lista_liczb = [1,34,6,4,7,1,8]
    if 8 in lista_liczb: #Czy 8 jest na liscie
        print("8 znajduje sie na liscie")
    
    if not 10 in lista_liczb: #Czy 10 nie jest na liscie
        print("10 nie znajduje sie na liscie")
    
    x = 4
    if x == 2: #Czy x==2?
        print("x==2")
    elif x == 3: #Jezeli x!=2 to sprawdz czy x==3?
        print("x==3")
    else: #Jezeli nic z powyzszych to wyswietl to #moze byc elif True:
        print("x!=2 and x!=3")
        
    if x > 1 and x <= 3: #and
        print("x jest z przedzialu do 1 do 3 wlacznie")
    elif not x==4: #not w cpp (!True)
        print("x nie jest 4")
        
    if x==4 or x<2: #lub
        print("x jest 4 lub jest mniejsze od 2")
      
    print("Podaj jakas liczbe")
    liczba = int(input()) #zapytaj o liczbe i rzutuj ja na inta
    if bool(liczba): #rzutuj na typ bool
        print("Wpisana liczba przechowuje wartosc typu True")
    else:
        print("Wpisana liczba przechowuje wartosc typu False")
        
    # WyRAŻENIE WARUNKOWE (krótki if - else)
    # wartość1 if pytanie else wartość2   np.:   'x' if a>0 else 'y'    (zwraca 'x' albo 'y')
    efect = 5 if 'r' in 'kura' else 10
    print ("efekt=",efect)
    efect2 = -1 if 'z' in 'kura' else -2 if False else -3  # efect2 = -1 if 'z' in 'kura' else (-2 if False else -3)
    print ("efect2=",efect2)

if pokarz_zmienne:
    string = "hello"
    print(string)
    string += " world " #add to string
    string *= 2 #powtorz string 2 razy
    print(string)
    
    print(r'\n\t to jest surowy napis')
    print("tekst MALY".lower()) #zamien tekst na male znaki
    print("tekst DUZY".upper()) #zamien tekst na duze znaki
    print("_-=-"*10) #pokaz ten tekst 10 razy
    print(2**3, 5%2, 5//2, sep="\n") #**-potegowanie 2 do 3, %-zwykle modulo, //-czesc calkowita reszty z dzielenia
    #sep="\n" czyli po , w princie przejdz do nowej lini
    
    print('''
To jest wszystko tekstem      nie ma tam nic
   ciekawego''') #do ''' to ''' wszystko to tekst
    
    intiger = "5"
    intiger = int(intiger) #zmiana na int, a na float to float()
    intiger += 33
    print(type(intiger))
    
    string_world = string[0] #pojedynczy znak
    print(string_world)
    string_world = string[0:5] #ciag od 0 do 4 znaku #zero mozna ominac [:5]
    print(string_world)
    string_world = string[-6:] #zapisz od 6 znkau od konca #moze byc cos takiego [-6:-2]
    print(string_world)
    
    lista_stringow = ["34", "ello", 4]
    lista_stringow[0] = "nie weris"
    #jak byly by same liczyb to mozna uzyc np. min(lista_str) lub max(lista_str) zwraca indeks
    lista_stringow.insert(1,"homis") #na indeks 1 wstaw homis
    lista_stringow.reverse() #odwroc cala liste
    lista_stringow.pop() #usun ostati element
    del lista_stringow[2] #usun element o indeksie 2
    print(lista_stringow) #wypisz cala liste
    print(lista_stringow[1:3]) #takie operacje jak na stringu czyli od 1 od 2
    lista_stringow.append(3) #dodaj na koncu
    lista_stringow.append("szer")
    print(lista_stringow[3:5])
    lista_stringow.clear() #wyczysc zawartosc calej listy
    lista_stringow.insert(0,20)
    
    lista_int = list(range(1,100)) #czyli od 2 do 99
    len(lista_int) #zwraca dlugosc listy
    lista_int2 = lista_int[1:25:3]+lista_stringow #utworz  liste z co 3 elementu listy_int ale tylko z liczb od 0 do 24 i dodaj cala liste_inna
    print(lista_int2)
    print(lista_int2.count(20)) #zlicz ile razy wystempuje 20 w lisce
    lista_int_3 = [5]*10 #czyli 10 razy zapisz w liscie 5
    lista_int_4 = [[5]]*3 #czyli w liscie zapisz pod-liste w ktorej jest po jednej 5
    print(lista_int_3)
    print(lista_int_4)
    
    tuple_str = (43, "43764", "hello kit") #tupla nie mozna edytowac (bezsensu)
    tuple_1 = tuple(range(0,100,5)) #stworzenie krotki z zakresu od 0 do 99 co 5 czyli 0,5,10,15 itp.
    print(tuple_str) #operacje jak na stringach ale tylko odczyt
    
    slownik = {"a": 1, "b": "Kamil", 4:"4"} #slownik
    print(slownik) #caly slownik
    print(slownik["b"]) #mozna uzywac tylko kluczy zdefiniowanych w slowniku {klucz:wartosc,}
    print(slownik[4]) 
    # zbiór - wartości nie będą się nigdy powtarzać, nawet jak dodam zdublowane
    zbiór = { 1, 2, 2, 3 }
    print('zbiór=',zbiór, type(zbiór))
    zbiór2 = { }  # pusty ... zbiór? Nie! Słownik.
    print('zbiór2', zbiór2, type(zbiór2))

    zbiór3 = set() # to samo co {}
    print(zbiór3,type(zbiór3))
    zbiór3.add(1)
    zbiór3.add(3)
    zbiór3.add(100)
    zbiór3.add(0)
    zbiór3.add(100)
    print('zbiór3', zbiór3, type(zbiór3))
    zbiór3.remove(100) # usuwa ale musi być
    zbiór3.discard(3) # usuwa o ile jest (jak nie ma to nic się nie dzieje)
    print('zbiór3.pop()',zbiór3.pop())
    print('zbiór3', zbiór3, type(zbiór3))
    zbiór3.clear()

    # ciekawostką jest że argument dla set( ) może być czymś
    # "iteracyjnym" np krotka, lista albo ... tekst jako ciąg znaków
    set1 = set([5,4,1,2,3,3,3]) # 3 nie będzie powtórzone
    print ('set1:',set1)
    set2 = set('literki') # literki są jako zbiór ! ani alfabetycznie ani się nie powtórzą
    print ('set2:',set2)
    set3 = sorted(set2)
    print ('set3 as sorted: set2',set3)
    set4 = set([3,4,5,6,7,8])
    print(set1.difference(set4)) # wynikiem podzbiór z set1, którego nie ma w set4
    print(set1.union(set4)) # zbiór z obu zbiorów, dalej nie ma dubli
    print(set1.intersection(set4)) # część wspólna
    print(set1.isdisjoint(set4)) # zwraca TRUE gdy nie ma wspólnych elementów
    print(set1.issubset(set4)) # TRUE gdy set1 zawiera się w set4 (cały)
    print(set1.issuperset(set4)) # TRUE gdy każdy element set4 jest w set1
    set5 = set4.copy()
    print("set5",set5)


    # słownik (ma dowolne klucze, dla jednego klucza jedna wartość)
    słownik = { 'a' : 1, 'banan' : 'ciarki', 123 : 120, 120: 'Rabarbar' }
    print('słownik:',słownik, type(słownik))
    print(słownik['a'], słownik['banan'], słownik[123], słownik[120] ,sep='  *  ')
    print(type(słownik['a']), type(słownik['banan']), type(słownik[123]), type(słownik[120]) ,sep='  *  ')
    del słownik['a']  # ciekawe, co robi del ?
    print (słownik)

    di = dict()
    di['rycerz']='Rodryg Podkowa'
    di['dama']='Gertruda von Wieża Zamkowa'
    di[102]='Rudy'

    di2 = di.copy()
    print("di2:",di2)
    di2.clear()
    print(di2)

    print(len(di))
    print(di['dama'])
    print('rycerz' in di)
    print('pies' not in di)
    print('kot' in di)
    print(di[102])
    print(di.get(102))
    print(di.get(103,'nie za bardzo'))
    print(di.items()) # zwraca specjalną klasę dict_items (dokładniej o tym w ćwiczeniach nr 1, po poznaniu pętli)
    print(di.keys()) # klucze
    print(di.values()) # wartości
    print(di.popitem()) # od 3.7 gwarancja LIFO    - usuwa ostatni dodany i zwraca  
    print(di.update(dama='Królowa Śniegu'))
    print(di)

    print("Hello {} {} {}".format("world", 5, slownik["a"])) #zamiena {} na kolejne rzeczy z listy argumentow
    
if pokarz_czas:
    time.sleep(1) #Zatrzymaj caly program na 1s
    timer = time.time() #pobierz aktualny czas w sekundach
    time.sleep(3)
    minelo = time.time() - timer
    print(minelo)
    timer2 = timer1 = timer = time.time()
    
    while True: #praca z kilkoma opznieniami jednoczesnie
        if time.time() - timer > 5:
            print("minelo 5s")
            timer = time.time()
        if time.time() - timer1 > 2:
            print("2s minely")
            timer1 = time.time()
        if time.time() - timer2 > 30.1:
            print("minelo 30s")
            break
    
    teraz = datetime.datetime.now() #pobierz aktualna date
    print(teraz) #wyswietl aktualna date (cala)
    print(str(teraz.hour)+":"+str(teraz.minute)) #pokaz tylko godzine i minuty
    print(teraz.strftime("%H:%M %d.%m.%y")) #%H-godzina, %M-minuta itp.
    print(teraz.strftime("%I:%M%p %d.%b.%y")) #%I-godzina w systemie 12h, %p-dodaje AM lub PM, %b- skrot miesiaca, %B-nazwa miesiaca
    
    curtime = time.localtime()
    print('Time\t\t', curtime.tm_hour, curtime.tm_min, curtime.tm_sec, sep=':')
    '''kolejne atrybuty z klasy
    tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday
    '''
    
def funkcja(zmienna_1, zmienna_2, zmienna_3=4, zmienna_4=0): #zmienna_3 i 4 maja wartosci domyslne
    '''dokumentacja'''
    print(zmienna_1, end=' ') #nie przechodz do nowej lini
    print(str(zmienna_2) + " " + str(zmienna_3))
    return ((zmienna_2 - zmienna_1) * zmienna_3) + zmienna_4
    #return None #zwroc nic lub po prostu return

def funkcja_pusta():
    pass #jeszcze nic tu niema ale kiedys cos bedzie (taka deklaracja)

def ileCzego(arg1, arg2='default') :
    arg1 = int(arg1)        
    print((' '+arg2) * arg1)
    global var # var to jest te var globalne
        
# funkcja o dowolnej liczbie argumentów ? proszę !
def multiArgs(*args) :
    suma = 0
    for arg in args :       # arg to wszystkie argumenty, które podano - jeden po drugim
        print(arg)
        if (isinstance(arg,int) or isinstance(arg,float)):  suma += arg; #czy jest intem lub floatem
    return suma

def yieldPresentation(a) :        
    yield a
    a+=1 # argument a przy kolejnym uruchomieniu funkcji zachowa zmienioną wartość
    yield a
    a+=a
    yield a
    a*=a
    yield a
        
# przykład wykorzystania yield (mniej eleganckie niż rekurencyjny fibonacci, ale szybsze
def fibo(n) :
    print('START fibo')
    a1 = 0
    a2 = 1
    yield a1 # 0
    yield a2 # 1
    if n<1 or isinstance(n,float) : n = int(1)
    while n>a1+a2:
        suma = a1+a2
        yield suma # suma wcześniejszych dwóch
        # przesuwam się na dwa ostatnie, tak by a1, i a2 były ostatnimi elementami
        a1 = a2 
        a2 = suma 

if pokarz_funkcje:
    print(funkcja(3,4))
    print(funkcja(zmienna_2=14, zmienna_1=8)) #argumenty nie musza byc w kolejnosci
    print(funkcja(1,2,3))
    print(funkcja(1,2,zmienna_4=100)) #mozna wybrac ktoremu argumentowi domyslnemu nadac wartosc
    
    ileCzego(3)
    ileCzego(12.8,'*-')

    #zmienna = funkcja  (nazwa funkcji)
    #zmienna()  - możliwe wywołanie, coś jak alias do funkcji
    f = ileCzego
    f(5,'-')

    # eval
    v='ileCzego'
    x=10
    tpl='#'
    print(v+'('+str(x)+",tpl)")
    # eval traktuje napis jak instrukcję pythona i tak ją wywołuje/wykonuje
    eval(v+'('+str(x)+",tpl)")  # fragment tpl zostaje zamieniony na wartość zmiennej tpl !
    # its the same
    eval(v+'('+str(x)+",'"+tpl+"')")

    print('multiArgs(1,2,3)=',multiArgs(1,2,3))
    nums = (1,2,3,4,5,0.5,'rabarbar') # kroteczka, posłuży jako kolejne argumenty
    s = multiArgs(*nums)  # *nums - jakby rozpakowanie krotki, zbioru
    print ('suma=',s)
    
    # LAMBDA, czyli funkcje anonimowe (nie posiadają nazwy, ale mogą mieć referencję)
    # nazwa = lambda argumenty : wyrażenie do obliczenia
    f = lambda arg : arg+1  # f staje się referencją do funkcji, która zwiększa argument o jeden
    print('lambda f(5)=',f(5))

    g = lambda x,y,z : (x+y)*z  # lambda może mieć wiele argumentów
    print('g(1,2,3)',g(1,2,3)) # 9

    # lambda może być łączona np. z wyrażeniem warunkowym
    h = lambda arg1 : 'jestem dodatnia' if arg1>0 else 'nie jestem dodatnia'
    print(h(5),h(-5), sep=' | ')
        
    # lambdy są częstym argumentem dla takich sprytnych funkcji jak map
    # funkcja map uruchamia podaną funkcję dla każdego elementu zbioru
    # map (funkcja, zbiór) - każdy element zbioru odpalony zostanie przetworzony prze f-ę
    # tu jako funkcję podałem właśnie lambdę.
    L = [1,2,3,4] # lista-zbiór
    newL = map(lambda x: x+1, L)  # newL to zwrócony przez map specjalny iterator ...
    # i ten iterator trzeba rzutować na np. listę lub inny zbiór/kolekcję
    print (list(newL))  # 2,3,4,5
    # samo newL to specjalny obiekt zwracany przez map, to nie jest jeszcze kolekcja
    print(newL)

    # podobnie lambdy poddane są jako argument dla funkcji filter. Ta z kolei wybiera
    # część elementów ze zbioru
    L = list(range(1,11))
    newL = filter(lambda x: x%2==0, L)
    print(list(newL)) # będą tylko parzyste :)

    # i ponownie lambda jako przydatna do funkcji reduce, która podaną ilość elementów
    # zastępuje jednym wg podanej mechaniki. Nowy element jest parowany z następnymi
    # aż do uzyskania jednego elementu
    
    suma = reduce( lambda x,y : x+y, L) 
    print(suma) # suma wszystkich z L

    # yield czyli YIELD czyli bardzo ciekawy sposób na opuszczanie funkcji :)
    # yield w funkcjiach wychodzi z funkcji jak return, ale ponowne wywołanie funkcji
    # kontunuuje jej działa za ostatnim yield'em
    # yield, gdzie każdy yield zwraca coś, co utworzy w przyszłości zbiór

    for i in yieldPresentation(5) :
        print(i, end='\t');

    print('\n\n', list(yieldPresentation(5))) 

    v1= yieldPresentation(5) # v1 to nie jest pierwszy zwrócony yield !!
    print (v1) # v1 to specjalny obiekt, który reprezentuje to, co zwracają wszystkie yield'y !
    v2 = yieldPresentation(5) # v2 to nie jest drugie yield, to jest dokładnie to, co v1
    print (v2) # zatem v2 jest już obiektem przechowującym wszystkie yield'y dla tej funkcji

    # funkcja next() pozwala pobrać kolejne rozwiązania
    print(next(v1), next(v2), next(v1), next(v2))
    print(next(v1), next(v2), next(v1), next(v2))

    # kiedy rzutujemy nasz obiekt (tzw. generator) na listę, wszystkie zwrócone yield'y utworzą listę
    v3 = yieldPresentation(2)
    print(list(v3))

    # nic nie stoi na przeszkodzie rzutować trochę inaczej ...
    v4 = yieldPresentation(3)
    print(tuple(v4))

    # ZATEM wywołanie funkcji z yield nie zwraca pierwszego wyniku,
    # ale zostaje uruchomiona niewidoczna iteracja, tak długo, aż odpalą się wszystkie yield'y
    # a zwracany wynik to specjalny zbiorowy obiekt, GENERATOR, z którego to można
    # utworzyć np. listę lub krotkę (elementy muszą być indeksowane od 0, dlatego lista/krotka)

    # a co, gdy pobiorę za dużo ?
    try: #wyjatki
        print(next(v1))  # zostanie zwrócony wyjątek StopIteration - z obiektu v1 nie da się już nic pobrać
    except:
        pass

    for x in (list(fibo(999999999999))):
        print(x)

def myReadFile(path) :
    if os.path.isfile(path):  # test na obecność pliku   
        fdread = open(path,'r',encoding="utf-8")
        lines = list(map(lambda line : line.strip() , fdread)) #oczyszczanie linii ze znaków białych .strip() z początku i końca tekstu 
        print(*lines,sep='\n') # a tu rozpakowałem lines i wyswietlenie go
        fdread.seek(0)
        fdtotal = fdread.read() #przeczytaj wszystko do jednej zmiennej i zapisz jako tekst
        print(fdtotal)
        fdread.close()
    else:
        print('Plik ',path,' nie istnieje!')
            
if pokarz_import_i_operacje_na_plikach:
    import_pliku.test_funkcji_z_importu("Importer") #jesli tylko jedna funkcje to bez przedrostka pliku
    
    file = open("test_wszystkich_funkcji_plik.txt", "w+") #otworz plik o (nazwie, parametrze)
    #"r"-tylko odczyt, "r+"-odczyt i zapis, "a"-tylko zapis/moze tworzyc nowy plik, "a+"-zapis i odczyt/tworzy nowy plik jesli potrzeba
    #"w"-tylko zapis/tworzy nowy plik jesli nie istnieje/czysci zawartosc pliku przed otwarciem, "w+"-to co w tylko z odczytem
    #dla "r","r+","w","w+" kursor jest na poczatku, dla "a","a+" kursor ustawia sie na koncu
    
    file.write("123 ")
    file.write(str(4))
    file.write(" 56\n") #"\n" to nowa linijak
    file.write("123 ")
    
    file.seek(0) #ustaw kursor na indeksie 0
    print(file.read())
    file.seek(6) #przesun kursor 6 znakow dalej
    print(file.read(4)) #pokarz  tylko cztery znaki od kursora i przesun go tam
    
    file.seek(0)
    print(file.readline()) #wyswietl cala linijke, mozna dac na koncu (... ,end = '') aby nie bylo kilku "\n" niepotrzebnie
    print(file.readline()) #wyswietla kolejna linijke
    
    file.seek(0)
    lista_readlines = file.readlines() #zwraca tablice/liste kolejnych linijek
    file.seek(0)
    print(file.readlines())
    print(lista_readlines[0]) #operacje jak na liscie
    
    file.seek(0)
    for line in file.readlines():
        print(line.strip()) #usuwa wszystkie biale znaki po obu stronach czyli ' ', "\t" itp., "rstip"-usuwa tylko z prawej strony znakow, "lstrip"-z lewej
    
    file.close()
    
    myReadFile('pliczek.txt')  

    with open('pliczek.txt','a',encoding="utf-8") as fd: #jesl sie nie zamnie to progam sam ja zamknie
        fd.close()

    lista = [10,20,'trzydzieści',[1,2,'trzy']]
    with open('plik.pickle','wb')  as outPut : #'wb' - zapis binarny
        pickle.dump(lista,outPut) #zapisywanie listy w pliku, moze to byc wszystko
        outPut.close()
    
    with open('plik.pickle','rb') as inPut: #'rb' odczyt binarny
        unpickle = pickle.load(inPut) #odczytywanie z pliku i wkladanie tego do zmiennej
    print(unpickle,type(unpickle))

if pokarz_operacje_na_systemie:
    lista_plikow_w_katalogu = os.listdir("..") #zapisz w liscie pliki z katalogu "."-biezacego, ".."-poprzedniego (poziom wyzej)
    #"../.."-dwa foldery wyzej, lub "/dev/..."-podajac sciezke bezwzglegna
    print(lista_plikow_w_katalogu)
    
    for plik_czy_katalog in lista_plikow_w_katalogu: #pokazuje         jest plikiem czy katalogiem
        if os.path.isfile(os.path.join("/home/grawiro/Documents/python/learn",plik_czy_katalog)): #join musi byc sciezka bezwzgledna bo inaczej nie dziala
            print("{} jest plikiem".format(plik_czy_katalog))
        if os.path.isdir(os.path.join("/home/grawiro/Documents/python/learn",plik_czy_katalog)):
            print("{} jest katalogiem".format(plik_czy_katalog))
    
    os.mkdir("folder_testtowy") #tworzy folder o podanej nazwie
    os.rename("folder_testtowy", "folder_do_testow") #zmienia nazwe
    os.rmdir("folder_do_testow") #usun folder
    
    path = "folder_testowy/01/dane_testowe.txt"
    os.makedirs(os.path.dirname(path)) #utworz katalogi z tej sciezki jesli ich nie ma, funkcja w () zwraca wartosc bez pliku
    os.path.basename(path) #zwraca nazwe pliku ze sciezki
    os.path.abspath(path) #zwraca sciezke bezwzgledna do katalogu/pliku tzn od poczatku
    open(path,"w").close() #utworz plik i go zamknij
    os.remove(path) #usun plik
    os.rmdir("folder_testowy/01") #usun folder 01
    os.rmdir("folder_testowy") #usun folder_testowy
    
if pokarz_inne_bibloiteki_i_funkcje:
    print("Losowa liczba -",random.randint(1,10)) #wylosuj liczbe od 1 do 10
    print (random.random()) #losuje liczbe z przecinkiem od 0 do 1
    
    print("zgubienie wartosci po przecinku -",math.floor(10.6))
    
    0xff
    0o14
    0b1001
    liczba = 31
    print(liczba,hex(liczba),oct(liczba),bin(liczba),sep=" = ") #zamiana wartosci na hex itp.

    cos = input("napisz cokowlwiek: ") #zapytaj o cokolwiek
    print(cos)

if pokarz_wyjatki:
    try: #sprawdz czy jest blad #jesli tak to przerwij to co robiles i przejdz do except
        pliczek = open("pliczek.txt", "a") #to generuje wyjatek
        pliczek.read()
        pliczek.close()
        
    except FileNotFoundError: #zlap wyjatek o nazwie File..., ale tylko o tej nazwie
        print("nie znaleziono pliku pliczek.txt")
        
    except Exception as erro: #zlap kazdy wyjatek (mozna go uzyc np do podania jego nazwy)
        print("nieznany blad \"{}\"".format(erro))

    finally:
        print("to sie wykona zawsze")

    class WlasnyWyjatek(Exception): #wlasna klasa wyjatku
        pass
    
    try:
        raise WlasnyWyjatek() #rzuc wyjatek o nazwie Wlas... #mozna uzywac na zawolanie
    except WlasnyWyjatek:
        print("uruchomiono wlasny wyjatek")
        
    class WlasnyWyjatek_2(Exception): #wlasna klasa wyjatku taka sie w sumie nie przydaje w normalnym uzyciu
    #ale mozna sie z takowo zapoznac    
        def __init__(self, parametr):
            super().__init__("Samowolne wywolanie bledu nr {}, jest zakazane :)".format(parametr))

    parametr_bledu = 3.46546

    try:
        raise WlasnyWyjatek_2(parametr_bledu) #z parametrem
    except WlasnyWyjatek_2 as erro:
        print("uruchomiono wlasny wyjatek 2", erro, sep='\n')

    try:
        input("Napisz cos ")
    except KeyboardInterrupt: #wyjatek CTRL+C #nie przerywaj programu
        print("CTRL+C")
    except:
        print("Zlap wszystkie wyjatki")

    try:
        raise Exception("Wypisz blad jaki chcesz")
    except Exception as Exce:
        print(Exce)

    x = 10
    assert x == 10 #jak sie nie zgadza to rzuc wyjatek

    #assert hasattr(k2, 'zdrowie') #sądzę, że k2 ma pole zdrowie. Jak nie ma - błąd

    ## asercja + try
    try:
        assert x==12
    except :
        print('mylisz się, x to nie jest 12')


if pokarz_klasy:
    class Kalkulator: #klasa Kalkulator nie trzeba podawac ()

        dzielnik = 423 #zmienna stala dla wszystkich obiektow chyba ze nada im sie inna wartosc
        
        def __init__(self, wartosc_zmiennej=-43): #konstruktor z parametrami
            self.zmienna_w_klasie = wartosc_zmiennej #zmienna dostepna w kazdej klasie
            self.ostatni_wynik = 0
            self.__priv = 2 #zmienna prywatna
            print("tworze klase kalkulator")
    
        def __del__(self): #destruktor
            print("usuwam klase")
        
        def __str__(self): #wywolywana samodzielnie podczas konwertowania klasy na string np w princie
            return "hello stringu "+str(self.__priv) #w metodach mozna normalnie korzystac z zmiennych prywatnych
        
        def __int__(self): #wywola sie podczas konwersji na inta
            return 13
        
        def __float__(sefl): #podczas kkonwersji na float
            return 4.5
        
        def __len__(self): #jaka dlugosc zwrucic
            return 4
        
        def __bool__(self): #podczas rzutownia na typ bool
            return False
        
        def dodaj(self, a, b): #matody w kalse a procdura w normalnej funkcji(procedura nic nie zwraca)
            self.ostatni_wynik = a+b
            print(a+b)
        
        def odejmij(self, a, b):
            self.ostatni_wynik = a-b
            print(a-b)
    
    class Kalkulator_v2(Kalkulator): #diedziczenie klas w (nazwa rodzica, kolejnego rodzica, itp.)
        '''nie ma to jak dobra dokumentacja, mozna ja napisac za pomoca \
           "", lub '', nie ma to zadnego znaczenia, dzieki \\ temu znakowi \
         mozna pisac od miejsca w ktorym sie zaczelo, a nie od poczatku lini'''
        #pod uwage brana jest tylko jedna dokumentacja czyli jedne "d", 'd', '''d'''
        #"to przerywa \
        #obecna linie"
        
        def __init__(self, wartosc_zmienne):
            super().__init__(wartosc_zmienne) #wywolanie konstruktora rodzica
            #super() to odwolanie sie do klasy nadzednej
            #jak dziedziczy sie z kilku klas to super() nie dziala i trzeba pisac np. Kalkulator.__init__() itp.
            print("tworze klase kalkulator_v2")
            self._alfa = None
        
        def dodaj(self, a, b, c):
            print(a+b+c)
        
        def pomnoz(self, a, b):
            self.ostatni_wynik = a*b
            print(a*b)

        # poprzedza metodę statyczną, jest to tzw. DEKORATOR (nie podoba mi się to określenie )       
        @staticmethod 
        def metoda_statyczna() :    # nie ma self !!, wywołanie to A.metoda_statyczna_klasy()
            print('Jestem instrukcją metody statycznej klasy')
            return True
  
        # Nie można używać na zewnątrz klasy, chyba, ze tak jak prywatny obiekt
        def __metoda_chroniona(self) :            
            return True
        
        @property #pobierz wartosc, ale najpierw urychom inny kod
        def alfa(self):
            print('a tu pobieramy sobie alfę i przy okazji wywolujemy cos innego')
            return self._alfa
  
        
        @alfa.setter #ustawia własność, i zrob cos jeszcze
        def alfa(self,v) :
            print('Zanim przypiszę wartość, mogę wywołać ... cokolwiek innego! ')
            self._alfa = v
            
        @alfa.deleter
        def alfa(self):
            print('no i sobie pokasujemy, bo co mamy robić?')
            del self._alfa
    
    kalku = Kalkulator() #obiekt klasy kalkulator
    
    kalku.dodaj(10,5)
    kalku.odejmij(5,7)
    
    print(kalku) #uzyje konwersji na str
    print(str(kalku)) #to samo co wczesniej
    print(int(kalku)) #konwersja na int
    print(len(kalku)) #zwraca dlugosc klasy
    print(bool(kalku)) #pokazuje typ bool klasy
    
    kalku.liczba = 10 #zmienne tworzona w locie tylko w tym obiekcie
    print(kalku.liczba) #uzycie tej zmiennej
    print(kalku.zmienna_w_klasie)
    print(kalku.ostatni_wynik)
    print(kalku.dzielnik)
    Kalkulator.dzielnik = 5
    print(kalku.dzielnik)
    kalku.dzielnik = 4 #juz jest traktowane jako zmienna tego obiektu a nie wspolny dla wszystkich obiektow
    print(kalku._Kalkulator__priv) #tak sie korzysta z prywatnych zmiennych inaczej jakby nie istnieja :) ale tylko poza klasa
    del kalku #usuwa obiekt ale i klase

    kalku_v2 = Kalkulator_v2(234)
    
    kalku_v2.dodaj(2,4,5) #z tej klasy
    kalku_v2.pomnoz(3,5)
    
    kalku_v2.odejmij(5,6)
    #kalku_v2.dodaj(1,3) #nie da sie wykonac poniewaz zostala zaslonieta przez funkcje z tej klasy
    print(kalku_v2.zmienna_w_klasie)
    print(kalku_v2.ostatni_wynik)

    Kalkulator_v2.metoda_statyczna() #wywolanie takie
    print('Chronione: ', kalku_v2._Kalkulator_v2__metoda_chroniona())
    
    print(kalku_v2._alfa) #zwyczajne nic sie nie dzieje nadzwyczajnego
    print(kalku_v2.alfa) #tu dobiorę się do _alfa, ale poprzez @property (geter)
    kalku_v2._alfa = 100 #przypisałem wartość bezpośrednio do _alfa nic nowego
    print(kalku_v2._alfa)
    kalku_v2.alfa = 10 #przypisałem wartość do _alfa, ale wywołałem też rzeczy przed bedace przed tym przypisaniem
    print(kalku_v2._alfa)

    del kalku_v2.alfa #wywołam deleter, czyli funkcję w momencue kasowania pola alfa

    print(kalku_v2.__doc__)#pokaz dokumentacje, czyli to co jest pod nazwa klasy, funkcji, jesli puste wypisze None
    print(Kalkulator_v2.mro()) #pokarz przodkow
    print(hasattr(kalku_v2,'opis')) #sprawdz czy jest taki attrybut i napisz True/False
    print(getattr(kalku_v2,'zdrowie',"Nie ma takiego atrubutu, moze zwracac cokolwiek np. 41 czy jakas liste")) #sprobuj pobrac wartosc z atrubutu, a jak ci sie nie uda to zwroc (obiekt, nazwa atrybutu,zwroc jak niema)

