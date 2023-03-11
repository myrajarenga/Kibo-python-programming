# Original instructions: Print the sum of the odd numbers between 10 and 25
# Add print statements to debug the code
total = 0
print("total before is", total)
for i in range(11,26,2):
  print("i is", i, "total is", total)
  total += i
print("total after is", total)
print(total)
# What is wrong with the code? (answer in a comment)
# supposed to be odd numbers
# range start at 11 not 1o and end at 26 not 25
# total + i shoul be total += i