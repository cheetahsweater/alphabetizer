import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

window = tk.Tk() 
window.title("The Ana Alphabetizer")

def openfile(): #Prompts user to open file if open button pressed
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("ALL FILES!!!", "*.*")]
        )
    if not filepath:
        return
    textedit.delete("1.0", tk.END) #Deletes text to replace with opened file
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read() #Gathers text of opened file
        textedit.insert(tk.END, text) #Inserts text of opened file
    window.title(f"The Ana Alphabetizer - {os.path.basename(filepath)}") #Changes window name to reflect opened file

def savefile(): #Prompts user to save file if save button pressed
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("ALL FILES!!!", "*.*")])
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = textedit.get("1.0", tk.END)
        output_file.write(text) #Gathers text from text field and writes to file
    window.title(f"The Ana Alphabetizer - {os.path.basename(filepath)}") #Changes window name to reflect saved file

def getfirstword(s): #Gets the first word of each line for alphabetization
    coolstring = str.casefold(s) #Allows alphabetization to ignore case
    words = coolstring.split(maxsplit=1) #Split lines by word
    if len(words)>0:
        return words[0] #Returns first word if there are multiple
    return ""

def sorting(text): #Actual alphabetizing
    lines = text.splitlines() #Splits text into lines and assigns to var as a list
    sortedlines = sorted(lines,key = getfirstword) #Sorts these lines via getfirstword and assigns to var as a list
    textedit.delete("1.0", tk.END) #Deletes the text from text edit field
    for line in sortedlines:
       textedit.insert(tk.END, f"{line}\n") #Inserts newly sorted text, with each line followed by a line break

def alphabetize(): #Function to alphabetize when alphabetize button pressed
    text = textedit.get("1.0", tk.END) #Gathers text from text edit field to sort
    getfirstword(text)
    sorting(text)
 
    #UI stuff
window.rowconfigure(0, minsize=500, weight=1) 
window.columnconfigure(1, minsize=500, weight=1)
textedit = tk.Text(window)
frame = tk.Frame(window, relief=tk.RAISED, bd=2)
openbutton = tk.Button(frame, text="Open", command=openfile)
alphabutton = tk.Button(frame, text="Alphabetize", command=alphabetize)
savebutton = tk.Button(frame, text="Save As...", command=savefile)


openbutton.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
alphabutton.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
savebutton.grid(row=2, column=0, sticky="ew", padx=5)
frame.grid(row=0, column=0, sticky="ns")
textedit.grid(row=0, column=1, sticky="nsew")

window.mainloop()


