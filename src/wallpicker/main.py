import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

app = QApplication(sys.argv) #Instanciate the PySide Application

window = MainWindow() #Creates the Window
window.show() #Shows the Window

sys.exit(app.exec()) #Keeps the Window from closing