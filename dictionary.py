# info = {
#     "name" : "Shees",
#     "subjects" : ["Python", ".Net", "JavaScript"],
#     "learning" : "coding",
#     "age" : 19,
#     "is_adult" : True,
#     "marks" : 98.3
# }

# info["name"] = "Abc"

# print(info)

#nested Dictionary

student = {
    "name" : "Shees",
    "subjects": {
        "Physics" : 77,
        "Maths" : 88,
        "Chemistry": 67
    }
}

#print(student["name1"]) #return error if key not exist
#print(student.get("name1")) #return none if key not exist

student.update({"city" : "Karachi"})
print(student)
