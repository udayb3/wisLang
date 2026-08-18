from tkinter import *
import html

THEME_COLOR = "#375362"


class Question:
    """It returns an object which has two attributes-question and its answer."""
    def __init__(self, q_text:str, q_answer:str)->None:
        self.text = q_text
        self.answer = q_answer


class QuizInterface():
    """
    It does the following works:
    1. It sets up the basic UI with the classes from the tkinter module such as Canvas, Tk and Button.after
    2. It allows to interact with the user through the correct and wrong buttons.
    3. It does all the logic work and minimize score.
    """
    def __init__(self,question_bank):
        self.score=0
        self.tot=0
        self.ques_set=question_bank
        self.Q=None;    self.A=None;    self.var=None
        self.sz=(40,40)
        
        self.win=Tk()
        self.win.title("Quiz Game")
        self.win.config(bg=THEME_COLOR)
        self.win.minsize(500,500)

        
        self.lb=Canvas(width=200,height=100,bg=THEME_COLOR,highlightthickness=0)
        self.scr=self.lb.create_text(70,40,text=f"Score={self.score}/{self.tot}",font=("arial",20,"normal"))
        self.lb.place(x=240,y=15)

        self.cn=Canvas(width=400,height=250,)
        self.new=self.cn.create_text(200,120,width=360,text="You will see the\n question written here.",font=("arial",20,"italic"))
        self.cn.place(x=50,y=90)

        self.img1=PhotoImage(file="images\\true.png")
        self.img2=PhotoImage(file="images\\false.png")

        self.bt1=Button(image=self.img1,padx=20,pady=20,borderwidth=5,command=self.option_correct)
        self.bt1.place(x=50,y=370)

        self.bt2=Button(image=self.img2,padx=20,pady=20,borderwidth=5,command=self.option_wrong)
        self.bt2.place(x=350,y=370)
        self.ask_question(self.ques_set)

        self.win.mainloop()
        
    def ask_question(self,qus):
        """It asks the next question from the user when the user pressed the right or wrong button."""

        if self.tot<10:
            self.lt=qus[self.tot]
            self.Q=html.unescape(s=self.lt.text);    self.A=html.unescape(s=self.lt.answer)
            self.tot+=1
            self.cn.itemconfig(self.new,text=f"Q.{self.tot}: {self.Q}")
        else:
            self.win.destroy()
            
    def option_correct(self):
        """It occurs when the button with right tick mark is pressed."""
        self.var="True"
        self.check(self.var)

    def option_wrong(self):
        """It occurs when the button with wrong click is pressed."""
        self.var="False"
        self.check(self.var)

    def check(self,chc:str):
        """It checks whether the answer choosen by the user is correct or not."""
        if (self.A)==chc:
            self.right()
        else:
            self.wrong()

    def right(self):
        """It works when the answer given by user is correct."""
        self.score+=1
        print(self.score)
        self.lb.itemconfig(self.scr,text=f"Score: {self.score}/{self.tot}")
        self.ask_question(self.ques_set)
    
    def wrong(self):
        """It works when the answer given by the user is incorrect."""
        print(self.score)
        self.lb.itemconfig(self.scr,text=f"Score: {self.score}/{self.tot}")
        self.ask_question(self.ques_set)