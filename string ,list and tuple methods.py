Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #strip
>>> #rstrip(),lstrip()
>>> a="       python       "
>>> a.strip()
'python'
>>> a.lstrip()
'python       '
>>> a.rstrip()
'       python'
>>> #concatenation
>>> a="hello"
>>> b="world"
>>> print(a+b)
helloworld
>>> print(a+" "+b)
hello world
>>> #formatting
>>> a=10
>>> b=20
>>> print(a+b)
30
>>> print("the sum is",a+b)
the sum is 30
>>> a="deekshi"
>>> b="ch"
>>> print("the full name is",a+b)
the full name is deekshich
>>> print("the sum is a+b")
the sum is a+b
>>> #.format()
>>> a="sita"
>>> b="ram"
>>> print(hello {}{}".format(a,b))
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("hello {}{}".format(a,b))
      
hello sitaram
print("hello {} {}".format(a,b))
      
hello sita ram
print("hello {} hello {}".format(a,b))
      
hello sita hello ram
print("hello {0} {1}".format(a,b))
      
hello sita ram
#fstring
      
a="motu"
      
b="patlu"
      
print(f"hello {a} {b}")
      
hello motu patlu
print("hello {a}{b}")
      
hello {a}{b}
print(f"hello {a}{b}")
      
hello motupatlu
print(f"hello {a} hello {b}")
      
hello motu hello patlu
#list()
      
a=[2,4.5,"python",8+9j,True,False]
      
type(a)
      
<class 'list'>
b=4.5
      
type(b)
      
<class 'float'>
b=[4.5]
      
type(b)
      
<class 'list'>
a=["python","java","c","c++"]
      
type(a)
      
<class 'list'>
#append
      
a.append("html")
      
a
      
['python', 'java', 'c', 'c++', 'html']
a.append("css","js")
      
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.append("css","js")
TypeError: list.append() takes exactly one argument (2 given)
#extend()
      
a=["ds","ai","ml"]
      
a.extend(["java","python","css"])
      
a
      
['ds', 'ai', 'ml', 'java', 'python', 'css']
a.extend("java","python")
      
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.extend("java","python")
TypeError: list.extend() takes exactly one argument (2 given)
#insert()
      
a=["vja","hyd","bng","vzg"]
      
a.insert(1,"chennai")
      
a
      
['vja', 'chennai', 'hyd', 'bng', 'vzg']
#index()
      
a=["apple","banana","grapes"]
      
a.index("banana")
      
1
#reverse()
      
a.reverse()
      
a
      
['grapes', 'banana', 'apple']
b=[4,5,6,7,8]
      
b.reverse()
      
b
      
[8, 7, 6, 5, 4]
#sort()
      
a=["java","css",".net","python","c"]
      
a
      
['java', 'css', '.net', 'python', 'c']
a.sort()
      
a
      
['.net', 'c', 'css', 'java', 'python']
b=[8,0,2,4,6,8,15]
      
b.sort()
      
b
      
[0, 2, 4, 6, 8, 8, 15]
b.reverse()
      
b
      
[15, 8, 8, 6, 4, 2, 0]
a=["code","codegnan","course"]
      
a.remove()
      
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
a.remove("code")
      
a
      
['codegnan', 'course']
#pop()
      
a.pop()
      
'course'
a
      
['codegnan']
a.pop(0)
      
'codegnan'
a
      
[]
a=["ml","ai","ds","python"]
      
a.copy()
      
['ml', 'ai', 'ds', 'python']
#clear()
      
a.clear()
      
a
      
[]
b=[]
      
b.append("hi")
      
b
      
['hi']
a=["ml","ai","ds","python"]
      
b=a.copy()
      
b
      
['ml', 'ai', 'ds', 'python']
a="python"
      
len(a)
      
6
b=["python"]
      
b
      
['python']
len(b)
      
1
a=["python","java","c","c++"]
      
a.count("java")
      
1
a=[0,1,2,3,5]
      
a.sorted()
      
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
b=sorted()
      
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    b=sorted()
TypeError: sorted expected 1 argument, got 0
sorted(True)
      
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    sorted(True)
TypeError: 'bool' object is not iterable
a="python"
      
len(a)
      
6
b=["python"]
      
b
      
['python']
len(b)
      
1
a=["python","java","c","c++"]
      
a.count("java")
      
1
#tuple()
      
a=(4,6.7,"class",5+8j,True,False)
      
type(a)
      
<class 'tuple'>
a.count(6.7)
      
1
len(a)
      
6
s.index(5+8j)
      
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    s.index(5+8j)
NameError: name 's' is not defined
a.index(5+8j)
      
3
