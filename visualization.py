import redblacktree as rbt
from tkinter import *
from tkinter import Canvas
import time
import redblacktree as RBT
import numpy as np
from numpy import random

window_width = 1680
window_height = 1050

canvas_width = 1600
canvas_height = 970

mid_canvas_width = canvas_width // 2
mid_canvas_height = canvas_height // 2

f_b = ('Roboto', 16, 'bold')
f = ('Roboto', 16)

colors = ['black', 'red']
radius = 16

day = "day"
err = 'error'
vr = 'verify'
de = 'delete'
se = 'search'
nodes = []
forest = []
step = 0
flag = -1
rbt = RBT.RedBlackTree()
line = -1
speed = 750
p = 1

def step_to_step():
    global step
    global flag
    global forest
    global speed 
    global p
    if p:
        c.delete(ALL)
        visualize(forest[flag])
    
        if flag == len(forest) - 1:
            step = flag
            return
        flag += 1

    c.after(speed, step_to_step)

def check_input(ar):
    for i in ar:
        if int(i) > 100:
            error = "Sorry, only values between 1 and 100 can be inserted"
            c.create_text(330, 780, text=error, font=(
                'Roboto', 12), fill='red', tag=err, justify='left')
            root.after(4000, c.delete, err)
            return 1
    return 0


def insert_tree():
    # c.delete(day)
    global forest
    global rbt
    global flag
    ar_split = box.get().split(',')
    if check_input(ar_split) == 0:
        box.delete(0, END)
        flag += 1
        for i in ar_split:
            # nodes.append([f'o{i}', f'l{i}'])
            rbt.insert(int(i))
            # forest.append(rbt.get_coordinates())
            forest = rbt.get_forest()
            # print(f"{forest[-1]}")
        step_to_step()
    print(ar_split)
    # print(f"{forest}")


def delete_tree():
    global line
    c.delete(day)
    ar_split = box.get().split(',')
    box.delete(0, END)
    for i in ar_split:
        # nodes.remove([f'o{i}', f'l{i}'])
        node = rbt.searchTree(int(i))
        line += 1
        if node.item == 0:
            error = f"Node {i} is not in the tree"
            # tag = f"err{line}"
            notion.create_text(100, 20 + line * 20, text=error,
                               font=f, fill='black', tag=de, justify='left')
            notion.after(3000, notion.delete, de)
        else:
            rbt.delete_node(int(i))
            verify = f"Deleted node {i}"
            # tag = f"err{line}"
            notion.create_text(100, 20 + line * 20, text=verify,
                               font=f, fill='black', tag=de, justify='left')
            notion.after(3000, notion.delete, de)
            forest.append(rbt.get_coordinates())
            step_to_step()
    print(ar_split)


def search_tree():
    global line
    c.delete(day)
    ar_split = box.get().split(',')
    box.delete(0, END)
    for i in ar_split:
        node = rbt.searchTree(int(i))
        line += 1
        if node.item == 0:
            error = f"Node {i} is not in the tree"
            # tag = f"err{line}"
            notion.create_text(100, 20 + line * 20, text=error,
                               font=f, fill='black', tag=se, justify='left')
            notion.after(3000, notion.delete, se)
        else:
            rbt.delete_node(int(i))
            verify = f"Exist node {i}"
            # tag = f"err{line}"
            notion.create_text(100, 20 + line * 20, text=verify,
                               font=f, fill='black', tag=se, justify='left')
            notion.after(3000, notion.delete, se)
    print(ar_split)

def random_tree():
    box.delete(0,END)
    arr = np.random.randint(100,size=16)
    arr_split = ",".join(map(str, arr))
    box.insert(0, arr_split)

def empty_canvas():
    global forest
    global step
    global flag
    c.delete(ALL)
    nodes = rbt.get_list_key()
    for i in nodes:
        rbt.delete_node(i)
    forest.clear()
    forest= []
    step = 0
    flag = -1


def list_key():
    keys = ''.join(str(i) + ' ' for i in rbt.get_list_key())
    return keys

def print_tree():
    keys = list_key()
    # c.delete(tags[0])
    node = c.create_text(mid_canvas_width, canvas_height - 50,
                         text=keys, font=('Roboto', 20), fill='black', tag=day, justify='center')


def skip_back():
    global step
    global forest
    if step <= 0:
        return
    step -= 1
    c.delete(ALL)
    visualize(forest[step])


def skip_forward():
    global step
    global forest
    if step >= len(forest) - 1:
        return
    step += 1

    c.delete(ALL)
    visualize(forest[step])

def pause():
    global p
    if p:
        pause_button.config(text='Play')
    else:
        pause_button.config(text='Pause')
    p = abs(p - 1)
    

def scale_speed(value):
    global speed
    speed = int(value)
    speed_text.configure(text= f"Speed: {speed/1000}x")
    print(f"\n{speed}")


def visualize(nodes):
    for i in nodes:
        if i.side == 'l':
            create_edge(i.pos0[0] - radius + 3, i.pos0[1] + 10,
                        i.pos1[0] + radius, i.pos1[1])
        elif i.side == 'r':
            create_edge(i.pos0[0] + radius - 3, i.pos0[1] + 10,
                        i.pos1[0] - radius, i.pos1[1])
        create_node(i.pos1, i.color, f"{i.key}")

def create_node(pos, color=0, text='null'):
    x = pos[0]
    y = pos[1]
    r = radius
    coord = x - r, y - r, x + r, y + r
    o_tag = 'o' + text
    l_tag = 'l' + text
    c.create_oval(coord, fill=colors[color], outline='black', width=3, tag=o_tag)
    c.create_text(pos, text=text, font=f, fill='white',
                  justify='center', tag=l_tag)
    # nodes.append([o_tag, l_tag])


def create_edge(x0, y0, x1, y1, color='black'):
    c.create_line(x0, y0, x1, y1, fill=color, width=3)


root = Tk()
root.title("Red Black Tree Visualization")
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# create canvas

main = Frame(root, width=window_width, height=window_height, bg='#000000', highlightthickness=0)
main.pack(anchor=CENTER)
# add control 
# add skipback button
skipback = Button(main, text='Skip Back', highlightbackground='#000000',
                  highlightthickness=0, bg='#000000', fg='#ffffff', command=skip_back)
skipback.place(x=window_width // 2 - 115, y=985)

# add skipforward button
skipforward = Button(main, text='Skip Forward', highlightbackground='#000000',
                     highlightthickness=0, bg='#000000', fg='#ffffff', command=skip_forward)
skipforward.place(x=window_width // 2 + 57, y=985)

# add pause button
pause_button = Button(main, text='Pause', highlightbackground='#000000',width=5,
                     highlightthickness=0, bg='#000000', fg='#ffffff', command=pause)
pause_button.place(x=window_width // 2 - 21, y=985)

# add scale speed button
var = IntVar(None, 750)
scale = Scale( main, variable = var , bg='#000000', from_=0, to=1500, resolution=100,showvalue=0, orient=HORIZONTAL, length=200,width = 15, fg='#ffffff',command=scale_speed)
scale.place(x=100, y=990)
speed_text = Label(main, bg='#000000', fg='#ffffff')
speed_text.config(text= f"Speed: {speed/1000}x")
speed_text.place(x=310, y=990)



c = Canvas(main, width=canvas_width, height=canvas_height, bg='white')
c.pack(padx=40, pady=40, fill=BOTH, expand=True)

fr_bg = '#FEC515'

notion = Canvas(c, width=200, height=300, bg='#B1D149',
                highlightthickness=0)  # B1D149
notion.place(x=1400 - 8, y=635)

# control panel
fr = Frame(c, width=150, height=172, bg=fr_bg,highlightcolor='#000000', highlightthickness=0)
fr.place(x=8, y=715)

# add box
box = Entry(fr, font=('Robot', 16), bg='#FFCC99', fg='white',
            width=15, highlightthickness=0, borderwidth=0)
box.pack(padx=5, pady=5, expand=True, fill=BOTH)

# add randomize button
random_button = Button(fr, text="Random", command=random_tree,
                       bg=fr_bg, fg='white', highlightbackground=fr_bg)
random_button.pack(expand=True, fill=BOTH)
# add insertion button
insert_button = Button(fr, text="Insert", command=insert_tree,
                       bg=fr_bg, fg='white', highlightbackground=fr_bg)
insert_button.pack(expand=True, fill=BOTH)

# add find button
search_button = Button(fr, text="Search", command=search_tree,
                       bg=fr_bg, fg='white', highlightbackground=fr_bg)
search_button.pack(expand=True, fill=BOTH)

# add deletion button
deletion_button = Button(fr, text="Delete", command=delete_tree,
                         bg=fr_bg, fg='white', highlightbackground=fr_bg)
deletion_button.pack(expand=True, fill=BOTH)

# add  empty button
empty_button = Button(fr, text="Empty", command=empty_canvas,
                      bg=fr_bg, fg='white', highlightbackground=fr_bg)
empty_button.pack(expand=True, fill=BOTH)

# add print button
print_button = Button(fr, text="Print", command=print_tree,
                      bg=fr_bg, fg='white', highlightbackground=fr_bg)
print_button.pack(expand=True, fill=BOTH)

# add label
label = Label(fr, text="Method", bg=fr_bg,
              fg='white', highlightbackground=fr_bg)
label.pack(padx=10, expand=True, fill=BOTH)
root.mainloop()
