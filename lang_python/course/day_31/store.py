import pandas as pd

global copy

def copy_s()->None:
  dat=pd.read_csv("data\\french_words.csv")
  copy=dat
  t=dat.to_csv("data\\temp_storage.csv")

def work()->list:
  data=pd.read_csv("data\\temp_storage.csv")
  copy=data
  lt_fr=data["French"].to_list()
  lt_en=data["English"].to_list()
  dt=[]
  for i in range(len(lt_fr)):
    dt.append({lt_fr[i]:lt_en[i]})
  return dt

def clear(words_wrong:dict)->None:
  with open(file="data\\temp_storage.csv",mode="w") as fil:
    pass
  new_data=pd.DataFrame(words_wrong)
  l=new_data.to_csv("data\\temp_storage.csv")