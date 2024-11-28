import tkinter as tk
from tkinter import ttk

conversion_rates = {
    ("CSGO", "Rainbow Six"): 7.67 / 2,
    ("CSGO", "Apex"): 2 / 2,
    ("CSGO", "Insurgency Sandstorm"): 0.314 / 2,
    ("CSGO", "Overwatch 2"): 6.667 / 2,
    ("CSGO", "Payday 2"): 2.933 / 2,
    ("CSGO", "Squad"): 0.251 / 2,
    ("CSGO", "Titanfall 2"): 2 / 2,
    ("CSGO", "Escape from Tarkov"): 0.352 / 2,
    ("CSGO", "Dying Light 2"): 5.280 / 2,
    ("CSGO", "Battlefield 1"): 9.00 / 2,
    ("CSGO", "Battlefield 2042"): 9.00 / 2,
    ("CSGO", "Battlefield 4"): 9.00 / 2,
    ("CSGO", "Battlefield 3"): 9.00 / 2,
}

def convert_sensitivity():
    try:
        source_game = source_game_var.get()
        target_game = target_game_var.get()
        sensitivity = float(sensitivity_entry.get())
        
        if (source_game, target_game) in conversion_rates:
            conversion_rate = conversion_rates[(source_game, target_game)]
            converted_sensitivity = sensitivity * conversion_rate
            result_label.config(text=f"Converted Sensitivity: {converted_sensitivity:.4f}")
        else:
            result_label.config(text="Conversion not available for selected games.")
    except ValueError:
        result_label.config(text="Please enter a valid number for sensitivity.")


root = tk.Tk()
root.title("Game Sensitivity Converter")
#source game
source_game_label = ttk.Label(root, text="Source Game:")
source_game_label.pack()
source_game_var = tk.StringVar(value="CSGO")
source_game_menu = ttk.OptionMenu(root, source_game_var, "CSGO", "CSGO")
source_game_menu.pack()

# desired game
target_game_label = ttk.Label(root, text="Target Game:")
target_game_label.pack()
target_game_var = tk.StringVar(value="Rainbow Six")
target_game_menu = ttk.OptionMenu(
    root, 
    target_game_var, 
    "Rainbow Six Siege", 
    "Apex", 
    "Insurgency Sandstorm", 
    "Overwatch 2", 
    "Payday 2", 
    "Squad", 
    "Titanfall 2", 
    "Escape from Tarkov", 
    "Dying Light 2", 
    "Battlefield 1", 
    "Battlefield 2042", 
    "Battlefield 4", 
    "Battlefield 3"
)
target_game_menu.pack()

# sens entry
sensitivity_label = ttk.Label(root, text="Current Sensitivity:")
sensitivity_label.pack()
sensitivity_entry = ttk.Entry(root)
sensitivity_entry.pack()

# convert button
convert_button = ttk.Button(root, text="Convert", command=convert_sensitivity)
convert_button.pack()

# final results
result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
