from main_window_ui import *
from registration_ui import *
import sys
import os

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec())