# Start by greeting the user
name = str(input("Hello! What's your name? "))
print("Hello", name + "!", "Let's see if it's time to leave this party.")

is_awkward = str(input("Is it awkward? "))
is_food = str(input("Is there free food? "))

if is_awkward == "no":
  print("Stay and par-tay")
  # add code that will print "Stay for the food!" if there is food, and otherwise print "Time to go home"
elif is_awkward.lower() == "yes":
  print("Time to go home")