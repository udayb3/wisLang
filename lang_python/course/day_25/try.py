"""
#The read_csv returns data frame- learn more about this. 
data=pnd.read_csv("day_25\\weather_data.csv")
#to_list function converts the series from a data frame into a list
list=data["temp"].to_list()
#Now we can simply calculate the average of the temperatures
avg=0;  ln=len(list)
for i in range(ln):
  avg+=list[i]
avg/=ln
print(avg)

#Alternative function to find the mean of all the values.
avg2=data.temp.mean()
print(avg2)

#Function to find the maximum value in the given series
max=data.temp.max()
print(max)

#Get data in columns
print(data.condition)

#Get data in the form of rows
print(data[data.temp==data.temp.max()])
#Getting data from a particular column of a certain row 
monday=data[data.day=="Monday"]
print((9*monday["temp"])/5+32)

#Creating data_frame from scratch
data_dict={
  "students":["aman","babloo","chetan","dj"],
  "marks":[12,23,34,45]
}
data1= pnd.DataFrame(data_dict)

#Converting the data frame to other formats
data.to_csv("new_data.csv")
"""