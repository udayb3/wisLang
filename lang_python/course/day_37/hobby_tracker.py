import requests as rq
import datetime as dt

tok=""
user=""

#	Step 1: It creates the user id and set a token for them.

pixela_ep=""
par_pix={
    "token":tok,
    "username":user,    
		"agreeTermsOfService":"yes",
    "notMinor":"yes",
  }

#res=rq.post(url="https://pixe.la/v1/users",json=par_pix)
#print(res.text)

gr_ep=f"{pixela_ep}/{user}/graphs"

#	Step 2: It creates the graph in the website.

tok_cr="grp1"
par_pix_cre={
    "id":tok_cr,
    "name":"Daily Hobby Checker",
    "unit":"commit",
    "type":"int",
		"color":"sora"
}
hdrs={
    "X-USER-TOKEN": tok
}

#	Posting the 
#res2=rq.post(url=gr_ep,json=par_pix_cre,headers=hdrs)
#print(res2.text)

#	STEP 3: Here we post the picture of the graph 

link_gr=f"{gr_ep}/{tok_cr}"

tod_date=(str(dt.datetime.now()).split(" ")[0]).replace("-","")
info={
    "date":tod_date,
    "quantity":"9"
}


res3=rq.post(url=link_gr,json=info,headers=hdrs)
print(res3.text)