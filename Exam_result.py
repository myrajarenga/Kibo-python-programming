# Ask for the exam score
score = float(input('Enter score: '))
# Check to see if the score is > 70
if score > 70:
  # Print "You passed!" if so
  print("You passed!")
elif 50 < score > 70:
  print("Passed on probation")
else:
  # Print "Try again" otherwise
  print("Try again")