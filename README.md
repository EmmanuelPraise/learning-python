## Learning Python

### What is Python?
Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

*It is used for:*
- web development (server-side),
- software development,
- mathematics,
- system scripting.

*What can Python do?*
- Python can be used on a server to create web applications.
- Python can be used alongside software to create workflows.
- Python can connect to database systems. It can also read and modify files.
- Python can be used to handle big data and perform complex mathematics.
- Python can be used for rapid prototyping, or for production-ready software development.

---

### Variables
Variables are containers for storing data values.
Creating Variables:
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
```python
x = 5
y = "John"
print(x)
print(y)
```
*RULES:*
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.

---

### Python Comments
Comments can be used to explain Python code.
Comments can be used to make the code more readable.
Comments can be used to prevent execution when testing code.
Creating a Comment:
Comments starts with a #, and Python will ignore them:
```python
#This is a comment
print("Hello, World!")
```

---

### Data Types
- Text Type:	str
- Numeric Types:	int, float, complex
- Sequence Types:	list, tuple, range
- Mapping Type:	dict
- Set Types:	set, frozenset
- Boolean Type:	bool
- Binary Types:	bytes, bytearray, memoryview
- None Type:	NoneType

| Example                                      | Data Type  |
|----------------------------------------------|------------|
| x = "Hello World"                            | str        |
| x = 20                                       | int        |
| x = 20.5                                     | float      |
| x = 1j                                       | complex    |
| x = ["apple", "banana", "cherry"]            | list       |
| x = ("apple", "banana", "cherry")            | tuple      |
| x = range(6)                                 | range      |
| x = {"name" : "John", "age" : 36}            | dict       |
| x = {"apple", "banana", "cherry"}            | set        |
| x = frozenset({"apple", "banana", "cherry"}) | frozenset  |
| x = True                                     | bool       |
| x = b"Hello"                                 | bytes      |
| x = bytearray(5)                             | bytearray  |
| x = memoryview(bytes(5))                     | memoryview |
| x = None                                     | NoneType   |

to print the type of any variable, use the type() function:
```python
x = "Hello World" #str
print(type(x))
```

---

### Python Numbers
There are three numeric types in Python:
- Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
- Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
- Complex numbers are written with a "j" as the imaginary part.
```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))
```

*Random Number*
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
```python
import random
print(random.randrange(1, 10))
```
---

### Python Casting
Casting in python is done using constructor functions:
- int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
- float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
- str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

```python
# Integers
x = int(2.8) # x will be 2
print(x)

# Floats
y = float(1) # y will be 1.0
print(y)

# Strings
z = str(3.0)  # z will be '3.0'
print(z)
```
---

### Python Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.
```python
a = "Hello, World!"
print(a)
```

*Multiline Strings*
You can assign a multiline string to a variable by using three quotes:
```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

*Slicing Strings:*
You can return a range of characters by using the slice syntax.
```python
b = "Hello, World!"
print(b[2:5]) # llo
```

*String Concatenation*
To concatenate, or combine, two strings you can use the + operator.
```python
a = "Hello"
b = "World"
c = a + b
print(c) # HelloWorld
```

*String Format*
To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
```python
name = "John"
age = 36
txt = f"My name is {name}, and I am {age}"
print(txt) # My name is John, and I am 36
```

A placeholder can contain variables, operations, functions, and modifiers to format the value.
A placeholder can include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
```python
price = 49
txt = f"The price is {price:.2f} dollars"
print(txt) # The price is 49.00 dollars
```

*Sring Methods*
Python has a set of built-in methods that you can use on strings.

| Method         | Description                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------|
| capitalize()   | Converts the first character to upper case                                                    |
| casefold()     | Converts string into lower case                                                               |
| center()       | Returns a centered string                                                                     |
| count()        | Returns the number of times a specified value occurs in a string                              |
| encode()       | Returns an encoded version of the string                                                      |
| endswith()     | Returns true if the string ends with the specified value                                      |
| expandtabs()   | Sets the tab size of the string                                                               |
| find()         | Searches the string for a specified value and returns the position of where it was found      |
| format()       | Formats specified values in a string                                                          |
| format_map()   | Formats specified values in a string                                                          |
| index()        | Searches the string for a specified value and returns the position of where it was found      |
| isalnum()      | Returns True if all characters in the string are alphanumeric                                 |
| isalpha()      | Returns True if all characters in the string are in the alphabet                              |
| isascii()      | Returns True if all characters in the string are ascii characters                             |
| isdecimal()    | Returns True if all characters in the string are decimals                                     |
| isdigit()      | Returns True if all characters in the string are digits                                       |
| isidentifier() | Returns True if the string is an identifier                                                   |
| islower()      | Returns True if all characters in the string are lower case                                   |
| isnumeric()    | Returns True if all characters in the string are numeric                                      |
| isprintable()  | Returns True if all characters in the string are printable                                    |
| isspace()      | Returns True if all characters in the string are whitespaces                                  |
| istitle()      | Returns True if the string follows the rules of a title                                       |
| isupper()      | Returns True if all characters in the string are upper case                                   |
| join()         | Joins the elements of an iterable to the end of the string                                    |
| ljust()        | Returns a left justified version of the string                                                |
| lower()        | Converts a string into lower case                                                             |
| lstrip()       | Returns a left trim version of the string                                                     |
| maketrans()    | Returns a translation table to be used in translations                                        |
| partition()    | Returns a tuple where the string is parted into three parts                                   |
| replace()      | Returns a string where a specified value is replaced with a specified value                   |
| rfind()        | Searches the string for a specified value and returns the last position of where it was found |
| rindex()       | Searches the string for a specified value and returns the last position of where it was found |
| rjust()        | Returns a right justified version of the string                                               |
| rpartition()   | Returns a tuple where the string is parted into three parts                                   |
| rsplit()       | Splits the string at the specified separator, and returns a list                              |
| rstrip()       | Returns a right trim version of the string                                                    |
| split()        | Splits the string at the specified separator, and returns a list                              |
| splitlines()   | Splits the string at line breaks and returns a list                                           |
| startswith()   | Returns true if the string starts with the specified value                                    |
| strip()        | Returns a trimmed version of the string                                                       |
| swapcase()     | Swaps cases, lower case becomes upper case and vice versa                                     |
| title()        | Converts the first character of each word to upper case                                       |
| translate()    | Returns a translated string                                                                   |
| upper()        | Converts a string into upper case                                                             |
| zfill()        | Fills the string with a specified number of 0 values at the beginning                         |

---

### Python Booleans
Booleans represent one of two values: True or False.
```python
print(10 > 9) # True
print(10 == 9) # False
print(10 < 9) # False
```

Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
```python
# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))
```

---

### Python Operators
Operators are used to perform operations on variables and values.
Python divides the operators in the following groups:
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

*Arithmetic Operators* are used with numeric values to perform common mathematical operations:

| Operator | Name           | Example | Try it |
|----------|----------------|---------|--------|
| +        | Addition       | x + y   |        |
| -        | Subtraction    | x - y   |        |
| *        | Multiplication | x * y   |        |
| /        | Division       | x / y   |        |
| %        | Modulus        | x % y   |        |
| **       | Exponentiation | x ** y  |        |
| //       | Floor division | x // y  |        |

*Assignment Operators* are used to assign values to variables:

| Operator | Example       | Same As    | Try it   |
|----------|---------------|------------|----------|
| =        | x = 5         | x = 5      |          |
| +=       | x += 3        | x = x + 3  |          |
| -=       | x -= 3        | x = x - 3  |          |
| *=       | x *= 3        | x = x * 3  |          |
| /=       | x /= 3        | x = x / 3  |          |
| %=       | x %= 3        | x = x % 3  |          |
| //=      | x //= 3       | x = x // 3 |          |
| **=      | x **= 3       | x = x ** 3 |          |
| &=       | x &= 3        | x = x & 3  |          |
|          | =             | x          | = 3      | x = x | 3   |              |
| ^=       | x ^= 3        | x = x ^ 3  |          |
| >>=      | x >>= 3       | x = x >> 3 |          |
| <<=      | x <<= 3       | x = x << 3 |          |
| :=       | print(x := 3) | x = 3      | print(x) |

*Comparison Operators* are used to compare two values:

| Operator | Name                      | Example | Try it |
|----------|---------------------------|---------|--------|
| ==       | Equal                     | x == y  |        |
| !=       | Not equal                 | x != y  |        |
| >        | Greater than              | x > y   |        |
| <        | Less than                 | x < y   |        |
| >=       | Greater than or equal to  | x >= y  |        |
| <=       | Less than or equal to     | x <= y  |        |

*Logical Operators* are used to combine conditional statements:

| Operator | Description                                             | Example               |
|----------|---------------------------------------------------------|-----------------------|
| and      | Returns True if both statements are true                | x < 5 and  x < 10     |
| or       | Returns True if one of the statements is true           | x < 5 or x < 4        |
| not      | Reverse the result, returns False if the result is true | not(x < 5 and x < 10) |

*Identity Operators* are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

| Operator | Description                                            | Example    |
|----------|--------------------------------------------------------|------------|
| is       | Returns True if both variables are the same object     | x is y     |
| is not   | Returns True if both variables are not the same object | x is not y |

*Membership Operators* are used to test if a sequence is presented in an object:

| Operator | Description                                                                      | Example    |
|----------|----------------------------------------------------------------------------------|------------|
| in       | Returns True if a sequence with the specified value is present in the object     | x in y     |
| not in   | Returns True if a sequence with the specified value is not present in the object | x not in y |

*Bitwise Operators* are used to compare (binary) numbers:

| Operator | Name                 | Description                                                                                             |
|----------|----------------------|---------------------------------------------------------------------------------------------------------|
| &        | AND                  | Sets each bit to 1 if both bits are 1                                                                   |
| \|       | OR                   | Sets each bit to 1 if one of two bits is 1                                                              |
| ^        | XOR                  | Sets each bit to 1 if only one of two bits is 1                                                         |
| ~        | NOT                  | Inverts all the bits                                                                                    |
| <<       | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost                                      |
| >>       | Signed right shift   | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off |

*Operator Precedence*
The following table lists all operators from highest precedence to lowest.

| Operator                 | Description                                                                    |
|--------------------------|--------------------------------------------------------------------------------|
| **                       | Exponentiation (raise to the power)                                            |
| ~ + -                    | Complement, unary plus and minus (method names for the last two are +@ and -@) |
| * / % //                 | Multiply, divide, modulo and floor division                                    |
| + -                      | Addition and subtraction                                                       |
| >> <<                    | Right and left bitwise shift                                                   |
| &                        | Bitwise 'AND'                                                                  |
| ^ \|                     | Bitwise exclusive `OR' and regular `OR'                                        |
| <= < > >=                | Comparison operators                                                           |
| <> == !=                 | Equality operators                                                             |
| = %= /= //= -= += *= **= | Assignment operators                                                           |
| is is not                | Identity operators                                                             |
| in not in                | Membership operators                                                           |
| not or and               | Logical operators                                                              |

---

### Python Collections
There are four collection data types in the Python programming language:
- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered and unindexed. No duplicate members.
- Dictionary is a collection which is unordered, changeable and indexed. No duplicate members. 

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
A collection is a group of objects (data). A collection is used to store, retrieve, manipulate, and communicate aggregate data.
Most collections are mutable. This means that the elements of a collection can be changed after the collection is created.

### Python Lists
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
```python
this_list = ["apple", "banana", "cherry"]
print(this_list)
```

*List Items* are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
```python
this_list = ["apple", "banana", "cherry"]
print(this_list[1]) # banana
```

*Change Item Value*
To change the value of a specific item, refer to the index number:
```python
this_list = ["apple", "banana", "cherry"]
this_list[1] = "blackcurrant"
print(this_list) # ['apple', 'blackcurrant', 'cherry']
```

*Loop Through a List*
You can loop through the list items by using a for loop:
```python
this_list = ["apple", "banana", "cherry"]
for x in this_list:
  print(x)
```

*Check if Item Exists*
To determine if a specified item is present in a list use the in keyword:
```python
this_list = ["apple", "banana", "cherry"]
if "apple" in this_list:
  print("Yes, 'apple' is in the fruits list")
```

*List Length*
To determine how many items a list has, use the len() method:
```python
this_list = ["apple", "banana", "cherry"]
print(len(this_list)) # 3
```

*Add Items*
To add an item to the end of the list, use the append() method:
```python
this_list = ["apple", "banana", "cherry"]
this_list.append("orange")
print(this_list) # ['apple', 'banana', 'cherry', 'orange']
```

*Insert Items*
To insert a list item at a specified index, use the insert() method:
```python
this_list = ["apple", "banana", "cherry"]
this_list.insert(1, "orange")
print(this_list) # ['apple', 'orange', 'banana', 'cherry']
```

*Remove Item*
There are several methods to remove items from a list:
- The remove() method removes the specified item.
- The pop() method removes the specified index, (or the last item if index is not specified).
- The del keyword removes the specified index.
- The clear() method empties the list.
```python
this_list = ["apple", "banana", "cherry"]
this_list.remove("banana")
print(this_list) # ['apple', 'cherry']
```

*Copy a List*
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
There are ways to make a copy, one way is to use the built-in List method copy().
```python
this_list = ["apple", "banana", "cherry"]
my_list = this_list.copy()
print(my_list) # ['apple', 'banana', 'cherry']
```

*Join Two Lists*
There are several ways to join, or concatenate, two or more lists in Python.
One of the easiest ways are by using the + operator.
```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) # ['a', 'b', 'c', 1, 2, 3]
```

*List Methods*
Python has a set of built-in methods that you can use on lists.

| Method    | Description                                                                  |
|-----------|------------------------------------------------------------------------------|
| append()  | Adds an element at the end of the list                                       |
| clear()   | Removes all the elements from the list                                       |
| copy()    | Returns a copy of the list                                                   |
| count()   | Returns the number of elements with the specified value                      |
| extend()  | Add the elements of a list (or any iterable), to the end of the current list |
| index()   | Returns the index of the first element with the specified value              |
| insert()  | Adds an element at the specified position                                    |
| pop()     | Removes the element at the specified position                                |
| remove()  | Removes the first item with the specified value                              |
| reverse() | Reverses the order of the list elements                                      |
| sort()    | Sorts the list                                                               |

---
