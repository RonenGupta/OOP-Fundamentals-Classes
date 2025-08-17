x = 5
y = 7

def add():
    global x, y
    return x + y

print(add())

# optimised
def add(x, y):
    return x + y

print(add(5, 7))