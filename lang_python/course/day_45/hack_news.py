from bs4 import BeautifulSoup as bs
import requests as rq

#	Getting the HTML file of a site
res=rq.get(url="https://news.ycombinator.com/")
pg=res.text

#		Parsing the html file.
soup=bs(pg,"html.parser")

# 	Making two list of all the headingsand the link for the articles.
spn=soup.find_all("span",class_="titleline");	ln=len(spn)
line_a=[ ( spn[i].find('a') ) for i in range(ln)	]
heading=[ line_a[i].text for i in range(ln)	]
link=[	line_a[i].get('href')	for i in range(ln) ]

# 	Making a list containing the list of number of votes
u_vote=soup.find_all("span",class_="score")
alnk=[ int(	(	(u_vote[i].text).split(' ')	)[0]	) for i in range(ln)	]

max=0;	pos=-1
for i in range(ln):
	if max>alnk[i]:
		max=i;	pos=i

print(	f"The topic with the maximum number of upvotes({alnk[pos]} points) is {heading[i]}."	)