# A
# B B
# C C C                          [DONE]
# D D D D

lst = "ABCD"
length = len(lst)
for r in range(length):
    for c in range(r+1):
        print(lst[r],end=" ")
    print()


# A
# B C
# D E F                           [DONE]
# G H I J
# K L M N O

A = ord("A")
for i in range(1,6):
    for x in range(1,i+1):
        print(chr(A),end=" ")
        A = A + 1
    print()


# * * * * *
# * * * *
# * * *                          [DONE]
# * *
# *

a = '*'
for i in range(6,1,-1):
    for e in range(i-1):
        print(a,end=" ")
    print()


# A B C D
# E F G                             [DONE]
# H I
# J

A = ord("A")
for i in range(5,1,-1):
    for x in range(i-1,0,-1):
        print(chr(A),end=" ")
        A += 1
    print()


# 1 2 3 4
# 1 2 3                          [DONE]
# 1 2
# 1

for i in range(6,1,-1):
    for a in range(1,i-1):
        print(a , end=" ")
    print()
