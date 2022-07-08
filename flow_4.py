"""
# iterative statement
# for loop
# patterns: star, numbers, alphabets
========================================
# Que. to print the given star patterns
========================================

*
* *
* * *
* * * *
* * * * *

for i in range (1,6):
    print(i* '* ')
=============================================

 *
 *  * *
 *  * *  * * *
 *  * *  * * *  * * * *

 for i in range (1,6):
    for j in range(i):
        print(j * '* ', end= ' ')
    print( )
============================================

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end= ' ')
    print()
============================================

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

for i in range(5 , 0 ,-1):
    for j in range(1, i + 1):
        print(j, end= ' ')
    print()
===========================================

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

for i in range(5 , 0 ,-1):
    for j in range(i, 0, -1):
        print(j, end= ' ')
    print()
==========================================

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end= ' ')
    print()
=======================================

5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

for i in range(5 , 0 ,-1):
    for j in range(1, i + 1):
        print(i, end= ' ')
    print()
=========================================
# Que. to print given alphabet patterns
=======================================

A
BB
CCC
DDDD
EEEEE

for i in range (1, 6):
    print(chr( i + 64)* i)
=========================================

E
DD
CCC
BBBB
AAAAA

for i in range (1,6):
    print(chr(70-i)* i)
========================================

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
================================================
"""
