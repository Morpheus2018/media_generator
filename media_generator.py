import os

while True:
    # Abfragen
    name = input("Wie lautet der Name der TV-Serie? ")
    season = None
    while season is None:
        try:
            season = int(input("Welches 'Season' ist das? "))
        except ValueError:
            print("Verwende eine Zahl für 'Season'")
    quali = input("Wie ist die Qualität? ").replace(" ", ".")
    year = input("Welches Jahr? ")
    episodes = None
    while episodes is None:
        try:
            episodes = int(input("Wie viele Episoden sollen erstellt werden? "))
        except ValueError:
            print("Verwende eine Zahl für 'Episoden Anzahl'")

    # Verzeichnisse erstellen
   # base_dir = "/<pfad>/<zum>/<ausgabepfad>" # Optional der gewünschte Ausgabepfad
   # name_year_dir = os.path.join(base_dir, f"{name} ({year})") # Ersetze durch die untere angabe: name_year_dir
    name_year_dir = os.path.join(f"{name} ({year})")
    season_dir = os.path.join(name_year_dir, f"Staffel {season}")
    if not os.path.exists(season_dir):
        os.makedirs(season_dir)

    # Ausgabe in Datei schreiben
    with open(f"{season_dir}/{name.replace(' ', '.')}.S{season:02}.txt", "w") as f:
        for i in range(episodes):
            episode_name = input(f"Wie lautet der Name der Episode {i+1}? ").replace(" ", ".")
            f.write(f"{name.replace(' ', '.')}.S{season:02}E{i+1:02}.{episode_name}.{quali}\n")

    # Weitere Episoden erstellen?
    repeat = input("Weitere Episoden erstellen? (Ja/Nein) ")
    if repeat.lower() not in ["ja", "j", "y", "yes"]:
        break