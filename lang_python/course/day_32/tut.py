"""
How can we make our mail seem less like spam:
1. Write subject int the mail.


"""
"""
import smtplib as mal
my_email="";		my_ps="";		t=""

#		Entering the e-mail from which we want to send the mail.
with mal.SMTP("smtp.gmail.com") as con:

#		This encrypts all the information so that it can be secured. Always enter this line. TLS means Transport Layer security. 
	con.starttls()
	con.login(user=my_email,password=my_ps)
	con.sendmail(from_addr=my_email,to_addrs=t,msg="Subject:Hello\n\nThis E-mail was sent via python.")
"""
"""
import datetime as dt

now=dt.datetime.now()
day=now.isoweekday()
print(day)

dob=dt.datetime(year=2003,day=20,month=8,hour=12,minute=32,second=23)
print(dob)
"""
