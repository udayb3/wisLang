from turtle import Turtle
import random as rd
ALIGNMENT =["center","left","right"]
FONT=[("arial",30,"normal"),("calibri",14,"bold")]

class Food_Ball(Turtle):
#First we create the initializer for the food class
	def __init__(self):
		super().__init__()  
		self.penup()
		self.shape("circle");			self.color("red");			self.shapesize(stretch_wid=0.5,stretch_len=0.5);			self.speed(0)
		self.REF()

	def REF(self):
		"""It assigns a random position to the red ball of food around the map."""
		random_x=rd.randint(-280,280);					random_y=rd.randint(-280,280)
		self.goto(random_x,random_y)


class Score_Board(Turtle):
	#It helps in increasing the score.
	def __init__(self,Hardness):
		super().__init__()
		self.score=0
		self.diff=Hardness
		self.penup()
		self.color("black");	self.goto(0,302);	self.speed(0)
		self.hideturtle()
		self.UPDAT_SCORE()
		

	def UPDAT_SCORE(self):
		"""It updates the score that is the number of food balls eaten by the snake."""
		self.write(arg=f"SCORE: {self.score} | DIFFICULTY LEVEL: {self.diff}",align=ALIGNMENT[0],font=FONT[1])

	def INC_SCORE(self):
		"""It increases the score everytime the snake eats the ball of food."""
		self.score+=1
		self.clear()
		self.UPDAT_SCORE()

	def GAME_OVER(self):
		"""It tells the user that the game is over."""
		self.goto(0,0)
		self.color("red")
		self.write(arg=f"GAME  OVER",align=ALIGNMENT[0],font=FONT[0])