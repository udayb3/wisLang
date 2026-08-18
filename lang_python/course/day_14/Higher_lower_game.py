from data import data
from  art import logo1, vs1
from random import randint as rd

def cl():
  print("\n\n\n")
def info(A,B):
  print(logo1)
  print(f"\nCompare A: {A['name']}, The {A['description']} from {A['country']}.\n")
  print(vs1)
  print(f"\nAgainst B: {B['name']}, The {B['description']} from {B['country']}.\n")
  return (input("Who has more followers (Type 'A' or 'B'): ").lower())


def comp(a,b):
  if a>b:
    return 'a'
  elif a<b:
    return 'b'
  return 'c'
  


ln=len(data)
p=rd(0,ln-1)
first_a=data[p]
eof=False
score=0

while not eof:
  pos=rd(0,ln-1)
  while pos==p:
    pos=rd(0,ln-1)
  next_b=data[pos]

  ans=comp(first_a['follower_count'],next_b['follower_count'])
  choice=info(first_a,next_b)

  cl()
  
  if ans==choice:
    data.pop(p)
    first_a=next_b;
    score+=1
    if score==ln-1:
      print(f"You have won the whole game. Your score is {score}")
      eof=True
  else:
    eof=True
    print(f"Sorry, Your answer is incorrect.\n\nYour score: {score}")
  