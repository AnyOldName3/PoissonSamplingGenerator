﻿# Form implementation generated from reading ui file '.\poisson_ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 714)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton1DLine = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton1DLine.setObjectName("radioButton1DLine")
        self.verticalLayout_2.addWidget(self.radioButton1DLine)
        self.radioButton1DRepeatedLine = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton1DRepeatedLine.setObjectName("radioButton1DRepeatedLine")
        self.verticalLayout_2.addWidget(self.radioButton1DRepeatedLine)
        self.radioButton2DDisk = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton2DDisk.setChecked(True)
        self.radioButton2DDisk.setObjectName("radioButton2DDisk")
        self.verticalLayout_2.addWidget(self.radioButton2DDisk)
        self.radioButton2DRotatedDisk = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton2DRotatedDisk.setObjectName("radioButton2DRotatedDisk")
        self.verticalLayout_2.addWidget(self.radioButton2DRotatedDisk)
        self.radioButton2DRect = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton2DRect.setObjectName("radioButton2DRect")
        self.verticalLayout_2.addWidget(self.radioButton2DRect)
        self.radioButton2DRepeatedRectangle = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton2DRepeatedRectangle.setObjectName("radioButton2DRepeatedRectangle")
        self.verticalLayout_2.addWidget(self.radioButton2DRepeatedRectangle)
        self.radioButton3DSphere = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton3DSphere.setObjectName("radioButton3DSphere")
        self.verticalLayout_2.addWidget(self.radioButton3DSphere)
        self.radioButton3DBox = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton3DBox.setObjectName("radioButton3DBox")
        self.verticalLayout_2.addWidget(self.radioButton3DBox)
        self.radioButton3DRepeatedBox = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton3DRepeatedBox.setObjectName("radioButton3DRepeatedBox")
        self.verticalLayout_2.addWidget(self.radioButton3DRepeatedBox)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.numberOfPointsSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.numberOfPointsSpinBox.setMinimum(1)
        self.numberOfPointsSpinBox.setMaximum(4096)
        self.numberOfPointsSpinBox.setProperty("value", 8)
        self.numberOfPointsSpinBox.setObjectName("numberOfPointsSpinBox")
        self.gridLayout.addWidget(self.numberOfPointsSpinBox, 1, 1, 1, 1)
        self.firstPointRandomCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.firstPointRandomCheckBox.setChecked(True)
        self.firstPointRandomCheckBox.setObjectName("firstPointRandomCheckBox")
        self.gridLayout.addWidget(self.firstPointRandomCheckBox, 6, 1, 1, 1)
        self.numberOfIterationsPerPointSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.numberOfIterationsPerPointSpinBox.setMinimum(1)
        self.numberOfIterationsPerPointSpinBox.setMaximum(1024)
        self.numberOfIterationsPerPointSpinBox.setProperty("value", 8)
        self.numberOfIterationsPerPointSpinBox.setObjectName("numberOfIterationsPerPointSpinBox")
        self.gridLayout.addWidget(self.numberOfIterationsPerPointSpinBox, 2, 1, 1, 1)
        self.cacheSortBucketsSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.cacheSortBucketsSpinBox.setMaximum(64)
        self.cacheSortBucketsSpinBox.setObjectName("cacheSortBucketsSpinBox")
        self.gridLayout.addWidget(self.cacheSortBucketsSpinBox, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.numberTotalIterationsSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.numberTotalIterationsSpinBox.setMinimum(1)
        self.numberTotalIterationsSpinBox.setMaximum(1048576)
        self.numberTotalIterationsSpinBox.setProperty("value", 64)
        self.numberTotalIterationsSpinBox.setObjectName("numberTotalIterationsSpinBox")
        self.gridLayout.addWidget(self.numberTotalIterationsSpinBox, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.rotationsAsRepetitions = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.rotationsAsRepetitions.setMaximum(16)
        self.rotationsAsRepetitions.setObjectName("rotationsAsRepetitions")
        self.gridLayout.addWidget(self.rotationsAsRepetitions, 5, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.generateButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.generateButton.setObjectName("generateButton")
        self.verticalLayout.addWidget(self.generateButton)
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setMaximum(1024)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.outputShaderCodeTextEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.outputShaderCodeTextEdit.setReadOnly(True)
        self.outputShaderCodeTextEdit.setObjectName("outputShaderCodeTextEdit")
        self.verticalLayout.addWidget(self.outputShaderCodeTextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Poisson-like pattern generator"))
        self.radioButton1DLine.setText(_translate("MainWindow", "1D line"))
        self.radioButton1DRepeatedLine.setText(_translate("MainWindow", "1D repeated line"))
        self.radioButton2DDisk.setText(_translate("MainWindow", "2D disk"))
        self.radioButton2DRotatedDisk.setText(_translate("MainWindow", "2D rotated disk"))
        self.radioButton2DRect.setText(_translate("MainWindow", "2D rectangle"))
        self.radioButton2DRepeatedRectangle.setText(_translate("MainWindow", "2D repeated rectangle"))
        self.radioButton3DSphere.setText(_translate("MainWindow", "3D sphere"))
        self.radioButton3DBox.setText(_translate("MainWindow", "3D box"))
        self.radioButton3DRepeatedBox.setText(_translate("MainWindow", "3D repeated box"))
        self.firstPointRandomCheckBox.setText(_translate("MainWindow", "First point random"))
        self.label_2.setText(_translate("MainWindow", "Number of iterations per point"))
        self.label.setText(_translate("MainWindow", "Number of points"))
        self.label_4.setText(_translate("MainWindow", "Pattern type"))
        self.label_5.setText(_translate("MainWindow", "Cache sort buckets"))
        self.label_3.setText(_translate("MainWindow", "Number of retires"))
        self.label_6.setToolTip(_translate("MainWindow", "Works only in rotated disk mode - maximizes distances / variances num between rotations - to be used with rotated patterns"))
        self.label_6.setText(_translate("MainWindow", "Rotations as repetitions (num)"))
        self.rotationsAsRepetitions.setToolTip(_translate("MainWindow", "Works only in rotated disk mode - maximizes distances / variances num between rotations - to be used with rotated patterns"))
        self.generateButton.setText(_translate("MainWindow", "Generate"))
