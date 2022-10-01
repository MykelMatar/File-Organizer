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

        # Scan and Sort Widget
        # right side
        self.widget_2 = QtWidgets.QWidget(self.central_widget)
        self.widget_2.setGeometry(10, 150, 481, 291)
        self.widget_2.setObjectName("widget_2")
        # left side
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setGeometry(10, 30, 461, 251)
        self.widget_4.setObjectName("widget_4")
        # right and left side layout
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # Label
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setText("Select desired file types to sort")
        self.label_2.setGeometry(20, 0, 150, 31)
        self.label_2.setObjectName("label_2")
        # checkbox frame
        self.file_list = QtWidgets.QListWidget(self.widget_4)
        self.file_list.setObjectName("file_list")
        self.horizontalLayout_2.addWidget(self.file_list)
        # list items
        item = QtWidgets.QListWidgetItem('item1')
        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.file_list.addItem(item)

        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2.addWidget(self.widget_5)

        self.listWidget = QtWidgets.QListWidget(self.widget_5)
        self.listWidget.setGeometry(20, 20, 181, 191)
        self.listWidget.setObjectName("listWidget")

    def select_directory(self):
        directory_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')
        # self.line_edit1.setText(directory_path)

        if os.path.isdir(directory_path):
            print(directory_path)
        else:
            print('Please input a valid directory')


app = QtWidgets.QApplication(sys.argv)
# app.setStyleSheet("""
#     QWidget {
#         background: none;
#         border-radius: 5px;
#     }
#     QLineEdit {
#         background: #b5b5b5;
#         border-width: 10px;
#         padding-left: 10px;
#         padding-right: 10px;
#         border-radius: 5px;
#     }
#     QLabel {
# 
#     }
#     QPushButton {
#         background: none;
#         font-size: 12px;
#     }
#     QFrame {
#         background: #c7c7c7;
#         border-radius: 5px;
#     }
#     QListWidget{
#         background: #adadad;
#         border-radius: 5px;
#     }
# """)

Organizer = MainWindow()
Organizer.show()
sys.exit(app.exec_())
