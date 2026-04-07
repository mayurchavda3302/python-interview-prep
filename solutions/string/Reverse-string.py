"""

question: Reverse string 

**Input:** `"Hello"`
**Output:** `"olleH"`
"""



str1="Hello"


# Method 1: using slicing
def reverse_string(str1):
    """ reverse string using slicing """
    #  syntax: string[start:stop:step]
    # here we are using step as -1 to reverse the string
    return str1[::-1]


# method 2: using  loop 
def reverse_string_fun(funstr):
   "use loop to reverse string"
   # here we are using loop to reverse the string by concatenating each character in reverse order
   str=""

   for s in funstr:
       str=s+str
   return str


# method 3: using built-in function reversed() 
def reverse_string_builtin(str1):
    """ reverse string using built-in function reversed() """


    """ 
    here we have used 
    join() consumes the iterator and builds a string becouse the reversed() function returns an iterator that 
    yields the characters of the string in reverse order, and join() concatenates those characters into a single string.
    """

    return ''.join(reversed(str1))

# Method 4: using recursion
def reverse_recursion(s):
    if len(s) <= 1: 
        return s

    # Logic:
    """
    Example: s = "Hello"

    Step 1:
    reverse("Hello")
    = "o" + reverse("Hell")

    Step 2:
    reverse("Hell")
    = "l" + reverse("Hel")

    Step 3:
    reverse("Hel")
    = "l" + reverse("He")

    Step 4:
    reverse("He")
    = "e" + reverse("H")

    Step 5 (Base Case):
    reverse("H")
    = "H"

    Now building the result while returning:

    reverse("He")   = "e" + "H"     = "eH"
    reverse("Hel")  = "l" + "eH"    = "leH"
    reverse("Hell") = "l" + "leH"   = "lleH"
    reverse("Hello")= "o" + "lleH"  = "olleH"

    Final Output: "olleH"
    """

    return s[-1] + reverse_recursion(s[:-1])


print(reverse_string_fun(str1))

print(reverse_string_builtin(str1))

print(reverse_recursion(str1))