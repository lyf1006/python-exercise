#Complete making sandwishes
sandwish_orders = ['tuna', 'chicken', 'rain_forest', 'pineapple', 'watermelon']
finished_sandwishes = []

#按照序号遍历，在remove之后出现少遍历的异常
for sandwish in sandwish_orders:
    print("I made your " + sandwish + " sandwish.")
    finished_sandwishes.append(sandwish)
    sandwish_orders.remove(sandwish) 

# while sandwish_orders:
#     sandwish = sandwish_orders.pop()
#     print("I made your " + sandwish + " sandwish.")
#     finished_sandwishes.append(sandwish)

print("\nFinished sandwishes are: ")
for sandwish in finished_sandwishes:
    print(sandwish)

