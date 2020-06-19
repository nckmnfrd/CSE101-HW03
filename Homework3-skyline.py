#Nicholas Manfredi
#110207186
#CSE 101
#Lab Section 8
#Homework3 Skyline

from turtle import *
import random
ryan = Turtle()
ryan.speed(1000)
screen = ryan.getscreen()


def drawBuilding(x,y,width,height,color,hasAntenna):
    ryan.penup()
    ryan.goto(x,y)
    ryan.pendown()
    ryan.color("black",color)
    ryan.begin_fill()
    ryan.goto(x+width,y)
    ryan.goto(x+width,y+height)
    ryan.goto(x,y+height)
    ryan.goto(x,y)
    ryan.end_fill()
    ryan.penup()

    winCols = int((width-10)/20)
    winRows = int((height-10)/20)
    for i in range(0,winRows):
        for j in range(0,winCols):
                winColor = ["yellow","black"][int(random.randrange(0,2))]
                winX = x+10+20*j
                winY = y+10+20*i
                ryan.goto(winX,winY)
                ryan.pendown()
                ryan.color("black",winColor)
                ryan.begin_fill()
                ryan.goto(winX+10,winY)
                ryan.goto(winX+10,winY+10)
                ryan.goto(winX,winY+10)
                ryan.goto(winX,winY)
                ryan.end_fill()
                ryan.penup()

    if hasAntenna:
        antennaX= x+width/2-1
        antennaY= y+height
        ryan.goto(antennaX,antennaY)
        ryan.pendown()
        #Draw first part
        ryan.color("black","black")
        ryan.begin_fill()
        ryan.goto(antennaX+3,antennaY)
        ryan.goto(antennaX+3,antennaY+20)
        ryan.goto(antennaX,antennaY+20)
        ryan.goto(antennaX,antennaY)
        ryan.end_fill()
        #Draw second part
        ryan.goto(antennaX+1,antennaY+20)
        ryan.goto(antennaX+1,antennaY+30)
        ryan.penup()

def drawSkyLine(x,y):
    for i in range(0,6):
        hasAntenna = [True,False,False,False][int(random.randrange(0,4))]
        buildingColor = (random.random(),random.random(),random.random())
        width = random.randrange(30,131)
        height = random.randrange(50,251)
        drawBuilding(x,y,width,height,buildingColor,hasAntenna)
        x+=width

drawSkyLine(-100,100)
done()
