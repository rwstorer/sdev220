import tkinter as tk
from tkinter import ttk

class WindowOne(tk.Tk):
    def __init__(self):
        super().__init__()
        # Things outside of this class do not need access to these variables
        self.__is_down_clk: bool = False
        self.__DOWN_BTN_PATH: str = 'down_button.png'
        self.__DOWN_BTN_TXT: str  = 'Download'
        self.__UP_BTN_TXT: str    = 'Upload'
        self.__UP_BTN_PATH: str   = 'up_button.png'
        self.__down_btn_png: tk.PhotoImage  = tk.PhotoImage(file=self.__DOWN_BTN_PATH)
        self.__up_btn_png: tk.PhotoImage    = tk.PhotoImage(file=self.__UP_BTN_PATH)
        self.__is_down_clk: bool = True
        self.__hello_label: tk.Label = tk.Label(
            self,
            text="Hello, Tkinter",
            foreground="white",  # Set the text color to white
            background="black"  # Set the background color to black
        )        
        self.title('Window One')
        self.geometry('640x480')
        self.__img_btn: tk.Button = tk.Button(self, text=self.__DOWN_BTN_TXT, image=self.__down_btn_png, command=lambda: self.img_btn_on_click())
        self.__hello_label.place(x=5, y=5)
        self.update()
        self.__img_btn.place(x=self.__hello_label.winfo_width()+5, y=5)
        self.__btn_new_window: tk.Button = tk.Button(self, text='open window', command=lambda: self.btn_new_window_on_click())
        self.update()
        self.__btn_new_window.place(x=0, y=self.__img_btn.winfo_height()+10)

    def btn_new_window_on_click(self) -> None:
        new_window: WindowTwo = WindowTwo(self)
        new_window.grab_set() # force this window to the foreground

    def img_btn_on_click(self) -> None:
        if self.__is_down_clk:
            self.__is_down_clk = False
            self.__img_btn.config(text=self.__UP_BTN_TXT, image=self.__up_btn_png)
        else:
            self.__is_down_clk = True
            self.__img_btn.config(text=self.__DOWN_BTN_TXT, image=self.__down_btn_png)


class WindowTwo(tk.Toplevel):
    def __init__(self, parent: tk.Tk):
        super().__init__(parent)
        self.title('Second Window')
        self.geometry('320x240')
        self.__data_entry: tk.Entry = tk.Entry(self, width=50, bg='blue', fg='yellow')
        self.__data_entry.place(x=0, y=0)
        self.update() # we need to inform allow TK to draw what it has so we can get the control measurements
        self.__btn_get_data: tk.Button = tk.Button(self, text='Get Data', command=lambda: self.get_data())
        self.__btn_get_data.place(x=0, y=self.__data_entry.winfo_height()+5)
        self.__btn_close: tk.Button = tk.Button(self, text='Close', command=lambda: self.destroy())
        self.update() # we need to inform allow TK to draw what it has so we can get the control measurements
        self.__btn_close.place(x=self.__btn_get_data.winfo_width()+10, y=self.__btn_get_data.winfo_y())

    def get_data(self) -> None:
        print(self.__data_entry.get())


window_one = WindowOne()
window_one.mainloop()