
import requests as rq 
cat={"books": 10 ,"movies": 11,"Sports": 21,"E-Games":15, "Computers":18, "History":23}
pr={    "amount":10,    "type":"boolean", "Category": cat["movies"]}
data=rq.get(url="https://opentdb.com/api.php",params=pr)
data.raise_for_status()

ques_set=(data.json())["results"]

