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

# List of all possible games involved in direct conversions
all_games = list({game for pair in conversion_rates.keys() for game in pair})

# Helper function to check if a conversion exists directly or via CSGO
def find_conversion_path(source, target):
    if source == target:
        return 1.0

    if (source, target) in conversion_rates:
        return conversion_rates[(source, target)]
    elif (target, source) in conversion_rates:
        return 1 / conversion_rates[(target, source)]
    else:
        if (source, "CSGO") in conversion_rates and ("CSGO", target) in conversion_rates:
            rate_to_csgo = conversion_rates[(source, "CSGO")]
            rate_to_target = conversion_rates[("CSGO", target)]
            return rate_to_csgo * rate_to_target
        elif ("CSGO", source) in conversion_rates and ("CSGO", target) in conversion_rates:
            rate_to_csgo = 1 / conversion_rates[("CSGO", source)]
            rate_to_target = conversion_rates[("CSGO", target)]
            return rate_to_csgo * rate_to_target

    return None

def convert_sensitivity():
    try:
        source_game = source_game_var.get()
        target_game = target_game_var.get()
        sensitivity = float(sensitivity_entry.get())

        conversion_rate = find_conversion_path(source_game, target_game)

        if conversion_rate is not None:
            converted_sensitivity = sensitivity * conversion_rate
            result_label.config(text=f"Converted Sensitivity: {converted_sensitivity:.4f}")
        else:
            result_label.config(text="Conversion not available for selected games.")
    except ValueError:
        result_label.config(text="Please enter a valid number for sensitivity.")

# GUI setup
root = tk.Tk()
root.title("Game Sensitivity Converter")
root.geometry("400x300")  # Set window size
root.resizable(False, False)

# Apply a modern theme
style = ttk.Style(root)
style.theme_use("clam")

# Configure colors
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 10), background="#0078D7", foreground="white")
style.configure("TCombobox", font=("Arial", 10))

# Title
title_label = ttk.Label(root, text="Game Sensitivity Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Source game dropdown
source_frame = ttk.Frame(root)
source_frame.pack(pady=5, padx=10, fill="x")
source_game_label = ttk.Label(source_frame, text="Source Game:")
source_game_label.pack(side="left", padx=5)
source_game_var = tk.StringVar()
source_game_dropdown = ttk.Combobox(source_frame, textvariable=source_game_var, state="readonly")
source_game_dropdown['values'] = all_games
source_game_dropdown.pack(side="right", fill="x", expand=True)

# Target game dropdown
target_frame = ttk.Frame(root)
target_frame.pack(pady=5, padx=10, fill="x")
target_game_label = ttk.Label(target_frame, text="Target Game:")
target_game_label.pack(side="left", padx=5)
target_game_var = tk.StringVar()
target_game_dropdown = ttk.Combobox(target_frame, textvariable=target_game_var, state="readonly")
target_game_dropdown['values'] = all_games
target_game_dropdown.pack(side="right", fill="x", expand=True)

# Sensitivity input
sensitivity_frame = ttk.Frame(root)
sensitivity_frame.pack(pady=5, padx=10, fill="x")
sensitivity_label = ttk.Label(sensitivity_frame, text="Sensitivity:")
sensitivity_label.pack(side="left", padx=5)
sensitivity_entry = ttk.Entry(sensitivity_frame)
sensitivity_entry.pack(side="right", fill="x", expand=True)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_sensitivity)
convert_button.pack(pady=10)

# Result label
result_label = ttk.Label(root, text="Converted Sensitivity will appear here.", anchor="center")
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
