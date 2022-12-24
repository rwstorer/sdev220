from tkinter import *


window = Tk()


def get_data(data_entry) -> None:
    data = data_entry.get()
    print(data)


def new_window() -> None:
    window2 = Toplevel(window)
    window2.title("Second Window")
    window2.geometry("320x240")
    frm2 = Frame(window2, background='grey')
    data_entry = Entry(
        frm2,
        fg="yellow",
        bg="blue",
        width=50
    )
    data_entry.grid(column=0, row=0)
    Button(
        frm2,
        text='Get data',
        command=lambda: get_data(data_entry)
    ).grid(column=0, row=1, sticky='w')
    Button(
        frm2,
        text='Close',
        command=lambda: window2.destroy()
    ).grid(column=0, row=1, sticky='e')
    frm2.pack()


def img_btn_on_click() -> None:
    global is_down_clk
    global up_btn_png
    global down_btn_png
    if is_down_clk:
        is_down_clk = False
        img_btn.config(text=UP_BTN_TXT, image=up_btn_png)
    else:
        is_down_clk = True
        img_btn.config(text=DOWN_BTN_TXT, image=down_btn_png)


window.title('tk demo')
window.geometry('640x480')
frm = Frame(
    window,
    background='red',
    height=640,
    width=480)
frm.grid(row=0, column=0, sticky='nsew')
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
DOWN_BTN_PATH = './down_button.png'
DOWN_BTN_TXT  = 'Download'
UP_BTN_TXT    = 'Upload'
UP_BTN_PATH   = './up_button.png'
down_btn_png  = PhotoImage(file=DOWN_BTN_PATH)
up_btn_png    = PhotoImage(file=UP_BTN_PATH)
is_down_clk   = True
label_hello = Label(
    frm,
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=10,
    height=3
)
label_hello.grid(column=0, row=0, sticky='w')
img_btn = Button(
    frm,
    text=DOWN_BTN_TXT,
    image=down_btn_png,
    command=lambda: img_btn_on_click()
)
img_btn.grid(column=0, row=1)
Button(
    frm,
    text='open window',
    command=lambda: new_window()
).grid(column=0, row=2, sticky='w')
Button(
    frm,
    text='Quit',
    command=lambda: window.destroy()
).grid(column=0, row=2, sticky='e')
frm.pack(anchor='nw', ipadx=0, ipady=0, padx=0, pady=0)
mainloop()
