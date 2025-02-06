# install geopy module using pip install
# pip install geopy

from geopy.distance import geodesic

# A simple class calculator to find the distance between two points on earth
# Ravi Tambade

class Calculator: 
  
    # init method or constructor  
    def __init__(self, name): 
        self.name = name 
  
    # Sample Method  
    def distance(self): 
        origin = (30.172705, 31.526725)  # (latitude, longitude) don't confuse
        dist = (30.288281, 31.732326)
        print(geodesic(origin, dist).meters)  # 23576.805481751613
        print(geodesic(origin, dist).kilometers)  # 23.576805481751613
        print(geodesic(origin, dist).miles)  # 14.64994773134371
  
calc = Calculator('GeoDistance') 
calc.distance()