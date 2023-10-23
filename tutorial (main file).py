#Running python program from terminal using just below line
# Python filename.py
#hit enter


#Checking same type 

'''name = "Nishant"

print(type(name) == str)
print(isinstance(name, str))

age = 2.
print(isinstance(age, int))'''

#Casting

'''s = str(age)
print(s)'''

#print(-1+ -1)
'''age = 2
age **=10
print(age)'''





#Boolean operator

# or returns first operand if it is true
#else if first is false returns second in any case

'''print(0 or 1) #1
print(False or 'hey') # hey
print('hi' or 'hey') # hi
print([] or False) # False
print(False or [])  #[]
'''


# and returns first operand if it is false
#else if first is true returns second in any case
'''
print(0 and 1) #0
print( 1 and 0) #0
print(False and 'hey') #False
print('hi' and 'hey') #hey
print([] and False) #[]
print(False and []) #False

'''



# is and in

'''is : identity operator
in : memeber ship operator

Ternaty operator : True if (condition) else False
'''




#Strings

#defined with " " or ' '

'''
#append with '+'
phrase  = 'My naame' + ' Nishanr'

#conver to string
age = str(39)


'''

#Printing multiple lines
"""
print('''My name is nishant

above is space
''')

"""





#string methods

'''

name = "nishant Singh parihar"

#get upper version of string
print(name.upper())

#get lower version of string
print(name.lower())

#get first letter upper and other lower
print(name.title())

#check of lower or not
print(name.islower())


#check of upper or not
print(name.isupper())

#check if string only have character and not empty
print(name.isalpha()) 

#check if a string contains characters or digits and is not empty
print(name.isalnum())

#check if a string contains only digits and is not empty
print(name.isdecimal())
print("n95".isdecimal())
print("95".isdecimal())

#check if string start with a specific pattern
print(name.startswith('ni'))

#check if string end with a specific pattern
print(name.endswith('ni'))

#replace a part of string
print(name.replace('n', 'z'))

#split a string on specific character separator, returns a list
print(name.split('a')) #splits string at every 'a' excluing it.
# ['nish', 'nt Singh p', 'rih', 'r']

l = ['1', '2', '3','4', '5']
print(" ".join(l))

#Find Position of substring

print(name.find('ni'))


#LEngth of string
print(len(name))

# use of 'in'

print('ni' in name) #true

#use of 'is'

exm = name
print(exm is name) #  true

#Scape character back slash '\'
exm = 'nish\'ant'
print(exm) # nish'ant

exm = 'nish\\ant'
print(exm)
 

 #string slicing
print(name[1:7]) #ishant
print(name[:7]) #nishant
print(name[7:]) # Singh parihar

'''










# Boolean true if a number excluding 0 including negatives
# Boolean true a string excluding empty string
# boolean false if list, string, tuple empty

'''
# use of any()
l = ['a', 'b', 'c' ,'']

#getting if any one value in l is true
print(any(l))

# use of all()

#getting all the value of l are true or not

print(all(l))

#complex number in python

num1 = 1 + 2j
num2 = complex(1, 2)
print(num1) #(1+2j)
print(num2) #(1+2j)
print(num2.real, num2.imag) #1.0 2.0

#Getting absolute value

n = -5.6
print(abs(n))

#getting rounded to zero 
print(round(n))'''






#Enums
'''

#way to create constant in python
from enum import Enum

class options(Enum):
    first = 'yes'
    second = 'no'

print(options.first.value)
print(options.second.value)
print(list(options)) #[<options.first: 'yes'>, <options.second: 'no'>]
print(len(options)) #count
'''



#Lists

dogs = ['roger', 'syd', 1, True]
print(dogs)

#checking value exist or not
print('roger' in dogs)

#slicing list
print(dogs[1:2])

#length of list
print(len(dogs))

#append in list
dogs.append(['h', 'g']) #appends as an elment
print(dogs)  #['roger', 'syd', 1, True, ['h', 'g']]


#extending list using another list
dogs.extend(['h', 'g'])
# dogs += ['h', 'g'] #works same
print(dogs) #['roger', 'syd', 1, True, ['h', 'g'], 'h', 'g']


#Remove
dogs.remove(['h', 'g'])
print(dogs)

 #remobe last item
print(dogs.pop()) #retuens popped item, here 5


#inserting at specific index
dogs.insert(3, 'hi')
print(dogs) #['roger', 'syd', 1, 'hi', True, 'h']


#inserting multiple element at specific index

dogs[1:2] = ['inserted1', 'inserted2']
print(dogs)


#sorting a list
test = ['hi', 'nish', 'pari', 'game']
testcopy = test[:] #Copy of list
# testcopy = test cant br done.
test.sort()
print(test) #['game', 'hi', 'nish', 'pari']
print(testcopy)

#new list without modifying the existing list
print(sorted(testcopy)) #return a list

#give key = str.lower to avoid upper lower case conflict



#Tuples
#You can no modify an exisiting tuple

names = ("Roger", "Syd", "hi","1")
print(names[-1])
print(names.index("1"))

print(len(names)) 
print("1" in names) #True

#slicing a tuple
print(names[0:2])

#soritng 
print(sorted(names, key=str.lower))

#making new from exisiting one
newnames = names + ("raj",)
print(newnames)




#Dictionary

# key : value pair
#Key can be any immutable value like string, number , tuple
#value  can be anything
dog = {"name" : "Roger",
       "age" : 8}

print(dog['name']) #roger

dog['name'] = "syd"
print(dog) #{'name': 'syd', 'age': 8}


print(dog.get('name'))
#can add a default value if element not found
print(dog.get('nam' , 0))


#return and delete the item
print(dog.pop("name")) #syd
print(dog) #{'age': 8}

#poping out last item added
print(dog.popitem()) #('age', 8)
print(dog) #{}

numbers = {1 : 'one',
       2 : 'two',
       3 : 'three'}
print(numbers)

#cheking if a key exist in a dict.
print(1 in numbers) #True

#getting all keys
print(numbers.keys())   #dict_keys([1, 2, 3])
#gwtting all key as a list
print(list(numbers.keys()))  #[1, 2, 3]


#getting all values
print(numbers.values())
print(list(numbers.values()))

#getting all items of dict. as a list
print(numbers.items()) #dict_items([(1, 'one'), (2, 'two'), (3, 'three')])

print(len(numbers)) #3

#Adding new item
numbers[4] = 'four'
print(numbers) #{1: 'one', 2: 'two', 3: 'three', 4: 'four'}


#delete an item
del numbers[4]
print(numbers)

#copy a dict
num_copy = numbers.copy()





#SETs

#Tuples like but not ordered
#mutable
#can work like dictionary without keys
#Frozen sets immutable version of set
#Sets remooves duplicates and keep single video


set1 = {"Roger", "Syd"}
set2 = {"Roger"}

intersect = set1 & set2
print(intersect)  #{'Roger'}
 

union = set1 | set2
print(union)   #{'Syd', 'Roger'}

difference = set1 - set2
print(difference)  #{'Syd'}

superset = set1 > set2 #True(set1 is superset of set2)
print(superset)

print(len(set1))

print(list(set1))

print('Roger' in set1)



#Functions

def hello():
    print('Hello!')

hello()

#with parameter

def hello(name):
    print('Hello! ' + name)

hello("Nishant")


#parameters are values excepted by the function inside function definition
#arguments are values paseed to the function


#Default parameter
def hello(name = "my friend"):
    print('Hello! ' + name)

hello("Nishant")



#Multiple parameter
#SyntaxError: non-default argument follows default argument
def hello(name , age = "15"):
    print('Hello! ' + name + " and your age is " + str(age))

hello("Nishant", 18)


#paremeters are passed by refernce
#chnges are reflected outside of the function
#but not with immutables like intergers, boolean, flaots, dtrings and tuples



#Return

def hello(name):
    if not type(name) == str:
        return "not", "a", "String" #return type <class 'tuple'>
    print("hello " + name)

print(type(hello(8)))



#Function inside a function

def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split(' ')
    for word in words:
        say(word)

talk("phrase as word")


#using local variable from outer function in inner function


def count():
    count = 0

    def increment():
        nonlocal count
        
        count = count + 1
        print(count)
    
    
    increment()

count()



#clusure
#returning a function and letting it active even if outer
#---function is not active


def count():
    count = 2

    def increment():
        nonlocal count
        
        count = count + 1
        print(count)
    
    
    return increment

inc = count()
inc() #3
inc() #4 #keeps track of the previous valus of outer function variable
inc() #5 #even after counter function is not active





#objects

#every things in python is object

#objects have methods and attributes to acces

a = 8
print(a.real)
print(a.bit_length())  #bit used here 4

items = [1, 2]
items.append(5)

print(id(items))  #lacotion in memory


#Loops

condition = True
while condition == True:
    print("blah")
    condition = False


item = [1, 2, 3, 4]

for i in item:
    print(i)

for i in range(8, 15):
    print(i)

#getting index and value together
#enumerate is used for this

for ind, value in enumerate(item):
    print(ind, value)


#break and continue

for i in range(8, 15):
    if(i == 10):
        continue
    print(i)

for i in range(8, 15):
    if(i == 10):
        break
    print(i)



#Classes

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def bark(self):
        print("woof!")
    
    def show(self, s):
        print(self.name + " " + s)
   

roger = Dog("Nishant", 18)
roger.show('blah')



#Inheritance

class vehicle:

    def start(self):
        print("vroom, vroom vroom....vrmmmm")

    def drive(self):
        print("Driving..parent")

class car(vehicle):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def getter(self):
        print(self.brand)
        print(self.color)

    def drive(self):
        print("Driving..child")

c = car("tata", "red")
c.getter()
c.start()
c.drive()





#modules
import module_example as i

# we can also import only function using below comment line
# from module_example import show

i.show()


#imporing a file or function from specific file
#which is inside a folder
#for this create a folder
#put module files in that folder
#and create an extra file __init__.py in same folder
#this file indicates that this is a module folder

from module_folder_example import module_in_folder_example

#we can aslo import functions directly using below commented line
#from module_folder_example.module_in_folder_example import show

module_in_folder_example.show()



#Pyython standard libraries

#math for math utility
#re for reguler expressions
#json for json related  works
#datetime for date and time
#sqlite3 to use SQLite
#os for OS utility
#random for random number generation
#statistics for statistics related work
#request to perform HTTP network request
#http to create HTTP servers
#urllib to manage URLs


#math for math utility
import math
# from math import sqrt

print(math.sqrt(16))




#Passing arguments from command line to python program
#it is done using sys module
import sys 

#put arguments after command Python filename.py
#all arguments should be space saparated
#all arguments are passed to program as a list of strings
#first element of the argument list is file name

#list of arguments is accessed using sys.argv

#commmand given:  python tutorial.py hi hello bye

print(sys.argv)  #['tutorial.py', 'hi', 'hello', 'bye']

print(sys.argv[0]) #tutorial.py






#Command line arguments using argparse

import argparse

#creating parser
parser = argparse.ArgumentParser(
        description='this is an example of using argparse'
)

#print(parser)

#creating arguments
#keep required = True if want tomake argument compulsory
parser.add_argument('-c', '--color',  metavar='color',
                    required=False, help='the color to search for')


'''
#only once this can be done thts why commented
#used below as well
args = parser.parse_args() 
print(args) #Namespace(color='red')
print(args.color)

'''

#Adding an arguments with choices

parser.add_argument('-s', '--size',  metavar='size',
                    required=False, help='the size to search for',
                    choices={'1', '2'})

args = parser.parse_args()
print(args) #Namespace(color='red')





#lamda functions

#no name only expression as a body
# lambda input_part : return_part
lambda num : num**2

var = lambda a,b : a**b
print(var(2, 3))  #8
 


#map(), filter(), reduce()

#map(): returns a new list with updating elemants according
#-to given function
number = [1, 2, 3]

def double(a):
    return a*2

result = list((map(double, number)))
print(result)

#Using lamda function

#new list
result = list((map(lambda a : a*2, number)))
print(result)



#Filter()
#Filters the elements of list and return new list

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def isEven(n):
    return n%2 == 0

result = list(filter(isEven, numbers))

print(result)


#Using lambda Function

result = list(filter(lambda n: n%2==0, numbers))

print(result)




#reduce()

from functools import reduce

expenses = [
            ('Dinner', 80),
            ('Car repair', 120)
            ]

sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)



#Recursion

def fact(n):
    if(n == 1): return 1

    return n*fact(n-1)

print(fact(5))





#Decorators 
#Decoratorrs are used to use an already defined funtions
#with some extra funtinality
# it is implimented using @
# It should return a function

def logtime(func): #taking a function as parameter
    def wrapper():
        print("Before")
        val = func()
        print("after")
        
    return wrapper  #returning a function

@logtime
def hello():
    print("original function")

hello()





#Docstrings

#Doc strings used to put documentation in an easy way
#It is impilmented using """Phrase""".
#Putting info at phrase space
#We can get documentation using help(class name)



class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """intialize a new dog"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print('Wof!')

#print(help(Dog))

#Output
'''
class Dog(builtins.object)
 |  Dog(name, age)
 |
 |  A class representing a dog
 |
 |  Methods defined here:
 |
 |  __init__(self, name, age)
 |      intialize a new dog
 |
 |  bark(self)
 |      Let the dog bark
 |
 |  ----------------------------------------------------------------------
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)


'''



#Annotation

# a way in python to specify expected data type
#for variable an expected data type can be declare
#using variable_name : variable type = vslue

var :int = 0

#in functioons also we can declare parameter type using :
#and also return type usin -> just after funcion name

def inc(n : int) -> int:
    return n+1

print(inc(4))




#Exception Handling

'''
try:
    # some line of code

except <ERROR1>:
    pass
    #Handle error1

except <ERROR2>:
    pass
    #Handle Error2

except:
    pass
    #haldle other error

else:
    pass
    #No exception were raised, code ran succesfully

finally:
    pass
    #do something in any case
'''


try:
    result= 2/0

except ZeroDivisionError:
    result = 1
    print('Can not divide by zero')


finally:
    print("error handling succesfull")


print(result)


#Raising your own made error 

try:
    raise Exception('An error!')
except Exception as error:
    print(error)


#Making your own Exception by inheriting Exception class

class DogNotFoundException(Exception):
    print("Inside")
    pass

try:
    raise DogNotFoundException()

except DogNotFoundException:
    print("Dog not found ")



#With for file handling
#with opens a file and at the end closes it automatically

filename = 'text.txt'

with open(filename, 'r') as f:
    content = f.read()
    print(content)





#list compressions

number = [n for n in range(1, 10)]
print(number)

number_power_2 = [2**n for n in number]
print(number_power_2)




#Operator overloading

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    """ Overloading greater than(>) """
    def __gt__(self, other):
        return True if self.age > other.age else False

roger = Dog('Roger', 18)
syd = Dog('Syd', 21)

print(roger > syd)

# __gt__() for '>'
# __add__() for '+'
#__sub__() for '-'
#__mul__() for '*'
#__truediv__() for '/'
#__floordiv__() for '//'
#__mod__() for '%'
#__pow__() for '**'
#__rshift__() for '>>'
#__lshift__() for '<<'
#__and__() for '&'
#__or__() for '|'
#__xor__() for '^'