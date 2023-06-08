counter=0

def glo():
    global counter
    counter+=1
    return counter

print(glo())

def outer():
    var=0
    def inner():
        nonlocal var
        var+=1
    inner()
    return var
print(outer())

globl=0
def shadow():
    globl=5
    return globl

print(shadow())
    