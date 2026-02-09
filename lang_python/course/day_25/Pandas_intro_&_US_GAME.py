from turtle import *
import pandas as pd
from time import sleep

ft=("Arial",10,"normal")
coun=0

#READING FROM THE CSV FILE
data=pd.read_csv('50_states.csv')

#MAKING LIST FOR THE DATA EXTRACTED FROM THE CSV FILES
st_list=data["state"].to_list()
x_list=data["x"].to_list()
y_list=data["y"].to_list()
sz=len(st_list)

#BASIC SET-UP FOR THE SCREEN such as making the instance of the objects.
scr=Screen();	tur=Turtle();	tr1=Turtle()
scr.title("U.S. Project game")
tr1.hideturtle();	tr1.penup()

#ADDING THE US GIF FILE TO THE SHAPES IN THE TURTLE
img="game.gif"
scr.addshape(name=img)
tur.shape(img)

def write_name(state,x,y):
  """This function takes the turtle to the state area and then writes the state name there."""
  tr1.goto(x,y);	tr1.pendown()
  tr1.write(arg=state,align="center",font=ft)
  tr1.penup();	tr1.goto(0,0);	

#MAIN PROGRAM TO ASK THE USER ABOUT THE STATE NAME AND CHECKING IF IT IS VALID OR NOT.
gc=True
while(gc):
	st=(scr.textinput(title=f"TOTAL STATES GUESSED: {coun}",	prompt="Name a state[if you cannot then write \"lost\"]:"))
	if (st!=None):
		st=st.title()

	for i in range(len(st_list)):
		if st==st_list[i]:
			write_name(st_list[i].title(),x_list[i],y_list[i]); coun+=1
	if st=="Lost":
		gc=False
	sleep(2)

tr1.pendown();  tr1.write(arg=f"Total States guessed:{coun}",align="center",font=("Arial",30,"normal"))

#AN ALTERNATIVE WAY TO MAKE THE PROGRAM RUN IS BY USING THE FUNCTION "mainloop()"
tr1.exitonclick()