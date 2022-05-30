#Exercise 1

from unicodedata import name


student = {
    "name": "steve",
    "age": "22",
    "major": "underwater_basket-weaving",
    "year": 7,
    "classes": {"snorkeling", "weaving_101", "basketry_210"}
}

print("Exercise 1")
print(student)

#Exercise 2

print("Exercise 2")
print(student.get("name"))

#Exercise 3
student.pop("year")

print("Exercise 3")
print(student)
#Exercise 4
student["gpa"] = 3.9

print("Exercise 4")
print(student)
#Exercise 5
student["gpa"] = 4.0

print("Exercise 5")
print(student)
#Exercise 6

collegeStudents = {
    "name": {"bob", "jill", "jack"},
    "age": {"19", "22", 42},
    "major": {"quidditch", "potionmaking", "herbology"},
    "year": {3, 4, 2},
    "classes": [["art", "defense", "brooms"],["gardening", "cooking", "astrology"],["gardening", "timeturning", "groundskeeping"]]
}

print("Exercise 6")
print(collegeStudents)

#Exercise 7
collegeStudents = sorted(collegeStudents.items())

print("Exercise 7")
print(collegeStudents)
