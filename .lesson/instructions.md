# Safari Animals: Instructions

Write a program to print out the description of safari animal, based on user input.

## Your Task

In the starter code, there's a list of safari animals, and a list of descriptions. There's also a loop that prints out each of the animal names and numbers. (See 'Starter Code' section below.)

Prompt the user to type in a number. Based on the number they type in, show the name and description of that animal.

## Expected Results

Here's a transcript of a successful run of the program:

```
Enter a number to read a description of an animal.
1. Lion
2. Elephant
3. Leopard
4. Rhino
5. Buffalo
Choose an animal: 1
Lion
The lion (Panthera leo) is a large mammal of the Felidae (cat) family. Some large males weigh over 250 kg (550 lb). Today, wild lions live in sub-Saharan Africa and in Asia. Lions are adapted for life in grasslands and mixed areas with trees and grass. The relatively small females are fast runners over short distances, and coordinate their hunting of herd animals.
```

## Rubric

Run the tests to verify that your program is correct. It should print out the right animal name and description, based on the value that the user typed in.

You should also run your code and see for yourself that the program works. The tests can help check your work, but they aren't perfect.

## Hints

Remember - list indices start at `0`. But, the user will type in the number of the animal, starting with `1`. So, you'll have to convert from the number to the list index.

## Starter Code

Lines 6 and 7 of the starter code list the animals, with numbers next to each animal.

```
for (i, animal) in enumerate(animals):
  print(f"{i+1}. {animal}")
```

`enumerate` is a new function. It takes a list like `animals`, and turns it into a list with the elements and the index of each element. Then, the `for` loop has two loop variables:

- `i` is the index (`0`, `1`, `2`, `3`, `4`)
- `animal` is the string (`"Lion"`, `"Elephant"`, `"Leopard"`, `"Rhino"`, `"Buffalo"`)

So the loop prints out the animals and the numbers. 

```
1. Lion
2. Elephant
3. Leopard
4. Rhino
5. Buffalo
```

`enumerate` is a handy function if you need the index of when you're looping over the elements of a list with `for`.

## Credits

Descriptions from Wikipedia.