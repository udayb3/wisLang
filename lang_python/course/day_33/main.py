import requests
from datetime import datetime
import mail as rq

def set_prop(hour:int , min:int)->list:
  """	It sets the time according to the IST."""
  hour+=5
  if hour>=24:
    hour%=24
# Now we will check for the minute
  if min>=30:
    min=(min+30)%60
    if hour==23:
      hour=0
    else:
      hour+=1
  else:
    min=min+30
  temp=min/60
  ans=float(hour)+min
  return ans


#	The latitudes and longitudes 
MY_LAT = 27.209193 # Your latitude
MY_LONG = 78.015236 # Your longitude

#	Basic procedure for getting the data as a dictionary
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

#	Taking out the current location of international space station as latitudes and longitudes
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
dif_lt=MY_LAT-iss_latitude;	dif_lng=MY_LONG-iss_longitude
che=0

if (dif_lt<5 and dif_lt>-5) and (dif_lng<5 and dif_lng>-5):
  che=1

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

#		Getting the time for sunrise and sunset 
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sr = ((data["results"]["sunrise"].split("T")[1]).split("+"))[0].split(":")[0];		st = (data["results"]["sunset"].split("T")[1]).split("+")[0].split(":")[0]

#		Taking out minutes and hour and converting it to the Indian time.
sur=set_prop( int(sr[0]) , int(sr[1]) );	sut=set_prop( int(st[0]) , int(st[1]) )

#		Finding the current time and taking out the hours and minutes. 
dt=datetime.now()
new=( ( (str(dt)).split(".")[0] ).split(" ")[1] ).split(":")
cur_hr=int(new[0]);	cur_mn=int(new[1]) 

ngt=sur-cur_hr;		mor=cur_hr-sut
if (ngt<=0.5 and ngt>=0) or (mor<=0.5 and ngt>=0):
  rq.snd_mail()
