x1 = 1
x2 = 2
x3 = 3

if (x1 >= x2) and (x1 >= x3):
   largest = x1
elif (x2 >= x1) and (x2 >= x3):
   largest = x2
else:
   largest = x3

print("The largest number between",x1,",",x2,"and",x3,"is",largest)
