"""Simple Miles to Km (and vice versa) converter GUI."""

import tkinter


def convert_to_Km():
    Km_entry.delete(0,tkinter.END)
    Km_entry.insert(0,f'{float(miles_entry.get())*1.61}')

def convert_to_miles():
    miles_entry.delete(0,tkinter.END)
    miles_entry.insert(0,f'{float(Km_entry.get())/1.61}')


# Make a window object
window = tkinter.Tk()

# Personalise
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# Labels - instance of the Label class

miles_label = tkinter.Label(window, text="Miles", font=("Ariel", 24))
miles_label.grid(row=1, column=3)

Km_label = tkinter.Label(window, text="Km", font=("Ariel", 24))
Km_label.grid(row=2, column=3)

# Buttons

toKm_button = tkinter.Button(window, text='Convert to Km', command=convert_to_Km)
toKm_button.grid(row=1, column=5)

toMiles_button = tkinter.Button(window, text='Convert to Miles', command=convert_to_miles)
toMiles_button.grid(row=2, column=5)

# Entry window(s)
miles_entry = tkinter.Entry(window)
miles_entry.grid(row=1, column=1)

Km_entry = tkinter.Entry(window)
Km_entry.grid(row=2, column=1)

# Needed to keep window open
window.mainloop()

