import turtle
import random

# 김민재 2021041070
myTurtle, tX, tY, tColor, tSize, tShape, tAngle = [None] * 7
playerTurtles = []
swidth, sheight = 500, 500



if __name__ == "__main__" :
    turtle.title('거북이 리스트 활용(정렬)')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)


    for i in range(0, 5) :
        myTurtle = turtle.Turtle('turtle')
        tX = random.randrange(-swidth / 2, swidth / 2)
        tY = random.randrange(-sheight / 2, sheight / 2)
        r = random.random(); g = random.random(); b = random.random()
        tSize = random.randrange(1, 100)/10
        tAngle = random.randrange(0,360)
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b,tAngle])


    soredTurtles = sorted(playerTurtles, key=lambda turtles : turtles[3] ,reverse = False)
    for index, tList in enumerate(soredTurtles[0:]) : 
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.seth(tList[7])
        myTurtle.penup()
        if index == 0 : 
            myTurtle.goto(tList[1], tList[2])
            continue
        myTurtle.goto(soredTurtles[index-1][1], soredTurtles[index-1][2])
        myTurtle.pendown()
        myTurtle.goto(tList[1], tList[2]) 

turtle.done()
