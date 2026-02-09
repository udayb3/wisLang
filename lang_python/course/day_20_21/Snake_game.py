from turtle import Screen,Turtle
import time as tm
from Snake_resources import CREATE_WALL, SNAKE_BODY, snk, turn_left, turn_right, up,down, SET_UP_CHOICE, snake_move, ADD_SEGMENT
from snake_food import Food_Ball, Score_Board 

#CREATING SCREEN
scr=Screen();				scr.tracer(0)		
size=3;		game_is_on=True

#BASIC SET-UP
dif=SET_UP_CHOICE();		CREATE_WALL();		SNAKE_BODY()
scr.listen();			scr.onkey(turn_left,"Left");			scr.onkey(turn_right,"Right");	scr.onkey(up,"Up");	scr.onkey(down,"Down")

#CREATING OBJECTS
fd=Food_Ball();			sb=Score_Board(6-(dif/0.05))

while game_is_on:
	scr.update();						tm.sleep(dif)
	snake_move(size)
#DETECTING COLLISIONS WITH DIFFERENT THINGS
#FOOD
	if snk[0].distance(fd) < 15:
		fd.REF();		sb.INC_SCORE();		q=ADD_SEGMENT(size); size=q

#WALL
	pos=snk[0].position()
	if pos[0]>=303 or pos[0]<=-303 or pos[1]>=303 or pos[1]<=-303:
		sb.GAME_OVER()
		game_is_on=False

#BODY
	pos_body=[]
	for i in range(size-1):
		pos_body.append(snk[i+1].position())
	if	snk[0].position() in pos_body:
		sb.GAME_OVER()
		game_is_on=False

scr.exitonclick()