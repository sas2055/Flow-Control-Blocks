"""
# Que.1 reverse the word from string
s = 'Shital Shelar'
expected = 'Shelar Shital'
for i in (s.split()[::-1]):
    print(i, end=' ')
===================================================

# Que.2 reverse the character/blocks from string
s = 'Shital Shelar'
expected = 'ralehs latihs'
# print(s[::-1])
print(reversed(s))
# print(tuple(reversed(s)))
final = ''
for i in reversed(s):
    final += i # it will concatenate one block at a time
print(final)
============================================

# Que.3 print every character from string
s = 'Shital Shelar'
print(s[4])
# -1 to -n
for i in range(-1, -(len(s)+1), -1):
    print (i, end=' ')

0r
s = 'Shital Shelar'
for i in range(-1, -(len(s)+1), -1):
    print(s[i], end='')
==============================================

# Que.4 reverse the character 0f individual word
s = 'Shital Shelar'
expected = 'latihS ralehS '
for i in s.split():
    print(i[::-1], end=' ')
=============================================

# Que.5 i want to fetch vowels from the string: a, i, e, o, u
s = 'Shital Shelar'
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in s:
    if i in vowels:
     print(i, end=' ')
==================================================

# Que.6 i want a dict of each block and its count
# {'S':2, 'h':2, 'i':1, 't':1, 'a':2 .............}
s = 'Shital Shelar'
d = {}
for i in s:
    # print(i, s.count(i))
    # d[key] = value
    d[i] = s.count(i)
print(d)
=================================================

# Que.7 interchange 1st and last two characters from string
s = 'Shital Shelar'
expected = 'lartal SheShi'
for i in s:
    if (len(s) > 2):
        pass
print(s[-3:13] + s[3:-3] + s[:3], end=' ')
=============================================

# Que.8 my key = 3
# means i want to shift character by 3
s = 'Shital Shelar'
for i in s:
    shifting_char = chr(ord(i) + 3)
    print(shifting_char, end=' ')

or
s = 'Shital Shelar'
for i in s:
    a = ord(i) + 3
    b = chr(a)
    print(b, end=' ')

or
s = 'Shital Shelar'
for i in s:
    if(i.isalpha()):
        print(chr(ord(i) + 3), end= ' ')
    else:
        print(' ', end='')
====================================
# Que.9 print the positive and negative index of each block/ character
s = 'Shital Shelar'
j = len(s)
for i, k in zip(s, range(j)):
    if i == ' ':
        print("' '", end ='')
    print(i, 'positive and negative index is:', (k ,-j))
    j -= 1
============================================    
"""
