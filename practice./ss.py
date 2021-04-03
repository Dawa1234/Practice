# Identifying an armstrong numbers.

num = int(input("Enter the number here --> "))
sum = 0
numm = num
while num > 0:
    rem = num % 10
    sum = sum + rem ** 3
    num = num // 10
print(numm)
if sum == numm:
    print("The entered number is an armstrong number")
else:
    print("The entered number is not an armstrong number")