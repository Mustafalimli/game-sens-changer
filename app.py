import tkinter as tk
from tkinter import ttk

# Direct conversion rates between games
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

# List of all possible games
all_games = ["CSGO", "Rainbow Six", "Apex", "Insurgency Sandstorm", 
             "Overwatch 2", "Payday 2", "Squad", "Titanfall 2", 
             "Escape from Tarkov", "Dying Light 2", "Battlefield 1", 
             "Battlefield 2042", "Battlefield 4", "Battlefield 3"]

# Helper function to check if a conversion exists directly or indirectly
def find_conversion_path(source, target):
    if (source, target) in conversion_rates:
        return conversion_rates[(source, target)]
    elif (target, source) in conversion_rates:
        return 1 / conversion_rates[(target, source)]
    else:
        # Attempt to find an indirect path using CSGO as a common hub
        for intermediate in all_games:
            if (source, intermediate) in conversion_rates and (intermediate, target) in conversion_rates:
                rate_to_intermediate = conversion_rates[(source, intermediate)]
                rate_to_target = conversion_rates[(intermediate, target)]
                return rate_to_intermediate * rate_to_target
        return None  # No conversion path found

def convert_sensitivity():
    try:
        # Retrieve selected games and sensitivity value
        source_game = source_game_var.get()
        target_game = target_game_var.get()
        sensitivity = float(sensitivity_entry.get())
        
        # Find conversion path
        conversion_rate = find_conversion_path(source_game, target_game)
        
        if conversion_rate is not None:
            converted_sensitivity = sensitivity * conversion_rate
            result_label.config(text=f"Converted Sensitivity: {converted_sensitivity:.4f}")
        else:
            result_label.config(text="Conversion not available for selected games.")
    except ValueError:
        # Handle invalid input for sensitivity
        result_label.config(text="Please enter a valid number for sensitivity.")

# GUI setup
root = tk.Tk()
root.title("Game Sensitivity Converter")

# Dropdown for source game selection
tk.Label(root, text="Source Game:").grid(row=0, column=0, padx=10, pady=10)
source_game_var = tk.StringVar()
source_game_dropdown = ttk.Combobox(root, textvariable=source_game_var)
source_game_dropdown['values'] = all_games
source_game_dropdown.grid(row=0, column=1, padx=10, pady=10)

# Dropdown for target game selection
tk.Label(root, text="Target Game:").grid(row=1, column=0, padx=10, pady=10)
target_game_var = tk.StringVar()
target_game_dropdown = ttk.Combobox(root, textvariable=target_game_var)
target_game_dropdown['values'] = all_games
target_game_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Input field for sensitivity value
tk.Label(root, text="Sensitivity:").grid(row=2, column=0, padx=10, pady=10)
sensitivity_entry = tk.Entry(root)
sensitivity_entry.grid(row=2, column=1, padx=10, pady=10)

# Button to trigger conversion
convert_button = tk.Button(root, text="Convert", command=convert_sensitivity)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display conversion results
result_label = tk.Label(root, text="Converted Sensitivity will appear here.")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
