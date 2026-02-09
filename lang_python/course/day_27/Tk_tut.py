"""
DIFFERENT TYPE OF ARGUMENTS FOR FUNCTION:
	DEFAULT arguments: We can directly save the values of the arguments when we make them by assigning them values.
  *args argument: This helps us in taking as many positional arguements as we want. It is because the asterisk keyword deposits all the arguments in a tuple.
  **kwargs argument: It helps us in working with an arbitary number of keyword arguments. kwargs becomes a type of dictionary.
tkinter is the module which deals with the GUI part. Some of its libraries and functions are listed below:
Tk
	mainloop(): It is a function which runs the in-built loop and then listens to the command which will be given. It should always be at the last line of the program.
	title(): 
  minsize():
Label
	pack(): It is a geometry management mechanism. It is very important in applying changes.
Button
  config(): It can change the default variables such as side, expand, font, text and other variables.
  pack(): It is very important in applying change.

LAYOUT MANAGEMENT:
There are majorly 3 layout managers in Tkinter:
1. pack()
2. place()
3. grid()

1. pack(): It only packs each of the widget next to each other in a format which starts from top. It packs next widget after the previous one. We can edit some of it using side parameter. It is still difficult to assign position

2. place(): It is about precise positioning. We can exactly pinpoint the location where we want to place the widget. (0,0) starts from top left of the screen. Calculation becomes difficult with an increase in the number of widget.

3. grid(): It imagines that the entire screen is divided in let's say m number of rows and n number of columns.
They should never be together in the window.

padding= the space around the widget.
Process done:
  1. How to create a label.
  2. How to create a button.
  3. How to create a entry.
  4. How to create a button.
  5. How to create a text box.
  6. How to create a spin box.
  7. How to create scale.
  8. How to create checkbox.
  9. How to create radio button.
  10. How to create list box.
  11. How to create canvas widget.
  """
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END , string="Some text to begin with.")
#Gets text in entry
# .delte() clears whatever is written in the entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
