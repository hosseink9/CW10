import json

def mydic(dict_):
    apnd=json.dumps(dict_,indent=3)
    return apnd
    

# dic={"name": 'hossein','age': "22"}
# print(mydic(dic))

def creat_json():
    with open("mydictanrray.json","w") as f:
        json.dump({"name": "John", "age": 25, "grade": "A"},f)
    
# creat_json()

def read_json():
    with open("mydictarray.json","r") as f:
        see=json.load(f)
        for i,j in see.items():
            if i=="name":
                print(j)
        print(see)


#read_json()

def enter_studet(name,age,grade):
    student_dict={"name":name,"age":age,"grade":grade}
    return student_dict

name=input("name: ")
age=input("age: ")
grade=input("grade: ")
s1=enter_studet(name,age,grade)

def student():
    global s1
    with open("new_student.json","w") as f:
        json.dump(s1,f)
        
    with open("new_student.json","r") as f:
        see=json.load(f)
        print(list(see))

student()
