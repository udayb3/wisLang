from tkinter import Tk, Label, Entry, Button


def conv_mile_to_km(val):
  """It is a funnction to convert miles to km."""
  ans=val*1.60934
  return ans

def button_click():
  """Is is a function for button click. It works everytime the button is clicked."""
  ml=float(et.get())
  km=round(conv_mile_to_km(ml),2)
  st=str(km)
  lb[4].config(text=st)

# CREATING A WINDOW FOR THE Tkinter module
window=Tk()
window.config(bg="grey",padx=5,pady=5)
window.minsize(width=500,height=500)
window.title("CONVERTER: Miles to Km ")

# Creating different labels
lb=[Label(),Label(),Label(),Label(),Label()]

lb[0].config(text="Enter distance in miles:",padx=10,pady=5,bg="grey")
lb[0].grid(row=1,column=1)

lb[1].config(text="Equal to",padx=10,pady=5,bg="grey")
lb[1].grid(row=2,column=1)

lb[2].config(text="miles",padx=10,pady=5,bg="grey")
lb[2].grid(row=1,column=3)

lb[3].config(text="Km",padx=10,pady=5,bg="grey")
lb[3].grid(row=2,column=3)

lb[4].config(bg="white",width=10)
lb[4].grid(row=2,column=2)
# Creating buttons
bt=Button(text="CONVERT",bg="white",command=button_click)
bt.grid(row=4,column=4)

# Creating entry
et=Entry(width=10,bg="white")
et.grid(row=1,column=2)

window.mainloop()