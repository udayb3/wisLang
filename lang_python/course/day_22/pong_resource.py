from turtle import Turtle

class Resource(Turtle):
  
	def __init__(self):
		super().__init__()
		self.alg="center"
		self.set=("Calibri",14,"normal")

	def mid_wall(self):
		"""It creates the middle wall for the pong game."""
		self.pensize(5)
		self.penup();			self.goto(0,-300);		self.lt(90);		self.pendown()	
		self.hideturtle()
		for i in range(21):
			self.color("white");		self.fd(15)
			self.color("black");		self.fd(15)

	def score_card(self):
		"""It creates the scorecard."""
		self.color("white");		self.penup()
		self.goto(50,290);		self.write(arg="RIGHT",align=self.alg,font=self.set)
		self.goto(-50,290);		self.write(arg="LEFT",align=self.alg,font=self.set)


class Slider(Turtle):

	def __init__(self):
		super().__init__()
		self.side_v=0
		self.dir="p"

	def move_up(self):
		"""It moves up the slider."""
		y=self.ycor()
		if(y<270):
			self.goto(self.side_v,y+20)

	def move_down(self):
		"""It moves the slider down."""
		y=self.ycor()
		if(y>-270):
			self.goto(self.side_v,y-20)

	def create_block(self,side):
		"""It creates the slider and shifts it to the respective position.
		side=="The side which has won.
		Eg..side=\"left\""""
		self.dir=side
		if	(self.dir).lower()=="right":
			self.side_v=370
		elif (self.dir).lower()=="left":
			self.side_v=-370
		self.penup();	self.hideturtle();	self.color("white");	self.goto(self.side_v,0);	self.showturtle()	
		self.shape("square");		self.pensize(width=20);	self.shapesize(stretch_len=5,stretch_wid=1)
		self.setheading(90)


class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle");	self.color("white");	self.penup()
		self.xmov=10;	self.ymov=10

	def move(self):
		"""It makes the ball move."""
		new_x=self.xcor()+self.xmov;		new_y=self.ycor()+self.ymov
		self.goto(new_x,new_y)
	
	def reset(self):
		"""It resets the ball."""
		self.hideturtle()
		self.goto(0,0)
		self.showturtle()
		self.xmov*=-1.15
		self.ymov*=-1.15

class Score(Turtle):

	def __init__(self):
		super().__init__()
		self.left_score=0
		self.right_score=0
		self.alg="center"
		self.set=("Calibri",14,"normal")
		self.color("white")
		self.penup()

	def update_score(self):
		"""It updates the score of the respective position."""
		self.hideturtle()
		self.clear()
		self.goto(50,270);		self.write(arg=str(self.right_score),align=self.alg,font=self.set)
		self.goto(-50,270);		self.write(arg=str(self.left_score),align=self.alg,font=self.set)

	def show_winner(self,side):
		"""It shows the winner of the 5 point game match."""
		self.goto(0,0);	self.color("red");
		if side.lower()=="left":
			self.write(arg="Left Side Won",align=self.alg,font=("Arial",30,"bold"))
		else:
			self.write(arg="Right Side Won",align=self.alg,font=("Arial",30,"bold"))
	