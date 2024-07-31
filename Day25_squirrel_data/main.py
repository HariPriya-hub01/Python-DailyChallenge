import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
fur_colour = data["Primary Fur Color"]
#print(fur_colour)
fur_colour_gray = data[data["Primary Fur Color"] == "Gray"]
fur_colour_gray_count = len(fur_colour_gray)
fur_colour_red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
fur_colour_black_count = len(data[data["Primary Fur Color"] == "Black"])
#print(fur_colour_black_count)
data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Total Count": [fur_colour_gray_count, fur_colour_red_count, fur_colour_black_count]
}

squirrel_data = pandas.DataFrame(data_dict)
print(squirrel_data)
squirrel_data.to_csv("squirrel colour data.csv")
