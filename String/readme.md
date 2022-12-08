1. capitalize()
   capitalize() method returns a string where the first character is upper case.
   ```python
   example:
       my_string = "hello world"
       print(my_string.capitalize())
   ```
   output:
    ```python
    Hello world
    ```

2. casefold()
    casefold() method returns a string where all the characters are lower case.
    ```python
    example:
         my_string = "HELLO WORLD"
         print(my_string.casefold())
    ```
    output:
    ```python
    hello world
    ```


3. center()
    center() method returns a string where the string is padded with a specified character.
    ```python
    example:
         my_string = "hello world"
         print(my_string.center(20, "0"))
    ```
    output:
    ```python
    000hello world0000000
    ```

4. count()
    count() method returns the number of times a specified value occurs in a string.
    ```python
    example:
         my_string = "hello world"
         print(my_string.count("l"))
    ```
    output:
    ```python
    3
    ```

5. find()
    find() method searches the string for a specified value and returns the position of where it was found.
    ```python
    example:
         my_string = "hello world"
         print(my_string.find("o"))
    ```
    output:
    ```python
    4
    ```

6. format()
    format() method formats specified values in a string.
    ```python
    example:
         my_string = "Hello {}"
         print(my_string.format("World"))
    ```
    output:
    ```python
    Hello World
    ```

7. index()
    index() method searches the string for a specified value and returns the position of where it was found.
    ```python
    example:
         my_string = "hello world"
         print(my_string.index("o"))
    ```
    output:
    ```python
    4
    ```

8. isalnum()
    isalnum() method returns True if all characters in the string are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
    ```python
    example:
         my_string = "hello world"
         print(my_string.isalnum())
    ```
    output:
    ```python
    False
    ```

9. isalpha()
    isalpha() method returns True if all characters in the string are in the alphabet.
    ```python
    example:
         my_string = "hello world"
         print(my_string.isalpha())
    ```
    output:
    ```python
    False
    ```
10. isdecimal()
    isdecimal() method returns True if all characters in the string are decimals.
    ```python
    example:
         my_string = "hello world"
         print(my_string.isdecimal())
    ```
    output:
    ```python
    False
    ```

11. isdigit()
    isdigit() method returns True if all characters in the string are digits.
    ```python
    example:
         my_string = "hello world"
         print(my_string.isdigit())
    ```
    output:
    ```python
    False
    ```

12. Title()
    title() method returns a string where the first character in every word is upper case.
    ```python
    example:
         my_string = "hello world"
         print(my_string.title())
    ```
    output:
    ```python
    Hello World
    ```

13. islower()
    islower() method returns True if all characters in the string are lower case.
    ```python
    example:
         my_string = "hello world"
         print(my_string.islower())
    ```
    output:
    ```python
    True
    ```

14. isnumeric()
    isnumeric() method returns True if all characters in the string are numeric.
    ```python
    example:
         my_string = "hello world"
         print(my_string.isnumeric())
    ```
    output:
    ```python
    False
    ```

15. isUpper()
    isUpper() method returns True if all characters in the string are upper case.
    ```python
    example:
         my_string = "hello world"
         print(my_string.isUpper())
    ```
    output:
    ```python
    False
    ```

16. join()
    join() method takes all items in an iterable and joins them into one string.
    ```python
    example:
         my_string = "hello world"
         print(my_string.join("abc"))
    ```
    output:
    ```python
    ahellobhellocworld
    ```

17. ljust()
    ljust() method returns a left justified version of the string.
    ```python
    example:
         my_string = "hello world"
         print(my_string.ljust(20, "0"))
    ```
    output:
    ```python
    hello world000000000000
    ```

18. lower()
    lower() method returns the string in lower case.
    ```python
    example:
         my_string = "HELLO WORLD"
         print(my_string.lower())
    ```
    output:
    ```python
    hello world
    ```
19. lstrip()
    lstrip() method returns a left trim version of the string.
    ```python
    example:
         my_string = "hello world"
         print(my_string.lstrip("h"))
    ```
    output:
    ```python
    ello world
    ```
20. replace()
    replace() method replaces a specified phrase with another specified phrase.
    ```python
    example:
         my_string = "hello world"
         print(my_string.replace("h", "j"))
    ```
    output:
    ```python
    jello world
    ```
21. rfind()
    rfind() method searches the string for a specified value and returns the last position of where it was found.
    ```python
    example:
         my_string = "hello world"
         print(my_string.rfind("o"))
    ```
    output:
    ```python
    7
    ```
22. rindex()
    rindex() method searches the string for a specified value and returns the last position of where it was found.
    ```python
    example:
         my_string = "hello world"
         print(my_string.rindex("o"))
    ```
    output:
    ```python
    7
    ```
23. rjust()
    rjust() method returns a right justified version of the string.
    ```python
    example:
         my_string = "hello world"
         print(my_string.rjust(20, "0"))
    ```
    output:
    ```python
    000000000000hello world
    ```
24. rstrip()
    rstrip() method returns a right trim version of the string.
    ```python
    example:
         my_string = "hello world"
         print(my_string.rstrip("d"))
    ```
    output:
    ```python
    hello worl
    ```
25. split()
    split() method splits the string at the specified separator, and returns a list.
    ```python
    example:
         my_string = "hello world"
         print(my_string.split(" "))
    ```
    output:
    ```python
    ['hello', 'world']
    ```
26. splitlines()
    splitlines() method splits the string at line breaks and returns a list.
    ```python
    example:
         my_string = "hello world"
         print(my_string.splitlines())
    ```
    output:
    ```python
    ['hello world']
    ```
27. startswith()
    startswith() method returns True if the string starts with the specified value.
    ```python
    example:
         my_string = "hello world"
         print(my_string.startswith("h"))
    ```
    output:
    ```python
    True
    ```
28. strip()
    strip() method returns a trimmed version of the string.
    ```python
    example:
         my_string = "hello world"
         print(my_string.strip("h"))
    ```
    output:
    ```python
    ello worl
    ```
29. swapcase()
    swapcase() method returns a string where all the upper case letters are lower case and vice versa.
    ```python
    example:
         my_string = "hello world"
         print(my_string.swapcase())
    ```
    output:
    ```python
    HELLO WORLD
    ```
30. upper()
    upper() method returns the string in upper case.
    ```python
    example:
         my_string = "hello world"
         print(my_string.upper())
    ```
    output:
    ```python
    HELLO WORLD
    ```
31. zfill()
    zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
    ```python
    example:
         my_string = "hello world"
         print(my_string.zfill(20))
    ```
    output:
    ```python
    000000000000hello world
    ```

32. format()
    format() method formats the specified value(s) and insert them inside the string's placeholder.
    ```python
    example:
         my_string = "hello world"
         print(my_string.format("h"))
    ```
    output:
    ```python
    hello world
    ```
33. format_map()
    format_map() method formats the specified value(s) and insert them inside the string's placeholder.
    ```python
    example:
         my_string = "hello world"
         print(my_string.format_map("h"))
    ```
    output:
    ```python
    hello world
    ```
34. maketrans()
    maketrans() method returns a translation table to be used in translations.
    ```python
    example:
         my_string = "hello world"
         print(my_string.maketrans("h"))

    ```
    output:
    ```python
    {104: None}
    ```
35. translate()
    translate() method returns a translated string.
    ```python
    example:
         my_string = "hello world"
         print(my_string.translate({104: 102}))
    ```
    output:
    ```python
    fello world
    ```

