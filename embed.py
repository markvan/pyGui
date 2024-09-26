import tkinter as tk
from tkinter import ttk

def embed(root_frame, row, label, value):

    # Create a nested frame within the root frame
    nested_frame = ttk.Frame(root_frame, padding="2")
    nested_frame.grid(column=1, sticky='ew')

    # Create and add a label to the nested frame
    label = ttk.Label(nested_frame, text=label)
    label.grid(row=0, column=1)
    # Create and add an entry widget (text field) to the nested frame
    text_field = ttk.Entry(nested_frame, width=50)
    text_field.insert(0, value)
    text_field.grid(row=0, column=2, sticky='ew')
    text_field.columnconfigure(1, weight=1)


