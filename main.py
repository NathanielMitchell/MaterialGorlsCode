from tkinter import *
from turtle import home
import pickle

# grab the barcodes from the previous section unless there are none
try:
    with open("barcodes.pickle", "rb") as f:
        barcodes = pickle.load(f)
except FileNotFoundError:
    barcodes = { }

# controls the framework and allows for switching between frames
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
        for F in (Home, One, Two, Three, Four, Five, Six, ManageBarcodes):
            frame = F(container, self)

            # add frames to the array
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        
        self.showFrame(Home)

    # display the current frame
    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# a class for creating, adding to, and removing from, the lists of items for each shelf
class ItemList():
    # initializes an empty shelf
    def __init__(self):
        self.items = []

    # method for printing the shelves
    def __str__(self):
        s = ""
        for item in self.items:
            s += item + "\n"
        return s

    # add an item to the list of items
    def addItem(self, event, entry, label):
        # pull the text from the entry field
        barcode = entry.get()
        # check to see if the item is stored in the barcodes list.
        # If not, it will simply add the item typed in to the shelf
        if (barcode in barcodes):
            item = barcodes[barcode]
        else: 
            item = entry.get()
        # append the text from the entry field or the item stored with the barcode to the list of shelf items
        self.items.append(item)
        # delete everything out of the list box to reset it
        label.delete(0, END)
        # put everything back in the list box
        for i in range(len(self.items)):
            label.insert(i + 1, self.items[i])
        # delete the text from the entry field to reset it
        entry.delete(0, END)
    
    # remove an item from the list on the shelf object
    def removeItem(self, listbox):
        # pull the text from the entry field
        item = listbox.get(listbox.curselection()[0])
        # remove the text from the list of items
        self.items.remove(item)
        # clear everything out the list box
        listbox.delete(0, END)
        # reset the list box
        for i in range(len(self.items)):
            listbox.insert(i + 1, self.items[i])

# if the pickles from previous sessions exist, 
# open them and store them as the shelf objects
try:
    with open("pickled_shelf_one.pickle", "rb") as f:
        shelf_one_items = pickle.load(f)
    with open("pickled_shelf_two.pickle", "rb") as f:
        shelf_two_items = pickle.load(f)
    with open("pickled_shelf_three.pickle", "rb") as f:
        shelf_three_items = pickle.load(f)
    with open("pickled_shelf_four.pickle", "rb") as f:
        shelf_four_items = pickle.load(f)
    with open("pickled_shelf_five.pickle", "rb") as f:
        shelf_five_items = pickle.load(f)
    with open("pickled_shelf_six.pickle", "rb") as f:
        shelf_six_items = pickle.load(f)

# if the pickles from previous sessions don't exist, 
# create new empty shelf objects 
except FileNotFoundError:
    shelf_one_items = ItemList()
    shelf_two_items = ItemList()
    shelf_three_items = ItemList()
    shelf_four_items = ItemList()
    shelf_five_items = ItemList()
    shelf_six_items = ItemList()

# class for the home page
class Home(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        # set fonts
        title_font = ("Cooper Black", 30)
        button_font = ("Century Gothic", 16, "bold")
        listbox_font = ("Century Gothic", 14)

        # create a title
        label = Label(self, text ="Home Page")
        label.grid(row=0, column=1, padx=10, pady=10)
        label.config(font=title_font)

        # create buttons to navigate to each shelf
        button1 = Button(self, text="Shelf 1", background="pink", command = lambda: controller.showFrame(One))
        button1.grid(row=1, column=0, padx=10, pady=10)
        button1.config(font=button_font)

        button2 = Button(self, text="Shelf 2", background="pink", command = lambda: controller.showFrame(Two))
        button2.grid(row=2, column=0, padx=10, pady=10)
        button2.config(font=button_font)

        button3 = Button(self, text="Shelf 3", background="pink", command = lambda: controller.showFrame(Three))
        button3.grid(row=1, column=1, padx=10, pady=10)
        button3.config(font=button_font)

        button4 = Button(self, text="Shelf 4", background="pink", command = lambda: controller.showFrame(Four))
        button4.grid(row=2, column=1, padx=10, pady=10)
        button4.config(font=button_font)

        button5 = Button(self, text="Shelf 5", background="pink", command = lambda: controller.showFrame(Five))
        button5.grid(row=1, column=2, padx=10, pady=10)
        button5.config(font=button_font)

        button6 = Button(self, text="Shelf 6", background="pink", command = lambda: controller.showFrame(Six))
        button6.grid(row=2, column=2, padx=10, pady=10)
        button6.config(font=button_font)

        manage_barcodes = Button(self, text="Barcode Manager", background="pink", command = lambda: controller.showFrame(ManageBarcodes))
        manage_barcodes.grid(row=3, column=1, padx=10, pady=10)
        manage_barcodes.config(font=button_font)

        # create a label in case the text in the searchable field isn't found
        # set it to empty until the search button is used
        self.not_found = Label(self, text="Search", fg="black")
        self.not_found.grid(row=4, columnspan=3, column=2, padx=10, pady=10)
        self.not_found.config(font=listbox_font)

        # create a searchable field
        self.field = Entry(self)
        self.field.grid(row=4, column=1, padx=10, pady=10)
        self.field.config(font=listbox_font)
        self.field.bind("<Return>", self.searchItems)

    # search for items in each list
    # the first list that the item is found in will be the list you're taken to
    def searchItems(self, event):
        # reset the item not found label to be empty
        self.not_found.config(text="")
        # grab the entry from the search field
        barcode = self.field.get()
        # check to see if the word is a barcode
        if (barcode in barcodes):
            word = barcodes[barcode]
             # exit if the word is quit
            if (word == "quit"):
                app.destroy()
            # check the shelf for each item and clear the field
            elif (word in shelf_one_items.items):
                self.controller.showFrame(One)
                self.field.delete(0, END)
            elif (word in shelf_two_items.items):
                self.controller.showFrame(Two)
                self.field.delete(0, END)
            elif (word in shelf_three_items.items):
                self.controller.showFrame(Three)
                self.field.delete(0, END)
            elif (word in shelf_four_items.items):
                self.controller.showFrame(Four)
                self.field.delete(0, END)
            elif (word in shelf_five_items.items):
                self.controller.showFrame(Five)
                self.field.delete(0, END)
            elif (word in shelf_six_items.items):
                self.controller.showFrame(Six)
                self.field.delete(0, END)
            else:
                self.not_found.config(text="Item not found", fg="red")
                self.field.delete(0, END)
        # if not, set the search phrase to the word input
        else:
            word = self.field.get()
            # exit if the word is quit
            if (word == "quit"):
                app.destroy()
            # check the shelf for each item and clear the field
            elif (word in shelf_one_items.items):
                self.controller.showFrame(One)
                self.field.delete(0, END)
            elif (word in shelf_two_items.items):
                self.controller.showFrame(Two)
                self.field.delete(0, END)
            elif (word in shelf_three_items.items):
                self.controller.showFrame(Three)
                self.field.delete(0, END)
            elif (word in shelf_four_items.items):
                self.controller.showFrame(Four)
                self.field.delete(0, END)
            elif (word in shelf_five_items.items):
                self.controller.showFrame(Five)
                self.field.delete(0, END)
            elif (word in shelf_six_items.items):
                self.controller.showFrame(Six)
                self.field.delete(0, END)
            else:
                self.not_found.config(text="Item not found", fg="red")
                self.field.delete(0, END)

class One(Frame):
    def __init__(self, parent, controller):
        title_font = ("Cooper Black", 30)
        button_font = ("Century Gothic", 16, "bold")
        listbox_font = ("Century Gothic", 14)
        Frame.__init__(self, parent)
        
        title = Label(self, text="Shelf One")
        title.grid(row=0, column=0, padx=10, pady=10)
        title.config(font=title_font)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=0, padx=10, pady=10)
        home.config(font=button_font)

        items_label = Label(self, text=f"Items on Shelf One: ")
        items_label.grid(row=0, column=5, padx=10, pady=10)
        items_label.config(font=button_font)

        self.items = Listbox(self)
        self.items.grid(row=1, rowspan=4, column=5, columnspan=2, padx=10, pady=10)
        for i in range(len(shelf_one_items.items)):
            self.items.insert(i + 1, shelf_one_items.items[i])
        self.items.config(font=listbox_font)

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)
        field.config(font=listbox_font)
        field.bind("<Return>", lambda event: shelf_one_items.addItem(event, field, self.items))

        # add = Button(self, text="ADD", command = lambda: shelf_one_items.addItem(field, items))
        # add.grid(row=2, column=1, padx=10, pady=10)
        # add.config(font=button_font)

        grab = Button(self, text="REMOVE", command = lambda: shelf_one_items.removeItem(self.items))
        grab.grid(row=3, column=1, padx=10, pady=10)
        grab.config(font=button_font)

        scroll = Scrollbar(self)
        scroll.grid(row=1, column=6)
        self.items.config(yscrollcommand=scroll.set)
        scroll.config(command=self.items.yview)

class Two(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title_font = ("Cooper Black", 30)
        button_font = ("Century Gothic", 16, "bold")
        listbox_font = ("Century Gothic", 14)

        title = Label(self, text="Shelf Two")
        title.grid(row=0, column=0, padx=10, pady=10)
        title.config(font=title_font)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=0, padx=10, pady=10)
        home.config(font=button_font)

        items_label = Label(self, text=f"Items on Shelf Two: ")
        items_label.grid(row=0, column=5, padx=10, pady=10)
        items_label.config(font=button_font)

        self.items = Listbox(self)
        self.items.grid(row=1, column=5, rowspan=4, columnspan=2, padx=10, pady=10)
        for i in range(len(shelf_two_items.items)):
            self.items.insert(i + 1, shelf_two_items.items[i])
        self.items.config(font=listbox_font)

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)
        field.config(font=listbox_font)
        field.bind("<Return>", lambda event: shelf_two_items.addItem(event, field, self.items))

        # add = Button(self, text="ADD", command = lambda: shelf_two_items.addItem(field, items))
        # add.grid(row=2, column=1, padx=10, pady=10)
        # add.config(font=button_font)

        grab = Button(self, text="REMOVE", command = lambda: shelf_two_items.removeItem(self.items))
        grab.grid(row=3, column=1, padx=10, pady=10)
        grab.config(font=button_font)

        scroll = Scrollbar(self)
        scroll.grid(row=1, column=6)
        self.items.config(yscrollcommand=scroll.set)
        scroll.config(command=self.items.yview)

class Three(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title_font = ("Cooper Black", 30)
        button_font = ("Century Gothic", 16, "bold")
        listbox_font = ("Century Gothic", 14)

        title = Label(self, text="Shelf Three")
        title.grid(row=0, column=0, padx=10, pady=10)
        title.config(font=title_font)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=0, padx=10, pady=10)
        home.config(font=button_font)

        items_label = Label(self, text=f"Items on Shelf Three: ")
        items_label.grid(row=0, column=5, padx=10, pady=10)
        items_label.config(font=button_font)

        self.items = Listbox(self)
        self.items.grid(row=1, column=5, rowspan=4, columnspan=2, padx=10, pady=10)
        for i in range(len(shelf_three_items.items)):
            self.items.insert(i + 1, shelf_three_items.items[i])
        self.items.config(font=listbox_font)

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)
        field.config(font=listbox_font)
        field.bind("<Return>", lambda event: shelf_three_items.addItem(event, field, self.items))

        # add = Button(self, text="ADD", command = lambda: shelf_three_items.addItem(field, items))
        # add.grid(row=2, column=1, padx=10, pady=10)
        # add.config(font=button_font)

        grab = Button(self, text="REMOVE", command = lambda: shelf_three_items.removeItem(self.items))
        grab.grid(row=3, column=1, padx=10, pady=10)
        grab.config(font=button_font)

        scroll = Scrollbar(self)
        scroll.grid(row=1, column=6)
        self.items.config(yscrollcommand=scroll.set)
        scroll.config(command=self.items.yview)

class Four(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title_font = ("Cooper Black", 30)
        button_font = ("Century Gothic", 16, "bold")
        listbox_font = ("Century Gothic", 14)

        title = Label(self, text="Shelf Four")
        title.grid(row=0, column=0, padx=10, pady=10)
        title.config(font=title_font)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=0, padx=10, pady=10)
        home.config(font=button_font)

        items_label = Label(self, text=f"Items on Shelf Four: ")
        items_label.grid(row=0, column=5, padx=10, pady=10)
        items_label.config(font=button_font)

        self.items = Listbox(self)
        self.items.grid(row=1, column=5, rowspan=4, columnspan=2, padx=10, pady=10)
        for i in range(len(shelf_four_items.items)):
            self.items.insert(i + 1, shelf_four_items.items[i])
        self.items.config(font=listbox_font)

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)
        field.config(font=listbox_font)
        field.bind("<Return>", lambda event: shelf_four_items.addItem(event, field, self.items))

        # add = Button(self, text="ADD", command = lambda: shelf_four_items.addItem(field, items))
        # add.grid(row=2, column=1, padx=10, pady=10)
        # add.config(font=button_font)

        grab = Button(self, text="REMOVE", command = lambda: shelf_four_items.removeItem(self.items))
        grab.grid(row=3, column=1, padx=10, pady=10)
        grab.config(font=button_font)

        scroll = Scrollbar(self)
        scroll.grid(row=1, column=6)
        self.items.config(yscrollcommand=scroll.set)
        scroll.config(command=self.items.yview)

class Five(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title_font = ("Cooper Black", 30)
        button_font = ("Century Gothic", 16, "bold")
        listbox_font = ("Century Gothic", 14)

        title = Label(self, text="Shelf Five")
        title.grid(row=0, column=0, padx=10, pady=10)
        title.config(font=title_font)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=0, padx=10, pady=10)
        home.config(font=button_font)

        items_label = Label(self, text=f"Items on Shelf Five: ")
        items_label.grid(row=0, column=5, padx=10, pady=10)
        items_label.config(font=button_font)

        self.items = Listbox(self)
        self.items.grid(row=1, column=5, rowspan=4, columnspan=2, padx=10, pady=10)
        for i in range(len(shelf_five_items.items)):
            self.items.insert(i + 1, shelf_five_items.items[i])
        self.items.config(font=listbox_font)

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)
        field.config(font=listbox_font)
        field.bind("<Return>", lambda event: shelf_five_items.addItem(event, field, self.items))

        # add = Button(self, text="ADD", command = lambda: shelf_five_items.addItem(field, items))
        # add.grid(row=2, column=1, padx=10, pady=10)
        # add.config(font=button_font)

        grab = Button(self, text="REMOVE", command = lambda: shelf_five_items.removeItem(self.items))
        grab.grid(row=3, column=1, padx=10, pady=10)
        grab.config(font=button_font)

        scroll = Scrollbar(self)
        scroll.grid(row=1, column=6)
        self.items.config(yscrollcommand=scroll.set)
        scroll.config(command=self.items.yview)


class Six(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title_font = ("Cooper Black", 30)
        button_font = ("Century Gothic", 16, "bold")
        listbox_font = ("Century Gothic", 14)

        title = Label(self, text="Shelf Six")
        title.grid(row=0, column=0, padx=10, pady=10)
        title.config(font=title_font)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=0, padx=10, pady=10)
        home.config(font=button_font)

        items_label = Label(self, text=f"Items on Shelf Six: ")
        items_label.grid(row=0, column=5, columnspan=2, padx=10, pady=10)
        items_label.config(font=button_font)

        self.items = Listbox(self)
        self.items.grid(row=1, column=5, rowspan=4, columnspan=2, padx=10, pady=10)
        for i in range(len(shelf_six_items.items)):
            self.items.insert(i + 1, shelf_six_items.items[i])
        self.items.config(font=listbox_font)

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)
        field.config(font=listbox_font)
        field.bind("<Return>", lambda event: shelf_six_items.addItem(event, field, self.items))

        # add = Button(self, text="ADD", command = lambda: shelf_six_items.addItem(field, items))
        # add.grid(row=2, column=1, padx=10, pady=10)
        # add.config(font=button_font)

        grab = Button(self, text="REMOVE", command = lambda: shelf_six_items.removeItem(self.items))
        grab.grid(row=3, column=1, padx=10, pady=10)
        grab.config(font=button_font)

        scroll = Scrollbar(self)
        scroll.grid(row=1, column=6)
        self.items.config(yscrollcommand=scroll.set)
        scroll.config(command=self.items.yview)

class ManageBarcodes(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title_font = ("Cooper Black", 30)
        button_font = ("Century Gothic", 16, "bold")
        listbox_font = ("Century Gothic", 14)
        self.new_item = None

        title = Label(self, text="Barcode Manager")
        title.grid(row=0, column=0, padx=10, pady=10)
        title.config(font=title_font)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=0, padx=10, pady=10)
        home.config(font=button_font)

        items_label = Label(self, text=f"Items Saved to Barcodes: ")
        items_label.grid(row=0, column=5, columnspan=2, padx=10, pady=10)
        items_label.config(font=button_font)

        items = Listbox(self)
        items.grid(row=1, column=5, rowspan=4, columnspan=2, padx=10, pady=10)
        count = 0
        for barcode in barcodes:
            items.insert(count + 1, barcodes[barcode])
            count += 1
        items.config(font=listbox_font)

        scroll = Scrollbar(self)
        scroll.grid(row=2, column=6)
        items.config(yscrollcommand=scroll.set)
        scroll.config(command=items.yview)

        self.field = Entry(self)
        self.field.grid(row=3, column=1, padx=10, pady=10)
        self.field.config(font=listbox_font)
        self.field.bind("<Return>", lambda event: self.addItem(items, self.field, event))
        self.field.grid_forget()

        self.scan = Label(self, text="Scan a barcode")
        self.scan.grid(row=2, column=1, padx=10, pady=10)
        self.scan.config(font=listbox_font)
        self.scan.grid_forget()

        # add = Button(self, text="ADD", command = lambda: self.addItem(items, field))
        # add.grid(row=3, column=1, padx=10, pady=10)
        # add.config(font=button_font)

        remove = Button(self, text="REMOVE", command = lambda: self.removeItem(items))
        remove.grid(row=5, column=2, padx=10, pady=10)
        remove.config(font=button_font)

        item_name = Entry(self)
        item_name.grid(row=3, column=0, padx=10, pady=10)
        item_name.config(font=listbox_font)
        
        name_label = Label(self, text="What would you like to name this item?")
        name_label.grid(row=2, column=0, padx=10, pady=10)
        name_label.config(font=listbox_font)
        
        button = Button(self, text="NAME", command= lambda: self.getItemName(item_name))
        button.grid(row=4, column=0, padx=10, pady=10)
        button.config(font=button_font)

        self.double_barcode = Label(self, text="")
        self.double_barcode.grid(row=5, column=0, padx=10, pady=10)
        self.double_barcode.config(font=listbox_font)

    def getItemName(self, entry):
        self.new_item = entry.get()
        self.scan.grid(row=2, column=1, padx=10, pady=10)
        self.field.grid(row=3, column=1, padx=10, pady=10)
        self.double_barcode.config(text="")
        entry.delete(0, END)
        
    def addItem(self, listbox, entry, event):
        barcode = entry.get()
        if (barcode in barcodes):
            index = listbox.get(0, "end").index(barcodes[barcode])
            listbox.selection_set(index)
            listbox.see(index)
            self.double_barcode.config(text=f"This barcode is already set as {barcodes[barcode]}.\nTry using another barcode\nor removing {barcodes[barcode]} from the list.")
        else:
            self.scan.grid_forget()
            self.field.grid_forget()
            if (self.new_item is not None):
                barcodes[barcode] = self.new_item
            listbox.delete(0, END)
            count = 0
            for barcode in barcodes:
                listbox.insert(count + 1, barcodes[barcode])
                count += 1
            self.new_item = None
        entry.delete(0, END)

    def removeItem(self, listbox):
        item = listbox.get(listbox.curselection()[0])
        keys = list(barcodes.keys())
        names = list(barcodes.values())
        index = names.index(item)
        barcode = keys[index]
        del barcodes[barcode]
        listbox.delete(0, END)
        count = 0
        for barcode in barcodes:
            listbox.insert(count + 1, barcodes[barcode])
            count += 1
        if (item in shelf_one_items.items):
            shelf_one_items.items.remove(item)
        if (item in shelf_two_items.items):
            shelf_two_items.items.remove(item)
        if (item in shelf_three_items.items):
            shelf_three_items.items.remove(item)
        if (item in shelf_four_items.items):
            shelf_four_items.items.remove(item)
        if (item in shelf_five_items.items):
            shelf_five_items.items.remove(item)
        if (item in shelf_six_items.items):
            shelf_six_items.items.remove(item)

app = ShelfApp()
app.title("The Shelfinator")
app.mainloop()
with open ("pickled_shelf_one.pickle", "wb") as f:
    pickle.dump(shelf_one_items, f)
with open ("pickled_shelf_two.pickle", "wb") as f:
    pickle.dump(shelf_two_items, f)
with open ("pickled_shelf_three.pickle", "wb") as f:
    pickle.dump(shelf_three_items, f)
with open ("pickled_shelf_four.pickle", "wb") as f:
    pickle.dump(shelf_four_items, f)
with open ("pickled_shelf_five.pickle", "wb") as f:
    pickle.dump(shelf_five_items, f)
with open ("pickled_shelf_six.pickle", "wb") as f:
    pickle.dump(shelf_six_items, f)
with open ("barcodes.pickle", "wb") as f:
    pickle.dump(barcodes, f)
# =======

