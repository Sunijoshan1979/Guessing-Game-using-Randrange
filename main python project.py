import random

flowers = ["rose","jasmine","lilly","lotus"]
print("List=",flowers)

selection = str(input("Enter your selection:"))

comp_guess = random.randrange(0,3)
guess = flowers[ comp_guess]
if selection==guess:
   print("You Won")

else:
    print("You failed")
print("computer selection=",guess)
print("your selection=",selection)
