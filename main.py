# Write your AC Load Estimator solution here
width = float(input("input width of the room: "))
height = float(input("input height of the room: "))
number_of_people = float(input("number of people in the room: "))

horsepower = width * height * 0.1 + number_of_people * 0.06

print(horsepower)