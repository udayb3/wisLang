"""
What is to be done:
    The code will send an e-mail to my college id through my id.
    It will mention the name of the person whose birthday occurs on that day. 
    If there is a birthday of more than one person tomorrow, then it will send more mails.
Steps:
    1. Reading through the csv files in which birthday date, month and year is saved.
    2. 

"""
import csv
import datetime as dtt
import smtplib as smt

my_email="zenetro4@gmail.com";  rec="vasubhardwaj.2008@gmail.com";    my_ps="ieqhavmtqdbsebdd"

data=[];  send=[]
ln=None
dat=dtt.datetime.now();   day=dat.day;   mon=dat.month

def store_msg()->None:

  global sub,temp,mesg
  with open(file="message.txt",mode='r') as fil:
    temp=fil.readlines()
    sub=temp[0]
    mesg=temp[1]

def conv(message:str,nme:str)->str:
  new=message.replace("[name]",f"{nme}")
  return new

with open("books.csv",mode='r') as fil:
  dt=csv.reader(fil,delimiter=',')
  for row in dt:
    data.append(row)


#   

ln=len(data)
for i in range(ln-1):
  
  temp_dat=int(data[i+1][1])-1;  temp_mn=int(data[i+1][2])
  if temp_dat==day  and temp_mn==mon:
    name=data[i+1][0]
    send.append(name)

ln=len(send)
if ln>-1:
  store_msg()
  with smt.SMTP("smtp.gmail.com") as con:
    for i in range(ln):
      new_msg=conv(mesg,send[i])
      con.starttls()
      con.login(user=my_email,password=my_ps)
      con.sendmail(from_addr=my_email,to_addrs=rec,msg=f"{sub}\n\n{new_msg}")