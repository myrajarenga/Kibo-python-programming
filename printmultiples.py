# See Instructions tab

# Print numbers 1 to 100
# For multiples of 3, print "X is a multiple of 3"
# For multiples of 5, print "X is a multiple of 5"
number = int(input("Enter a number: "))

for i in range(number,1,-1):
  if (i % 3 == 0) and (i % 5 == 0):
    print(i, "is a multiple of 3 and 5")
  elif (i % 3 == 0):  
    print(i, "is a multiple of 3")
  elif (i % 5 == 0):  
    print(i, "is a multiple of 5")
  else:
    print(i)