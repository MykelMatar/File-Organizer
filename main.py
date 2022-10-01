# 1. user navigates to desired directory via GUI
# 2. directory gets scanned
# 3. file dictionary sorts by extension and puts into categories e.g. .jpeg and .png files go under 'images"
# 4. user selects which categories to sort
# 5. folders get created and desired files get sorted into them
# potential features: sort by title,


import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QFileDialog, QDialog


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        labelFont = QFont('OpenSans', 12)
        buttonFont = QFont('Open Sans', 10)

        self.setWindowTitle('File Organizer')
        self.setFont(labelFont)

        center = QDesktopWidget().availableGeometry().center()
        win_width: int = 500
        win_height: int = 500
        self.setGeometry(center.x() - win_width // 2, center.y() - win_height // 2, win_width, win_height)

        label = QtWidgets.QLabel(self)
        label.setText("File Directory: ")
        label.move(50, 50)

        directory_box = QtWidgets.QFileDialog(self)
        directory_box.move(80, 100)

        browseButton = QtWidgets.QPushButton(self)
        browseButton.setText('Browse')
        browseButton.setFont(buttonFont)
        browseButton.setGeometry(200, 50, 70, 30)
        browseButton.clicked.connect(self.browseFiles)

        self.show()

    def browseFiles(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Select Directory')
        print(fileName)


app = QtWidgets.QApplication(sys.argv)
Organizer = MainWindow()
sys.exit(app.exec_())

