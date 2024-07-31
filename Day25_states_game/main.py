import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "India_map.gif"
screen.addshape(image)
#screen.setup(height=850, width=750)
turtle.shape(image)

#creating a csv data file with sates of india
'''data_dict ={
    "states": ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagarhaveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"],
}
data = pandas.DataFrame(data_dict)
#print(data)
data.to_csv("States_of_India.csv")'''

#finding coordinates for each state
'''def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()'''

#getting input on screen
answer_state = screen.textinput(title="Guess the state", prompt= "What's the name of the state?")
print(answer_state)

#read csv file
data = pandas.read_csv("States_of_India.csv")
all_states = data.states.to_list()
print(all_states)

#check if ans is correct
guessed_states = []
while len(guessed_states) == 29:
    if answer_state in all_states:
        tim = turtle.Turtle()
        tim.color("black")
        tim.hideturtle()
        tim.penup()
        state_row = data[data.states == answer_state]
        x = int(state_row.x)
        y = int(state_row.y)
        coord = (x,y)
        tim.goto(coord)
        tim.write(answer_state)








screen.exitonclick()