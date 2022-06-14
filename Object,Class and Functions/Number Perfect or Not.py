def perfect_numbers(word):
   sum = 0
   for i in range(1, word):
      if word%i == 0:
         sum = sum+i
   return sum


n = int(input("Enter Number: "))

# check perfect number or not
if n == perfect_numbers(n):
   print(n, "is a perfect number")
else:
   print(n, "is not a perfect number")