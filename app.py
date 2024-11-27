import tkinter as tk
from tkinter import ttk

# Oyunlar arasındaki dönüşüm oranları
def conversion_rates():
    return {
        "csgo_to_rainbow_six": 7.67 / 2,  
        "csgo_to_apex": 2 / 2,          
        "csgo_to_insurgency": 0.314 / 2,
        "csgo_to_overwatch2": 6.667 / 2, 
        "csgo_to_payday2": 2.933 / 2,    
        "csgo_to_squad": 0.251 / 2,     
        "csgo_to_titanfall2": 2 / 2,    
        "csgo_to_escape_tarkov": 0.352 / 2,  
        "csgo_to_dying_light2": 5.280 / 2,  
        "csgo_to_battlefield1": 9.00 / 2,    
        "csgo_to_battlefield_2042": 9.00 / 2, 
        "csgo_to_battlefield4": 9.00 / 2,    
        "csgo_to_battlefield3": 9.00 / 2,    
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

# Arayüz
root = tk.Tk()
root.title("Game Sensitivity Converter")

# Kaynak oyun seçimi
tk.Label(root, text="Source Game:").grid(row=0, column=0, padx=10, pady=10)
source_game_var = tk.StringVar()
source_game_dropdown = ttk.Combobox(root, textvariable=source_game_var)
source_game_dropdown['values'] = list(set([key[0] for key in conversion_rates.keys()]))
source_game_dropdown.grid(row=0, column=1, padx=10, pady=10)

# Hedef oyun seçimi
tk.Label(root, text="Target Game:").grid(row=1, column=0, padx=10, pady=10)
target_game_var = tk.StringVar()
target_game_dropdown = ttk.Combobox(root, textvariable=target_game_var)
target_game_dropdown['values'] = list(set([key[1] for key in conversion_rates.keys()]))
target_game_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Hassasiyet girişi
tk.Label(root, text="Sensitivity:").grid(row=2, column=0, padx=10, pady=10)
sensitivity_entry = tk.Entry(root)
sensitivity_entry.grid(row=2, column=1, padx=10, pady=10)

# Dönüştür düğmesi
convert_button = tk.Button(root, text="Convert", command=convert_sensitivity)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Sonuç etiketi
result_label = tk.Label(root, text="Converted Sensitivity will appear here.")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()