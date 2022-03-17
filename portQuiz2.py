

from tkinter import *



class Window(Frame):    # Initialize the master widget

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):                      # Creation of init_window
        self.master.title("GUI")                # changing the title of our master widget
        self.pack(fill=BOTH, expand=1)          # allowing the widget to take the full space of the root window
        quitButton = Button(self, text="Quit", fg="red")  # creating a button instance
        quitButton.place(x=0, y=0)              # placing the button on my window


root = Tk()                 # Create root window. Can have other windows spawn from root window.
root.geometry("400x300")    # Size of the window
app = Window(root)          # Create the actual instance
root.mainloop()             # Show the window in a mainloop.