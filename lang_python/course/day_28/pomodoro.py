from tkinter import Tk, Canvas, PhotoImage, Label, Button
"""
1. 	Photoimage() class helps in inputting a png file.
2. Dynamic typing means that the type of the variable is only determined during run-time.



"""

# 	 CONSTANTS 
PINK = "#e2979c";	RED = "#e7305b";	GREEN = "#9bdeac";	YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25;	SHORT_BREAK_MIN = 5;	LONG_BREAK_MIN = 20
reps=0; TICK="✅" 
reset_timer=None

window=Tk()
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
  """It resets the counter back to 0 and sets all the other widgets to reset."""
  global reps
  window.after_cancel(reset_timer)
  reps=0
  #timer_text=00:00
  can.itemconfig(tim_sec,text="00")
  can.itemconfig(tim_min,text="00")
  #checkmarks
  can.itemconfig(tick,text="")
  #timer_label
  can.itemconfig(tit,text="CLOCK",fill=RED)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def sta_tim():
  """It starts the timer."""
  global reps
  reps+=1
  if(reps%8==0):
    can.itemconfig(tit,text="BREAK",fill=GREEN)
    countdown(LONG_BREAK_MIN*60)

  elif(reps%2==0):
    can.itemconfig(tit,text="BREAK",fill=RED)
    countdown(SHORT_BREAK_MIN*60)
    tic((reps-1)//2)

  else:
    can.itemconfig(tit,text='TIMER')
    countdown(WORK_MIN*60)

# 		 COUNTDOWN MECHANISM - There is already a loop which is looping through it 
def con(var)->str:
  """It checks for the bug of proper display of format of time remaining."""
  if var<10:
    return "0"+str(var)
  else:
    return str(var)
   
def countdown(num):
  """This counts the time."""
  sec=num%60;	min=(num//60)
  sec=con(sec);	min=con(min)
  can.itemconfig(tim_sec,text=sec);			can.itemconfig(tim_min,text=min)
  
  # Checking for the remaining time.
  if num>0:
    global reset_timer
    reset_timer=window.after(1000,countdown,num-1)
  else:
    sta_tim()

def tic(r):
  """It displays the tick which comes after completion of every round."""
  global TICK

  for i in range(r):
    TICK+="✅"
  can.itemconfig(tick,text=TICK)

# 		 UI SETUP 
window.title("Pomodoro")
window.config(padx=20,pady=20,bg="light blue",highlightthickness=0)
window.minsize(width=600,height=600)

can=Canvas(width=550,height=550)

# How to add photo to tkinter- Use of tkinter canvas widget
img=PhotoImage(file="photo.png")
can.create_image(275,275,image=img)

# Setting the text for counter
tim_sec=can.create_text(230,420,text="00",fill="black",font=(FONT_NAME,60,"normal"))
can.create_text(180,415,text=":",font=(FONT_NAME,60,"normal"))
tim_min=can.create_text(130,420,text="00",font=(FONT_NAME,60,"normal"))

# Setting the text for tickmark
tick=can.create_text(150,480,text="",font=(FONT_NAME,20,"normal"))

# Setting the text for task_name and initially setting it to clock
tit=can.create_text(170,320,text="CLOCK",fill=RED,font=(FONT_NAME,80,"italic"))

can.place(x=0,y=0)

# The START button 
bt1=Button(text="Start",font=(FONT_NAME,15,"italic"),border=5,command=sta_tim)
bt1.place(x=70,y=25)

# The RESET button
bt2=Button(text="Reset",font=(FONT_NAME,15,"italic"),border=5,command=reset)
bt2.place(x=250,y=25)

window.mainloop()