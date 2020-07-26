import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.pencolor('green')
a=0
b=0
c=0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while True :
    t.forward(a)
    t.right(b)
    t.backward(c)
    a+=2
    b+=1
    c+=1
    if b==210:
        break
    t.hideturtle()
turtle.dot()