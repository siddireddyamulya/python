# single comment  


''' multi comment'''

'''variables'''
# a=10
# print(a)

# a=10,20,40
# print(a)  

# a, b, c =10
# print(a, b, c) not running

# a=b=c= 1,9,6
# print(a)

# a,b,c=10,20,30
# print(a,b,c)


'''DATA TYPE----> TYPE OF THE VALUE'''

''' BASIC DATATYPES'''
'''
INT
FLOAT
BOOLEAN
STRING
COMPLEX
'''

# a=10
# b=-10
# print(type(a),type(b))

# a=True
# b=False
# print(type(a),type(b))


# a=4.44
# print(type(a))

# a="amulya"
# print(type(a))

# a=4+4j
# print(type(a))

'''TYPE CONVERSION '''
''' data lose----> explict type conversion'''
'''no data lose ---->implict type conversion'''

# a=4
# print(float(a))

# a=4.07
# print(int(a))

'''CONDITION STATEMENTS'''
'''
IF
ELSE
ELIF
NESTED IF
'''

# age=18
# if age > 18:
#     print("you are vote")
# elif age == 18:
#     print("you can vote")
# else:
#     print("you are not vote")  


# n=int(input())
# if n%11==0:
#     if n%11==1:
#         print("special eleven")
# else:
#     print("normal num")        


# n=input()
# if n==True:
#     if n==False:
#         print("hii")
#     else:
#         print("heyy") 
# elif n==False:
#     print("hello nana")


'''LOOPING STATEMENTS'''
'''RANGE METHOD AND EACH METHOD'''
 
 
# for i in range(0,10):
#     print(i)

# for i in range(0,10,2):
#     print(i)  

# a=[2,3,4,5,6,7]
# for i in a:
#     print(i)

# a="ammuamulya"
# for i in a:
#     print(i)

# while True:
#     print("hi")

# a=9
# while a<15:
#     print("hi",a)
#     a+=1

# for i in range(0,100):
#     for j in range(0,100):
#         print(i+j)

'''JUMPING STATEMENTS'''
'''
PASS
BREAK
CONTINE
'''

# for i in range(0,10):
#     pass


# a="python language"
# for i in a:
#     if i=="l":
#         break
#         print(i)

# a="pythonlanguage"
# for i in a:
#     if a=="l":
#         continue
#         print(i)

'''STRING AND STRING METHODS'''

# a='ammu'
# b="ammu"
# c='''ammu'''
# print(type(a), type(b), type(c))

'''STRING METHODS'''

'''
lower()
upper()
isupper()
islower()
split()
strip()
Rstrip()
Lstrip()
count()
index()
removeperfix()
removesuffix()
replace(old one,new one)
find()
starts with()
ends with()
'''

# a="python language"
# print(a.upper())

# a="APYTHON LANGUAGE"
# print(a.lower())

# a="python language"
# print(a.isupper())


# a="APYTHON LANGUAGE"
# print(a.islower())


# a="python language"
# print(a.split("/"))


# a="python language"
# print(a.count(a))


# a="python language"
# print(a.index(a))


# a="python language"
# print(a.find(a))


# a="      python language      "
# print(a.strip())
# print(a.Rstrip())
# print(a.Lstrip())



# a="python language"
# print(a.removeprefix(a))
# print(a.removesuffix(a))

# a="python language"
# print(a.replace("language","programmming"))


# a="python language"
# print(a.endswith("e"))
# print(a.startswith("p"))


'''STRING SLICING [start:end:skip]'''

# a="python is programming language"
# print(a[0:5])
# print(a[0:10:2])
# print(a[:-1])  
# print(a[:-2])
# print(a[:-1:4])


'''STRING INDEXING'''
# a="python is programming language"
# print(a[2])
# print(a[-1])
# print(a[10])

'''LIST METHODS []'''
'''
append
extend
count
insert
pop
remove
index
'''
'''MUTABLE DATA TYPE ----> CHANGEALBE'''


# a=[5,6,7,8,9,"amulya"]
# print(type(a))
# print(a[2])
# print(a[-1])
# print(a[0:7:2])


# a=[3,5,7,9,1,,3,"ammulu","python"]
# print(a.append("program"))
# print(a.extend([1,3,5,6,"ammu"]))
# print(a.count(3))
# print(a.remove(3))
# print(a.pop(3))
# print(a.index(3))


# a=[3,5,7,9,1,,3,"ammulu","python"]
# for i in a:
#     print(i)

'''TUPLE DATA TYPE ( )'''
''' IMMUTABLE--->NO CHANGES'''

'''tuple operations'''
'''
concatenation
iteration
membership operation
identity operation
repetation
'''
# a=(1,2,3,4,5,6)
# print(type(a))
# print(a[-1])
# print(a[0:5:2])
# print(max(a))
# print(min(a))
# print(sum(a))
# print(len(a))

# a=(1,2,3)
# b=(4,5,6)
# print(a+b)

# a=(1,2,3,4,5,6)
# print(a*5)
# for i in c:
#     print(i)

# print(2 in a)
# print(11 not in a)

'''DICTIONARY DATA TYPE {KEY : VALUE, ..... }'''
''' IMMUTABLE--->NO CHANGES   KEY ----> IMMUTABLE , VALUES---->MUTABLE'''
'''NO SLICING AND NO INDEX'''
'''METHODS'''
'''
get
update
values
keys
item
'''

# a={1:555,'g':123,6:888,'r':999}
# print(type(a))
# # print(a[1]) key calling
# print(a.get(1))
# print(a.keys())
# print(a.values())
# print(a.items())
# print(a.update({'a':777}))


# for i,j in {1:555,'g':123,6:888,'r':999}.items():
#     print(i,j)


'''SET { ELEMENTS AND NO DUPLICATES} UNORDERED'''
'''NO INDEX AND NO SLICING'''
''' SET METHODS'''
'''
add
update
pop
remove
'''
'''SET OPERATIONS'''
'''
UNION
INTERSECTION
DIFFERENCE
ISSUBSET
ISSUPERSET
'''

# s={1,3,4,2,14,7,8,3,2,9}
# print(s)
# s.add(123)
# print(s)
# s.update({1,2,366})
# print(s)
# s.pop()
# s.remove(2)
# print(s)


'''FUNCTION----> BLOCK OF CODE,RUN WHEN ITS CALLED'''
'''SYNTAX ---->def--->keyword, function name():'''

# def add(a,b):
#     return a+b
# print(add(1,2))

# def func(a,b,c):# function defination   
#     print("this is function:",a,b,c) # function body
# func(1,2,3)    #function call

# '''orbitary arguments ----> TUPLE'''

# def func(*a):# function defination   
#     print("this is function:",a) # function body
# func(1,2,3)    #function call

# '''KEYWORS ARGUMENTS ---->DICTIONARY'''

# def func(**a):# function defination   
#     print("this is function:",a) # function body
# func(a=1,b=2) 

# '''NESTED FUNCTIONS'''

# def outer():
#     print("outer function")
#     def inner():
#         print("inner function")
#     inner()
# outer()


# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)

'''FILE HANDLING ----> READING,WRITING,CREATING,DELETING'''

'''MODES'''
'''

OPEN

r--read mode
w--write mode (trucate)
a--append mode
r+--read write
w+--write read (truncate)

CLOSE
'''

# s=open('demo2.txt',mode='r')
# print(s.read())
# s.close()

# # s=open('demo2.txt',mode='w')
# # print(s.write())
# # s.close()

# s=open('demo2.txt',mode='r+')
# s.read()
# s.write("r+ mode")
# s.close()

# s=open('demo2.txt',mode='w+')
# s.write("w+ mode")
# s.seek(0)
# print(s.read())
# s.close()

# f = open("geek.txt", "r")

# print("Filename:", f.name)
# print("Mode:", f.mode)
# print("Is Closed?", f.closed)

# f.close()
# print("Is Closed?", f.closed)

''' ERROR HANDING'''

'''
try:
risky code
except:
print("error")
else:
print("mo error")
finally:
print("always")
'''

# try:
#     print(b)
# except:
#     print("error")    
# else:
#     print("no error")
# finally:
#     print("always")


# try:
#     print('a'+33)
# except TypeError :
#     print("type error")
# except ValueError:
#      print("value error") 


'''OOPS CONCEPT'''
''' CLASS ---> class is a blue print of obeject and template'''
'''SYNTAX---> class class_name():'''
'''OBJECT----> PHYSICAL ENTTY AND combination of DATA AND FUNCTION'''
'''SYNTAX---->object name=clas name()'''

# class python():
#     a=2
#     def output(self):
#         print(self.a)
# b=python()
# b.output()   

# class ummar:
#     print("outer")
#     def display(self):
#         a=10
#         b=20
#         print(a,b)
# obj=ummar()
# obj.display()     

# class ummar:
#     d=60
#     def display(self):
#         a=10
#         b=20
#         print(a,b)
# obj=ummar()
# obj.display()
# print(obj.d)



# class mobile:
#     def __init__(self,brand,battery,ram,camera,price):
#         self.brand=brand
#         self.battery=battery
#         self.ram=ram
#         self.camera=camera
#         self.price=price
#     def display(self):
#         print("brand:",self.brand)
#         print("battery:",self.battery)
#         print("ram:",self.ram)
#         print("camera:",self.camera) 
#         print("price:",self.price)     
# obj=mobile("apple","400mah","8gb","48mp","9000")
# obj.display()
        
# class mobile:
#     def __init__(self,brand,battery,ram,camera,price):
#         self.brand=brand
#         self.battery=battery
#         self.ram=ram
#         self.camera=camera
#         self.price=price
#     def display(self):
#         print("brand:",self.brand)
#         print("battery:",self.battery)
#         print("ram:",self.ram)
#         print("camera:",self.camera) 
#         print("price:",self.price)     
# obj=mobile("apple","400mah","8gb","48mp","9000")
# obj.display()
# obj=mobile("oneplus","900mah","9gb","98mp","9000")
# obj.display()


# class mobile:
#     def __init__(self,brand,battery,ram,camera,price):
#         self.brand=brand
#         self.battery=battery
#         self.ram=ram
#         self.camera=camera
#         self.price=price
#     def display(self):
#         print("brand:",self.brand)
#         print("battery:",self.battery)
#         print("ram:",self.ram)
#         print("camera:",self.camera) 
#         print("price:",self.price)    

# for i in range(5):
#     obj=mobile("apple","400mah","8gb","48mp","9000")
#     obj.display()
#     obj=mobile("oneplus","900mah","9gb","98mp","9000")
#     obj.display()   

'''init method--->is called constuctor ---> when the object is create pro execute''' 

# class ummar:
#     def __init__(self):
#         print("this is init")
#     def display(self):
#         print("this is methd")
# obj=ummar()            
    

'''INHERTANCE----> parent porperties---->child'''
'''
SINGLE INHERITANCE
MULTILEVEL INHERTANCE
MULTIPLE INHERITANCE
HIERARCHICAL INHERITANCE
'''
'''single'''
# class parent():
#     def output(self):
#         print("i am parent")
# class child(parent):
#     def outputc(self):
#         print("i am chid")
# c=child()
# c.outputc()        # child method 
# c.output()         # parent method
     
'''multilevel'''
# class grandfather():
#     def outputgf(self):
#         print("i am grand father")
# class parent(grandfather):
#     def output(self):
#         print("i am parent")
# class child(parent):
#     def outputc(self):
#         print("i am chid")
# c=child()
# c.outputc()        # child method 
# c.output()        # parent method
# c.outputgf()      

'''multiple'''
# class father():
#     def outputgf(self):
#         print("i am father")
# class mother():
#     def output(self):
#         print("i am mother")
# class child(father,mother):
#     def outputc(self):
#         print("i am chid")
# c=child()
# c.outputc()        # child method 
# c.output()        # parent method
# c.outputgf()      

'''hierarchical'''
# class father():
#     def outputgf(self):
#          print("i am father")
# class child1(father):
#      def output(self):
#          print("i am child1")
# class child2(father):
#      def outputc(self):
#        print("i am child2")
# c1=child1()
# c2=child2()
# c1.output()                  # child method 
# c1.outputgf()        # parent method   
# c2.outputc()        # child method                 # parent method
# c2.outputgf()      


'''SUPER KEYWORD'''

# class A:
#     def __init__(self):
#         print("this is class a")
#     def fun1(self):
#         print("method")    
# class B(A):
#     def __init__(self):
#         print("this is class b")
#         super().__init__()
#     def fun2(self):
#         print("method2")

# obj=B()
    
'''
PLOYMORPHISM---->2 types--->compile time
a) method over-loading---->same class,same func(or)methods names,diff arguments
run time
b) method over-riding--->diff class,same func name,diff para
'''

'''method over-loading ---->over comes the method over loading '''

# class A:
#     def sum(self,a,b):
#         return a+b
#     def sum(self,a,b,c=1):
#         return a+b+c       # this should be run frit than you can take defalt values
# obj=A()
# print(obj.sum(1,3))


'''method over-riding---->over come using super keyword in method over-riding'''

# class A:
#     def display(self):
#         print("this is class A")
# class B(A):
#     def display(self):
#         print("this is class B")
#         super().display()
# obj=B()
# obj.display()

'''ABSTRACTION---->Hidding of data'''

''' ENCAPSUTION--->binting of var and func'''

'''wrapping of variables methods in a single unti i call encapsulation
public
private  __
protected_'''


# class demo():
#     def  __init__(self,a,b):
#         self.__a=a
#         self._b=b
# class demo2(demo):
#     def output(self):
#         print(self._b)
# d=demo2(3,2)
# d.output()                
    

# def add(a,b):
#     print(a+b)
# add(1,2)
# add('a','b')
# add([34,8],[9,7])
# add((4,6),(6,9))   




# import os

# # single directory
# os.mkdir("my_directory")

# # nested directories
# os.makedirs("parent_directory/child_directory")
























































































