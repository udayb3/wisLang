from turtle import Turtle, Screen
from pong_resource import Resource, Slider, Ball, Score
import time as tm

scr=Screen();			rs=Resource();		s_right=Slider();	s_left=Slider();	ball=Ball()

scr.bgcolor("black");     scr.setup(width=800,height=640)
s_right.create_block("right");   s_left.create_block("left")
scr.tracer(0)

scr.listen()
scr.onkeypress(s_right.move_up,"Up");		scr.onkeypress(s_right.move_down,"Down")
scr.onkeypress(s_left.move_up,"w");		scr.onkeypress(s_left.move_down,"s")

rs.mid_wall();					rs.score_card();		sc=Score()
gio=True

while(gio):
  tm.sleep(0.1)
  scr.update()
  ball.move()

  z=ball.ycor()
#To detect the collision of slider with the wall
  if z>=300 or z<=-300:
    ball.ymov*=-1
#To detect collision of ball with the slider
  if (ball.distance(s_right.pos())<40 and ball.xcor()>320) or (ball.distance(s_left.pos())<40 and ball.xcor()<-320):
    ball.xmov*=-1
#To update the score of both the playing sides
  if	ball.xcor()<-400:
    ball.reset();	sc.right_score=sc.right_score+1
  if	ball.xcor()>400:
    ball.reset(); sc.left_score=sc.left_score+1
  sc.update_score()
#To Show the final winner of the game
  if sc.left_score==5:
    gio=False; sc.show_winner("left") 
  if sc.right_score==5:
    gio=False;  sc.show_winner("right")
    
scr.exitonclick()