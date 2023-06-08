counter = 0

def inc():

    global counter
    counter+=1
    return counter

print(inc())

def outer():
    var=0
    def inner():
        nonlocal var
        var+=1
    inner()
    return var

print(outer())


glob=0
def func():
    glob=4
    print(glob)

func()
