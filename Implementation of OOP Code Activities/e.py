fruit_stock = ["apple", "banana", "cherry"]
i = 0
for fruit in fruit_stock:
    print(i, fruit)
    i += 1

# optimised

fruit_stock = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruit_stock):
    print(index, fruit)