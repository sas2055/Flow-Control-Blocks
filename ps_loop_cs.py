"""
# using for loop and while loop
# Que.1 print all natural numbers from 1 to n
num = int(input('enter any natural number: '))
print('\nNatural numbers from 1 to ', num)
for i in range(1, num + 1):
    print(i, end= ' ')

 or
num = int(input('enter maximum natural number: '))
i = 1
while (i<= num):
    print(i)
    i = i+ 1
==================================================

# Que.2 print all natural numbers reverse from n to 1
num = int(input('enter any natural number: '))
print('\nNatural numbers from 1 to', num)
for i in range(num, 0, - 1 ):
    print(i, end= ' ')

or
num = int(input('enter any natural number: '))
i = num
while (i >= 1):
    print(i, end = '')
    i = i- 1
===================================================

# Que.3 print all alphabets from a to z
# Printing a - z
print('alphabets from a - z are : ')
# a = 97 and z = 122
for alpha in range(97, 123):
    print(chr(alpha), end=' ')

or
# Printing A - Z
print('alphabets from A - Z are : ')
# A = 65 and Z = 90
for alpha in range(65, 90):
    print(chr(alpha), end=' ')

or
print('alphabets from a - z are: ')
for ch in string.ascii_lowercase:
    print(ch, end= ' ')
print('\nAlphabets from A - Z are: ')
for ch in string.ascii_uppercase:
    print(ch, end=' ')
===================================================

# Que.4 print all even numbers between 1 to 100
print('\nEven numbers from 1 to 100 are : ')
for i in range(1, 101):
    #Check for even or not.
    if((i % 2) == 0):
        print(i, end=' ')

or
num = 2
while num<= 100:
    print(num)
    num = num + 2

or
i = 1
while (i <= 100):
    if((i % 2)== 0):
        print(i, end = ' ')
    i = i + 1
==============================================

# Que.5 print all odd numbers between 1 to 100
print('\nOdd numbers from 1 to 100 are: ')
for i in range(1, 100):
    #Check for odd or not.
    if((i % 2) != 0):
        print(i, end=' ')

or
i = 1
while (i <= 100):
    if((i % 2)!=0):
        print(i, end = ' ')
    i = i + 1
===========================================

# Que.6 find sum of all natural numbers between 1 to n
num = int(input('Enter any natural number 1 to : '))
sum = 0
for i in range(1, num + 1):
    sum += i
print('\nSum of all natural numbers: ', sum)

or
num = int(input('enter any natural numbers 1 to: '))
sum = 0
i = 1
while i <= num:
    print(i,end = ' ')
    sum += i
    i += 1
print()
print('Sum of all natural numbers: ', sum)
===================================================

# Que.7 find sum of all even numbers between 1 to n
num = int(input('enter sum of even numbers 1 to: '))
total = 0
for i in range(1, num + 1):
     # Check for even or not.
    if((i % 2) == 0):
        total = total + i
print('\nSum of even numbers from 1 to', num,'is: ', total)
===================================================

# Que.8 find sum of all odd numbers between 1 to n
num = int(input('enter sum of odd numbers 1 to: '))
sum = 0
for i in range(1, num + 1):
    #Check for odd or not.
    if(not (i % 2) == 0):
        sum = i + sum
print('\nSum of odd numbers from 1 to', num, 'is:', sum)
====================================================

# Que.9 check whether number is perfect or not
num = int(input('enter any number: '))
sum = 0
# Calculate sum of all proper divisors
for i in range(1, num):
    if num % i == 0:
        sum += i
# Empty print statement for new line
print()
# Check whether the sum of divisors is equal to num
if sum == num:
    print(num, 'is PERFECT number')
else:
    print(num, 'is not PERFECT number')
=======================================================

# Que.10 print multiplication table of any number take user input
num = int(input('enter number to print table: '))
print('\nTable of:', num)
# Printing table of given number
for i in range(1, 11):
    print(num, '*', i, '=', (num * i))
========================================================

# Que.11 count number of digits in a number
num = str(input('enter the number: '))
count = 0
for digit in num:
    count = count +1
print('total number of digit present is: ',count)

or
num = int(input('enter any number: '))
# Store to temporary variable.
temp = num
count = 0
while (temp != 0):
    # Increment counter
    count += 1
    # Remove last digit of 'temp'
    temp = int(temp / 10);
print('\nTotal digits in', num, ':', count)
=======================================================

# Que.12 find first and last digit of a number
num = input('enter the number: ')
while num.isnumeric():
    l = len(num)
    print('first digit of given number is:', num[0])
    print('last digit of given number is:', num[l-1])
    break
=======================================================

# Que.13 find sum first and last digit of a number
num = input('enter the number: ')
while num.isnumeric():
    l = len(num)
    sum = int(num[0]) + int(num[l-1])
    print('sum of first and last digit is: ',sum)
    break
========================================================

# Que.14 swap first and last digit of a number
num = input('enter the number: ')
while num.isnumeric():
    l = len(num)
    print('the number', num, 'after swapping first and last digit is: ', num[l-1] +num[1:l-1] +num[0])
    break
=======================================================

# Que.15 calculate sum of digits of a number
num = input('enter any number: ')
total = 0
for i in range(0, len(num)):
    total = total + int(num[i])
print(total)

or
num = int(input('enter any number: '))
temp = num
total = 0
while(temp != 0):
    total = total + (temp % 10);
    # Remove last digit from temp.
    temp = int(temp / 10)
print('\nSum of all digits in', num, ':', total)
======================================================

# Que.16 calculate product of digit of number
num = int(input('enter any number: '))
product = 1
while(num != 0):
    product = product * (num % 10)
    # Remove last digit from num
    num = int(num / 10)
print('\nProduct of all digits in', num, ':', product)
======================================================

#Que.17 to enter the number and print its reverse
num = int(input('enter any number: '))
temp = num
reverse = 0
while(temp != 0):
    reverse = (reverse * 10) + (temp % 10)
    temp = int(temp / 10)
print('\nReverse of', num, ':', reverse)
=======================================================

# Que.18 check whether a number is palindrome or not
num=input('enter any number:')
i=0
for i in range(len(num)):
    if num[i]!=num[-1-i]:
        print('It is not a palindrome')
        break
    else:
        print('It is a palindrome')
        break
======================================================

# Que.19 find frequency of each digit in a given integer
num = int(input('enter any number: '))
print('digit\tFrequency')
for i in range(0,10):
    count = 0
    n = num
    while n > 0:
        digit = n %10
        if digit == i:
            count = count +1
        n = n //10
    if count > 0:
        print(i, '       ', count)
======================================================
# Que.21 find power of number
base = int(input('enter base: '))
exponent = int(input('enter exponent: '))
power = 1
for i in range(1, exponent + 1):
    power = power * base
print('\nResult', base, '^', exponent, ':', power)
print('Using math class:', math.pow(base, exponent))
=======================================================

# Que.22 calculate factorial of a number
num = int(input('enter any number: '))
print('\nAll factors of', num, 'are: ')
for i in range(1, num + 1):
    # Completely divisible or not.
    if(num % i == 0):
        print(i, end = ' ')
=======================================================
# Que.23 find HCF of two numbers
num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
# Find minimum between two numbers
min = num1
if num2 < num1:
    min = num2
for i in range(1, min + 1):
    if((num1 % i) == 0 and (num2 % i) == 0):
            hcf = i
print('\nHCF of', num1, 'and', num2, ':', hcf)

or
num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
i = 1
while (i <= num1 and i <= num2):
        if((num1 % i) == 0 and (num2 % i) == 0):
            gcd = i
        i = i +1
print('\nHCF', num1, 'and', num2, ':', gcd)
========================================================

# Que.24 find LCM of two numbers
num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
# l = to store the lcm
# g = to store the gcd
# Find maximum between two numbers
for i in range(1, num1 + 1):
    if i <= num2:
        if((num1 % i) == 0 and (num2 % i) == 0):
            g = i
l = (num1 * num2)/ g
print('\nLCM of', num1, 'and', num2, ':', l)

or
num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
# Find the max number
max_num = num2
if (num1 > num2):
    max_num = num1
i = max_num
lcm = 1
while(True):
    if((i % num1) == 0 and (i % num2) == 0):
        lcm = i
        break
    i += max_num
print('\nLCM of', num1, 'and', num2, ':', lcm)
========================================================

# Que.25 check whether a number is prime number or not
num = int(input('enter any number: '))
i = 1
# Check for prime
for i in range(2, num):
    if (int(num % i) == 0):
        i = num
        break
if i is num:
    print('\n' + str(num), 'is not a prime number')
else:
    print('\n' + str(num), 'is a prime number')
=======================================================

# Que.26 print all prime number between 1 to n
num = int(input('find prime numbers 1 to: '))
print('\nAll prime numbers 1 to', num, 'are: ')
for i in range(2, i + 1):
    j = 2
    for j in range(2, num):
        if(i % j == 0):
            j = i
            break
    # If the number is prime then print it.
    if(j != i):
        print(i, end=' ')
=======================================================

# Que.27 find sum of all prime numbers between 1 to n
num = int(input('Find sum of prime numbers 1 to: '))
sum = 0
for i in range(2, num + 1):
    j = 2
    for j in range(2, i):
        if (int(i % j) == 0):
            j = i
            break
    # If the number is prime then add it.
    if j is not i:
        sum += i
print('\nSum of all prime numbers 1 to', num, ':', sum)
======================================================

# Que.28 check whether a number is armstrong number or not
num = int(input('enter number to check: '))
original_num = num
# Find total digits in given number
digits = int(math.log10(num) + 1)
sum = 0
while (num > 0):
    last_digit = int(num % 10)
    sum = sum + round(math.pow(last_digit, digits))
    # Remove the last digit
    num = num / 10
    # Empty print statement for new line
print()
if original_num == sum:
    print(original_num, 'is ARMSTRONG NUMBER')
else:
    print(original_num, 'is not ARMSTRONG NUMBER')
========================================================

# Que.29 print all armstrong number between 1 to n
num = int(input('enter the armstrong number 1 to: '))
for i in range(1, num + 1):
    n = i
    result = 0
    s = len(str(i))
    while(i != 0):
        digit = i % 10
        result = result + digit**s
        i = i//10
    if n == result:
        print(n, end= ' ')
========================================================

# Que.30 print fibonacci series up to n terms
num = int(input('enter number of series: '))
n1 = 0
n2 = 1
print(n1,end= ' ')
print(n2,end= ' ')
for i in range(num-2):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end= ' ')
==================================================i=====

# Que.31 to print the given number pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

n = int(input('enter the number of rows:'))
# outer loop to handle number of rows
for i in range(n + 1):
    # nested loop
        for j in range(i):
            # display numbers
            print(i,end='')
            # new line after each row
        print('')
===========================================

# Que.32 to print the given star pattern
*
**
***
****
*****

n = int(input('enter the number of rows:'))
# outer loop to handle number of rows
for i in range(0,n):
    # inner loop to handle number of columns
    # values is changing according to outer loop
        for j in range(0,i + 1):
            # printing stars
            print('*',end='')
            # ending line after each row
        print()
"""

