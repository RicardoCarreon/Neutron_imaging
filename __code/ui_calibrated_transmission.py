# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/IPTS/python_notebooks/ui/ui_calibrated_transmission.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1025, 824)
        MainWindow.setMinimumSize(QtCore.QSize(0, 300))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pyqtgraph_widget = QtWidgets.QWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pyqtgraph_widget.sizePolicy().hasHeightForWidth())
        self.pyqtgraph_widget.setSizePolicy(sizePolicy)
        self.pyqtgraph_widget.setObjectName("pyqtgraph_widget")
        self.horizontalLayout_2.addWidget(self.pyqtgraph_widget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.previous_image_button = QtWidgets.QPushButton(self.layoutWidget)
        self.previous_image_button.setEnabled(False)
        self.previous_image_button.setObjectName("previous_image_button")
        self.horizontalLayout_3.addWidget(self.previous_image_button)
        self.file_slider = QtWidgets.QSlider(self.layoutWidget)
        self.file_slider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.file_slider.setOrientation(QtCore.Qt.Horizontal)
        self.file_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.file_slider.setObjectName("file_slider")
        self.horizontalLayout_3.addWidget(self.file_slider)
        self.next_image_button = QtWidgets.QPushButton(self.layoutWidget)
        self.next_image_button.setObjectName("next_image_button")
        self.horizontalLayout_3.addWidget(self.next_image_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget1)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 0, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_15.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout.addWidget(self.lineEdit_15, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 1, 0, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout.addWidget(self.lineEdit_21, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 0, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout.addWidget(self.lineEdit_22, 2, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 3, 0, 1, 1)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout.addWidget(self.lineEdit_23, 3, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 4, 0, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout.addWidget(self.lineEdit_24, 4, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_16.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_2.addWidget(self.lineEdit_16, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 1, 0, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_2.addWidget(self.lineEdit_17, 1, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 2, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_2.addWidget(self.lineEdit_18, 2, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 3, 0, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_2.addWidget(self.lineEdit_19, 3, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 4, 0, 1, 1)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_2.addWidget(self.lineEdit_20, 4, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.layoutWidget1)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_5.addWidget(self.tableWidget)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.remove_row = QtWidgets.QPushButton(self.groupBox_4)
        self.remove_row.setMinimumSize(QtCore.QSize(50, 40))
        self.remove_row.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.remove_row.setFont(font)
        self.remove_row.setObjectName("remove_row")
        self.horizontalLayout_6.addWidget(self.remove_row)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.add_row = QtWidgets.QPushButton(self.groupBox_4)
        self.add_row.setMinimumSize(QtCore.QSize(50, 40))
        self.add_row.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.add_row.setFont(font)
        self.add_row.setObjectName("add_row")
        self.horizontalLayout_6.addWidget(self.add_row)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.measurement_widget = QtWidgets.QWidget(self.splitter_2)
        self.measurement_widget.setObjectName("measurement_widget")
        self.verticalLayout_7.addWidget(self.splitter_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setObjectName("export_button")
        self.horizontalLayout.addWidget(self.export_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1025, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport_Profile = QtWidgets.QAction(MainWindow)
        self.actionExport_Profile.setObjectName("actionExport_Profile")
        self.actionWater_Intake = QtWidgets.QAction(MainWindow)
        self.actionWater_Intake.setObjectName("actionWater_Intake")
        self.actionImportedFilesMetadata = QtWidgets.QAction(MainWindow)
        self.actionImportedFilesMetadata.setObjectName("actionImportedFilesMetadata")
        self.actionBy_Time_Stamp = QtWidgets.QAction(MainWindow)
        self.actionBy_Time_Stamp.setObjectName("actionBy_Time_Stamp")
        self.actionBy_File_Name = QtWidgets.QAction(MainWindow)
        self.actionBy_File_Name.setObjectName("actionBy_File_Name")
        self.actionDsc_files = QtWidgets.QAction(MainWindow)
        self.actionDsc_files.setObjectName("actionDsc_files")
        self.actionDsc = QtWidgets.QAction(MainWindow)
        self.actionDsc.setObjectName("actionDsc")
        self.actionWater_Intake_2 = QtWidgets.QAction(MainWindow)
        self.actionWater_Intake_2.setObjectName("actionWater_Intake_2")
        self.actionProfiles = QtWidgets.QAction(MainWindow)
        self.actionProfiles.setObjectName("actionProfiles")

        self.retranslateUi(MainWindow)
        self.file_slider.sliderMoved['int'].connect(MainWindow.slider_file_changed)
        self.file_slider.valueChanged['int'].connect(MainWindow.slider_file_changed)
        self.previous_image_button.clicked.connect(MainWindow.previous_image_button_clicked)
        self.next_image_button.clicked.connect(MainWindow.next_image_button_clicked)
        self.export_button.clicked.connect(MainWindow.export_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calbrated Transmission"))
        self.previous_image_button.setText(_translate("MainWindow", "Prev. Image"))
        self.next_image_button.setText(_translate("MainWindow", "Next Image"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Calibration"))
        self.groupBox.setTitle(_translate("MainWindow", "Region 1"))
        self.label_22.setText(_translate("MainWindow", "X0"))
        self.label_23.setText(_translate("MainWindow", "y0"))
        self.label_24.setText(_translate("MainWindow", "width"))
        self.label_25.setText(_translate("MainWindow", "height"))
        self.label_26.setText(_translate("MainWindow", "Value"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Region 2"))
        self.label_17.setText(_translate("MainWindow", "X0"))
        self.label_18.setText(_translate("MainWindow", "y0"))
        self.label_19.setText(_translate("MainWindow", "width"))
        self.label_20.setText(_translate("MainWindow", "height"))
        self.label_21.setText(_translate("MainWindow", "Value"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Measurement"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X0"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y0"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Width"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Height"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Mean Counts"))
        self.remove_row.setText(_translate("MainWindow", "-"))
        self.add_row.setText(_translate("MainWindow", "+"))
        self.pushButton.setText(_translate("MainWindow", "Help"))
        self.export_button.setText(_translate("MainWindow", "Export ..."))
        self.actionExport_Profile.setText(_translate("MainWindow", "Profiles ..."))
        self.actionWater_Intake.setText(_translate("MainWindow", "Water Intake ..."))
        self.actionImportedFilesMetadata.setText(_translate("MainWindow", "Imported Files and Metadata ..."))
        self.actionBy_Time_Stamp.setText(_translate("MainWindow", "by Time Stamp"))
        self.actionBy_File_Name.setText(_translate("MainWindow", "by File Name"))
        self.actionDsc_files.setText(_translate("MainWindow", "dsc files ..."))
        self.actionDsc.setText(_translate("MainWindow", "dsc ..."))
        self.actionWater_Intake_2.setText(_translate("MainWindow", "Water Intake ..."))
        self.actionProfiles.setText(_translate("MainWindow", "Profiles ..."))

