# TIL

A repo for adding my Today I learned stuffs related to programming, technology, mistakes I have done and solutions to them.

-----
-----

# November 14 2017

Today I started to learn git and its commands.Also I started to maintain a TIL repo in my github account.

-----
-----

# November 15 2017

Started learning python from Bucky's tutorials. The Webcrawler example didn't work because the website he mentioned was out of order so I used the website photooverlay.com/photo_new/front.html .

-----
-----

# November 16 2017

Completed assignment to predict the price of the house with a given area using Linear Regression.

Based on formula y = a + bx we found a = -10091.12991 and b = 70.2263182428852

-----

#### Some useful python functions

```
str.splitlines("String_name") - to split the string based on new line character 
```
----
```
global a- to make the variable global
```
----

##### Exception

```

try:

except ValueError:   #If string data is passed instead of integer

except ZeroDivisionError:   #If division by zero

except:   #Default catch expression

finally:   #gets executed no matter what
```

-----
```
pass - does not do anything
```
-----
```
string_name.lower()   #changes the string to lower case
```
-----
```
for _ in range(10):   #loop 10 times
```
-----

##### Classes

```

class Class_name():   or    class Class_name:   #creating a class

def function_name(self):    #defining a function in class

object_name = class_name(Attributes)    #Instantiating a class

def __init__(self):   #constructor

```

-----

##### Threading

```

import threading    #import statement

Class_name(threading.thread)    #threading class inherited to our new class

object_name = Class_name(name = "thread_name")    #setting the name of the thread

threading.currentThread().getName()   #getting the name of the thread

object_name.start()   #run the thread

def run(self):    #overrinding the run function of thread class

```

-----

##### Inheritance
```
Class Child_class(Parent_class)   #Creating a child class inheriting the parent class

Class Child_class(Parent1, Parent2)   #Multiple Inheritance
```
-----
```
list_name.append(value)
```
-----
```
word = word.replace(symbols[i],"")    #Replacing the characters of the word with "" if it matches with one of the characters in the list symbols.
```
-----

## December 4, 2017

```
How to create a .jar using IntelliJ IDEA 14.1.5:

    File > Save All.
    Run driver or class with main method.
    File > Project Structure.
    Select Tab "Artifacts".
    Click green plus button near top of window.
    Select JAR from Add drop down menu. Select "From modules with dependencies"
    Select main class.
    The radio button should be selecting "extract to the target JAR." Press OK.
    Check the box "Build on make"
    Press apply and OK.
    From the main menu, select the build dropdown.
    Select the option build artifacts.
```
-----








