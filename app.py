import tkinter as tk
from tkinter import ttk

# Oyunlar arasındaki dönüşüm oranları
conversion_rates = {
    ("CSGO", "Valorant"): 0.3145,  # Örnek oran
    ("Valorant", "CSGO"): 3.1818, # Tersi dönüşüm
    # Daha fazla oyun eklenebilir
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
