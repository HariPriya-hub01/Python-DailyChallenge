
'''import csv

with open("weather_data.csv") as main_file:
    data = csv.reader(main_file)
    #print(data)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temp = row[1]
            temperature.append(int(temp))
    print(temperature)
'''
import pandas


#printing out the data
#data = pandas.read_csv("weather_data.csv")
#print(data)      #prints the entire tabular column
#print(data["temp"])    #prints the temp column

#finding the data type
#print(type(data))               # DataFrame
#print(type(data["temp"]))       # series

#Converting to other forms of data
#data_dictionary = data.to_dict()       #for a dataframe
#print(data_dictionary)

#data_list = data["temp"].to_list()     #for a series
#print(data_list)

#calculating average of all the temperatures
#avg = data["temp"].mean()
#print(avg)

#max_temp = data["temp"].max()
#print(max_temp)

#Get data in columns
#print(data.condition)

#Get data in rows
#print(data[data.temp == "Tuesday"])

#finding maximum temp and printing out the row
#max = data.temp.max()
#print(data[data.temp == max])

#printing out a particular value from a row
#monday = data[data.day == "Monday"]
#print(monday.condition)

#getting hold of monday temoerature and converting to celsius
#monday = data[data.day == "Monday"]
#monday_temp = monday.temp[0]
#mon_f = monday_temp*(9/5)+32
#print(mon_f)

#creating a dataframe from scratch and adding to new csv file
data_dict = {
    "name" : ["hari", "priya", "ram"],
    "score" : [60, 95, 78]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")