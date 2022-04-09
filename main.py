from tkinter import *

class ShelfApp(Tk):
    def __init__(self, *args, **kwargs):
        # inherit from parent class
        Tk.__init__(self, *args, **kwargs)

        # create a container
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # initialize frames
        self.frames = {}

        # iterate through the different frames
        for F in (Home, One, Two, Three, Four, Five, Six):
            frame = F(container, self)

            # add frames to the array
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        
        self.showFrame(Home)

    # display the current frame
    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Home(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text ="Home Page")
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = Button(self, text="Shelf 1", command = lambda: controller.showFrame(One))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = Button(self, text="Shelf 2", command = lambda: controller.showFrame(Two))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = Button(self, text="Shelf 3", command = lambda: controller.showFrame(Three))
        button3.grid(row=3, column=1, padx=10, pady=10)

        button4 = Button(self, text="Shaelf 4", command = lambda: controller.showFrame(Four))
        button4.grid(row=1, column=2, padx=10, pady=10)

        button5 = Button(self, text="Shelf 5", command = lambda: controller.showFrame(Five))
        button5.grid(row=2, column=2, padx=10, pady=10)

        button6 = Button(self, text="Shelf 6", command = lambda: controller.showFrame(Six))
        button6.grid(row=3, column=2, padx=10, pady=10)

class One(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Shelf One")
        label.grid(row=0, column=4, padx=10, pady=10)

        button = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        button.grid(row=1, column=1, padx=10, pady=10)

class Two(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Shelf Two")
        label.grid(row=0, column=4, padx=10, pady=10)

        button = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        button.grid(row=1, column=1, padx=10, pady=10)

class Three(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Shelf Three")
        label.grid(row=0, column=4, padx=10, pady=10)

        button = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        button.grid(row=1, column=1, padx=10, pady=10)

class Four(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Shelf Four")
        label.grid(row=0, column=4, padx=10, pady=10)

        button = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        button.grid(row=1, column=1, padx=10, pady=10)

class Five(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Shelf Five")
        label.grid(row=0, column=4, padx=10, pady=10)

        button = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        button.grid(row=1, column=1, padx=10, pady=10)

class Six(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Shelf Six")
        label.grid(row=0, column=4, padx=10, pady=10)

        button = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        button.grid(row=1, column=1, padx=10, pady=10)

app = ShelfApp()
app.mainloop()