import sys, random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6 import QtCore, QtGui

class MainWindow(QMainWindow): #Class for Window customization and contents
    def __init__(self): 
        super().__init__()

        self.setWindowTitle("Wallpicker") #Window Title
        self.resize(900, 600) #Window Initial Sizing

        layout = QVBoxLayout() 

        label = QLabel("No Folder Selected")
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)