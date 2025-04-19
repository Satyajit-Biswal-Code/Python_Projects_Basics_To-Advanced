import turtle as t

t.getscreen()
for _ in range(10):  # 10 dashes
    t.forward(10)    # draw dash
    t.penup()
    t.forward(10)    # gap
    t.pendown()
t.exitonclick()