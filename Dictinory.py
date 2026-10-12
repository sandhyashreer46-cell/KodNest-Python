student = {
    'name':"Amith",
    "name":"Rahul",
    "age": 21,
    "Course": "computer science",
    "Tech":["computer science","python","SQL"]
}
student["age"]=25
student.update({"cgpa":8.5})
print(student["age"])
print(student,type(student),len(student))
print(student.keys())
print(student.values())
print(student.items()) 
print(student.get("cgpa"))
print(student.popitem())
print(student.clear())
del student
student = {
    "name":"Rahul",
    "age":21,
    "Tech":["python","SQL"]
}
student.setdefault("age",22)
print(student)

keys = ["name","age","course"]
y = 0

student = dict.fromkeys(keys,y)
print(student)
my_dict = student.copy()
print(my_dict)
my_dict.update({"name":"Amith"})
print(my_dict)