import sys
from UserInterface import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ =="__main__":
    app= QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())



