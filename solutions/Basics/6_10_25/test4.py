
team={
    "teamName":"Python students",
    "founded":2025,
    "members": ["Karan", "Nitish", "Sachin", "Rahul", "Ajay", "Sneha", "Dhanashree", "Yash"],  #array of strings
    "location":(19.0760, 72.8777)  #tuple (latitude, longitude)
}


print(team)
print(team["members"][2])


participants={
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

print(participants)
print(participants["students"][2]["name"])  #accessing nested object value


indians = {
    "state": [
        {
            "name": "Maharashtra",
            "districts": [
                {
                    "name": "Pune",
                    "city": "Pune",
                    "people": [
                        {"name": "Abhay", "age": 27},
                        {"name": "Anish", "age": 28},
                        {"name": "Ujwal", "age": 22}
                    ]
                },
                {
                    "name": "Raigad",
                    "city": "Mumbai",
                    "people": [
                        {"name": "Neeta", "age": 27},
                        {"name": "Sameer", "age": 28},
                        {"name": "Manish", "age": 22}
                    ]
                }
            ]
        },
        {
            "name": "Punjab",
            "districts": [
                {
                    "name": "Amritsar",
                    "city": "Amritsar",
                    "people": [
                        {"name": "Simran", "age": 25},
                        {"name": "Gurpreet", "age": 30},
                        {"name": "Harpreet", "age": 26}
                    ]
                },
                {
                    "name": "Ludhiana",
                    "city": "Ludhiana",
                    "people": [
                        {"name": "Raj", "age": 29},
                        {"name": "Kiran", "age": 27},
                        {"name": "Deep", "age": 24}
                    ]
                }
            ]
        }
    ]
}



print(indians["state"][0]["name"])