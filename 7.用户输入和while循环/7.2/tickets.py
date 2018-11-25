tip = "How old are you?"
while True:
    age = input(tip)
    if int(age) < 3:
        print("票价为0$")
    elif int(age) <= 12:
        print("票价为10$")
    else:
        print("票价为15$")