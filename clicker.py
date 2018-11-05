from tkinter import *

root = Tk()

canv = Canvas(bg='white')
mouseX = 0
mouseY = 0
ok = False

def click(event,needX1,needX2,needY1,needY2):
    global mouseX, mouseY, ok
    mouseX = event.x
    mouseY = event.y
    if mouseX >= needX1 and mouseX <= needX2 and mouseY >= needY1 and mouseY <= needY2:
        ok = True

canv.bind('<1>', click)
