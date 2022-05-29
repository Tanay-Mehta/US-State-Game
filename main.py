from turtle import Turtle, Screen
import pandas

turtle = Turtle()
writer = Turtle()
writer.hideturtle()
writer.penup()

screen = Screen()
screen.setup(800, 500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states_data = pandas.read_csv("50_states.csv")
x_cor = all_states_data["x"]
y_cor = all_states_data["y"]
states = all_states_data["state"]
state = states.to_list()

total = []
life = 3
answered = 0
game_is_on = True
while game_is_on:

    user_guess = screen.textinput(f"{answered}/50", "guess a state").lower()
    answered += 1
    if life == 1:
        print(f"you loose\n you got {answered-1} correct")
        game_is_on = False

    elif user_guess in state:
        state_user = (all_states_data[all_states_data.state == user_guess])
        state_ycor = int((all_states_data[all_states_data.state == user_guess]).y)
        state_xcor = int((all_states_data[all_states_data.state == user_guess]).x)
        writer.goto(state_xcor, state_ycor)
        writer.write(f"{user_guess}", False, "center", ('Arial', 8, 'normal'))
        total.append(user_guess)

    else:
        life -= 1
        answered -= 1
        print(f"wrong answer\nyou lost a life you have {life} remaining")


for i in total:
    state.remove(i)
pandas.DataFrame(state).to_csv("new_states_to_learn.csv")


