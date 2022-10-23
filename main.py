# 1. user navigates to desired directory via GUI
# 2. directory gets scanned
# 3. file dictionary sorts by extension and puts into categories e.g. .jpeg and .png files go under 'images"
# 4. user selects which categories to sort
# 5. folders get created and desired files get sorted into them
# potential features: sort by title,
import shutil
import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
from helpers import scan_dir
from file_dictionary import file_dictionary


# TODO add rescan button that scans text edit box

def iter_tree_widget(tree):
    iterator = QtWidgets.QTreeWidgetItemIterator(tree)
    while True:
        item = iterator.value()
        if item is not None:
            yield item
            iterator += 1
        else:
            break


def tree_item_count(tree):
    count = 0
    iterator = QtWidgets.QTreeWidgetItemIterator(tree)  # pass your treewidget as arg
    while iterator.value():
        item = iterator.value()

        if item.parent():
            if item.parent().isExpanded():
                count += 1
        else:
            # root item
            count += 1
        iterator += 1
    return count


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        # variables
        self.scanned_categories = []
        self.directory_path = None
        self.scanned = False
        font = QFont('Open Sans', 10)
        center = QtWidgets.QDesktopWidget().availableGeometry().center()
        win_width: int = 500
        win_height: int = 500

        # main window creation
        self.setWindowTitle('File Organizer')
        self.setObjectName('MainWindow')
        self.setGeometry(center.x() - win_width // 2, center.y() - win_height // 2, win_width, win_height)
        self.setFixedSize(win_width, win_height)

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
        self.status_label.setText('')

        # Scan and Select Widget (bottom widget)
        # right side widget
        self.widget_2 = QtWidgets.QWidget(self.central_widget)
        self.widget_2.setGeometry(10, 150, 481, 251)
        self.widget_2.setObjectName("widget_2")
        # left side widget
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setGeometry(10, 30, 461, 211)
        self.widget_4.setObjectName("widget_4")
        # layout
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # label
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setText("Select desired file types to sort")
        self.label_2.move(20, 0)
        self.label_2.setObjectName("label_2")
        # scanned file tree (empty)
        self.file_tree = QtWidgets.QTreeWidget(self.widget_4)
        self.horizontalLayout_2.addWidget(self.file_tree)
        self.file_tree.setColumnCount(1)
        self.file_tree.setHeaderLabel("Scanned Files")

        # Sort Widget
        self.widget_5 = QtWidgets.QWidget(self.central_widget)

        self.widget_5 = QtWidgets.QWidget(self.central_widget)
        self.widget_5.setGeometry(10, 420, 481, 41)
        self.widget_5.setObjectName("widget_5")

        self.sort_button = QtWidgets.QPushButton(self.widget_5)
        self.sort_button.setText('Sort')
        self.sort_button.move(10, 10)
        self.sort_button.setObjectName("scan_button")
        self.sort_button.setEnabled(False)
        self.sort_button.clicked.connect(self.sort_files)

        self.sort_progress = QtWidgets.QProgressBar(self.widget_5)
        self.sort_progress.setGeometry(100, 14, 125, 20)
        self.sort_progress.setVisible(False)
        self.sort_progress.setAlignment(QtCore.Qt.AlignCenter)

    # Functions
    def show_popup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText("Files sorted successfully")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Open)
        msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
        msg.buttonClicked.connect(self.popup_button)

        msg.exec_()

    def popup_button(self, i):
        if i.text() == "Open":
            os.startfile(self.directory_path)

    def select_directory(self):
        self.directory_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')
        line_edit_text = self.lineEdit.text()

        if os.path.isdir(self.directory_path):
            self.status_label.setText('')
            self.lineEdit.setText(self.directory_path)
            files = scan_dir(self.directory_path)
            self.generate_file_tree(files)
        elif len(line_edit_text) != 0:
            if os.path.isdir(line_edit_text):
                files = scan_dir(line_edit_text)
                self.generate_file_tree(files)
            else:
                self.status_label.setText('Please Input a valid directory')
        elif len(line_edit_text) == 0:
            self.status_label.setText('Please Input a valid directory')

    def generate_file_tree(self, files):
        self.file_tree.clear()
        self.scanned_categories.clear()
        parents = []
        category_dict = {}
        column = 0

        for file in files:
            extension = file.split(".")[-1].lower()
            if extension in file_dictionary.keys():
                category = file_dictionary[extension]
                if category in self.scanned_categories:
                    # add child to category
                    child_item = QtWidgets.QTreeWidgetItem(1)
                    child_item.setText(column, file)
                    child_item.setFlags(child_item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    child_item.setCheckState(column, QtCore.Qt.Checked)
                    parents[category_dict[category]].addChild(child_item)
                else:
                    # add category to dict
                    category_dict[category] = (len(self.scanned_categories))
                    self.scanned_categories.append(category)
                    # create child
                    child_item = QtWidgets.QTreeWidgetItem(1)
                    child_item.setText(column, file)
                    child_item.setFlags(child_item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    child_item.setCheckState(column, QtCore.Qt.Checked)
                    # create parent
                    parent_item = QtWidgets.QTreeWidgetItem(column)
                    parent_item.setText(column, category)
                    parent_item.setFlags(parent_item.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
                    parent_item.setCheckState(column, QtCore.Qt.Checked)
                    parent_item.addChild(child_item)  # add child to parent
                    parents.append(parent_item)  # push parent to parent array
            else:
                category = "miscellaneous"
                if category not in self.scanned_categories:
                    # add category to dict
                    category_dict[category] = (len(self.scanned_categories))
                    # create parent
                    parent_item = QtWidgets.QTreeWidgetItem(column)
                    parent_item.setText(column, category)
                    parent_item.setFlags(parent_item.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
                    parent_item.setCheckState(column, QtCore.Qt.Checked)
                    parents.append(parent_item)  # push parent to parent array
                    self.scanned_categories.append(category)
                # add child to category
                child_item = QtWidgets.QTreeWidgetItem(1)
                child_item.setText(column, file)
                child_item.setFlags(child_item.flags() | QtCore.Qt.ItemIsUserCheckable)
                child_item.setCheckState(column, QtCore.Qt.Checked)
                parent_item.addChild(child_item)  # add child to parent
                parents[category_dict[category]].addChild(child_item)

            self.file_tree.insertTopLevelItems(column, parents)

        if len(parents) == 0:
            self.scanned = False
        else:
            self.scanned = True
        self.sort_button.setEnabled(self.scanned)

    def sort_files(self):
        # check for checked boxes
        column = 0
        category = str
        item_count = tree_item_count(self.file_tree)
        self.sort_progress.setVisible(True)

        for i, item in enumerate(iter_tree_widget(self.file_tree)):
            # print('State: %s, Text: "%s"' % (item.checkState(column), item.text(column)))
            progress_value = i // item_count * 100 # normalize value to make percentage
            self.sort_progress.setValue(progress_value)
            if item.checkState(column) != 0:
                if item.text(column) in self.scanned_categories:  # if name is category name
                    category = item.text(column)
                    # create directory
                    if os.path.exists(os.path.join(self.directory_path, category).replace("\\", "/")):
                        continue
                    else:
                        path = os.path.join(self.directory_path, category).replace("\\", "/")
                        os.mkdir(path)
                else:  # if name is file name
                    # sort file into directory
                    sorted_dir = os.path.join(self.directory_path, category).replace("\\", "/")
                    sorted_filepath = os.path.join(sorted_dir, item.text(column)).replace("\\", "/")
                    shutil.move(os.path.join(self.directory_path, item.text(column)).replace("\\", "/"),
                                sorted_filepath)
        self.sort_progress.setVisible(True)
        files = scan_dir(self.directory_path)
        self.generate_file_tree(files)
        self.show_popup()


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
    QListWidget {
        background: #adadad;
        border-radius: 5px;
    }
    QProgressBar {
        border: solid grey;
        border-radius: 5px;
        color: black;
    }
    QProgressBar::chunk {
        background-color: #6bffa4;
        border-radius :5px;
    }
""")

Organizer = MainWindow()
Organizer.show()
sys.exit(app.exec_())
