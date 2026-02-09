"""
DAY-29 -> Password manager
KEY points:
1. we have used messageboxes here.

MAJOR STEPS:
1. Constants
2. Generate password
3. Saving details to a file
4. User Experience

"""
from tkinter import Tk, Button, Label, PhotoImage, Canvas, Entry, messagebox as mg
from random import randint as rd, shuffle
import json as js

#			    Constants
FONT1=("calibri",14,"normal")
FONT2=("calibri",12,"normal")
SPECIAL=['!','@','#','$','&','(',')','?','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


#			    Generate password
def ps(sz)-> str:
  """It works on password."""
  num_alp=rd(1,sz-2);		num_dig=rd(1,sz-1-num_alp);		num_sym=sz-num_alp-num_dig
  temp=[];	word=""
  for i in range(num_sym):
    temp.append(SPECIAL[rd(0,7)])
    
  for i in range(num_alp):
    temp.append(SPECIAL[rd(8,33)])
    
  for i in range(num_dig):
    temp.append(str(rd(0,9)))

  shuffle(temp)
  for i in range(sz):
    word+=temp[i]
  return word

def gen_pas():
  """It generates a random password and returns the password to the password entry."""
  sz=rd(0,5)+10
  PASSWORD=ps(sz)
  ent_ps.delete(first=0,last='end')
  ent_ps.insert('end' ,string=PASSWORD)
  
#         Saving details to the file.
def sav():
  """It saves all the information- Email, password, website to the text file \"info.txt\"."""
  st_p=ent_ps.get()
  st_e=ent_ml.get()
  st_w=(ent_site.get()).lower()
  new_dt={
    st_w:
    {
    "E-mail":st_e,
    "Password":st_p
    }
  }
  if len(st_p)==0 or len(st_e)==0 or len(st_w)==0:
    mg.showinfo(title="Warning",message="You have left one of the fields empty.")
  else:
    isok=mg.askokcancel(title=st_w,message=f"These are the details provided:\n\nE-mail/Username: {st_e}\n\npassword: {st_p}\n\n.Do you want to save?",)
    if isok==True:
      final="Website: "+st_w+" | "+"E-mail: "+st_e+" | "+"Password: "+st_p+"\n"
      
      #   Opening the file
      with open(file="data.json",mode="w") as file:
        js.dump(new_dt,file,indent=4)
      
      ent_ps.delete(first=0,last='end')
      ent_ml.delete(first=0,last='end')
      ent_site.delete(first=0,last='end')

#         Reading from json file
def rd():
  name_wbs=(ent_site.get()).lower()
  info=None
  
  with open(file="data.json",mode='r') as fil:
    st=js.load(fil)
    try:
      info=st[name_wbs]
    except:
      mg.showinfo(title="WARNING",message="This file does not exists in the database.")
    else:
      mg.showinfo(title=name_wbs,message=f"E-mail: {info['E-mail']}\nPassword: {info['Password']}")

#			    User Experience
window=Tk()
window.config(bg="#ffffff")
window.minsize(width=500,height=500)
window.title("Password Manager")

#         Setting the lock icon
img=PhotoImage(file="image.png")
can=Canvas()
can.create_image(120,120,image=img)
can.config(bg="#ffffff",highlightthickness=0)
can.place(x=130,y=10)

"""       Website name          """
lb_site=Label();		lb_site.config(text="Website",font=FONT1);		lb_site.place(x=50,y=250,width=150)
ent_site=Entry();		ent_site.config(borderwidth=5);		ent_site.place(x=240,y=250)

"""       E-mail/Username       """ 	
lb_ml=Label();		lb_ml.config(text="E-Mail/Username",font=FONT1);		lb_ml.place(x=50,y=300,width=150)
ent_ml=Entry();		ent_ml.config(borderwidth=5);		ent_ml.place(x=240,y=300)

"""       Password              """
lb_ps=Label();		lb_ps.config(text="Password",font=FONT1);		lb_ps.place(x=50,y=350,width=150)
ent_ps=Entry();		ent_ps.config(borderwidth=5);		ent_ps.place(x=240,y=350)

"""		BUTTONS		"""
bt_s=Button();		bt_s.config(text="SAVE",command=sav,padx=0,pady=0,width=12,font=FONT2);		bt_s.place(x=60,y=400)
bt_g=Button();		bt_g.config(text="Generate password",command=gen_pas,width=20,padx=0,pady=0,font=FONT2);		bt_g.place(x=240,y=400)
bt_show=Button(); bt_show.config(text="Show",command=rd,width=20,font=FONT2);   bt_show.place(x=150,y=450)

window.mainloop()