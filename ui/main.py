# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_39 = QtWidgets.QLabel(self.frame_5)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_10.addWidget(self.label_39)
        self.label_40 = QtWidgets.QLabel(self.frame_5)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_10.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.frame_5)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_10.addWidget(self.label_41)
        self.label_42 = QtWidgets.QLabel(self.frame_5)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_10.addWidget(self.label_42)
        self.horizontalLayout_9.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.name_lineedit_tab5 = QtWidgets.QLineEdit(self.frame_5)
        font = QtGui.QFont()
        font.setItalic(True)
        self.name_lineedit_tab5.setFont(font)
        self.name_lineedit_tab5.setObjectName("name_lineedit_tab5")
        self.horizontalLayout_8.addWidget(self.name_lineedit_tab5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.staffel_lineedit_tab5 = QtWidgets.QLineEdit(self.frame_5)
        font = QtGui.QFont()
        font.setItalic(True)
        self.staffel_lineedit_tab5.setFont(font)
        self.staffel_lineedit_tab5.setObjectName("staffel_lineedit_tab5")
        self.verticalLayout_11.addWidget(self.staffel_lineedit_tab5)
        self.qualitat_lineedit_tab5 = QtWidgets.QLineEdit(self.frame_5)
        font = QtGui.QFont()
        font.setItalic(True)
        self.qualitat_lineedit_tab5.setFont(font)
        self.qualitat_lineedit_tab5.setObjectName("qualitat_lineedit_tab5")
        self.verticalLayout_11.addWidget(self.qualitat_lineedit_tab5)
        self.jahr_lineedit_tab5 = QtWidgets.QLineEdit(self.frame_5)
        font = QtGui.QFont()
        font.setItalic(True)
        self.jahr_lineedit_tab5.setFont(font)
        self.jahr_lineedit_tab5.setObjectName("jahr_lineedit_tab5")
        self.verticalLayout_11.addWidget(self.jahr_lineedit_tab5)
        self.horizontalLayout_9.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_12.addWidget(self.label_4)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.neu_erstellen_button_tab5 = QtWidgets.QPushButton(self.frame_5)
        self.neu_erstellen_button_tab5.setObjectName("neu_erstellen_button_tab5")
        self.horizontalLayout_32.addWidget(self.neu_erstellen_button_tab5)
        self.erstellen_button_tab5 = QtWidgets.QPushButton(self.frame_5)
        self.erstellen_button_tab5.setObjectName("erstellen_button_tab5")
        self.horizontalLayout_32.addWidget(self.erstellen_button_tab5)
        self.offnen_button_tab5 = QtWidgets.QPushButton(self.frame_5)
        self.offnen_button_tab5.setObjectName("offnen_button_tab5")
        self.horizontalLayout_32.addWidget(self.offnen_button_tab5)
        self.exit_button_tab5 = QtWidgets.QPushButton(self.frame_5)
        self.exit_button_tab5.setObjectName("exit_button_tab5")
        self.horizontalLayout_32.addWidget(self.exit_button_tab5)
        self.verticalLayout_12.addLayout(self.horizontalLayout_32)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.text_edit_episode_name_tab5 = QtWidgets.QPlainTextEdit(self.frame_5)
        self.text_edit_episode_name_tab5.setObjectName("text_edit_episode_name_tab5")
        self.verticalLayout_8.addWidget(self.text_edit_episode_name_tab5)
        self.weitere_erstellen_button_tab5 = QtWidgets.QPushButton(self.frame_5)
        self.weitere_erstellen_button_tab5.setObjectName("weitere_erstellen_button_tab5")
        self.verticalLayout_8.addWidget(self.weitere_erstellen_button_tab5)
        self.verticalLayout_12.addLayout(self.verticalLayout_8)
        self.gridLayout_7.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 20))
        self.menubar.setObjectName("menubar")
        self.menuMen = QtWidgets.QMenu(self.menubar)
        self.menuMen.setObjectName("menuMen")
        MainWindow.setMenuBar(self.menubar)
        self.action_Erstellen_tab4 = QtWidgets.QAction(MainWindow)
        self.action_Erstellen_tab4.setObjectName("action_Erstellen_tab4")
        self.action_oeffnen_tab4 = QtWidgets.QAction(MainWindow)
        self.action_oeffnen_tab4.setObjectName("action_oeffnen_tab4")
        self.action_Weitere_Staffel_erstellen_tab4 = QtWidgets.QAction(MainWindow)
        self.action_Weitere_Staffel_erstellen_tab4.setObjectName("action_Weitere_Staffel_erstellen_tab4")
        self.action_Neue_Dateien_erstellen_tab4 = QtWidgets.QAction(MainWindow)
        self.action_Neue_Dateien_erstellen_tab4.setObjectName("action_Neue_Dateien_erstellen_tab4")
        self.action_Beenden_tab4 = QtWidgets.QAction(MainWindow)
        self.action_Beenden_tab4.setObjectName("action_Beenden_tab4")
        self.menuMen.addAction(self.action_Erstellen_tab4)
        self.menuMen.addAction(self.action_oeffnen_tab4)
        self.menuMen.addSeparator()
        self.menuMen.addAction(self.action_Weitere_Staffel_erstellen_tab4)
        self.menuMen.addAction(self.action_Neue_Dateien_erstellen_tab4)
        self.menuMen.addSeparator()
        self.menuMen.addAction(self.action_Beenden_tab4)
        self.menubar.addAction(self.menuMen.menuAction())

        self.retranslateUi(MainWindow)
        self.exit_button_tab5.clicked.connect(MainWindow.close) # type: ignore
        self.action_Beenden_tab4.triggered.connect(MainWindow.close) # type: ignore
        self.weitere_erstellen_button_tab5.clicked.connect(self.text_edit_episode_name_tab5.clear) # type: ignore
        self.weitere_erstellen_button_tab5.clicked.connect(self.staffel_lineedit_tab5.clear) # type: ignore
        self.neu_erstellen_button_tab5.clicked.connect(self.text_edit_episode_name_tab5.clear) # type: ignore
        self.neu_erstellen_button_tab5.clicked.connect(self.jahr_lineedit_tab5.clear) # type: ignore
        self.neu_erstellen_button_tab5.clicked.connect(self.qualitat_lineedit_tab5.clear) # type: ignore
        self.neu_erstellen_button_tab5.clicked.connect(self.staffel_lineedit_tab5.clear) # type: ignore
        self.neu_erstellen_button_tab5.clicked.connect(self.name_lineedit_tab5.clear) # type: ignore
        self.action_Weitere_Staffel_erstellen_tab4.triggered.connect(self.text_edit_episode_name_tab5.clear) # type: ignore
        self.action_Neue_Dateien_erstellen_tab4.triggered.connect(self.jahr_lineedit_tab5.clear) # type: ignore
        self.action_Weitere_Staffel_erstellen_tab4.triggered.connect(self.staffel_lineedit_tab5.clear) # type: ignore
        self.action_Neue_Dateien_erstellen_tab4.triggered.connect(self.staffel_lineedit_tab5.clear) # type: ignore
        self.action_Neue_Dateien_erstellen_tab4.triggered.connect(self.qualitat_lineedit_tab5.clear) # type: ignore
        self.action_Neue_Dateien_erstellen_tab4.triggered.connect(self.name_lineedit_tab5.clear) # type: ignore
        self.action_Neue_Dateien_erstellen_tab4.triggered.connect(self.text_edit_episode_name_tab5.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_39.setText(_translate("MainWindow", "Name:"))
        self.label_40.setText(_translate("MainWindow", "Staffel Nr.:"))
        self.label_41.setText(_translate("MainWindow", "Qualität:"))
        self.label_42.setText(_translate("MainWindow", "Jahr:"))
        self.name_lineedit_tab5.setPlaceholderText(_translate("MainWindow", "Name der Serie eintragen."))
        self.staffel_lineedit_tab5.setPlaceholderText(_translate("MainWindow", "Staffel Nr. der Serie eintragen."))
        self.qualitat_lineedit_tab5.setPlaceholderText(_translate("MainWindow", "Qualität der Serie eintragen."))
        self.jahr_lineedit_tab5.setPlaceholderText(_translate("MainWindow", "Jahr der Serie eintragen."))
        self.label_4.setText(_translate("MainWindow", "Optionen Auswahl:"))
        self.neu_erstellen_button_tab5.setToolTip(_translate("MainWindow", "Zurücksetzen und neue Dateien erstellen."))
        self.neu_erstellen_button_tab5.setText(_translate("MainWindow", "  Neue Dateien erstellen  "))
        self.erstellen_button_tab5.setToolTip(_translate("MainWindow", "Erstellen und speichern."))
        self.erstellen_button_tab5.setText(_translate("MainWindow", "  Erstellen"))
        self.offnen_button_tab5.setToolTip(_translate("MainWindow", "Ordner mit erstellten Datei öffnen."))
        self.offnen_button_tab5.setText(_translate("MainWindow", "  Öffnen"))
        self.exit_button_tab5.setToolTip(_translate("MainWindow", "Beenden."))
        self.exit_button_tab5.setText(_translate("MainWindow", "  Beenden"))
        self.label_3.setToolTip(_translate("MainWindow", "Episoden Name eintragen."))
        self.label_3.setText(_translate("MainWindow", "Episoden Name:"))
        self.weitere_erstellen_button_tab5.setToolTip(_translate("MainWindow", "Weitere Staffel erstellen."))
        self.weitere_erstellen_button_tab5.setText(_translate("MainWindow", "  Weitere Staffel erstellen"))
        self.menuMen.setTitle(_translate("MainWindow", "Menü"))
        self.action_Erstellen_tab4.setText(_translate("MainWindow", "Erstellen"))
        self.action_oeffnen_tab4.setText(_translate("MainWindow", "Öffnen"))
        self.action_Weitere_Staffel_erstellen_tab4.setText(_translate("MainWindow", "Weitere Staffel erstellen"))
        self.action_Neue_Dateien_erstellen_tab4.setText(_translate("MainWindow", "Neue Dateien erstellen"))
        self.action_Beenden_tab4.setText(_translate("MainWindow", "Beenden"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
