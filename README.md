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