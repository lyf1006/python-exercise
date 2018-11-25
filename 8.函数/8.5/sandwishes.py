def ingrident(*toppings):
    print("Making a pizza with the following ingridents: ")
    for topping in toppings:
        print(topping)
    
ingrident('onion', 'bacon', 'lettuce')
ingrident('onion')
ingrident('lettuce', 'bacon')