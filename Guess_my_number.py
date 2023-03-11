# See the Instructions tab
import random

# Set secret number
secret_number = random.randint(1,99)
print("I'm thinking of a number between 1 and 99")
while True:
# Ask the user to guess
  user_input = int(input("Entre a guess:"))
# Check to see if the guess is <, >, or = secret number
  if user_input > secret_number:
    print("Your guess is too high")

  elif user_input < secret_number:
    print("Your guess is too low")  

# Print the right message
  else:
    print("Congrats! you found the number")
    break