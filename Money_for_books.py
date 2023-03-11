# Write your code below. See the Instructions in the tab to the right
no_of_books = int(input("How many books do you want to buy? "))
user_amount = int(input("How much do you have? "))
if user_amount >= 20*no_of_books:
  print("You have enough money, go for it!")

elif user_amount == 20*no_of_books:
  print("How much money do you have? ")
else:
  print(f"You need ${((20*no_of_books) - user_amount)} more to buy that number of books")
  