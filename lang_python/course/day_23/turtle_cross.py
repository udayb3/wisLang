"""
STEPS:
1. MOVEMENT OF THE TURTLE THROUGH THE GAME: Done
2. MOVEMENT OF THE OBSTACLES: Done
3. CHECKING WHETHER THE COLLISION HAS HAPPENED OR NOT: Done	
4. RESETING THE TURTLE TO THE INITIAL POSITION AFTER IT HAS FINISHD THE LEVEL: Done
5. INCREASING THE SCOREBOARD AND OTHER PRINT STATEMENTS SUCH AS GAME OVER AND WINNNER: Done
"""
from turtle import Screen
from tur_cross_source import User, Scoreboard, Obstacles
from random import randint as rd
import time  


#Creating objects from the available classes
scr=Screen();	  body=User();   score=Scoreboard();   obs=Obstacles()

#	General Set-Up
scr.tracer(0)
scr.setup(width=800,height=720);		scr.bgcolor("black")

#Set-up for user connect
scr.onkeypress(body.move_up,"Up");	scr.onkeypress(body.move_down,"Down")
scr.listen()

eog=True
coun=0
num=1
lev=1

score.show_score(lev)

while eog:
  time.sleep(0.1)
  obs.create_car()
  obs.move()
  eog=obs.check_col(body)

#Checking whether the turtle has reached the finish line of the given level.
  if body.ycor()>=300:
    body.rstrt();   lev+=1;   obs.speed+=4;   score.show_score(lev)
  
  eog=score.win_game(lev)

  scr.update()

scr.exitonclick()