### SET UP
#libraries
import turtle
import random
#variables
    #screen
xsize = 800
ysize = 600
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
#food
    #apple
turtle.register_shape("apple.gif")
apple = turtle.clone()
apple.shape("apple.gif")
apple.hideturtle()
apple_pos = []
apple_stamps = []
apple.goto(100, 100)
apple_pos.append((100,100))
apple_stamps.append(apple.stamp())
    #goldapple
turtle.register_shape("goldapple.gif")
gapple = turtle.clone()
gapple.shape("goldapple.gif")
gapple.hideturtle()
gapple_pos = [(-100, -100)]
gapple_stamps = []
gapple.goto(gapple_pos[0])
gapple_stamps.append(gapple.stamp())

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
        #eat apple
    if snake.pos() in apple_pos:
        apple_index = apple_pos.index(snake.pos())
        apple.clearstamp(apple_stamps[apple_index])
        apple_pos.pop(apple_index)
        apple_stamps.pop(apple_index)
        print("Yummy apple!")
        #eat gapple
    if snake.pos() in gapple_pos:
        gapple_index = gapple_pos.index(snake.pos())
        gapple.clearstamp(gapple_stamps[gapple_index])
        gapple_pos.pop(gapple_index)
        gapple_stamps.pop(gapple_index)
        print("Whoa, a golden apple!!!")
        #keep going
    turtle.ontimer(move, step_time)
#directions
def up():
    snake.direction = "Up"
    print("Going up!")
def down():
    snake.direction = "Down"
    print("Going down!")
def right():
    snake.direction = "Right"
    print("Going right!")
def left():
    snake.direction = "Left"
    print("Going left!")
#apple
#def make_apple():
food_x = random.randint(down_edge/square_size+1, up_edge/square_size-1)
food_y = random.randint(left_edge/square_size+1, right_edge/square_size-1)
apple.goto(food_x*20,food_y*20)
apple_stamps.append(apple.stamp())
apple_pos.append(apple.pos())


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
