# quadratic equation
print('ex 1 my')
a, b, c = 1, -14, 49
d = b**2 - 4*a*c

if d == 0:
    print((-b) / (2*a))
elif d > 0:
    d **=.5
    print((-b-d) / (2*a), (-b+d) / (2*a))
else:
    print('there are no elements')

# Prime number
print('\nex 3 my')
import math
n = 2
prime = True
if n == 2:
    print("{} is a Prime number".format(n))
elif n > 1:
    for i in range(2, math.ceil(n**0.5)+1):
        if n%i == 0:
            print("{} is not a Prime number".format(n))
            prime=False
            break
    if prime:
        print("{} is a Prime number".format(n))
else:
    print("{} is not a Prime number".format(n))

print('\nex 3 my v2.0')
n = 4
prime = True
for i in range(2, int((n**0.5)+1)):
    if n%i == 0:
        prime=False
        break
print("{} is{} a Prime number".format(n, '' if prime else ' not'))

# this dont work correct, because 2 is prime number
print('\nex 3 they')
n=3
i=1
prime = True
while i*i<=n:
    i+=1
    if n%i==0:
        prime=False
        break
print(prime)

# find all sub indexes
print('\nex 4 my')
x = 'find all sub indexes: I like coffee, I like tea,'\
'I want you to play with me!'\
'I like coffee, I like tea,'\
'I like my friends, and they like me!'
s ='I'
l=[]
i=0
while True:
    i = x.find(s, i)
    if i!=-1:
        l.append(i)
        i+=1
    else:
        break
print(l)

print('\nex 4 they')
l=[]
i=-1
while s in x:
  j=x.index(s)
  x=x[j+1:]
  i+=j+1
  l.append(i)
print(l)

# fast power algorithm
print('\nex 5 they v1.0')
# intiger division and modulo in one
print(divmod(5,2))

x, n = 2, 8 
res=1
kw=x
while n:
  if n%2:
    res*=kw
  kw*=kw
  n/=2
# it's from me, it doesn't work without it
  n = int(n)
print(res)

print('\nex 5 they v1.5')
x, n = 2, 8
res=1
kw=x
while n:
  n,m=divmod(n,2)
  if m:
    res*=kw
  kw*=kw
print(res)


print('\nex 5 they v2.0')
x, n = 2, 8
res=1
kw=x
while n:
  if n&1:
    res*=kw
  kw*=kw
  n>>=1
print(res)

# Euclid's algorithm
print('\nex 6 my')
a, b = 10, 14
while a != b:
    if a > b:
        a-=b
    else:
        b-=a
print(a)

print('\nex 6 they')
a, b = 10, 14
if a<b:
  a,b=b,a
while b:
  a,b=b,a%b
print(a)

# Extended Euclid's algorithm
print("\nI don't understand what's going on in this exercise")
print('ex 7 my')
a, b = 30, -28
xa, xb, ya, yb = 1,0,0,1
while b != 0:
    a %= b
    xa -= xb * (a//b)
    ya -= yb * (a//b)

    a, b = b, a
    xa, xb = xb, xa
    ya, yb = yb, ya

print(a,b, xa, ya) 


print('\nex 7 they')
a, b = -30, 28
zamien=(a<b)
if zamien:
  a,b=b,a
k=(1,0,0,1)
while b:
  a,d,b=[b]+list(divmod(a,b))
  k = (k[2], k[3], k[0] - d*k[2], k[1] - d*k[3])
if zamien:
  x,y=k[1],k[0]
else:
  x,y=k[0],k[1]
print(a, b, x, y)

print('\nex 8 my')
some_list = list(range(1,15))
print([i*2 if i%2 else i for i in some_list if i%3!=0])

# cutting from a string of characters, numbers or letters
print('\nex 9/10 my')
some_list = ['a1b', '2cb', '432', 'sa']
i, j=0, 0
while True:
    # isalpha() to cut letters
    if some_list[i][j].isdigit():
        some_list[i] = some_list[i][:j] + some_list[i][j+1:]
        j-=1
    if j < len(some_list[i])-1:
        j+=1
    else:
        i+=1
        j=0
    if i > len(some_list)-1:
        break
while ('' in some_list):
    some_list.remove('')
# this to convert to int
# some_list = [int(i) for i in some_list]
print(some_list)

# it was hard to guess both
print('\nex 9 they')
some_list = ['a1b', '2cb', '432', 'sa']
print([''.join([i for i in j if i.isalpha()]) for j in some_list])

print('\nex 10 they')
some_list = ['a1b', '2cb', '432', 'sa']
print([int(k) for k in [''.join([i for i in j if i.isdigit()])
    for j in some_list] if k])

print('\nex 11 my')
some_list = [(1,), (2,3,4), (3,4), (2,4), (6,9,21)]
# tuple(i[:2]) # better
print([tuple([i[0], i[1]]) for i in some_list if len(i)>=2])

print('\nex 12 my')
some_list = [(1,), (2,3,4), (3,4), (2,4), (6,9,21)]
print([i for i in some_list if not sum(i)%2])

print('\nex 13 my')
some_list = [(1,), (2,3,4), (3,4), (2,4), (6,9,21)]
print([i for i in some_list if len([j for j in i if not j%3])==len(i)])

print('\nex 13 they')
some_list = [(1,), (2,3,4), (3,4), (2,4), (6,9,21)]
print([i for i in some_list if all([j%3==0 for j in i])])

print('\nex 14 my')
some_list = [(1,), (2,3,4), (3,4), (2,4), (6,9,21)]
print([i for i in some_list if [j for j in i if not j%3]])

print('\nex 14 they')
some_list = [(1,), (2,3,4), (3,4), (2,4), (6,9,21)]
print([i for i in some_list if any([j%3==0 for j in i])])

print('\nex 15 my')
some_list = ['this is', 'so far', 'none to none']
print([i.split(' ')[0] for i in some_list])

print('\nex 17 they')
some_text = '2 * a * b_1 + sin(alpha) * cos(alpha)'
print(['+'] +[['*']+i.split('*') for i in some_text.split('+')])

print('\nex 20 my')
def decode_tree(some_dict):
    some_list = [[]]
    tmp = list(some_dict.items())
    for i in tmp:
        if len(i[1])==1:
            some_list.insert(int(i[1][0]), i[0])
        elif len(i[1])==2:
            if some_list[int(i[1][0])]:
                some_list[int(i[1][0])].insert(int(i[1][1]), i[0])
            elif not some_list[int(i[1][0])]:
                some_list.insert(int(i[1][0]), [])
                some_list[int(i[1][0])].insert(int(i[1][1]), i[0])
    some_list.remove([])
    return some_list

some_dict = {
    'a':'00',
    'b':'01',
    'c':'1',
    'd':'20',
    'e':'21',
    }
some_list= decode_tree(some_dict)
print(some_list)

print('\nex 21 my')
def figure_fields(*args):
    if len(args)==1:
        print(args[0]*args[0])
    elif len(args)==2:
        print(args[0]*args[1])
    
figure_fields(2)
figure_fields(3,4)



print('\nex 22 my')
some_list = list(range(1,15))
print(list(map(lambda x: x*2 if x%2 else x, filter(lambda x: x%3, some_list))))
some_list = ['a1b', '2cb', '432', 'sa']
print(list(map(lambda x: ''.join(filter(lambda y: y.isalpha(), x)), some_list)))
# 1
some_list = ['a1b', '2cb', '432', 'sa']
tmp = list(map(lambda x: ''.join(filter(lambda y: y.isdigit(), x)), some_list))
tmp.remove('')
print(list(map(lambda x: int(x), tmp)))
some_list = [(1,), (2,3,4), (3,4), (2,4), (6,9,21)]
print(list(map(lambda x: x[:2], filter(lambda y: len(y)>=2, some_list))))
some_list = [(1,), (2,3,4), (3,4), (2,4), (6,9,21)]
print(list(filter(lambda x: not sum(x)%2, some_list)))
print(list(filter(lambda x: all(map(lambda y: not y%3, x)), some_list)))
some_list = ['this is', 'so far', 'none to none', 'zero_spaces']
print(list(map(lambda x: x.split(' ')[0],filter(lambda y: ' ' in y, some_list))))


print('\nex 22 they')
# 1
some_list = ['a1b', '2cb', '432', 'sa']
print(list(map(int,filter(bool,map(lambda j:''.join(filter(
    lambda i:i.isdigit(),j)),some_list)))))

print('\nex 23 my')
some_list_1 = [1, 2]
some_list_2 = [3,-5]
print(sum(map(lambda x : x[0]*x[1], zip(some_list_1, some_list_2))))

print('\nex 25 my')
some_list = ['this is', 'so far', 'none to none', 'zero_spaces']
print(sorted(some_list, key=lambda x: len(x)))
print(sorted(some_list, key=lambda x: x.split()))
print(sorted(some_list, key=lambda x: x.split()[-1]))
# sort by number of letters
print(sorted(some_list, key=lambda x: sum(map(bool, filter(
    lambda y: y.isalpha(), x)))))

# sort dict by values
print('\nex 26 my')
some_dict = {
    'aba': 123,
    'gtr': 32,
    'ddf': 311,
    }
some_list = list(some_dict.items())
print(sorted(some_list, key=lambda x: x[1]))

print('\nex 26 they')
print(sorted(some_dict.keys(),key=lambda x: some_dict.get(x)))

print('\nex 27 my')
some_list = [lambda x: x-1, lambda x: x**2, lambda x: 2**x]
print(sorted(some_list, key=lambda x: x(0)))

print('\nex 28 my')
some_list = [4, 0, 9, 6]
import functools
print(functools.reduce(lambda x,y: 10*x+y, some_list))

print('\nex 31 my')
some_dict = {
    'aba': 123,
    'gtr': 32,
    'ddf': 311,
    }
print(min(some_dict.items(), key=lambda x: x[1]))

print('\nex 31 they')
print(min(some_dict.keys(), key=some_dict.get))

print('\nex 33 my')
import subprocess
some_list = (subprocess.check_output(
    'du -s {}/* | sort -hr'.format('/usr'), shell=True)).decode().split('\n')
some_list = list(map(lambda x: x.split('\t'), some_list))
some_list.remove([''])
print(some_list)

print('\nex 34 my')
a = int(some_list[0][0])/40
k = -1
i = 0
some_list.reverse()
while i<len(some_list): 
    if int(some_list[i][0])<a:
        if k==-1:
            k=i
            some_list[i][1] = 'rest'
        elif int(some_list[k][0])+int(some_list[i][0])<int(some_list[-1][0]):
            some_list[k][0]=int(some_list[k][0])+int(some_list[i][0])
            some_list[i][0] = ''
            some_list[i][1] = ''
        else:
            some_list[i][1] = some_list[i][1].rsplit('/',1)[-1]
    else:
        some_list[i][1] = some_list[i][1].rsplit('/',1)[-1]
    i+=1
while ['',''] in some_list:
    some_list.remove(['',''])
some_list.reverse()
print(some_list)

print('\nex 35 my')
i=0
while i<len(some_list):
    print('{:<7} {:<}'.format(some_list[i][0], some_list[i][1]))
    i+=1

print('\nex 33 they')
s='/usr/'
s=subprocess.check_output('du -s {0}* | sort -hr'.format(s),shell=True)[:-1]
s=s.decode('utf8').split('\n')
s=[i.split('\t') for i in s]

print('ex 34 they')
s=[(int(i[0]),i[1].rsplit('/',1)[-1]) for i in s]
r=0
while (len(s)>2) and s[-1][0]+r < s[0][0] and s[-1][0]<s[0][0]/40:
  r+=s.pop()[0]
if r:
  s.append((r,'reszta'))

print('ex 35 they')
ss = s
ss='\n'.join(map(lambda i:'{:<7} {}'.format(*i),ss))
print(ss)

print('ex 36 they')
s=[(i[0]*40//s[0][0]*chr(9617),i[1])for i in s]
s='\n'.join(map(lambda i:'{0:<40s} {1:s}'.format(*i),s))
print(s)

print('ex 38 my')
from time import time
from requests import get

def capital_1(country):
    '''to search in Polish need:
    change en to pl and Capital to Stolica'''
    wiki = get('https://en.wikipedia.org/wiki/{}'.format(country))
    if '>Capital<' in wiki.text:
        a = wiki.text.find('title="' ,wiki.text.index('>Capital<'))+7
        b = wiki.text.find('">',a)
        return wiki.text[a:b]
    wiki.close()

def capital_2(country):
    b=''
    wiki = get('https://en.wikipedia.org/wiki/{}'.format(country), stream=True)
    for i in wiki.iter_lines():
        a,b=b, i.decode()
        if '>Capital<' in a:
            beg = a.find('title="', a.index('>Capital<'))+7
            end = a.find('">',beg)
            return a[beg:end]
    wiki.close()

def capital_2_pl(country):
    c,b='',''
    wiki = get('https://pl.wikipedia.org/wiki/{}'.format(country), stream=True)
    for i in wiki.iter_lines():
        a,b,c=b,c, i.decode()
        if '>Stolica<' in a:
            beg = c.find('title="')+7
            end = c.find('">',beg)
            return c[beg:end]
    wiki.close()

countries = [ 'Poland', 'Lithuania', 'Latvia', 'Estonia', 'Finland', 'Sweden', 'Norway', 'Iceland']

time_less=time()
print(list(map(capital_1,countries)))
time_less_1=time()

time_less_2=time()
print(list(map(capital_2,countries)))
time_less_3=time()
print('{:.2f}'.format(time_less_1-time_less))
print('{:.2f}'.format(time_less_3-time_less_2))

print('ex 38 they')
def stolica1(s):
  f=get('http://pl.wikipedia.org/wiki/'+s)
  s=f.text
  f.close()
  return s.split('Stolica</a>',1)[1].split('">',1)[1].split('<',1)[0]

  
def stolica2(s):
  f=get('http://pl.wikipedia.org/wiki/'+s,stream=True)
  b,c='',''
  for l in f.iter_lines():
    a,b,c = (b,c,l.decode('UTF-8'))
    if 'Stolica</a>' in a:
      f.close()
      return c.split('">',1)[1].split('<',1)[0]
  f.close()


kraje=['Polska','Litwa','Łotwa','Estonia','Finlandia','Szwecja','Norwegia','Islandia']

t=time()
print(list(map(stolica1,kraje)))
t_2=time()
print(list(map(stolica2,kraje)))
print(t_2-t)
print(time()-t_2)