# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/IPTS/notebooks/ui/ui_linear_profile.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 400))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.file_index_slider = QtWidgets.QSlider(self.layoutWidget)
        self.file_index_slider.setOrientation(QtCore.Qt.Horizontal)
        self.file_index_slider.setObjectName("file_index_slider")
        self.horizontalLayout_2.addWidget(self.file_index_slider)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.table_profile = QtWidgets.QTableWidget(self.layoutWidget)
        self.table_profile.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.table_profile.setObjectName("table_profile")
        self.table_profile.setColumnCount(7)
        self.table_profile.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_profile.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_profile.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_profile.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_profile.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_profile.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_profile.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_profile.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.table_profile)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_profile = QtWidgets.QPushButton(self.layoutWidget)
        self.add_profile.setMinimumSize(QtCore.QSize(53, 46))
        self.add_profile.setMaximumSize(QtCore.QSize(53, 46))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.add_profile.setFont(font)
        self.add_profile.setObjectName("add_profile")
        self.horizontalLayout.addWidget(self.add_profile)
        self.add_profile_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.add_profile_2.setMinimumSize(QtCore.QSize(53, 46))
        self.add_profile_2.setMaximumSize(QtCore.QSize(53, 46))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.add_profile_2.setFont(font)
        self.add_profile_2.setObjectName("add_profile_2")
        self.horizontalLayout.addWidget(self.add_profile_2)
        spacerItem1 = QtWidgets.QSpacerItem(408, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(53, 46))
        self.pushButton.setMaximumSize(QtCore.QSize(53, 46))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.splitter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport_Profile = QtWidgets.QAction(MainWindow)
        self.actionExport_Profile.setObjectName("actionExport_Profile")
        self.menuFile.addAction(self.actionExport_Profile)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.file_index_slider.sliderMoved['int'].connect(MainWindow.slider_changed)
        self.add_profile.clicked.connect(MainWindow.add_profile)
        self.add_profile_2.clicked.connect(MainWindow.remove_profile)
        self.pushButton.clicked.connect(MainWindow.ok_button_clicked)
        self.actionExport_Profile.triggered.connect(MainWindow.export_button_clicked)
        self.table_profile.cellChanged['int','int'].connect(MainWindow.save_roi_table)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "File Index"))
        item = self.table_profile.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table_profile.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Xo"))
        item = self.table_profile.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Yo"))
        item = self.table_profile.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "X1"))
        item = self.table_profile.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Y1"))
        item = self.table_profile.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Width"))
        item = self.table_profile.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Color"))
        self.add_profile.setText(_translate("MainWindow", "+"))
        self.add_profile_2.setText(_translate("MainWindow", "-"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExport_Profile.setText(_translate("MainWindow", "Export Profile ..."))

