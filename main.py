# 1. user navigates to desired directory via GUI
# 2. directory gets scanned
# 3. file dictionary sorts by extension and puts into categories e.g. .jpeg and .png files go under 'images"
# 4. user selects which categories to sort
# 5. folders get created and desired files get sorted into them
# potential features: sort by title,


import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
from helpers import scan_dir

 
class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        # variables
        font = QFont('Open Sans', 10)
        center = QtWidgets.QDesktopWidget().availableGeometry().center()
        win_width: int = 500
        win_height: int = 500

        # main window creation
        self.setWindowTitle('File Organizer')
        self.setObjectName('MainWindow')
        self.setGeometry(center.x() - win_width // 2, center.y() - win_height // 2, win_width, win_height)

        # Central Widget (required)
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.central_widget.setFont(font)

        # Directory Selection Widget
        self.top_widget = QtWidgets.QWidget(self.central_widget)
        self.top_widget.setGeometry(10, 10, 481, 131)
        self.top_widget.setObjectName("widget")

        self.widget_3 = QtWidgets.QWidget(self.top_widget)
        self.widget_3.setGeometry(30, 40, 431, 41)
        self.widget_3.setObjectName("widget_3")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.top_widget)
        self.label.setText('File Directory')
        self.label.setGeometry(10, 10, 81, 16)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.browse_button = QtWidgets.QPushButton(self.widget_3)
        self.browse_button.setText("Browse")
        self.browse_button.setObjectName("browse_button")
        self.horizontalLayout.addWidget(self.browse_button)

        self.browse_button.clicked.connect(self.select_directory)

        self.status_label = QtWidgets.QLabel(self.top_widget)
        self.status_label.setGeometry(50, 75, 200, 16)
        self.status_label.setText('test')

        # Scan and Select Widget
        # right side
        self.widget_2 = QtWidgets.QWidget(self.central_widget)
        self.widget_2.setGeometry(10, 150, 481, 251)
        self.widget_2.setObjectName("widget_2")
        # left side
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setGeometry(10, 30, 461, 211)
        self.widget_4.setObjectName("widget_4")
        # right and left side layout
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # Label
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setText("Select desired file types to sort")
        self.label_2.move(20, 0)
        self.label_2.setObjectName("label_2")
        # scanned file tree

        self.file_tree = QtWidgets.QTreeWidget(self.widget_4)
        self.horizontalLayout_2.addWidget(self.file_tree)
        self.file_tree.setColumnCount(1)
        self.file_tree.setHeaderLabel("Scanned Files")

        item0 = QtWidgets.QTreeWidgetItem(0)
        item0.setText(0, "Images")
        item0.setFlags(item0.flags() | QtCore.Qt.ItemIsUserCheckable)
        item0.setCheckState(0, QtCore.Qt.Unchecked)
        child_item = QtWidgets.QTreeWidgetItem(1)
        child_item.setText(0, "file1.png")
        item0.addChild(child_item)

        self.file_tree.insertTopLevelItem(0, item0)

        # Scan Widget
        self.widget_5 = QtWidgets.QWidget(self.central_widget)

        self.widget_5 = QtWidgets.QWidget(self.central_widget)
        self.widget_5.setGeometry(10, 420, 481, 41)
        self.widget_5.setObjectName("widget_5")

        self.scan_button = QtWidgets.QPushButton(self.widget_5)
        self.scan_button.setText('Sort')
        self.scan_button.move(10, 10)
        self.scan_button.setObjectName("scan_button")

    # Functions
    def select_directory(self):
        directory_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')
        line_edit_text = self.lineEdit.text()

        if os.path.isdir(directory_path):
            self.status_label.setText('')
            self.lineEdit.setText(directory_path)
            scan_dir(directory_path)
        elif len(line_edit_text) != 0:
            if os.path.isdir(line_edit_text):
                scan_dir(line_edit_text)
            else:
                self.status_label.setText('Please Input a valid directory')
        elif len(line_edit_text) == 0:
            self.status_label.setText('Please Input a valid directory')


app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet("""
    QLineEdit {
        background: #b5b5b5;
        border-width: 10px;
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 5px;
    }
    QLabel {
        background: none;
    }
    QListWidget{
        background: #adadad;
        border-radius: 5px;
    }
""")

Organizer = MainWindow()
Organizer.show()
sys.exit(app.exec_())
