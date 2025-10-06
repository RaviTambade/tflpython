# Python program to read # json file 
# Simple program which will read json data from file and 
  
import json 
  
# Opening JSON file 
f = open('data.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
for i in data['user_details']: 
    print(i) 
  
# Closing file 
f.close() 