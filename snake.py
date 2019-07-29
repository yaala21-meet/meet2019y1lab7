### SET UP
#libraries
import turtle
import random
#variables
    #screen
xsize = 800
ysize = 500
up_edge = ysize/2
down_edge = -ysize/2
right_edge = xsize/2
left_edge = -xsize/2
    #snake
start_len = 4
square_size = 20
step_time = 100
#turtle
turtle.tracer(1,0)
turtle.setup(xsize, ysize)
turtle.penup()
#new snake
snake = turtle.clone()
snake.shape("square")
turtle.hideturtle()
snake.color("green")
snake.direction = "Up"
#lists
pos_list = []
stamp_list = []


### FUNCTIONS
#drawing
def stampit():
    pos_list.append(snake.pos())
    stamp_list.append(snake.stamp())
def clean():
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
#moving
def move():
    if snake.direction == "Up":
        snake.goto(snake.xcor(), snake.ycor() + square_size)
    elif snake.direction == "Down":
        snake.goto(snake.xcor(), snake.ycor() - square_size)
    elif snake.direction == "Right":
        snake.goto(snake.xcor() + square_size, snake.ycor())
    elif snake.direction == "Left":
        snake.goto(snake.xcor() - square_size, snake.ycor())
        #update
    stampit()
    clean()
        #edges
    if snake.xcor() > right_edge:
        print("You hit the right edge! Game over!")
        quit()
    elif snake.xcor() < left_edge:
        print("You hit the left edge! Game over!")
        quit()
    elif snake.ycor() > up_edge:
        print("You hit the top edge! Game over!")
        quit()
    elif snake.ycor() < down_edge:
        print("You hit the bottom edge! Game over!")
        quit()
        #keep going
    turtle.ontimer(move, step_time)
def up():
    snake.direction = "Up"
    #move()
    print("Going up!")
def down():
    snake.direction = "Down"
    #move()
    print("Going down!")
def right():
    snake.direction = "Right"
    #move()
    print("Going right!")
def left():
    snake.direction = "Left"
    #move()
    print("Going left!")


### PLAYING
#listening
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")
turtle.listen()
#looping
for piece in range(start_len):
    x_pos = snake.xcor() + square_size
    y_pos = snake.ycor()
    snake.goto(x_pos, y_pos)
    stampit()
#starting
move()
turtle.mainloop()
