"""
# docstrings:
    - it means documentation strings.
    - it is used to give an explanation about a code snippet.
    - it is used for multiple comment.
    - the content inside the docstring will not be a part of code it
    will be treated as a plain text.
    - it provides a convenient way of associating documentation
    with Python modules, functions, classes, and methods.
----------------------------------------------------------------------

# Declaring Docstrings:
    - The docstrings are declared using ”’triple single quotes”’
    or “”” triple double quotes ”””
    - it is used class, method or function declaration.
    - All functions should have a docstring.
--------------------------------------------------------------------

# Accessing Docstrings:
    - The docstrings can be accessed using the __doc__ method
    of the object or using the help function.
-------------------------------------------------------------------

# Que.1 Using triple single quotes


def my_func():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
    return None


print('Using __doc__: ')
print(my_func.__doc__)
print('\nUsing help: ')
help(my_func)
=======================================================

# Que.2 Using triple double quotes


def my_func():
    “”” Demonstrates triple double quotes
     docstrings and does nothing really.”””
    return None


print('Using __doc__: ')
print(my_func.__doc__)
print('\nUsing help: ')
help(my_func)
=======================================================

# Que.3 One-line Docstrings


def power(a, b):
     “”” Returns arg1 raised to power arg2.”””
    return a ** b


print(power.__doc__)
print(power(2, 7))
================================================================

# Que.4 Multy-line Docstrings


def my_func(arg1):
    “””
    Summary line.
    Extended description of function.

    Parameters:
    arg1 (int): Description of arg1

    Returns:
    int: Description of return value.
    ”””
    return arg1


print(my_func.__doc__)
=======================================================

# Que. Difference between comments and docstrings in Python
comments:
    - Single line comments using a #
    - it cannot be associated with any object.
    - it can only be access to the source code file.
    - it is used to increase the understandability of the code
------------------------------------------------------------

docstrings:
    - multiline comments using multiline strings
    - it is associated object using  __doc__ attribute
    - it is used to associate the documentation with the objects
=====================================================================
"""
