import sys, random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6 import QtCore, QtGui

class MainWindow(QMainWindow): #Class for Window customization and contents
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wallpicker")
        self.resize(900, 600)

        layout = QVBoxLayout

        

app = QApplication(sys.argv) #Instanciate the PySide Application

window = MainWindow() #Creates the Window
window.show() #Shows the Window

sys.exit(app.exec()) #Keeps the Window from closing