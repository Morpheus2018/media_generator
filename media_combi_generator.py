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
    quali = input("Wie ist die Qualität? ")
    year = input("Wie lautet das Jahr? ")
    episodes = None
    while episodes is None:
        try:
            episodes = int(input("Wie viele Episoden sollen erstellt werden? "))
        except ValueError:
            print("Verwende eine Zahl für 'Episoden Anzahl'")

    # Episoden-Abfragen
    episode_names = []
    for i in range(episodes):
        episode_name = input("Wie lautet der Name der Episode {}? ".format(i+1))
        episode_names.append(episode_name)

    # Erste Variante
    output_str_1 = ""
    for i in range(episodes):
        episode_str = episode_names[i].replace(" ", ".")
        output_str_1 += "{}.S{}E{:02d}.{}.{}\n".format(name.replace(" ", "."), season, i+1, episode_str, quali.replace(" ", "."))

    # Zweite Variante
    output_str_2 = ""
    for i in range(episodes):
        episode_str = episode_names[i]
        episode_num = str(i+1)
        season_num = str(int(season))
        output_str_2 += "{}: Season {} ({}): Episode {} - {}\n".format(name, season_num, year, episode_num, episode_str)

    # Verzeichnisse erstellen
   # base_dir = "/<pfad>/<zum>/<ausgabepfad>" # Optional der gewünschte Ausgabepfad
   # name_year_dir = os.path.join(base_dir, f"{name} ({year})") # Ersetze durch die untere angabe: name_year_dir
    name_year_dir = os.path.join(f"{name} ({year})")
    season_dir = os.path.join(name_year_dir, f"Staffel {season}")
    if not os.path.exists(season_dir):
        os.makedirs(season_dir)

    # Ausgabe in Datei schreiben
    output_file = os.path.join(season_dir, f"{name.replace(' ', '.')}.S{season:02}.txt")
    with open(output_file, "w") as f:
        f.write(output_str_1)
        f.write("\n")
        f.write(output_str_2)

    # Weitere Episoden erstellen?
    repeat = input("Weitere Episoden erstellen? (Ja/Nein) ")
    if repeat.lower() not in ["ja", "j", "y", "yes"]:
        break