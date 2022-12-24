import tkinter as tk
from tkinter import ttk

"""
This merely attempts to provide a very simple example of using tkinter inside
a class and using the place() function to put widgets in the windows.
It also demonstrates updating an image within a Button widget and retrieving
data from an Entry widget.
I did not use any ttk widgets. So, I could remove that import. But, I'll leave
it in case I change my mind later.
"""

class WindowOne(tk.Tk):
    """
    This is the root window of a tkinter demo done with classes and using the place()
    method to put widgets in precise x/y coordinates.
    Args:
        (tk.Tk): Inheriting from tk.Tk so this can become the "root" window (the app)
    """
    def __init__(self):
        super().__init__()
        self.title('Window One')
        self.geometry('640x480')        
        # Things outside of this class do not need access to these variables
        self._is_down_clk: bool  = False
        self._DOWN_BTN_PATH: str = 'down_button.png'
        self._DOWN_BTN_TXT: str  = 'Download'
        self._UP_BTN_TXT: str    = 'Upload'
        self._UP_BTN_PATH: str   = 'up_button.png'
        self._down_btn_png: tk.PhotoImage = tk.PhotoImage(file=self._DOWN_BTN_PATH)
        self._up_btn_png: tk.PhotoImage   = tk.PhotoImage(file=self._UP_BTN_PATH)
        self._hello_label: tk.Label = tk.Label(
            self,
            text="Hello, Tkinter",
            foreground="white",  # Set the text color to white
            background="black"  # Set the background color to black
        )        
        self._btn_img: tk.Button = tk.Button(self,
            text=self._DOWN_BTN_TXT,
            image=self._down_btn_png,
            command=lambda: self.img_btn_on_click())
        self._hello_label.place(x=5, y=5)
        self.update()
        self._btn_img.place(x=self._hello_label.winfo_width()+5, y=5)
        self._btn_new_window: tk.Button = tk.Button(
            self,
            text='open window',
            command=lambda: self.btn_new_window_on_click())
        self.update()
        self._btn_new_window.place(x=0, y=self._btn_img.winfo_height()+10)

    def btn_new_window_on_click(self) -> None:
        """
        Create the second window and set focus to it
        """
        new_window: WindowTwo = WindowTwo(self)
        new_window.grab_set() # force this window to the foreground

    def img_btn_on_click(self) -> None:
        """
        Respond to the img_btn "OnClick" event and demonstrate changing
        an image within the button at runtime
        """
        if self._is_down_clk:
            self._is_down_clk = False
            self._btn_img.config(text = self._UP_BTN_TXT, image = self._up_btn_png)
        else:
            self._is_down_clk = True
            self._btn_img.config(text = self._DOWN_BTN_TXT, image = self._down_btn_png)


class WindowTwo(tk.Toplevel):
    """
    This creates our second window for some data entry

    Args:
        (tk.Toplevel): We inherit from the tk.Toplevel class
    """
    def __init__(self, parent: tk.Tk):
        super().__init__(parent)
        self.title('Second Window')
        self.geometry('320x240')
        # Things outside of this class do not need access to these variables
        self._data_entry: tk.Entry = tk.Entry(self, width=50, bg='blue', fg='yellow')
        self._data_entry.place(x=0, y=0)
        self._btn_get_data: tk.Button = tk.Button(self, text='Get Data', command=lambda: self.get_data())
        self._btn_close: tk.Button = tk.Button(self, text='Close', command=lambda: self.destroy())
        self.update() # we need to inform TK to draw what it has so we can get the control measurements
        self._btn_get_data.place(x=0, y=self._data_entry.winfo_height()+5)
        self.update() # we need to inform TK to draw what it has so we can get the control measurements
        self._btn_close.place(x=self._btn_get_data.winfo_width()+10, y=self._btn_get_data.winfo_y())

    def get_data(self) -> None:
        """
        Get the data from the data_entry widget
        """
        print(self._data_entry.get())


window_one = WindowOne()
window_one.mainloop()