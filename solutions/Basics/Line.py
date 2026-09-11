#Class Relation ship:
## containment
# Point has x and y
# Line has  STartPoint and EndPoint
#  has a relationship


class Point:
    def  __init__(self,x, y):
        self.X=x
        self.Y=y
    def show(self):
        print(f"X={self.X}, Y={self.Y}")


class Line:
    def __init__(self,pt1,pt2,color):
        self.startPoint=pt1
        self.endPoint=pt2
        self.color=color
    
    def draw(self):
        print(f"Start Point:( {self.startPoint.X}, {self.startPoint.Y} )")
        print(f"End Point:( {self.endPoint.X}, {self.endPoint.Y} )")
        print(f"Color: {self.color}")
    

stpt=Point(23,54)
endpt=Point(77,78)

l1=Line(stpt, endpt, "red")
l1.draw()



anotherStartPoint=Point(199,233)
anotherEndPoint=Point(67,34)

l2=Line(anotherStartPoint,anotherEndPoint,"blue")

l2.draw()

