def calculate(**kwargs):
    print(kwargs)
    for (k, v) in kwargs.items():
        print (k, v)
print(calculate(add=3, multiply=5))