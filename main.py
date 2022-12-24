import shutil
import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
from helpers import scan_dir
from file_dictionary import file_dictionary

class Ui_MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        # variables
        self.scanned_categories = []
        self.directory_path = None
        self.scanned = False
        font = QFont('Open Sans', 10)
        center = QtWidgets.QDesktopWidget().availableGeometry().center()
        win_width: int = 500
        win_height: int = 500

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setObjectName("widget_6")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.widget = QtWidgets.QWidget(self.widget_6)
        self.widget.setObjectName("widget")

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.label = QtWidgets.QLabel(self.widget_7)
        self.label.setObjectName("label")

        self.verticalLayout_3.addWidget(self.label)

        self.lineEdit = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit.setObjectName("lineEdit")

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.status_label = QtWidgets.QLabel(self.widget_7)
        self.status_label.setObjectName("label_3")

        self.verticalLayout_3.addWidget(self.status_label)

        self.horizontalLayout_5.addWidget(self.widget_7)

        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.select_directory)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayout_5.addWidget(self.widget_3)

        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QtWidgets.QWidget(self.widget_6)
        self.widget_2.setObjectName("widget_2")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.file_tree = QtWidgets.QTreeWidget(self.widget_4)
        self.file_tree.setObjectName("file_tree")

        self.horizontalLayout_2.addWidget(self.file_tree)

        self.verticalLayout.addWidget(self.widget_4)

        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_5 = QtWidgets.QWidget(self.widget_6)
        self.widget_5.setObjectName("widget_5")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.sort_button = QtWidgets.QPushButton(self.widget_5)
        self.sort_button.setObjectName("sort_button")
        self.sort_button.setText('Sort')
        self.sort_button.setEnabled(False)
        self.sort_button.clicked.connect(self.sort_files)

        self.horizontalLayout_4.addWidget(self.sort_button)

        self.sort_progress = QtWidgets.QProgressBar(self.widget_5)
        self.sort_progress.setObjectName("progressBar")
        # self.sort_progress.setVisible(False)
        self.sort_progress.setAlignment(QtCore.Qt.AlignCenter)

        self.size_policy = QtWidgets.QSizePolicy()
        self.size_policy.setRetainSizeWhenHidden(True)

        self.sort_progress.setSizePolicy(self.size_policy)

        self.horizontalLayout_4.addWidget(self.sort_progress)

        self.verticalLayout_2.addWidget(self.widget_5)

        self.horizontalLayout_6.addWidget(self.widget_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "File Directory"))
        self.status_label.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "Select File Types To Sort"))
        self.file_tree.headerItem().setText(0, _translate("MainWindow", "Scanned Files"))
        __sortingEnabled = self.file_tree.isSortingEnabled()
        self.file_tree.setSortingEnabled(False)
        self.file_tree.setSortingEnabled(__sortingEnabled)
        self.sort_button.setText(_translate("MainWindow", "Sort"))

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
