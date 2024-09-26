import tkinter as tk
from tkinter import ttk

from get_vars import get_vars
from embed import embed

window = tk.Tk()
window.title('Report generator')
window.geometry('1600x500')
window_width, window_height = 1600, 500
window.minsize(window_width, window_height)

visibility_panel = tk.Frame(window, bg='red')
substitution_panel = tk.Frame(window, bg='green')
editor_panel = tk.Frame(window, bg='black')
output_panel = tk.Frame(window, bg='blue')

visibility_panel_height = 30
visibility_panel.place(x=0, y=0, relwidth=1, height=visibility_panel_height)

def resize_event(height, show_substitution_panel=True, show_editor_panel=True, show_output_panel=True):
    global visibility_panel_height
    substitution_panel.place_forget()
    editor_panel.place_forget()
    output_panel.place_forget()
    count = 0
    count += show_substitution_panel
    count += show_editor_panel
    count += show_output_panel
    if count == 0:
        count, show_substitution_panel = 1, True
    panel_rel_width = 1 / count
    next_rel_x = 0
    if show_substitution_panel:
        substitution_panel.place(x=0, y=visibility_panel_height, relwidth=panel_rel_width, height=height-visibility_panel_height)
        next_rel_x = panel_rel_width
    if show_editor_panel:
        editor_panel.place(relx=next_rel_x, y=visibility_panel_height, relwidth=panel_rel_width, height=height-visibility_panel_height)
        next_rel_x = next_rel_x + panel_rel_width
    if show_output_panel:
        output_panel.place(relx=next_rel_x, y=visibility_panel_height, relwidth=panel_rel_width, height=height-visibility_panel_height)

def resize(event):
    global window_width, window_height, window_widget
    if window_widget == None and event.width == 500 and event.height == 500:
        window_widget = event.widget
    if event.widget == window_widget and (window_width != event.width or window_height != event.height):
        window_width, window_height = event.width,event.height
        print(f"The width of Toplevel is {window_width} and the height of Toplevel "
              f"is {window_height}")
        resize_event(window_height)

window_widget = None

window.bind("<Configure>", resize)

resize_event(window_height)
resize_event(window_height+100)

index=0
for key, value in get_vars().items():
    embed( substitution_panel, index, key, value)
    index += 1




window.mainloop()

