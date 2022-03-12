from tkinter import *

root = Tk()

root.title("red black tree")
root.geometry("1500x1000")
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

# add find button
print_button = Button(root, text="Print").grid(column=0, row=3)

quit_button = Button(root, text="Quit", command=root.destroy).grid(column=0, row=4, padx=5)

root.mainloop()
