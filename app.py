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
