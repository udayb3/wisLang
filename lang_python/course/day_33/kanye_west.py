from tkinter import *
import requests as rqs


#      Functions for using the API
def quote()->dict:
    """     It gives back a dictionary which came from the following API."""
    res=rqs.get(url="https://api.kanye.rest/")
    res.raise_for_status()
    data=res.json()
    return data

def get_quote():

    qte=quote()
    canvas.itemconfig(quote_text,text=qte["quote"])
    print(0)

#   User Interface
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()



