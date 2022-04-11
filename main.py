from tkinter import *
from turtle import home

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

class ItemList():
    def __init__(self):
        self.items = []

    def __str__(self):
        s = str(self.items)
        return s

    def addItem(self, entry, label, shelf):
        item = entry.get()
        self.items.append(item)
        label.config(text=f"Items on Shelf {shelf}: {self.items}")
        entry.delete(0, END)
    
    def removeItem(self, entry, label, shelf):
        item = entry.get()
        self.items.remove(item)
        label.config(text=f"Items on Shelf {shelf}: {self.items}")
        entry.delete(0, END)

shelf_one_items = ItemList()
shelf_two_items = ItemList()
shelf_three_items = ItemList()
shelf_four_items = ItemList()
shelf_five_items = ItemList()
shelf_six_items = ItemList()

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

        button4 = Button(self, text="Shelf 4", command = lambda: controller.showFrame(Four))
        button4.grid(row=1, column=2, padx=10, pady=10)

        button5 = Button(self, text="Shelf 5", command = lambda: controller.showFrame(Five))
        button5.grid(row=2, column=2, padx=10, pady=10)

        button6 = Button(self, text="Shelf 6", command = lambda: controller.showFrame(Six))
        button6.grid(row=3, column=2, padx=10, pady=10)

class One(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        title = Label(self, text="Shelf One")
        title.grid(row=0, column=4, padx=10, pady=10)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=1, padx=10, pady=10)

        items = Label(self, text=f"Items on Shelf One: {shelf_one_items.items}")
        items.grid(row=0, column=5, padx=10, pady=10)
        items.config(shelf_one_items.items)

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)

        add = Button(self, text="ADD", command = lambda: shelf_one_items.addItem(field, items, "One"))
        add.grid(row=3, column=0, padx=10, pady=10)

        grab = Button(self, text="REMOVE", command = lambda: shelf_one_items.removeItem(field, items, "One"))
        grab.grid(row=3, column=2, padx=10, pady=10)

class Two(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title = Label(self, text="Shelf Two")
        title.grid(row=0, column=4, padx=10, pady=10)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=1, padx=10, pady=10)

        items = Label(self, text=f"Items on Shelf Two: {shelf_two_items.items}")
        items.grid(row=0, column=5, padx=10, pady=10)
        items.config(shelf_one_items.items)

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)

        add = Button(self, text="ADD", command = lambda: shelf_two_items.addItem(field, items, "Two"))
        add.grid(row=3, column=0, padx=10, pady=10)

        grab = Button(self, text="REMOVE", command = lambda: shelf_two_items.removeItem(field, items, "Two"))
        grab.grid(row=3, column=2, padx=10, pady=10)

class Three(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title = Label(self, text="Shelf Three")
        title.grid(row=0, column=4, padx=10, pady=10)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=1, padx=10, pady=10)

        items = Label(self, text=f"Items on Shelf Three: {shelf_three_items.items}")
        items.grid(row=0, column=5, padx=10, pady=10)
        items.config(shelf_one_items.items)

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)

        add = Button(self, text="ADD", command = lambda: shelf_three_items.addItem(field, items, "Three"))
        add.grid(row=3, column=0, padx=10, pady=10)

        grab = Button(self, text="REMOVE", command = lambda: shelf_three_items.removeItem(field, items, "Three"))
        grab.grid(row=3, column=2, padx=10, pady=10)

class Four(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title = Label(self, text="Shelf Four")
        title.grid(row=0, column=4, padx=10, pady=10)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=1, padx=10, pady=10)

        items = Label(self, text=f"Items on Shelf Four: {shelf_four_items.items}")
        items.grid(row=0, column=5, padx=10, pady=10)
        items.config(shelf_one_items.items)

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)

        add = Button(self, text="ADD", command = lambda: shelf_four_items.addItem(field, items, "Four"))
        add.grid(row=3, column=0, padx=10, pady=10)

        grab = Button(self, text="REMOVE", command = lambda: shelf_four_items.removeItem(field, items, "Four"))
        grab.grid(row=3, column=2, padx=10, pady=10)

class Five(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title = Label(self, text="Shelf Five")
        title.grid(row=0, column=4, padx=10, pady=10)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=1, padx=10, pady=10)

        items = Label(self, text=f"Items on Shelf Five: {shelf_five_items.items}")
        items.grid(row=0, column=5, padx=10, pady=10)
        items.config(shelf_one_items.items)

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)

        add = Button(self, text="ADD", command = lambda: shelf_five_items.addItem(field, items, "Five"))
        add.grid(row=3, column=0, padx=10, pady=10)

        grab = Button(self, text="REMOVE", command = lambda: shelf_five_items.removeItem(field, items, "Five"))
        grab.grid(row=3, column=2, padx=10, pady=10)


class Six(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title = Label(self, text="Shelf Six")
        title.grid(row=0, column=4, padx=10, pady=10)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=1, padx=10, pady=10)

        items = Label(self, text=f"Items on Shelf Six: {shelf_six_items.items}")
        items.grid(row=0, column=5, padx=10, pady=10)
        items.config(shelf_one_items.items)

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)

        add = Button(self, text="ADD", command = lambda: shelf_six_items.addItem(field, items, "Six"))
        add.grid(row=3, column=0, padx=10, pady=10)

        grab = Button(self, text="REMOVE", command = lambda: shelf_six_items.removeItem(field, items, "Six"))
        grab.grid(row=3, column=2, padx=10, pady=10)


app = ShelfApp()
app.mainloop()
# =======

# def ListCreator(listLen):
# 	newList = []
# 	for i in range(1, listLen + 1):
# 		newList.append(i)
# 	return(newList)

# listLen = 17

# print(ListCreator(listLen))

# print("hello world, bleh")

