from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from ui import main

class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Media Generator")

        self.action_Erstellen_tab4.triggered.connect(self.erstellen)
        self.action_oeffnen_tab4.triggered.connect(self.ordner_offnen)
        self.action_Neue_Dateien_erstellen_tab4.triggered.connect(self.neu_erstellen)
        self.action_Weitere_Staffel_erstellen_tab4.triggered.connect(self.weitere_erstellen)

        self.erstellen_button_tab5.clicked.connect(self.erstellen)
        self.offnen_button_tab5.clicked.connect(self.ordner_offnen)
        self.neu_erstellen_button_tab5.clicked.connect(self.neu_erstellen)
        self.weitere_erstellen_button_tab5.clicked.connect(self.weitere_erstellen)
        self.season_dir = ""


    def neu_erstellen(self):
        self.erstellen_button_tab5.setEnabled(True)

    def weitere_erstellen(self):
        self.erstellen_button_tab5.setEnabled(True)

    def erstellen(self):
        name = self.name_lineedit_tab5.text().replace(" ", ".")
        try:
            staffel = int(self.staffel_lineedit_tab5.text())
        except ValueError:
            QtWidgets.QMessageBox.information(self, "Warnung", "Verwende eine Zahl für Staffel.")
            return
        qualitat = self.qualitat_lineedit_tab5.text().replace(" ", ".")
        jahr = self.jahr_lineedit_tab5.text()

        episodenamen = self.text_edit_episode_name_tab5.toPlainText().split('\n')

        # Überprüfung der Listen
        if not name or not staffel or not qualitat or not jahr or not episodenamen:
            QtWidgets.QMessageBox.information(self, "Ungültige Eingabe", "Bitte füllen Sie alle Felder aus.")
            return
        episodes = len(episodenamen)

        # Erste Variante
        output_str_1 = ""
        for i in range(episodes):
            episodename = episodenamen[i]
            episode_str = episodename.replace(" ", ".")
            output_str_1 += "{}.S{:02d}E{:02d}.{}.{}\n".format(name.replace(" ", "."), staffel, i + 1, episode_str, qualitat.replace(" ", "."))

        # Zweite Variante
        output_str_2 = ""
        for i in range(episodes):
            episodename = episodenamen[i]
            episode_str = episodename
            episode_num = str(i + 1)
            season_num = str(int(staffel))
            output_str_2 += "{}: Season {} ({}): Episode {} - {}\n".format(self.name_lineedit_tab5.text(), season_num, jahr, episode_num, episode_str)

        # Verzeichnisse erstellen
        base_dir = ""#"/<pfad>/<zum>/<öffnen>" # Optional den gewünschten Pfad ändern.
        name_year_dir = os.path.join(base_dir, f"{self.name_lineedit_tab5.text()} ({self.jahr_lineedit_tab5.text()})")
        season_dir = os.path.join(name_year_dir, f"Staffel {self.staffel_lineedit_tab5.text()}")
        if not os.path.exists(season_dir):
            os.makedirs(season_dir)
        self.season_dir = season_dir


        # Ausgabe in Datei schreiben
        output_file = os.path.join(season_dir, f"{name.replace(' ', '.')}.S{staffel:02}.txt")
        with open(output_file, "w") as f:
            f.write(output_str_1)
            f.write("\n")
            f.write(output_str_2)

        self.erstellen_button_tab5.setEnabled(False)
        QtWidgets.QMessageBox.information(self, "Erfolgreich", f"{self.name_lineedit_tab5.text()} ({self.jahr_lineedit_tab5.text()}), Staffel {self.staffel_lineedit_tab5.text()} wurden erstellt.")

    def ordner_offnen(self):
        folder_path = self.season_dir
        folder_path2 = ""#"/<pfad>/<zum>/<öffnen>" # Optional den gewünschten Pfad ändern.

        if sys.platform == 'linux':
            if os.path.exists(folder_path):
                os.system(f'xdg-open "{folder_path}"')
            elif os.path.exists(folder_path2):
                os.system(f'xdg-open "{folder_path2}"')
            else:
                QtWidgets.QMessageBox.information(self, "Hinweis", "Noch kein Ordner verfügbar")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    sys.exit(app.exec_())