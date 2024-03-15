import tkinter as tk
from tkinter import ttk

def convert():
    print(entry.get())



#creation of main window
window = tk.Tk()
window.title('Conversion App')
window.geometry('800x500')

#Title and text components
HeadingLabel = ttk.Label(master = window, text='Miles to kilometers', font = 'Helvetica 24')
HeadingLabel.pack()

#Input components
input_box = ttk.Frame(master=window)
entryInt = tk.IntVar()
entry = ttk.Entry(master=input_box, textvariable= entryInt)
button = ttk.Button(master=input_box, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack()
input_box.pack(pady=10)

#Output Components
output_label = ttk.Label(master=window, text='Output', font='Helvetica 24')
output_label.pack(pady= 10)



#displaying of window
window.mainloop()