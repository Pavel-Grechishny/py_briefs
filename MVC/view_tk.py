"""
View (MVC): графическое представление.
"""

from tkinter import Tk, Frame, Label, RAISED, LEFT
from screeninfo import get_monitors

# Size and margin screen
monitor = get_monitors()[0]
columns, rows = 16, 9
sm_width = round(monitor.width / columns) * (columns - 2)
sm_heigth = round(monitor.height / rows) * (rows - 2)
margin_left = (monitor.width - sm_width) // 2
margin_top = (monitor.height - sm_heigth) // 3



# Main window
root = Tk()
root.title('Model View Controller')
root.config(bg='#0f0c4d')
root.geometry(f'{sm_width}x{sm_heigth}+{margin_left}+{margin_top}')
root.resizable(False, False)
# root.attributes("-fullscreen", True)

#mainframe
mainframe = Frame(root)  
# mainframe.padx=10
# mainframe.pady=10
mainframe.config(bg='#0c9c4d')
mainframe.pack()





label_2 = Label(mainframe) 
label_2.text='LABEL_2\nother_text'
label_2.pack()

label_3 = Label(
    mainframe, 
    text='LABEL_3\nother_text',
    bg='#9d0c5d',
    fg='white',
    font=('Hack', 9),
    padx=30,
    pady=15,
    width=25,
    height=5,
    bd=10,
    highlightbackground="white", 
    highlightthickness=1,
).pack()





root.mainloop()