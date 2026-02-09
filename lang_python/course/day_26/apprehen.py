"""
List Comprehension is where we can create a new list from a previously existing list.
We can also add if statements.

list=[1,2,3]
new_list=[n+1 for n in list]
print(new_list)

name=["aman","mayank","ajay","naruto"]
new_name=[wrd.title() for wrd in name]
print(new_name)

list=[i for i in range(5)]
print(list)

list=["carol","dave","aryan","chetan","buck"]
new_list=[name for name in list if len(name)>4]
print(new_list)
"""
import pandas as pnd

std={
    "student":["mac","lyo","reo"],
    "marks":[56,34,45]
}
#for (key,value) in std.items():
#  print(value)
dt=pnd.DataFrame(std)

#looping through  a data frame 
# iterrows() is a function which iterates through all thee rows of the DataFrame
for (index,rows) in dt.iterrows():
    if rows.student=="mac":
        print(rows)