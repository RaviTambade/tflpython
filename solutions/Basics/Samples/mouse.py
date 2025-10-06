import numpy as np
import cv2

a = []
def click_event(event, x, y, flags, param):
    
    #  mouse move event should show mouse position co-ordinates
    #  at one fixed position

    if event == cv2.EVENT_MOUSEMOVE:
        print(x,', ' ,y)
        font = cv2.FONT_HERSHEY_PLAIN
        
        strXY = str(x) + ', '+ str(y)
        cv2.putText(img, strXY, (100, 100), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img) 
        a.append([x,y])
    elif event ==cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        cv2.putText(img, strXY, (10, 10), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img) 
        a.append([x,y])
    elif event ==cv2.EVENT_RBUTTONDOWN:
        print(x,', ' ,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img) 
        a.append([x,y])



img = cv2.imread('mission.png')
cv2.imshow('image', img)
print("*Press q to terminate*")
while True:
    cv2.setMouseCallback('image', click_event)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#def convert(a): 
#    return tuple(a)
print(a) 
while True:
    pts = np.array([a], np.int32)
    cv2.polylines(img,pts,True,(0,255,255),3)
    #cv2.line(img, a[0], a[1], (0, 255, 0),3)
    #cv2.line(img, a[1], a[2], (0, 255, 0),3)
    #cv2.line(img, a[2], a[3], (0, 255, 0),3)
    #cv2.line(img, a[3], a[0], (0, 255, 0),3)
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()