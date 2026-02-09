"""
Step_1: We create a  dictionary in the format where key is alphabet and value is the corresponding NATO keyword for that alphabet
Step_2: We have to create a list of phoentic keywords for each of the letters in the word which user gave.
"""
import pandas as pnd
#We have converted the csv file into a dataframe and then extracted data in the form of a dictionary.
data=pnd.read_csv("day_26\\nato_phonetic_alphabet.csv")
dict={series["letter"]:{series["code"]} for (index,series)  in data.iterrows()}
print(dict)

word=input("Enter a name for which you want to get the Nato phonetic codes: ").upper()
#We print the word according to their letters
ln=len(word)
for i in range(ln):
  print(f"{word[i]}=={dict[word[i]]}",end="\n")
