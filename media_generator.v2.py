import os

while True:
    # Abfragen
    serie_name = input("Wie lautet der Name der TV-Serie? ")
    season = None
    while season is None:
        try:
            season = int(input("Welches 'Season' ist das? "))
        except ValueError:
            print("Verwende eine Zahl für 'Season'")
    year = input("Wie lautet das Jahr? ")
    episodes = None
    while episodes is None:
        try:
            episodes = int(input("Wie viele Episoden sollen erstellt werden? "))
        except ValueError:
            print("Verwende eine Zahl für 'Episoden Anzahl'")

    # Episoden-Abfragen
    episode_names = []

    if episodes > 0:
        for i in range(1, episodes+1):
            name = input(f"Wie lautet der Name der Episode {i}? ")
            episode_names.append(name)

    # Verzeichnisse erstellen
   # base_dir = "/<pfad>/<zum>/<ausgabepfad>" # Optional der gewünschte Ausgabepfad
   # name_year_dir = os.path.join(base_dir, f"{serie_name} ({year})") # Ersetze durch die untere angabe: name_year_dir
    name_year_dir = os.path.join(f"{serie_name} ({year})")
    season_dir = os.path.join(name_year_dir, f"Staffel {season}")
    if not os.path.exists(season_dir):
        os.makedirs(season_dir)

    # Ausgabe in Datei schreiben
    with open(f"{season_dir}/{serie_name.replace(' ', '.')}.S{season:02}.txt", "w") as file:
        # Schreibe jede Episode in die Datei
        for episode in range(1, episodes+1):
            # Schreibe die Details der Episode in die Datei und füge den Namen hinzu, wenn vorhanden
            episode_name = episode_names[episode-1] if episode <= len(episode_names) else ""
            file.write(f"{serie_name}: Season {season} ({year}): Episode {episode} - {episode_name}\n")

    # Weitere Episoden erstellen?
    repeat = input("Weitere Episoden erstellen? (Ja/Nein) ")
    if repeat.lower() not in ["ja", "j", "y", "yes"]:
        break