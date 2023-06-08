import json

def func1(my_dict):
    y = json.dumps(my_dict,indent=4, separators=(",",":"))
    return y

x = { "name":"John", "age":30, "city":"New York"}
print(func1(x))
print()

def func2():
    with open("data.json", "r") as f:
        x= json.load(f)
        for i, j in x.items():
            if i == "name":
                print(j)


func2()
print()

def func3(**kwargs):
    with open("new_student.json","w") as f:
        json.dump(json.dumps(kwargs),f)

    with open("new_student.json","r") as f:
        print(json.load(f))


name=input("Enter Your name: ")
age=int(input("Enter Your age: "))
grade=input("Enter Your grade: ")
func3(name=name,age=age,grade=grade)






