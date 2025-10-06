
# Object  and Variables
# Notation: In Python, dictionaries are used to represent objects.
# Key-Value pairs
# JSON (Universal data representation)
# Javascript Object Notation

person={
    "name":"John",
    "age":30,
    "city":"New York",
    "isEmployed":True,
    "assets":["car","bike","house"] , #array
    "birthdate":(1975,8,18)  #tuple
}
print(person)

team={
    "teamName":"Sambhanji Bridge",
    "founded":2025,
    "members": ["Karan", "Nitish", "Sachin", "Rahul", "Ajay"],  #array of strings
    "location":(19.0760, 72.8777)  #tuple (latitude, longitude)
}
print(team)
print(team["members"][2])


tapStudents={
    "course":"Python Programming",
    "duration":"3 months",
    "instructor":"Ravi Tambade",
    "isOnline":True,
    "students":[{"name":"Abhay", "age":27},        #array of objects
                {"name":"Anish", "age":28},
                {"name":"Ujwal", "age":22}
        
    ], 
    "schedule":(2024, 7, 1)  #tuple
}

print(tapStudents)
print(tapStudents["students"][2]["name"])  #accessing nested object value


