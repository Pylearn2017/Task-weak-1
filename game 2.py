#laberint
#game
import turtle

def player_forward():
        if player.xcor() < -15 or player.xcor() > 15:
                player.goto(0, -300)
        if player.ycor() > 280:
                pen.goto(0, 0)
                pen.write('Победа', font=('Arial', 24))

        player.forward(5)

def player_left():
        player.left(20)

def player_right():
        player.right(20)

def player_backward():
        player.backward(5)
        if player.xcor() < -15 or player.xcor() > 15:
                player.goto(0, -300)
        if player.ycor() > 280:
                pen.goto(0, 0)
                pen.write('Победа', font=('Arial', 24))

wn = turtle.Screen()
wn.bgcolor('lightgrey')

pen = turtle.Turtle()
pen.penup()
pen.goto(-40, -320)
pen.begin_fill()
pen.color('green')
pen.down()
pen.forward(80)
pen.left(90)
pen.forward(40)
pen.left(90)
pen.forward(80)
pen.left(90)
pen.forward(40)
pen.end_fill()
pen.penup()

pen.color('white')
pen.goto(-15, -280)
pen.begin_fill()
pen.down()
pen.left(180)
pen.forward(560)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(560)
pen.right(90)
pen.forward(30)
pen.end_fill()
pen.penup()

pen.color('red')
pen.goto(40, 320)
pen.begin_fill()
pen.down()
pen.forward(80)
pen.left(90)
pen.forward(40)
pen.left(90)
pen.forward(80)
pen.left(90)
pen.forward(40)
pen.end_fill()
pen.penup()

player = turtle.Turtle()
player.shape('circle')
player.penup()
player.color('lightgreen')
player.goto(0, -300)

turtle.listen()
turtle.onkey(player_forward, 'w')
turtle.onkey(player_left, 'a')
turtle.onkey(player_right, 'd')
turtle.onkey(player_backward, 's')

wn.exitonclick()
#ggaamme