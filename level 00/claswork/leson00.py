from turtle import *

speed(30)

#davxazot kvadrati 
width(4)
color("brown")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


#davxazot karebi 
forward(70)
color("gray")
begin_fill()
left(90)
forward(120) # karebis simagle 
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup() # kalmis ageba
goto(200, 200)
pendown() # kalmis chamoweva

# davxazot saxuravi 
color("brown")
begin_fill()# shignit gaferadeba
right(150)
forward(200)
left(120)
forward(200)
end_fill() # gaferadebis dasruleba
exitonclick()