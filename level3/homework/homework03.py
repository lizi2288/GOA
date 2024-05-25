from turtle import *

#მდელო
speed(9999)
penup()
begin_fill()
color("dark green")
goto(-1000,-200)
pendown()
forward(2000)
right(90)
forward(300)
right(90)
forward(2000)
right(90)
forward(300)
end_fill()

#მარცხენა კოშკი
penup()
color("brown")
goto(-400, -350)
pendown()
left(295)
begin_fill()
circle(200,-50)
left(115)
forward(560)
right(90)
forward(172)
right(90)
forward(560)
penup()
end_fill()

#მარცხენა კოშკის ფანჯრები.
color("yellow")
goto(-460, 150)
pendown()
left(295)
begin_fill()
left(310)
left(115)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
penup()
end_fill()
goto(-460, -40)
pendown()
left(115)
begin_fill()
color("yellow")
left(310)
left(115)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
right(90)
forward(40)
end_fill()
penup()

#მარჯვენა კოშკი
penup()
color("brown")
goto(300, -350)
pendown()
left(25)
begin_fill()
circle(200,-50)
left(115)
forward(560)
right(90)
forward(172)
right(90)
forward(560)
penup()
end_fill()
 
 #მარჯვენა კოშკის ფანჯრები
penup()
color("yellow")
goto(240, 150)
pendown()
left(295)
begin_fill()
left(310)
left(115)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
penup()
end_fill()
goto(240, -40)
pendown()
left(115)
begin_fill()
color("yellow")
left(310)
left(115)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
right(90)
forward(40)
end_fill()
penup()

#გალავანი
begin_fill()
color("red")
goto(-398,-30)
pendown()
forward(530)
right(90)
forward(280)
right(90)
forward(530)
right(90)
forward(280)
penup()
end_fill()

#კარები
color("peru")
goto(-398,-355)
begin_fill()
forward(50)
right(90)
forward(170)
right(90)
forward(40)
left (90)
pendown()
begin_fill()
forward(220)
left(90)
forward(200)
left(90)
forward(220)
left(90)
forward(200)
end_fill()
penup()
begin_fill()
color("peru")
goto(-145,-345)
pendown()
left(180)
forward(90)
right(170)
circle(30,-200)
right(170)
forward(90)
right(90)
forward(60)
end_fill()
penup()

#ორნამენტები
goto(-145,-345)
color("khaki")
right(90)
forward(200)
left(90)
forward(83)
right(90)
pendown()
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(225)
end_fill()
penup()

#მარცხენა ორნამენტები
goto(-420,210)
forward(172)
pendown()
right(90)
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(225)
end_fill()
penup()

#მარჯვენა ორნამენტები
goto(275,210)
forward(172)
pendown()
right(90)
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(225)
end_fill()
penup()

#მესამე კოშკი.
goto(140,-30)
pendown()
begin_fill()
color("brown")
forward(155)
right(90)
forward(200)
left(90)
forward(210)
left(90)
forward(200)
left(90)
forward(210)
end_fill()

#ძირითადი კოშკის ფანჯრები
penup()
color("yellow")
left(90)
goto(-140, 60)
pendown()
left(295)
begin_fill()
left(310)
left(115)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
penup()
end_fill()


#ძირითადი კოშკის ორნამენტები
goto(130,12)
pendown()
color("darkkhaki")
begin_fill()
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(53)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(53)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(53)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(53)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(53)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(53)
left(90)
forward(30)
right(90)
forward(30)
left(90)
forward(42)
left(90)
forward(530)
left(90)
forward(42)
end_fill()
penup()

#ძირითადი კოშკის სახურავი
goto(180,170)
left(90)
forward(160)
right(30)
pendown()
begin_fill()
forward(160)
left(60)
forward(160)
right(210.)
forward(280)
end_fill()


#დროშა
width(3)
penup()
goto(-120,249)
left(90)
pendown()
begin_fill()
color("red")
forward(110)
right(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
penup()
color("green")
width(5)
goto(-112,310)
pendown()
right(90)
forward(40)
right(90)
forward(20)
left(90)
right(180)
forward(8)
left(180)
forward(8)
left(90)
forward(20)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(15)
left(90)
forward(5)
penup()
goto(-85,310)

# G
pendown()
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)
penup()

# O
goto(-57,310)
pendown()
right(110)
forward(43)
right(140)
forward(45)

# A
penup()
goto(-35,320)
pendown()
right(110)
forward(15)
penup()
goto(1000,1000)

exitonclick()



























































































































































































































































































































































































































































































