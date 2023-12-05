n = int(input("input: "))
def fibo(n):
   if n <= 2:
      return n - 1
   else:
      return fibo(n - 1) + fibo(n - 2)
print(fibo(n))
