import random
import turtle

#set up border
# w = 500
# h = 800

def screen_setup(width, height, bgcolor, title):
    race.title(title)
    race.bgcolor(bgcolor)
    race.setup(width, height)
def draw_finish_line():
    t= turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color("#1e36eb")
    t.goto(-230,340)
    t.pendown()
    t.pensize(3)
    t.goto(220,340)

def create_racecars():
    color_list = ["red", "orange", "yellow", "green", "blue", "purple", "indigo"]
    random.shuffle(color_list)
    x_coor_list = [-210, -140, -70, 0, 70, 140,210]
    random.shuffle(x_coor_list)
    for _ in range(7):
        car = turtle.Turtle()
        car.speed(100)
        car.shapesize(2)
        car.shape("triangle")
        car.tiltangle(90)
        car.direction= "up"
        car.color(color_list.pop())
        car.penup()
        car.goto(x_coor_list.pop(), -330)
        car_list.append(car)

def car_moves():
    global start_race
    # car1 = turtle.Turtle()
    for car in car_list:
        car_distance =random.randint(1,20)
        # car_distance= 20
        if (car.ycor() + car_distance)> 315:
            start_race = False
            car.sety(315)
            # print(f'{car.color()[0]} car is the winner!!')
            print_winner(car)
            break
        else:
            car.sety(car.ycor() +car_distance)
def print_winner(car):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 345)
    pen.color(car.color()[0])
    pen.write(f'{car.color()[0].title()} car is the winner!!', font= ("Times New Roman",48, "normal"), align="center")

def start_game():
    global start_race
    start_race = True


race = turtle.Screen()
race.onkeypress(start_game,'s')
start_race = False
screen_setup(500,800, "#a8eeff","Turtle Race!")
draw_finish_line()
car_list = []
create_racecars()
while True:
    race.update()
    if start_race:
        car_moves()

# race.exitonclick()
