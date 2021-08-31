name = input("What is your name? ")
arv1 = int(input(f"Hello, {name}! Enter a random number: "))
arv2 = int(input("Great! Now enter a second random number: "))
arv3 = arv1 + arv2
print(f" {arv1} + {arv2} is {arv3}")

print("Help us to finish the poem!")
a = input("Colour of roses? ")
b = input("Plural noun? ")
c = input("Verb? ")
print(f"Roses are {a},\n"
      f"{b} are blue,\n"
      f"I love to {c}\n"
      f"And so will you!")

a = input("Enter a greeting: ")
b = input("Enter a recipient: ")
c = int(input("How many times to repeat:  "))
print((a + " " + " " + b + "!" + " ")*c)
