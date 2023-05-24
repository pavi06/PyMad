import turtle as t

t.bgcolor("pink")
t.speed(9)
t.hideturtle()

t.penup()
t.goto(-90,250)
t.pendown()
t.color("white")
style=(80)
t.write("Hey buddy! Am the snowMan!..",font=style,move=True)

#end of body
t.penup()
t.goto(0,-280)
t.pendown()
t.pensize(3)
t.color("white")
t.begin_fill()
t.circle(110)
t.end_fill()

#middle part
t.penup()
t.goto(0,-110)
t.pendown()
t.begin_fill()
t.circle(90)
t.end_fill()

#upper part
t.penup()
t.goto(0,20)
t.pendown()
t.begin_fill()
t.circle(70)
t.end_fill()

def black_circle():
    t.color("black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

#eyes
x=-20
for i in range(2):
    t.penup()
    t.goto(x,110)
    t.pendown()
    black_circle()
    x=x+40
#buttons
y=0
for i in range(5):
    t.penup()
    t.goto(0,y)
    t.pendown()
    black_circle()
    y=y-55

#mouth
t.penup()
t.goto(0,70)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(17)
t.end_fill()
t.penup()
t.goto(0,75)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(17)
t.end_fill()

#right arm
t.penup()
t.goto(75,0)
t.pendown()
t.color("brown")
t.begin_fill()
t.left(40)
for i in range(2):
    t.forward(75)
    t.left(90)
    t.forward(7)
    t.left(90)
t.end_fill()

#finger1
t.penup()
t.goto(115,38)
t.pendown()
t.begin_fill()
t.left(40)
for i in range(2):
    t.forward(25)
    t.left(90)
    t.forward(5)
    t.left(90)
t.end_fill()

#finger2
t.begin_fill()
t.right(100)
for i in range(2):
    t.forward(25)
    t.left(90)
    t.forward(5)
    t.left(90)
t.end_fill()

#left arm
t.penup()
t.goto(-140,50)
t.pendown()
t.color("brown")
t.begin_fill()
t.right(10)
for i in range(2):
    t.forward(75)
    t.left(90)
    t.forward(7)
    t.left(90)
t.end_fill()

#left  finger1
t.penup()
t.goto(-112,58)
t.pendown()
t.begin_fill()
t.right(40)
for i in range(2):
    t.forward(25)
    t.right(90)
    t.forward(5)
    t.right(90)
t.end_fill()

#finger2
t.begin_fill()
t.right(100)
t.penup()
t.goto(-108,31)
t.pendown()
for i in range(2):
    t.forward(25)
    t.right(90)
    t.forward(5)
    t.right(90)
t.end_fill()

#hat
t.penup()
t.goto(50,150)
t.pendown()
t.color("black")
t.begin_fill()
t.right(10)
t.forward(100)
t.right(90)
t.forward(10)
t.right(90)
t.forward(20)
t.left(90)
t.forward(45)
t.right(90)
t.forward(60)
t.right(90)
t.forward(45)
t.left(90)
t.forward(20)
t.right(90)
t.forward(10)
t.hideturtle()
t.end_fill()
t.done()

  