# sq_game.py
import turtle # Импортируем библиотеку
import random 
import math

wn = turtle.Screen() # Создаем окно
wn.tracer(3)
player = turtle.Turtle() # Создаем игрока
player.shape('square') # Меняем форму на квадрат
player.speed(0) # Скорость героя
player.penup()
player.setposition(0, -200)

max_anamy = 10
anamys = []
for count in range(max_anamy):
        anamys.append(turtle.Turtle())
        anamys[count].turtlesize(random.randint(1,5))
        anamys[count].color('red')
        anamys[count].penup()
        anamys[count].speed(0)
        anamys[count].setposition(random.randint(-200,200), random.randint(400, 1000))
        anamys[count].right(90)

def go_right(): # 
        if player.xcor() < 200:
                player.forward(15)

def go_left():
        if player.xcor() > -200:
                player.backward(15)	

def isColision(t1,t2):
        d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+ math.pow(t1.ycor() - t2.ycor(),2))
        if d < 30:
                return True
        else:
                return False	

def game_over():
        global game
        game = False
        t = turtle.Turtle()
        wn.bgcolor('red')	
        t.hideturtle()
        t.color('white')
        text = f'У Вас {score} очков(а)'	
        t.write(text, font=('Arial', 24, 'normal'))


turtle.listen()
turtle.onkey(go_right, 'Right')
turtle.onkey(go_left, 'Left')
score = 0 
speed = 1
game = True
while game:
        for count in range(max_anamy):
                anamys[count].forward(speed)
                if anamys[count].ycor() < -300:
                        speed += 0.1
                        score += 1 
                        anamys[count].setposition(random.randint(-200,200), random.randint(400, 1000))
                if isColision(player, anamys[count]):
                        game_over()
wn.exitonclick()