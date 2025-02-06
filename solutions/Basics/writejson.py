# Python program to write JSON to a file 
   
   
import json 
   
# Data to be written 
dictionary ={ 
    "title" : "Gerbera", 
    "description" : "The best festival flower of world", 
    "unitprice" : 10, 
    "quantity" : 5000
} 
   
with open("flower.json", "w") as outfile: 
    json.dump(dictionary, outfile) 