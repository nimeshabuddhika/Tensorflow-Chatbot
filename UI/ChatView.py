import tkinter  as tk
import pygubu
import datetime
from Bot import ChatBot as bot


class Application:

    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('chat_window.ui')
        self.mainWindow = builder.get_object('mainwindow', master)

        self.etMessage = builder.get_object('etMessage', master)
        self.etMessage.grid(sticky='nsew')

        self.textArea = builder.get_object('taDisplay', master)
        self.textArea.config(font=("consolas", 12), undo=True, wrap='word')

        self.master.bind("<Return>", self.showContents)

        self.scrollBar = builder.get_object('sbDisplay', master)
        self.scrollBar.grid(sticky='nsew')
        self.textArea['yscrollcommand'] = self.scrollBar.set
        self.chatBot = bot.ChatBot.getBot()
        builder.connect_callbacks(self)

    def sendMessage(self):
        message = self.etMessage.get()
        date = "[" + datetime.datetime.now().strftime("%H:%M:%S") + "] "
        self.textArea.insert(tk.END, date + message + "\n")
        self.textArea.insert(tk.END, date + self.chatBot.response(message) + "\n\n")
        self.textArea.see(tk.END)
        self.etMessage.delete(0, tk.END)

    def onSend(self):
        self.sendMessage()

    def showContents(self, event):
        self.sendMessage()


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
