#五香烟熏牛肉卖完啦，请选择其他的吃吧！！！
sandwish_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'rain_forest', 'pastrami', 'chicken']
print("Sorry,our pastrami had been sold out.")

for sandwish in sandwish_orders:
    if sandwish == 'pastrami':
        sandwish_orders.remove('pastrami')

print("\nModified list :")
for sandwish in sandwish_orders:
    print(sandwish)
