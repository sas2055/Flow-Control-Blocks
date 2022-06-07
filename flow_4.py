"""
# conditional statement
# for loop
# patterns: star, numbers, alphabets
========================================
# Que. to print the given star patterns
========================================
*
**
***
****
*****

for i in range (1,6):
    print(i* '*')

or
for i in range (0,5):
    for j in range(0, i+ 1):
        print('*', end= '')
    print()
========================================
*****
****
***
**
*

for i in range (6,0,-1):
    print(i* '*')
======================================
    *
   **
  ***
 ****
*****

for i in range (1,6):
    for k in range(1, 6-i):
        print(' ', end= '')
    for j in range(1, i+ 1):
       print('*', end= '')
    print()
========================================
*****
 ****
  ***
   **
    *

for i in range (5,0,-1):
    for k in range(1, 6-i):
        print(' ', end= '')
    for j in range(1, i+ 1):
       print('*', end= '')
    print()
=====================================
    *
   ***
  *****
 *******
*********

for i in range (1,6):
    for k in range(1, 6-i):
        print(' ', end= '')
    for j in range(1,(2* i- 1)+ 1):
       print('*', end= '')
    print()
=====================================
*********
 *******
  *****
   ***
    *

for i in range (5,0,-1):
    for k in range(1, 6 - i):
        print(' ', end='')
    for j in range(1,(2* i- 1)+ 1):
       print('*', end= '')
    print()
======================================
# Que. to print given number patterns
=======================================
1
12
123
1234
12345

for i in range (1,6):
    for j in range(1, i+ 1):
       print(j, end= '')
    print()
=======================================
12345
1234
123
12
1

for i in range(5,0,-1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
========================================
12345
 1234
  123
   12
    1

for i in range (5,0,-1):
    for k in range(1, 6-i):
        print(' ', end= '')
    for j in range(1, i+ 1):
       print(j, end= '')
    print()
========================================
    1
   12
  123
 1234
12345

for i in range (1,6):
    for k in range(1, 6-i):
        print(' ', end= '')
    for j in range(1, i+ 1):
       print(j, end= '')
    print()
========================================
    1
   123
  12345
 1234567
123456789

for i in range (1,6):
    for k in range(1, 6 - i):
        print(' ', end='')
    for j in range(1,(2* i- 1)+ 1):
       print(j, end= '')
    print()
========================================
123456789
 1234567
  12345
   123
    1

for i in range (5,0,-1):
    for k in range(1, 6 - i):
        print(' ', end='')
    for j in range(1,(2* i- 1)+ 1):
       print(j, end= '')
    print()
========================================
1
22
333
4444
55555

for i in range (1,6):
    for j in range(1, i+ 1):
       print(i, end= '')
    print()
========================================
55555
4444
333
22
1

for i in range (5,0,-1):
    for j in range(1, i+ 1):
       print(i, end= '')
    print()
=========================================
    1
   22
  333
 4444
55555

for i in range (1,6):
    for k in range(1, 6-i):
        print(' ', end= '')
    for j in range(1, i+ 1):
       print(i, end= '')
    print()
=======================================
55555
 4444
  333
   22
    1

for i in range (5,0,-1):
    for k in range(1, 6-i):
        print(' ', end= '')
    for j in range(1, i+ 1):
       print(i, end= '')
    print()
=======================================
    1
   222
  33333
 4444444
555555555

for i in range (1,6):
    for k in range(1, 6 - i):
        print(' ', end='')
    for j in range(1,(2* i- 1)+ 1):
       print(i, end= '')
    print()
========================================
555555555
 4444444
  33333
   222
    1

for i in range (5,0,-1):
    for k in range(1, 6 - i):
        print(' ', end='')
    for j in range(1,(2* i- 1)+ 1):
       print(i, end= '')
    print()
========================================

# Que. to print given alphabet patterns
=======================================
A
BB
CCC
DDDD
EEEEE

for i in range (1,6):
    print(chr(i + 64)* i)
========================================
EEEEE
DDDD
CCC
BB
A

for i in range (5,0,-1):
    print(chr(i + 64)* i)
=================================
AAAAA
BBBB
CCC
DD
E

for i in range (5,0,-1):
    print(chr(70-i)* i)

or
for i in range (1,6):
    print(chr(i+ 64)*(6-i))
===================================
E
DD
CCC
BBBB
AAAAA

for i in range (1,6):
    print(chr(70-i)* i)

or
for i in range (5,0,-1):
    print(chr(i+ 64)*(6-i))
==================================
"""