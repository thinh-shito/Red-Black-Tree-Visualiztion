from tkinter import *
from tkinter import Canvas

root = Tk()
root.title("red black tree")
window_width = 1500
window_height = 900

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# root.geometry("1500x1000+50+50")
root.resizable(0, 0)


def split_string():
    ar_split = insertion_textbox.get().split(',')
    insertion_textbox.delete(0, END)
    print(ar_split[1])
    return ar_split


# add insert button
insert_button = Button(root, text="Insert", command=split_string)
insert_button.grid(column=1, row=0, padx=3, pady=3)

insertion_textbox = Entry(root)
insertion_textbox.grid(column=0, row=0, padx=3, pady=3)

# add delete button
delete_button = Button(root, text="Delete", command=split_string)
delete_button.grid(column=1, row=1, padx=3, pady=5)

delete_textbox = Entry(root)
delete_textbox.grid(column=0, row=1, padx=3, pady=5)

# add find button
find_button = Button(root, text="Find")
find_button.grid(column=1, row=2, padx=3, pady=5)

find_textbox = Entry(root)
find_textbox.grid(column=0, row=2, padx=3, pady=5)

checkbox1 = Checkbutton(root,
                        text='pre order',
                        onvalue='agree',
                        offvalue='disagree')
checkbox1.place(x=20, y=110)
checkbox2 = Checkbutton(root,
                        text='post order',
                        onvalue='agree',
                        offvalue='disagree')
checkbox2.place(x=20, y=150)
checkbox3 = Checkbutton(root,
                        text='in order',
                        onvalue='agree',
                        offvalue='disagree')
checkbox3.place(x=20, y=190)

# add find button
print_button = Button(root, text="Print").place(x=120, y=150)

quit_button = Button(root, text="Quit", command=root.destroy).place(y=860, x=10)

c = Canvas(root, width=1180, height=890, bg='white').place(x=310, y=0)
root.mainloop()
