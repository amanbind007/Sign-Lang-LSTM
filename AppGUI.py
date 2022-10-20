

#create tkinter app for sign language recognition
import tkinter as tk
#from tkinter import Tk
import os
from main import function2




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Sign Language Recognition")
        self.geometry("400x200")
        img = tk.Image('photo', file='icon.gif')
        self.call('wm','iconphoto', self._w, img)
        #self.tk.call('wm','iconphoto',root._w,img)
        self._frame = None
        self.switch_frame(StartPage)

        

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.label = tk.Label(self, text="Sign Language Recognition")
        self.label.pack(pady=10, padx=10)
        
        self.button1 = tk.Button(self, text="Start", command = function2)
        #=function2())
        self.button1.pack()
        self.button2 = tk.Button(self, text="Quit", command=self.quit)
        self.button2.pack()

        #start openCV capture window when start button is clicked
        #self.button1.bind("<Button-1>", self.startCapture)


    



if __name__ == "__main__":
    app = App()
    app.mainloop()