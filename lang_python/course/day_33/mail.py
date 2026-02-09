import smtplib as sm


def snd_mail():
	"""		It will send the mail for the required subject."""
	my_email="zenetro4@gmail.com";  rec="vasubhardwaj.2008@gmail.com";    my_ps="ieqhavmtqdbsebdd"

	with sm.SMTP() as con:
		con.starttls()
		con.login(user="my_email",password=my_ps)
		con.sendmail(from_addr=my_email,to_addrs=rec,msg="watch\n\nThe international space station is directly above you, You can go and watch it.")
