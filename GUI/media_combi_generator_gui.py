import os
import tkinter as tk
import tkinter.messagebox as tkMessageBox

def create_widget(widget_type, text, row, column, padx=5, pady=5):
    widget = widget_type(root, text=text)
    widget.grid(row=row, column=column, padx=padx, pady=pady)
    return widget

def create_episodes():
    global num_episodes
    if not name_entry.get() or not season_entry.get() or not num_episodes_entry.get():
        tk.messagebox.showwarning("Warnung", "Bitte füllen Sie alle Felder aus.")
        return

    try:
        num_episodes = int(num_episodes_entry.get())
    except ValueError:
        tk.messagebox.showwarning("Warnung", "Verwende eine Zahl für Episoden Anzahl.")
        return

    for i in range(num_episodes):
        # create label and entry for episode name
        create_widget(tk.Label, f"Name der Episode {i+1}:", i+5, 0)
        episode_entry = create_widget(tk.Entry, "", i+5, 1)
        episode_entries.append(episode_entry)

    # create button to create files
    create_files_button = create_widget(tk.Button, "Dateien erstellen", num_episodes+5, 1, 2)
    create_files_button.config(command=create_files)

def create_files():
    if not name_entry.get() or not season_entry.get() or not quali_entry.get() or not episode_entries:
        tk.messagebox.showwarning("Warnung", "Füllen alle Felder aus.")
        return

    name = name_entry.get().replace(" ", ".")
    try:
        season = int(season_entry.get())
    except ValueError:
        tk.messagebox.showwarning("Warnung", "Verwende eine Zahl für Season.")
        return
    quali = quali_entry.get().replace(" ", ".")
    year = year_entry.get()
    episodes = len(episode_entries)
    episode_names = [episode_entry.get() for episode_entry in episode_entries]

    # Erste Variante
    output_str_1 = ""
    for i in range(episodes):
        episode_str = episode_names[i].replace(" ", ".")
        output_str_1 += "{}.S{:02d}E{:02d}.{}.{}\n".format(name.replace(" ", "."), season, i+1, episode_str, quali.replace(" ", "."))

    # Zweite Variante
    output_str_2 = ""
    for i in range(episodes):
        episode_str = episode_names[i]
        episode_num = str(i+1)
        season_num = str(int(season))
        output_str_2 += "{}: Season {} ({}): Episode {} - {}\n".format(name_entry.get(), season_num, year, episode_num, episode_str)

    # Verzeichnisse erstellen
   # base_dir = "/<pfad>/<zum>/<ausgabepfad>" # Optional der gewünschte Ausgabepfad
   # name_year_dir = os.path.join(base_dir, f"{name_entry.get()} ({year_entry.get()})") # Ersetze durch die untere angabe: name_year_dir
    name_year_dir = os.path.join( f"{name_entry.get()} ({year_entry.get()})")
    season_dir = os.path.join(name_year_dir, f"Staffel {season_entry.get()}")
    if not os.path.exists(season_dir):
        os.makedirs(season_dir)

    # Ausgabe in Datei schreiben
    output_file = os.path.join(season_dir, f"{name.replace(' ', '.')}.S{season:02}.txt")
    with open(output_file, "w") as f:
        f.write(output_str_1)
        f.write("\n")
        f.write(output_str_2)

def reset_form():
    global episode_entries, num_episodes
    episode_entries = []
    num_episodes = 0
    name_entry.delete(0, tk.END)
    season_entry.delete(0, tk.END)
    quali_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    num_episodes_entry.delete(0, tk.END)
    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) >= 5 and widget != reset_button:
            widget.grid_forget()

# create main window
root = tk.Tk()
root.title("Media Generator GUI")

# create widgets
name_label = create_widget(tk.Label, "Name der Serie:", 0, 0)
name_entry = create_widget(tk.Entry, "", 0, 1)
season_label = create_widget(tk.Label, "Season:", 1, 0)
season_entry = create_widget(tk.Entry, "", 1, 1)
quali_label = create_widget(tk.Label, "Qualität:", 2, 0)
quali_entry = create_widget(tk.Entry, "", 2, 1)
year_label = create_widget(tk.Label, "Jahr:", 3, 0)
year_entry = create_widget(tk.Entry, "", 3, 1)
num_episodes_label = create_widget(tk.Label, "Anzahl der Episoden:", 4, 0)
num_episodes_entry = create_widget(tk.Entry, "", 4, 1)
create_episodes_button = create_widget(tk.Button, "Episoden erstellen", 4, 2)
create_episodes_button.config(command=create_episodes)

#initialize variables
episode_entries = []
num_episodes = 0

#create reset button
reset_button = create_widget(tk.Button, "Zurücksetzen", num_episodes+5, 2, pady=10)
reset_button.config(command=reset_form)

root.mainloop()