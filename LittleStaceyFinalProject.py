# Final Project: Drug Information Cheatsheet
# Stacey Little
# SDEV140-10P
# Program prompts the user for a drug name and retrieves information to display

import tkinter as tk
from tkinter import *


# main function to search the data sheet for user input drug
def main():
    # take the user entry from window box and use that for drug search
    drug_input = drug.get()
    # using upper helps find word matches regardless of case user enters
    global drug_search
    drug_search = drug_input.upper()

    # uses user input to display the drug being searched
    print()
    print("Thank you. Here is information regarding " + drug_search + ":")
    print()

    # import csv with drug information
    import csv

    # display and format the spacing of the search results header
    with open("LittleStaceyFinalProjectdata.csv", 'r') as reader:
        header_data = [(reader.readlines()[0])]
        for row in header_data:
            global header
            header = (row[0:].strip().split(","))
            print("{: <30} {: <25} {: <15}".format(*header))


    # find the user entered drug in csv file and locate information in that row
    with open("LittleStaceyFinalProjectdata.csv", 'r') as reader:
        for row in reader.readlines()[1:]:
            columns = row.strip().split(",")

    # search for drug entered in first column (generic name)
            if drug_search in columns[0]:
                global search1
                search1 = (row.strip().split(","))
                print("{: <30} {: <25} {: <15}".format(*search1))
                print('------------------------------------------------------------------------')
    
    # search for drug entered in second column (brand name) if not in first            
            elif drug_search in columns[1]:
                global search2
                search2 = (row.strip().split(","))
                print("{: <30} {: <25} {: <15}".format(*search2))
                print('------------------------------------------------------------------------')   

# window created for second window      
class Window(tk.Toplevel):
    def search_results(self):
        global t1
        t1 = Label(self, text="Thank you. Here is information regarding " + drug_search + ":" + "\n" + "{: <30} {: <25} {: <15}".format(*header) + "\n").grid(row=3,column=0,columnspan=4)
        try:
            search1
            global t2
            t2 = Label(self, text="{: <30} {: <25} {: <15}".format(*search1)).grid(row=4,column=0,columnspan=4)

            
        except:
            global t3
            t3 = Label(self, text="{: <30} {: <25} {: <15}".format(*search2)).grid(row=4,column=0,columnspan=4)
            

    def __init__(self, parent):
        super().__init__(parent)
# format window
        self.configure(background="pink")      
        self.geometry('400x220')
        self.title('Drug Input')

        global image2
        image2 = tk.PhotoImage(file="pill2.gif")
        tk.Label(self, image=image2).grid(row=0,column=0,columnspan=3,pady=5)
        my_text2 = Label(self, text="Enter a drug name below", font="Times 12 bold").grid(row=1,column=0,columnspan=2,padx=100)
        drug_text = Label(self, text="Drug: ").grid(row=2,column=0)

        global drug
        drug = Entry(self)

        drug.grid(row=2,column=0,columnspan=2,padx=50)
        but4 = Button(self, text="Restart", command=self.destroy).grid(row=2,column=1)
        but3 = Button(self, text="Search", command=lambda:[main(),Window.search_results(self)]).grid(row=3,column=0,columnspan=2)
    







# window created for the main (parent) window
class App(tk.Tk):
    def __init__(self):
        super().__init__()
# format window to look nicer
        self.configure(background="pink")
        self.geometry('430x300')
# give window a title and some basic text to welcome the user
        global image
        image = tk.PhotoImage(file="pill1.gif")
        self.title('Top 100 Drugs Cheatsheet')
        tk.Label(self, image=image).grid(row=0,column=0)
        my_text1 = Label(self, text="Welcome to my program!", font="Times 16 bold").grid(row=1,column=0,padx=60,pady=15)
        my_text2 = Label(self, text="We're here for all your drug information needs.").grid(row=2,column=0,padx=60,pady=15)
        my_instruction = Label(self, text="To begin, please click 'Open Drug Input' below." + "\n" + "To exit the program, please click 'close'", font="Arial 10 bold").grid(row=2,column=0,padx=60,pady=15)
# button to open the drug search tool
        but1 = Button(self, text='Open Drug Input', command=self.open_window).grid(row=3,column=0, pady = 15)
        close_but = Button(self, text="Close", command=self.destroy).grid(row=4, column=0)
        
    def open_window(self):
        window = Window(self)
        window.grab_set()

# run the program
if __name__ == "__main__":
    app = App()
    app.mainloop()
