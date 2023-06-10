# In the name of GOD
import json


def dict_to_json(the_dict: dict) -> json:
    result = json.dumps(the_dict, indent=4,)
    return result


dictionary ={
                "name": "sathiyajith",
                "rollno": 56,
                "cgpa": 8.6,
                "phonenumber": "9976770500"
            }
dictionary_txt = dict_to_json(dictionary)
print("dictionary_txt", dictionary_txt)


with open("json_files//my_jason.json", "w") as outfile:
    json.dump(dictionary_txt, outfile)


def jason_loader(jason_file_path):
    with open(jason_file_path, "r") as the_file:
        result = json.load(the_file)
    return result


text_dictionary = jason_loader("json_files//my_jason.json")
print("text_dictionary", text_dictionary)


def new_student():
    name = input("Enter the name of student: ")
    age = input("Enter the Age of student: ")
    grade = input("Enter the grade of student: ")
    result = {"name": name, "age": int(age), "grade": int(grade)}
    return result


new_student1 = new_student()
new_student1_json = dict_to_json(new_student1)

with open("json_files//new_student.json", "w") as outfile:
    json.dump(new_student1_json, outfile)

loaded_student = jason_loader("json_files//new_student.json")
print(loaded_student)