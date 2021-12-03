
""" Widget for effective work-time management"""

from tkinter import *
from PIL import ImageTk, Image
import math

# ------------ Constants -------------------
Timer_mins = 25
Timer_secs = int(Timer_mins*60)
Small_break_mins = 5
Small_break_secs = int(Small_break_mins*60)
Long_break_mins = 20
Long_break_secs = int(Long_break_mins*60)

total_reps = 0
ticks = ''
timer = None

# ------------ Timer Mechanisms -------------------
def start_timer():
    """ Start counting down timer depending on whether it is break or work time, adding a tick when work session complete """
    
    global total_reps, ticks
    
    if total_reps%2 ==0:
        count_down(Timer_secs)
        canvas.itemconfig(label_text, text='Timer', font=('Ariel', 50), fill='black')
    elif total_reps%7 ==0:
        count_down(Long_break_secs)
        canvas.itemconfig(tick_text, text=ticks + '✅')
        canvas.itemconfig(label_text, text='Set Complete, Break Time!', font=('Ariel', 50), fill='black')
    elif total_reps%2 ==1:
        count_down(Small_break_secs)
        ticks += '✅'
        canvas.itemconfig(tick_text, text=ticks)
        canvas.itemconfig(label_text, text='Break Time!', font=('Ariel', 50), fill='black')


def count_down(count):
    """ Create visual of the time left as well as count down in seconds """
    
    global total_reps, timer

    count_mins = math.floor(count/60)
    count_secs = count % 60

    if len(str(count_secs)) == 1:
        count_secs = '0' + str(count_secs)

    canvas.itemconfig(timer_text, text=f'{count_mins}:{count_secs}')
    if count > 0:
        timer = win.after(1000, count_down, count-1)
    else:
        total_reps += 1
        start_timer()


def reset_timer():
    """ Cancel the timer, reset the ticks and timer back to start """
    
    global total_reps, ticks, timer

    win.after_cancel(timer)

    ticks = ''
    total_reps = 0

    canvas.itemconfig(tick_text, text=ticks)
    canvas.itemconfig(label_text, text='Timer', font=('Ariel', 50), fill='black')
    canvas.itemconfig(timer_text, text=f'{Timer_mins}:00', font=('Ariel', 50), fill='black')


# ------------ Window and canvas -------------------
win = Tk()
win.title("Effective Working Tool")


# Setting up and adding image in folder for widget
canvas = Canvas(width=909, height=1000, highlightthickness=0)
work_im = ImageTk.PhotoImage(Image.open("Study_image.jpg"))
canvas.create_image(500, 909/2, image=work_im)

# Adding some text to canvas. This is used instead of tkinter labels as the tkinter backgrounds wont dissapear.
timer_text = canvas.create_text(500, 709/2, text=f'{Timer_mins}:00', font=('Ariel', 40), fill='black')
label_text = canvas.create_text(500, 609/2, text='Timer', font=('Ariel', 50), fill='black')
tick_text = canvas.create_text(500, 809/2, text=ticks)

# Use grid() instead of pack() so the buttons etc. can be placed exactly.
canvas.grid(column=2, row=1)


# Buttons
start_button = Button(text='Start', command=start_timer, highlightthickness=0, anchor='center')
#start_button.pack()
start_button.place(x=300, y=550)

reset_button = Button(text='Reset', command=reset_timer, highlightthickness=0, anchor='center')
#reset_button.pack()
reset_button.place(x=650, y=555)



win.mainloop()
