import tkinter as tk
from tkinter import ttk

#creation of main window
window = tk.Tk()
window.title('Conversion App')
window.geometry('300x300')

#adding components
HeadingLabel = ttk.Label(master = window, text='Miles to kilometers', font = 'Helvetica 24')
HeadingLabel.pack()

#displaying of window
window.mainloop()