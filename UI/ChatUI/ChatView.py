import Tkinter as tk
import pygubu
import tkMessageBox

class Application:
    def __init__(self,master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('chat_window.ui')
        self.mainWindow = builder.get_object('mainwindow', master)

        self.textView = builder.get_object('Entry_1',master)
        builder.connect_callbacks(self)




    def onQuit(self):
        print(self.textView.get())


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()