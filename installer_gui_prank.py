# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installer_gui_prank.ui',
# licensing of 'installer_gui_prank.ui' applies.
#
# Created: Thu Nov 22 17:47:44 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import winsound
import threading
import requests
import sys
import os

class Ui_InstallerWindow(object):
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def setupUi(self, InstallerWindow):
        # Sets up the main layout of the installer.
        InstallerWindow.setObjectName("InstallerWindow")
        InstallerWindow.resize(697, 518)
        InstallerWindow.setMaximumSize(697, 518)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InstallerWindow.sizePolicy().hasHeightForWidth())
        InstallerWindow.setSizePolicy(sizePolicy)
        InstallerWindow.setStyleSheet("background-color: rgb(17, 152, 255);")
        self.InstallerWidget = QtWidgets.QWidget(InstallerWindow)
        self.InstallerWidget.setObjectName("InstallerWidget")
        self.TitleText = QtWidgets.QLabel(self.InstallerWidget)
        self.TitleText.setGeometry(QtCore.QRect(170, 20, 361, 81))
        self.TitleText.setObjectName("TitleText")
        self.InstallButton = QtWidgets.QPushButton(self.InstallerWidget)
        self.InstallButton.setGeometry(QtCore.QRect(200, 210, 301, 111))
        self.InstallButton.setObjectName("InstallButton")
        self.InstallButton.clicked.connect(self.startInstaller)
        self.CreditsText = QtWidgets.QLabel(self.InstallerWidget)
        self.CreditsText.setGeometry(QtCore.QRect(560, 440, 131, 51))
        self.CreditsText.setObjectName("CreditsText")
        self.StatusText = QtWidgets.QLabel(self.InstallerWidget)
        self.StatusText.setGeometry(QtCore.QRect(240, 350, 330, 41))
        self.StatusText.setObjectName("StatusText")
        self.RickyText = QtWidgets.QLabel(self.InstallerWidget)
        self.RickyText.setGeometry(QtCore.QRect(20, 460, 181, 31))
        self.RickyText.setObjectName("RickyText")
        self.Ricky = QtWidgets.QLabel(self.InstallerWidget)
        self.Ricky.setGeometry(QtCore.QRect(30, 320, 131, 141))
        self.Ricky.setObjectName("Ricky")
        self.Tivo = QtWidgets.QLabel(self.InstallerWidget)
        self.Tivo.setGeometry(QtCore.QRect(610, 10, 71, 91))
        self.Tivo.setObjectName("Tivo")
        self.InstallLocation = QtWidgets.QLineEdit(self.InstallerWidget)
        self.InstallLocation.setGeometry(QtCore.QRect(210, 410, 241, 20))
        self.InstallLocation.setObjectName("InstallLocation")
        self.ChooseFolderButton = QtWidgets.QToolButton(self.InstallerWidget)
        self.ChooseFolderButton.setGeometry(QtCore.QRect(460, 410, 25, 19))
        self.ChooseFolderButton.setObjectName("ChooseFolderButton")
        self.ChooseFolderButton.clicked.connect(self.setFolder)
        InstallerWindow.setCentralWidget(self.InstallerWidget)
        self.InstallerStatusBar = QtWidgets.QStatusBar(InstallerWindow)
        self.InstallerStatusBar.setObjectName("InstallerStatusBar")
        InstallerWindow.setStatusBar(self.InstallerStatusBar)

        self.retranslateUi(InstallerWindow)
        QtCore.QMetaObject.connectSlotsByName(InstallerWindow)

    def startInstaller(self):
        # If the destination box was not set, display an error.
        if self.InstallLocation.text() == "":
            self.playSound(self.resource_path("error.wav"))
            self.changeStatusText("Error! Please enter your Corporate Clash folder!")
            return
        # If CorporateClash.exe does not exist, display an error.
        elif not os.path.isfile("{}\\CorporateClash.exe".format(self.InstallLocation.text())):
            self.playSound(self.resource_path("error.wav"))
            self.changeStatusText("Error! Can not find Corporate Clash game file!")
            return
        self.playSound(self.resource_path("select.wav"))
        # Start downloading if everything is good to go.
        installTread = threading.Thread(target=self.Installer) 
        installTread.start()

    def playSound(self, sound_file):
        # Play a sound file.
        sound_thread = threading.Thread(target=winsound.PlaySound, args=[sound_file, winsound.SND_NODEFAULT])
        sound_thread.start()

    def setFolder(self):
        self.InstallLocation.setText(self.getFolder())

    def getFolder(self):
        # If the default Corporate Clash install directory was found, automatically set it.
        if os.path.isdir("C:\\Program Files (x86)\\Corporate Clash"):
            location = "C:\\Program Files (x86)\\Corporate Clash"
            self.changeStatusText("Error, please enter your Corporate Clash folder!")
        else:
            location = "C:\\"
        # Bring up a dialog box to choose the game directory.
        folder = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QFileDialog(), "Select your Corporate Clash folder.", location)
        return folder
    
    def Installer(self):
        print("Test")
        self.changeStatusText("Preparing to Install...")
        json_url = requests.get("https://www.dropbox.com/s/u6mxjq6y9t143pr/InstallInfo.json?dl=1")
        json_data = json_url.json()
        install_folder = self.InstallLocation.text()
        # Create the GetKiwiEarly if it does not exist.
        if not os.path.isdir("{}\\resources\\contentpacks\\GetKiwiEarly".format(install_folder)):
            os.makedirs("{}\\resources\\contentpacks\\GetKiwiEarly".format(install_folder))
        for entry in json_data["files"]:
            url = json_data["files"][entry]
            self.changeStatusText("Downloading {}.mf...".format(entry))
            # Download and save the file in the manifest.
            phase_downloader = requests.get(url)
            with open("{}\\{}.mf".format("{}\\resources\\contentpacks\\GetKiwiEarly".format(install_folder), entry), "wb") as phase_file:
                phase_file.write(phase_downloader.content)
        self.changeStatusText("You can now make your Kiwi!")
        self.playSound(self.resource_path("finished.wav"))
        

    def changeStatusText(self, text_content):
        # Changes the status text.
        self.StatusText.setText(QtWidgets.QApplication.translate("InstallerWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">{}</span></p></body></html>".format(text_content), None, -1))

    def retranslateUi(self, InstallerWindow):
        # Sets up the inital HTML text of the installer.
        InstallerWindow.setWindowTitle(QtWidgets.QApplication.translate("InstallerWindow", "Get Kiwi Early!", None, -1))
        self.TitleText.setText(QtWidgets.QApplication.translate("InstallerWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">Get Kiwi Early!!!</span></p></body></html>", None, -1))
        self.InstallButton.setText(QtWidgets.QApplication.translate("InstallerWindow", "Get my Kiwi now!", None, -1))
        self.CreditsText.setText(QtWidgets.QApplication.translate("InstallerWindow", "<html><head/><body><p>Made by:</p><p>Comrade Napoleon</p></body></html>", None, -1))
        self.StatusText.setText(QtWidgets.QApplication.translate("InstallerWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Click Get my Kiwi to get started.</span></p></body></html>", None, -1))
        self.RickyText.setText(QtWidgets.QApplication.translate("InstallerWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Thank you Ricky!!!</span></p></body></html>", None, -1))
        self.Ricky.setText(QtWidgets.QApplication.translate("InstallerWindow", "<html><head/><body><p><img src=\"{}\"/></p></body></html>".format(self.resource_path("ricky.png")), None, -1))
        self.Tivo.setText(QtWidgets.QApplication.translate("InstallerWindow", "<html><head/><body><p><img src=\"{}\"/></p></body></html>".format(self.resource_path("TiVo.png")), None, -1))
        self.ChooseFolderButton.setText(QtWidgets.QApplication.translate("InstallerWindow", "...", None, -1))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InstallerWindow = QtWidgets.QMainWindow()
    ui = Ui_InstallerWindow()
    ui.setupUi(InstallerWindow)
    InstallerWindow.show()
    sys.exit(app.exec_())

