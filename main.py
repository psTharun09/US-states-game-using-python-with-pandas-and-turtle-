import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

#it is used to find the states coordinate

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
ALIGN = "center"
FONT =("Courier",15,"normal")

Data = pd.read_csv("50_states.csv")
all_states = Data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What's another state's name").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
            New_Data = pd.DataFrame(missing_states)
            New_Data.to_csv("missed_state.csv")
        break

    if answer_state in all_states :
        n += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = Data[Data.state == answer_state]
        t.goto(x=state_data.x.item(),y=state_data.y.item())
        t.write(arg=answer_state)


screen.exitonclick()




