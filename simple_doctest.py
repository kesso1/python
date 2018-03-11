"""
Welcome to your first exercise! Many exercises will start with a
multiline string, like this. The multiline strings are delineated
by triple quotes and represent such called docstrings.

Embedded in this multiline string will be what looks like copy-pastes
from interactive Python prompts:

>>> hello('world')
'Hello, world!'

That is actually an automated test. Your job is to write code to make
it pass. In other words, you must define a function named 'hello' that
takes one argument, and returns the greeting. You do that below,
where it says "Write your code here".

Here's another test, which gives an important distinction:
>>> print_hello('world')
Hello, world!

Notice the output has no quotes around it? That means the function
printed, rather than returning a string.

Task: implement the two functions. If you implemented them correctly,
running this script does not produce any output. Otherwise, errors
are shown.

Tips:
 * ONLY write code in the area below. Don't modify this multiline
   string!
 * When you run the script and see multiple failures, focus on fixing
  the first failure. Often later failures will then go away.
"""


def greeter(greetString):
    print("Hello " + greetString)

def print_hello(world):
    print("Hello, world!")

def hello(world):
    print("'Hello, world!'")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #greeter("Otti")
