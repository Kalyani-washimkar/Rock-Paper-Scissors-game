from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('Rock Paper Scissor')
root.geometry("800x650")
c = Canvas(root, bg='pink', width=800, height=650)
c.grid(row=0, column=0)

l1 = Label(root, text='Player', font=('Algerian',25))
l2 = Label(root, text='Computer', font=('Algerian',25))
l3 = Label(root, text='vs', font=('Algerian',50))

l1.place(x=80, y=20)
l2.place(x=560, y=20)
l3.place(x=360, y=230)

default = Image.open("default.png")
default = default.resize((300,300))

default_flip = default.transpose(Image.FLIP_LEFT_RIGHT)

default = ImageTk.PhotoImage(default)
default_flip = ImageTk.PhotoImage(default_flip)

rock = Image.open("rock.png")
rock = rock.resize((300,300))

rock_flip = rock.transpose(Image.FLIP_LEFT_RIGHT)

rock = ImageTk.PhotoImage(rock)
rock_flip = ImageTk.PhotoImage(rock_flip)

paper = Image.open("paper.png")
paper = paper.resize((300,300))

paper_flip = paper.transpose(Image.FLIP_LEFT_RIGHT)

paper = ImageTk.PhotoImage(paper)
paper_flip = ImageTk.PhotoImage(paper_flip)

scissor = Image.open("scissor.png")
scissor = scissor.resize((300,300))

scissor_flip = scissor.transpose(Image.FLIP_LEFT_RIGHT)

scissor = ImageTk.PhotoImage(scissor)
scissor_flip = ImageTk.PhotoImage(scissor_flip)

select = Image.open("select.png")
select = select.resize((300, 130))
select = ImageTk.PhotoImage(select)

c.create_image(0, 100, anchor=NW, image=default)
c.create_image(500, 100, anchor=NW, image=default_flip)
c.create_image(0, 400, anchor=NW, image=select)
c.create_image(500, 400, anchor=NW, image=select)

def play(player):
    options = ['rock', 'paper', 'scissor']
    computer = random.choice(options)

    # for player
    if player == 'rock':
        c.create_image(0, 100, anchor=NW, image=rock)
    elif player == 'paper':
        c.create_image(0, 100, anchor=NW, image=paper)
    else:
        c.create_image(0, 100, anchor=NW, image=scissor)

    # for computer
    if computer == 'rock':
        c.create_image(500, 100, anchor=NW, image=rock)
    elif computer == 'paper':
        c.create_image(500, 100, anchor=NW, image=paper)
    else:
        c.create_image(500, 100, anchor=NW, image=scissor)

    # case of draw
    if player == computer:
        result = 'Draw'

    # case of players win
    elif (player == 'rock' and computer == 'scissor') or (player == 'paper' and computer == 'rock') or(player == 'scissor' and computer == 'paper'):
        result = 'You won'

    # case of computers win
    else:
        result = 'Computer won'

    c.create_text(390, 600, text='Result:- ' + result,fill="black", font=('Algerian', 25), tag='result')


def clear():
    # Removes result from canvas
    c.delete('result')

    # Puts default image on canvas
    c.create_image(0, 100, anchor=NW, image=default)
    c.create_image(500, 100, anchor=NW, image=default_flip)

# Button for selecting rock
rock_b = Button(root, text='Rock', command=lambda: play('rock'))
rock_b.place(x=35, y=487)

# Button for selecting paper
paper_b = Button(root, text='Paper', command=lambda: play('paper'))
paper_b.place(x=128, y=487)

# Button for selecting scissor
scissor_b = Button(root, text='Scissor', command=lambda: play('scissor'))
scissor_b.place(x=220, y=487)

# Button for clear
clear_b = Button(root, text='CLEAR', font=('Times',15, 'bold'),width=10, command=clear).place(x=340, y=28)

root.mainloop()