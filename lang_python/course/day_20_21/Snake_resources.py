from turtle import Turtle, Screen

snk=[Turtle(),Turtle(),Turtle()]
scr=Screen()

def CREATE_WALL():
	"""This functions creates the outer wall for the snake game."""
	use=Turtle()
	use.shape("square");	use.color("white")	
	use.penup();	use.goto(305,315);	use.pendown();  use.pensize(width=40)
	for _ in range(4):
		use.rt(90);  use.fd(620)
	use.penup()

def SNAKE_BODY():
	"""It make a snake body at the centre of the screen."""
	for i in range(3):
		snk[i].color("white");  snk[i].shape("square")
		snk[i].penup(); snk[i].goto((1-i)*10,0); 

def SET_UP_CHOICE():
	"""It sets up the basic parts
	such as the screen size, changing the background color and giving the title to the graphics window."""
	scr.setup(width=700,height=700);		scr.bgcolor("black");		scr.title("Snake Game")
	choice=float(scr.textinput(title="Difficulty Level",prompt="Choose hardness from 1 to 5."))
	if	choice<1 or choice>5:
		choice=0.05
	else:
		choice=(6-choice)*0.05
	return choice

def ADD_SEGMENT(size):
	"""It adds a segment to the snake whenever it eats the food."""
	p=Turtle()
	p.penup()
	snk.append(p)
	snk[size].color("white")
	snk[size].shape("square")	
	snk[size].goto(snk[size-1].position())
	size=size+1
	return size

def up():
	"""It changes the snake direction to upwards"""
	if	snk[0].heading !=90.0:
		snk[0].setheading(90)

def down():
	"""It changes the direction of snake to downwards."""
	if snk[0].heading != 270:
		snk[0].setheading(270)

def turn_left():
	"""It makes the snake turn left."""
	if snk[0].heading !=180:
		snk[0].setheading(180)


def turn_right():
	"""It makes the snake turn right."""
	if snk[0].heading !=0.0:
		snk[0].setheading(0)

def snake_move(size):
		"""It moves the snake move ahead."""
		for i in range(size-1):
			new_x=snk[size-2-i].xcor()
			new_y=snk[size-2-i].ycor()
			snk[size-1-i].goto(new_x,new_y)
		snk[0].fd(20)