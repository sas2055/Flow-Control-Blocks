"""
# selective / conditional statement:
       - it is known as decision-making statements.
       - it is used to need execute the specific block of code
       if the given condition is true or false.
-----------------------------------------------------------------------------

 - In Python we can achieve decision-making by using the following statements:
    1. if statements
    2. if-else statements
    3. elif statements
    4. elif ladder
    5. Nested if and if-else statements
-------------------------------------------------------------------

1. if condition:
    - An "if statement" is written by using the if keyword.
    - it is used to test only one condition
-----------------------------------------------------

num = 2
# Que.1 check number is +ve or -ve
if num > 0:
    print('then num is positive')
========================================

num = -2
if num > 0:
    print('then num is negative')
=======================================

2. if else condition:
    - it is used to test two condition
------------------------------------------------------

# Que.2 check number even or odd
num = 20
if num %2 == 0:
    print(num,'is even')
else:
    print(num,'is odd')
=================================================

num = 31
if num % 2 == 0:
    print(num, 'is even')
else:
    print(num, 'is odd')
==================================================

3. if elif else condition:
    - it is used to test three condition
----------------------------------------------

# Que.3 find greatest num among of 3
n1 = 100
n2 = 40
n3 = 260
if (n1>n2) and (n1>n3):
    print('n1 is greater than n2 and n3')
elif n2>n3:
    print('n2 is greater than n1 and n3')
else:
    print('n3 is greater than n1 and n2')
==============================================

4. if elif elif....else condition:
        can test multiple conditions
-----------------------------------------------------------

# Que.4 check the percentage and assign a class of student
per = float(input('enter your percentage:'))
if per >= 75:
    print('you got distinction')
elif per >= 65:
    print('you got first class')
elif per >= 55:
    print('you got second class')
elif per >= 45:
    print('you got pass class')
else:
    print('sorry you are fail')
==================================================================

5. nested if:
    - if statements inside if statements, this is called nested if statements.
---------------------------------------------------------------------

# Que.5
x = 41
if x > 10:
  print('Above ten')
  if x > 20:
    print('and also above 20')
  else:
    print('but not above 20')
====================================================================

# Que.6
mob = 'redmi'
ram = '4gb'
if mob == 'redmi':
    if ram == '8gb':
        print('prize is Rs.:',17000)
    elif ram == '6gb':
        print('prize is Rs.:',13000)
    else:
        print('prize is Rs.:',11000)
else:
    print('sorry we only sell redmi mobiles')
===========================================================================
"""
