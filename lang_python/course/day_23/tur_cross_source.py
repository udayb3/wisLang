from turtle import Turtle
from random import randint as rd

clr=["red","blue","green","light blue","navy","yellow green","firebrick","light salmon","orchid","dark orchid","dark magenta","indian red","dark violet"]
fn=("Arial",20,"bold")

class User(Turtle):
    
	def __init__(self):
		super().__init__() #Inheritance of the super class 
		self.hideturtle();	self.penup();	self.goto(0,-350)
		self.color("white");	self.shape("turtle");	self.lt(90);	self.showturtle()
	
	def move_up(self):
		"""It allows the turtle to move forward."""
		cur_y=self.ycor();	self.goto(0,cur_y+5)
	
	def move_down(self):
		"""It allows the turtle  to move backwards."""
		cur_y=self.ycor();	self.goto(0,cur_y-5)

	def rstrt(self):
		"""It brings the turtle back to its starting position."""
		self.hideturtle();	self.goto(0,-350);	self.showturtle()
	

class Obstacles():
	
	def	__init__(self):
#Genral settings for the turtle
		self.obs=[];	self.speed=4

	def create_car(self):
		"""This creates a new obstacle every time this is called."""
		if rd(1,5)==4:
			new_obs=Turtle("square");		new_obs.penup();		rand_y=20*rd(-13,13);		new_obs.goto(430,rand_y)
			new_obs.color(clr[rd(0,12)]);		new_obs.shapesize(stretch_len=2,stretch_wid=1)
			self.obs.append(new_obs)
		
	def move(self):
		"""It allows the obstacles to move along the turtle screen."""
		for i in range(len(self.obs)):
			cur_x=self.obs[i].xcor()-self.speed
			cur_y=self.obs[i].ycor()
			self.obs[i].goto(cur_x,cur_y)

	def check_col(self,check):
		"""It checks whether the turtle has collided with the obstacle or not."""
		for i in range(len(self.obs)):
			if self.obs[i].distance(check)<20:
				self.finish()
				return False
		return True		
	
	def finish(self):
		"""It tells the user when the game is over."""
		use=Turtle()
		use.hideturtle();	use.color("red");		use.write(arg="GAME OVER",font=fn,align="center")


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.prop=("Arial",12,"normal")
		self.hideturtle();	self.color("white");	self.penup();	
		self.goto(-200,300);	self.pendown();	self.write(arg="LEVEL: ",align="center",font=self.prop)
		self.temp=Turtle();	self.temp.hideturtle()
		

	def show_score(self,score):
		"""It shows the increased level of the game."""
		self.temp.clear();	self.temp.penup();	self.temp.goto(-150,300);	self.temp.pendown();	self.temp.color("white")
		self.temp.write(arg=score,align="center",font=self.prop)

	def win_game(self,che):
		"""It tells if the user has won the game. It also returns whether the user is in the game or not."""
		if che==6:
			self.temp.penup();	self.temp.goto(0,0);	self.temp.pendown()
			self.temp.write(arg="WINNER",align="center",font=fn)		
			return False
		return True