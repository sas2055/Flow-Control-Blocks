"""
# Transfer statement / loop control statement:
    - it is change execution from its normal sequence.
    - When execution leaves a scope, all automatic objects
    that were created in that scope are destroyed.
---------------------------------------------------------------

1. break:
       - it is used to current execution flow and exit the loop.
       - it is only works inside the block
       - break is the hold and stop of the condition of block
---------------------------------------------------------------

for i in range(6):
    # print(i)
    if i == 4:
        break
    else:
        print(i)
==========================================

2. continue:
    - we can use 1 and more than conditions
    - if skips the value at given condition but continues loop
-------------------------------------------------------------

temp = [12,23,45,12,65,78,95,32,15]
for i in temp:
    if i == 45:
        continue
    else:
        print('current temp is:',i)
--------------------------------------------------------

# flipkart cart scenario using continue
cart = [299, 499, 399, 599, 1999, 2999, 450, 99, 158, 5999, 9450]
for i in cart:
    if i < 500:
        continue
        print('product price is Rs: ', i, 'delivery charges applied')
    else:
        print('product price is Rs: ', i, 'free delivery applicable')
==============================================================

Que. difference between break and continue
for i in range(5):
    if i == 3:
        break
    else:
        print(i)
print('----------------------------------')
for i in range(5):
    if i == 3:
        continue
    else:
        print(i)
==============================================

3. pass:
    - it is used to create empty block.
    - it is used to inside the block.
    - it is a keyword in python.
----------------------------------------------------

if True:
    pass
for i in range(5):
    pass
=====================================================
"""