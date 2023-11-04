import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title="Choose color my G")
    if color[1]:
        print(color)
        text_area.config(fg=color[1])


def change_font(event=None):
    text_area.config(font=(font_name.get(), size_box.get()))


def new_file():
    window.title("Name de bsdk")
    text_area.delete(1.0, END)


def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)
        with open(file, "r") as file_handle:
            text_area.insert(1.0, file_handle.read())
    except Exception as e:
        print(f"Eita txt file laage?: {e}")


def save_file():
    file=filedialog.asksaveasfilename(initialfile="Namede.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file=open(file,"w")

            file.write(text_area.get(1.0,END))

        except Exception:
            print("Save korini,bhar me ja")

        finally:
            file.close()

def copy():
    text_area.event_generate("<<Copy>>")


def cut():
    text_area.event_generate("<<Cut>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About this dumb thing", "Made by Rishi(isse accha CA3 keliye parleta)")


def quit():
    window.destroy()


window = Tk()
window.title("Text Editor")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Comic Sans")

font_size = StringVar(window)
font_size.set("20")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()
color_button = Button(frame, text="Color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()
