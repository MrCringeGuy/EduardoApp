version = 1.3
title = """
FORTNITE HACKS {}
================

https://discord.gg/YDYZumtSPA for help
""".format(version)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, os

class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.setGeometry(190, 210, 975, 475)
        self.setWindowTitle(f"◍ EduardoCheats v{version}")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Mod menu:")
        self.label.move(15, 10)

        self.aimbot = QtWidgets.QPushButton(self)
        self.aimbot.setText("Start aimbot")
        self.aimbot.move(0, 50)
        self.aimbot.clicked.connect(self.aimbot_clicked)

        self.reboot = QtWidgets.QPushButton(self)
        self.reboot.setText("Restart")
        self.reboot.move(150, 50)
        self.reboot.clicked.connect(self.reboot_clicked)

    def reboot_clicked(self):
        if not os.path.isfile("Reboot.exe"):
            os.system("Start ENR.vbs")
        else:
            os.system("Start Reboot.exe")

    def aimbot_clicked(self):
        #if not "Aimbot.exe" in correct_files:
        if not os.path.isfile("Aimbot.exe"):
            os.system("Start ENA.vbs")
        
        else:
            os.system("Start Aimbot.exe")

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = Main()

    win.show()
    sys.exit(app.exec_())


window()
