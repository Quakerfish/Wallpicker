import sys, random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
from PySide6 import QtCore, QtGui
from ui.styles import DARK_THEME

class MainWindow(QMainWindow): #Class for Window customization and contents
    def __init__(self): 
        super().__init__()
        
        self.setWindowTitle("Wallpicker") #Window Title
        self.resize(900, 600) #Window Initial Sizing
        self.label = QLabel() #Label Instanciation
        self.button = QPushButton() #Button Instanciation

        self.setStyleSheet(DARK_THEME) #Sets the Window Style (Dark, Light)
        layout = QVBoxLayout() 

        #File & Folder Selection
        self.button.setText("Add Folder")
        self.button.clicked.connect(self.select_folder)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "NANI")
        if folder_path:
            self.label.setText(folder_path)
        else:
            self.label.setText("No Selected Folder")