# IN the name of GOD

counter = 0


def incrementer():
    global counter
    counter += 1
    return counter


def outer():
    var = 0

    def inner():
        nonlocal var
        var += 5
    inner()
    return var


def shadow_demonstrator():
    counter = 10
    return counter


print(outer())
print(shadow_demonstrator())
print(counter)