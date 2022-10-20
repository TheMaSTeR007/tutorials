def fact(n):
 while n > 0:
  fact = fact*n
  n = n + 1
num = int(input("Enter a number : "))
c=fact(num)
print(c)
