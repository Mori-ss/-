a = 45
b = 5
def f():
    global a
    a = a * 2
    print(a)
f()
print(a)
print(a+2)