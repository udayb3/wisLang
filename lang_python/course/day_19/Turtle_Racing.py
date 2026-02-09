from turtle import Turtle, Screen
from random import randint as rd
#Calling Screen class
scr=Screen()
t=[Turtle(), Turtle(), Turtle(), Turtle(),Turtle()]
st=Turtle()
#Setting up the screen
scr.setup(width=800,height=600)
choice=scr.textinput("Make your Bet","Which turtle will win the race:\nRed/Green/Grey/Black/Blue").lower()
#Making array for different forward movement and for different color
dis=[20,40,60,80,100]
cl=["red","blue","green","black","grey"]

def ch():
  """It moves a random turtle from its initial position."""
  n=rd(0,4)
  t[n].fd(dis[rd(0,4)])
  return n

def set_in_pos():
  """It sets all the turtle to their initial position in the race."""
  for i in range(5):
    t[i].shape("turtle")
    t[i].penup()
    t[i].color(cl[i])
    t[i].goto(x= -325, y= (i-2)*100)

def create_ground():
  """This creates the ground for the race.\nIt includes the set-up of finish line and lines separating participating turtles"""
  for i in range(6):
    st.penup()
    st.goto(-325,(float(i)-2.5)*100)
    st.pendown()
    st.forward(650) 
  st.rt(90)
  st.fd(500)
#Making the inital arrangement for the race
create_ground()
set_in_pos()
eop=False
temp=-1
#Starting the race
while not eop:
  sel=ch()
  index=t[sel].position()
  if index[0]>=325:
      eop=True
      temp=sel
#Checking and telling the user who has finally won
if cl[temp]==choice:
  print("Congratulations, You have won the race.")
else:
  print(f"Sorry, You have lost the race. The winner is {(cl[temp]).title()}.")

scr.exitonclick()