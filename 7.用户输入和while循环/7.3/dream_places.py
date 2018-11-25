#I want to travel around the world! Romance, History, Stories...
q1 = "What's your name?"
q2 = "If you could visit one place in the world, where would you go?"
dream_places = {}
willing = True
while willing:
    name = input(q1)
    place = input(q2)
    dream_places[name] = place
    ans = input("Would you like to ask for another person?(yes/no)")
    if ans == 'no':
        willing = False

print("\nPeople's dream places are:")
for name,place in dream_places.items():
    print(name + ": " + place)
