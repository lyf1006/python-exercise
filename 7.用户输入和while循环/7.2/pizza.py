tip = "Please enter an ingrident you want to add: "
tip += "\n(Enter 'quit' when you are finished)"
while True:
    ingrident = input(tip)
    if ingrident == "quit":
        break
    else:
        print("We will add this ingrident for you.")
