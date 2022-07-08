"""
# iterative statement:
    - it is also known as looping statements or repetitive statements.
    - it is used to execute a part of the program as a given condition is True.
------------------------------------------------------------------------

# for loop:
    - it is used to iterate over a sequence
    (list, tuple, string) or other iterable objects.
-------------------------------------------------------------
syntax:
    for (keyword) var (identifier)
    in (operator)
--------------------------------------------------------------

# Que.1 input as list
nm = ['tanu','manu','anu','renu','sanu']
for n in nm:
    print(n)
=========================================================

# Que.2 input as string
s = 'i love you jaan'
for char in s:
    print(char, end='')
==========================================================

# Que.3 string : needs to print only words
s = 'i love you jaan'
print(s.split())
for word in s.split():
    print(word)
=============================================================

# Que.4 string : needs to print words ending with 'u'
s = 'i love you aju jaan'
print(s.split())
for word in s.split():
    # print(word)
    if word.endswith('u'):
        print(word)
================================================================

 # Que.5 string : needs to print only numbers into another list
s = 'i love you 2055 jaan 9595452055'
print(s.split())
n = []
for word in s.split():
        # print(word)
        if word.isdigit():
             # print word
            n.append(word)
print(n)
=============================================================

# Que.7 input is set
s = {1,2,3,4,6,7,4,3,1}
for i in s:
    print(i)
==============================================================

# Que.8 input is dict
d = {'name': 'shital','age': 27,'place': 'kale'}
for i in d:
    print(i)
==============================================================

d = {'name': 'shital', 'age': 27, 'place': 'kale'}
for i in d:
    # b = i, d.get(i)
    # print(b)
    print(i, d.get(i))
==============================================================

d = {'name': 'shital', 'age': 27, 'place': 'kale'}
for i in d.items():
    print(i)
===========================================================

d = {'name': 'shital', 'age': 27, 'place': 'kale'}
for i in d.values():
    print(i)
==========================================================

# Que.9 input is range
for i in range (9):
        #print(i)
        print('shivansh')
============================================================

for i in range (69,54,-1):
         print(i)
==========================================================

for i in range (5,30):
        print(i)
==============================================================
"""
