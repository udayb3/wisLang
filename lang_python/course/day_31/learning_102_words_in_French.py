"""
STEPS in the order in which they are coded in the program.

1.  Basic functions which create flash cards and writes the french and english words on them. 
2.  Creating UI
3.  Giving the data back to a different .csv file to know which words we didn't understand."""

from tkinter import Tk, Label, Button, PhotoImage, Canvas
import store as stt
from random import randint as rd

new_dat={"French":[],"English":[]}

img_f=None; img_b=None
BACKGROUND_COLOR = "#B1DDC6"; chec=1

"""   Calling the funcitons from the store file."""
stt.copy_s();   dt=stt.work()


#   Functions

def show_back(word_eng:str):
  """   This makes the back side of the card and writes the english translation of the french word."""
  cn.itemconfig(img_set,image=img_b)

  cn.itemconfig(l1,text="Eng")
  cn.itemconfig(l2,text=word_eng)
  cn.place(x=120,y=90)

def show_front(word_fre,word_eng):
  """   This makes the front side of the flash card and writes the french word on the front side. """
  global k
  cn.itemconfig(img_set,image=img_f)

  cn.itemconfig(l1,text="Fre")
  cn.itemconfig(l2,text=word_fre)

  k=win.after(10000,show_back,word_eng)

def create_flash():
  """   This makes the flash card for the GUI."""
  global chec
  if chec==0:
    win.after_cancel(k)
  chec=0
  global temp,ind
  sz=len(dt)
  ind=rd(0,sz-1)
  temp=dt[ind]
  word_en=None; word_fr=None
  for key in temp:
    word_fr=key;  word_en=temp[key]
  show_front(word_fr,word_en)

def right():
  """This works when right button is clciked and it removes the word for which you have choosen correct."""
  try:
    p=dt.pop(ind)
    p=dt[0]
  except:
    print("Congratulations, You have finished learning all the possible words.")
  else:
    create_flash()

def create():
  """It starts creating flash cards for the words."""
  global cn, img_set, l1,l2
  cn=Canvas()
  img_set=cn.create_image(50,50,image=None)
  l1=cn.create_text(190,70,text="title",font=("arial",15,"normal"))
  l2=cn.create_text(190,140,text="Word",font=("calibri",30,"normal"))
  cn.config(highlightthickness=0)

  cn.place(x=120,y=90)
  create_flash()


#   UI

win=Tk()
win.config(bg=BACKGROUND_COLOR)
win.title("Learn French")
win.minsize(width=600,height=600)

"""   Storing all the four images which are required for the gui."""
img_f=PhotoImage(file="images\\card_front.png")
img_b=PhotoImage(file="images\\card_back.png")
img_r=PhotoImage(file="images\\right.png")
img_w=PhotoImage(file="images\\wrong.png")

"""    It is a button for the right tick."""
bt_c=Button(image=img_r,highlightthickness=0,command=right)
bt_c.place(x=400,y=400)

"""   It is the button for the wrong tick."""
bt_w=Button(image=img_w,highlightthickness=0,command=create_flash)
bt_w.place(x=100,y=400)

"""   It is the button for the showing of first flash card."""
bt_show=Button(text="Show Word",padx=5,pady=5,width=14,bd=5,command=create)
bt_show.place(x=220,y=540)


win.mainloop()

"""   It stores the words which we didn't know meaning for in a different file in the data section."""
for i in range(len(dt)):
  temp=dt[i]
  for key in temp:
    new_dat["English"].append(temp[key])
    new_dat["French"].append(key)

stt.clear(new_dat)