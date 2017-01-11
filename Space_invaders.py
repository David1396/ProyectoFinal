from tkinter import *
y=750

vent = Tk()
vent.title("Space Invaders")
canvas= Canvas(vent, width=960, height=600)
canvas.pack()

i= PhotoImage(file="fondo1.png")
i1= PhotoImage(file="space1.png")

canvas.create_image(0,0,anchor=NW, image=i)
canvas.create_image(480,500,anchor=NW, image=i1)

def choque(event):
    if event.keysym == 'Left':
        canvas.move(2,-10,0)
        if y==633:
            print("Choque")
    else:
        canvas.move(2,10,0)


canvas.bind_all('<KeyPress-Left>',choque)
canvas.bind_all('<KeyPress-Right>',choque)


vent.mainloop()
