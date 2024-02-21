def factorial (n):
   return 1 if (n==1) else n* factorial(n-1)
num=5
print("  factorial of ",num,"is",factorial(num))
