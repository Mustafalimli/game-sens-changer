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

# List of all games
all_games = list({game for pair in conversion_rates.keys() for game in pair})

# Helper function to calculate conversion
def convert_sensitivity(source, target, sensitivity):
    if source == target:
        return sensitivity
    if (source, target) in conversion_rates:
        return sensitivity * conversion_rates[(source, target)]
    if (target, source) in conversion_rates:
        return sensitivity / conversion_rates[(target, source)]
    return None

# Update sensitivities of all sliders
def update_all_sensitivities(selected_game, sensitivity):
    for game, widgets in sliders.items():
        if game != selected_game:
            converted_sensitivity = convert_sensitivity(selected_game, game, sensitivity)
            if converted_sensitivity is not None:
                sliders[game]["slider"].set(converted_sensitivity)
                sliders[game]["entry"].delete(0, tk.END)
                sliders[game]["entry"].insert(0, f"{converted_sensitivity:.2f}")

# Update sensitivity based on slider
def update_sensitivity_from_slider(game, value):
    sensitivity = float(value)
    sliders[game]["entry"].delete(0, tk.END)
    sliders[game]["entry"].insert(0, f"{sensitivity:.2f}")
    update_all_sensitivities(game, sensitivity)

# Update sensitivity based on entry
def update_sensitivity_from_entry(game):
    try:
        sensitivity = float(sliders[game]["entry"].get())
        sliders[game]["slider"].set(sensitivity)
        update_all_sensitivities(game, sensitivity)
    except ValueError:
        pass

# GUI setup
root = tk.Tk()
root.title("Game Sensitivity Converter")
root.geometry("600x600")

# Dropdown to select game
selected_game_var = tk.StringVar()
selected_game_var.set(all_games[0])
tk.Label(root, text="Selected Game:").pack(pady=10)
selected_game_menu = ttk.Combobox(root, textvariable=selected_game_var, values=all_games, state="readonly")
selected_game_menu.pack()

# Frame for sliders and entries
slider_frame = tk.Frame(root)
slider_frame.pack(pady=20)

sliders = {}

# Create sliders and entries for all games
for game in all_games:
    frame = tk.Frame(slider_frame)
    frame.pack(fill="x", pady=5)

    tk.Label(frame, text=game, width=20, anchor="w").pack(side="left")

    slider = tk.Scale(frame, from_=0.1, to=10, resolution=0.01, orient="horizontal", length=200)
    slider.pack(side="left", padx=5)

    entry = tk.Entry(frame, width=10)
    entry.pack(side="left", padx=5)

    sliders[game] = {"slider": slider, "entry": entry}

    # Link slider and entry updates
    slider.config(command=lambda value, g=game: update_sensitivity_from_slider(g, value))
    entry.bind("<Return>", lambda event, g=game: update_sensitivity_from_entry(g))

# Add a slider for the selected game to make adjustments easier
selected_game_slider_frame = tk.Frame(root)
selected_game_slider_frame.pack(pady=10)

tk.Label(selected_game_slider_frame, text="Adjust Selected Game Sensitivity:").pack(side="left")

selected_game_slider = tk.Scale(selected_game_slider_frame, from_=0.1, to=10, resolution=0.01, orient="horizontal", length=200)
selected_game_slider.pack(side="left", padx=5)

selected_game_slider.config(command=lambda value: update_sensitivity_from_slider(selected_game_var.get(), value))

# Bind selected game change to update its slider and other game sliders
def on_game_selected(event):
    selected_game = selected_game_var.get()
    current_sensitivity = sliders[selected_game]["slider"].get()
    selected_game_slider.set(current_sensitivity)
    update_all_sensitivities(selected_game, current_sensitivity)

selected_game_menu.bind("<<ComboboxSelected>>", on_game_selected)

# Initialize all sliders and entries
update_all_sensitivities(selected_game_var.get(), 1.0)

root.mainloop()
