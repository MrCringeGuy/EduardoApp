version = 1.2
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
        self.setWindowTitle(f"◍ EduardoApp v{version}")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Mod menu:")
        self.label.move(15, 10)

        self.trigger = QtWidgets.QPushButton(self)
        self.trigger.setText("Start trigger bot")
        self.trigger.move(0, 50)
        self.trigger.clicked.connect(self.trigger_clicked)

        self.macro = QtWidgets.QPushButton(self)
        self.macro.setText("Start macro")
        self.macro.move(0, 50)
        self.macro.clicked.connect(self.macro_clicked)

    def trigger_clicked(self):
        self.trigger.setText("Trigger bot key: E")
        os.system("Start TriggerBot.exe")
        self.update()

    def macro_clicked(self):
        self.macro.setText("Macro key: L")
        os.system("start Macro.exe")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = Main()

    win.show()
    sys.exit(app.exec_())


# print(title)
window()
