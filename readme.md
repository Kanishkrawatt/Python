## Python

### Basic Introduction to Python

#### Origin

Python is a programming language that was created by Guido van Rossum in 1991. It was named after the British comedy group Monty Python. Python is a high-level programming language that is easy to read and write. It is also a general-purpose programming language that can be used for many different types of applications.

#### Features

Python is an interpreted language. This means that the code is not compiled into machine language before it is executed. Instead, the code is executed by an interpreter. The interpreter reads the code and executes it. Python is also an object-oriented programming language. This means that the code is organized into objects. These objects can contain data and code. Python is also a dynamically typed language. This means that the type of a variable is determined at runtime.

#### Program Structure

Python programs are organized into modules. A module is a file that contains Python code. Modules can be imported into other modules.

```python
import module_name  # This imports the module
```

Modules can also be executed directly.

```python
code:
    def function_name():
        print("Hello World")
    if __name__ == "__main__": # This is the main module
        function_name()
output:
    Hello World
```

Python programs are also organized into statements. A statement is a unit of code that the Python interpreter can execute. Statements are terminated by a newline character.

```python
print("Hello World")   # This is a statement
```

Python programs are also organized into blocks. A block is a section of code that is grouped together. Blocks are delimited by indentation.

```python
if True:        # This a block
    print("Hello World")
```

#### Identifiers

Python uses identifiers to name variables, functions, classes, modules, and other objects . An identifier must start with a letter or underscore. It can contain letters, numbers, and underscores. It is case sensitive. Python does not allow punctuation characters such as `@` , `$` , and `%` within identifiers.

```python
_hi = 10        # This is valid
_ = 20          # This is valid
my_var = 10     # This is valid
2my_var = 10    # This is invalid
@my_var = 10    # This is invalid
```

#### Reserved Words

Python has a set of reserved words that cannot be used as identifiers. These words are used to define the syntax and structure of the Python language.

```python
False       class       is          return
None        continue    for         try
True        def         from        while
and         del         global      not
with        as          elif        if
or          else        import      pass
break       except      in          raise
```

#### Escape Sequences

Python uses escape sequences to represent certain whitespace characters. These characters cannot be typed directly into a string. The escape sequences are:

```python
\'      Single quote
\"      Double quote
\\      Backslash
\n      Newline
\t      Tab
\r      Carriage return
\b      Backspace
```

#### Variables and assignment statements

Variables are used to store data values. A variable is created the first time it is assigned a value.

The equal sign `=` is used to assign a value to a variable. The value is stored in the variable.

```python
my_var = 10     # This assigns the value 10 to the variable my_var
```

#### Data Types

Python has five standard data types:

- Numbers
  Numbers are used to store numeric values. Python supports four different numerical types:
  1. int (signed integers)
  2. long (long integers, they can also be represented in octal and hexadecimal)
  3. float (floating point real values)
  4. complex (complex numbers)
  ```python
  example:
    signed_int = 10     # This is a signed integer
    long_int = 10L      # This is a long integer
    my_float = 10.0     # This is a float
    my_complex = 10j    # This is a complex number
  ```
- String
  Strings are used to store textual data. Strings can be enclosed in single quotes or double quotes.
  ```python
  example:
      my_string = "Hello World"   # This is a string
      single_quotes = 'Hello World'   # This is also a string
  ```
- List
  Lists are used to store a sequence of values. Lists are enclosed in square brackets. `[ ]`.
  ```python
  example:
      my_list = [1, 2, 3]     # This is a list
  ```
- Tuple
  Tuples are used to store a sequence of values. Tuple are enclosed in parentheses.`( )`.
  ```python
  example:
      my_tuple = (1, 2, 3)    # This is a tuple
  ```
- Dictionary
  Dictionaries are used to store data values in key:value pairs. Dictionaries are enclosed in curly braces. `{ }`.
  ```python
  example:
      my_dict = {"key1": 1, "key2": 2, "key3": 3}    # This is a dictionary
  ```

#### Operators

Python supports the following types of operators:

- Arithmetic operators
  Arithmetic operators are used with numeric values to perform common mathematical operations.

  ```python
  example:
      addition = 10 + 5      # This is addition
      subtraction = 10 - 5   # This is subtraction
      multiplication = 10 * 5    # This is multiplication
      division = 10 / 5      # This is division
      modulus = 10 % 5       # This is modulus
      exponent = 10 ** 5     # This is exponentiation
      floor_division = 10 // 5   # This is floor division
  ```

- Assignment operators
  Assignment operators are used to assign values to variables.

  ```python
  example:
      x = 10      # This is an assignment operator
      x += 5      # This is an augmented assignment operator
      x -= 5      # This is an augmented assignment operator
      x *= 5      # This is an augmented assignment operator
      x /= 5      # This is an augmented assignment operator
      x %= 5      # This is an augmented assignment operator
      x **= 5     # This is an augmented assignment operator
      x //= 5     # This is an augmented assignment operator

  ```

- Comparison operators
  Comparison operators are used to compare two values.

  ```python
  example:
      x = 10
      y = 5
      x == y      # This is an equality operator
      x != y      # This is an inequality operator
      x > y       # This is a greater than operator
      x < y       # This is a less than operator
      x >= y      # This is a greater than or equal to operator
      x <= y      # This is a less than or equal to operator
  ```

- Logical operators
  Logical operators are used to combine conditional statements.

  ```python
  example:
      x = 10
      y = 5
      x > 5 and y > 5     # This is an and operator
      x > 5 or y > 5      # This is an or operator
      not(x > 5 and y > 5)    # This is a not operator
  ```

- Identity operators/ Membership operators
  Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

  ```python
  example:
      x = 10
      y = 5
      x is y      # This is an is operator
      x is not y  # This is an is not operator
  ```

- Bitwise operators
  Bitwise operators are used to compare (binary) numbers.

  ```python
  example:
      x = 10
      y = 5
      x & y       # This is a bitwise and operator
      x | y       # This is a bitwise or operator
      x ^ y       # This is a bitwise xor operator
      ~x          # This is a bitwise not operator
      x << 2      # This is a bitwise left shift operator
      x >> 2      # This is a bitwise right shift operator
  ```

#### Control Structures

Control structures are used to change the flow of execution of a program.

Python supports the following control structures:

1. Conditional statements
2. Looping statements
3. Jump statements

##### Conditional Statements

Conditional statements are used to perform different actions based on different conditions.

Python supports the following conditional statements:

1. If statement
   If statement is used to execute a block of code if a condition is true.
   ```python
   syntax:
       if condition:
           # code block
   ```
   ```python
   example:
       x = 10
       if x > 5:
           print("x is greater than 5")
   ```
2. If...else statement
   If...else statement is used to execute a block of code if a condition is true. If the condition is false, another block of code can be executed.

   ```python
   syntax:
       if condition:
           # code block
       else:
           # code block
   ```

   ```python
   example:
       x = 10
       if x > 5:
           print("x is greater than 5")
       else:
           print("x is less than or equal to 5")
   ```

3. If...elif...else statement
   If...elif...else statement is used to execute a different block of code for more than two conditions.
   ```python
   syntax:
       if condition:
           # code block
       elif condition:
           # code block
       else:
           # code block
   ```
   ```python
   example:
       x = 10
       if x > 5:
           print("x is greater than 5")
       elif x < 5:
           print("x is less than 5")
       else:
           print("x is equal to 5")
   ```
