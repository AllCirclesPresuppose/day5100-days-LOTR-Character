print("Which Lord of the Rings Character are you?")
print()
print()
print("Answer the questions below with a y or n and lets find out!")
yesNo = input("Do you like shiny rings?")
if yesNo == "y":
  yesNo = input("would you call the ring my precious?")
  if yesNo == "y":
    yesNo = input("is your hair thin and scraggly, and your skin pale gray?")
    if yesNo == "y":
      print("*Gollum* *Gollum* Yes, my precious, you are Smeagol")
    else:
      yesNo = input("are you old, having already gone on your adventure?")
      if yesNo == "y":
        print("It is time, old Bilbo, to pass the ring along to the next adventurer")
      else:
        print("Frodo, my dear boy, we have an adventure to go on!")
  else:
    print("It would seem as though you are the Dark Lord, Sauron!")
else:
  yesNo = input("would you consider yourself of the race of men?")
  if yesNo == "y":
    yesNo = input("Are you from the house of Gondor, the King who will return?")
    if yesNo == "y":
      print("Always valiantly helping, you are Aragorn!")
    else:
      print("It is good to see you, Boromir, may you not be tempted by the ring!")
  else:
    yesNo = input("would you consider yourself tall, and elvish in nature?")
    if yesNo == "y":
      print("Legolas! Hail and well met!")
    else:
      yesNo = input("Are you short and stout, with a glorious beard?")
      if yesNo == "y":
        print("Ah, Gimli, come have an ale!")
      else:
        print("I do not recall you, perhaps try again...")