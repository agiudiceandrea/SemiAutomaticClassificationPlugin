# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_semiautomaticclassificationplugin_scatter_plot.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScatterPlot(object):
    def setupUi(self, ScatterPlot):
        ScatterPlot.setObjectName("ScatterPlot")
        ScatterPlot.resize(710, 579)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScatterPlot.sizePolicy().hasHeightForWidth())
        ScatterPlot.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ScatterPlot.setWindowIcon(icon)
        ScatterPlot.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout_5 = QtWidgets.QGridLayout(ScatterPlot)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.splitter = QtWidgets.QSplitter(ScatterPlot)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scatter_list_plot_tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scatter_list_plot_tableWidget.sizePolicy().hasHeightForWidth())
        self.scatter_list_plot_tableWidget.setSizePolicy(sizePolicy)
        self.scatter_list_plot_tableWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.scatter_list_plot_tableWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.scatter_list_plot_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.scatter_list_plot_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.scatter_list_plot_tableWidget.setObjectName("scatter_list_plot_tableWidget")
        self.scatter_list_plot_tableWidget.setColumnCount(6)
        self.scatter_list_plot_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(5, item)
        self.scatter_list_plot_tableWidget.horizontalHeader().setDefaultSectionSize(62)
        self.scatter_list_plot_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.scatter_list_plot_tableWidget.verticalHeader().setDefaultSectionSize(22)
        self.gridLayout_2.addWidget(self.scatter_list_plot_tableWidget, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Scatter_Widget_2 = ScatterWidget2(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Scatter_Widget_2.sizePolicy().hasHeightForWidth())
        self.Scatter_Widget_2.setSizePolicy(sizePolicy)
        self.Scatter_Widget_2.setMinimumSize(QtCore.QSize(0, 100))
        self.Scatter_Widget_2.setObjectName("Scatter_Widget_2")
        self.gridLayout_3.addWidget(self.Scatter_Widget_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.splitter, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(ScatterPlot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_49 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy)
        self.label_49.setObjectName("label_49")
        self.horizontalLayout_8.addWidget(self.label_49)
        self.scatter_ROI_Button = QtWidgets.QToolButton(self.frame)
        self.scatter_ROI_Button.setStyleSheet("margin: 0px;padding: 0px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_enter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scatter_ROI_Button.setIcon(icon1)
        self.scatter_ROI_Button.setIconSize(QtCore.QSize(22, 22))
        self.scatter_ROI_Button.setObjectName("scatter_ROI_Button")
        self.horizontalLayout_8.addWidget(self.scatter_ROI_Button)
        self.gridLayout_6.addLayout(self.horizontalLayout_8, 6, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.precision_checkBox = QtWidgets.QCheckBox(self.frame)
        self.precision_checkBox.setObjectName("precision_checkBox")
        self.horizontalLayout_2.addWidget(self.precision_checkBox)
        self.precision_comboBox = QtWidgets.QComboBox(self.frame)
        self.precision_comboBox.setObjectName("precision_comboBox")
        self.precision_comboBox.addItem("")
        self.precision_comboBox.addItem("")
        self.precision_comboBox.addItem("")
        self.precision_comboBox.addItem("")
        self.precision_comboBox.addItem("")
        self.precision_comboBox.addItem("")
        self.precision_comboBox.addItem("")
        self.precision_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.precision_comboBox)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 8, 0, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fitToAxes_pushButton_2 = QtWidgets.QToolButton(self.frame)
        self.fitToAxes_pushButton_2.setStyleSheet("margin: 0px;padding: 0px;")
        self.fitToAxes_pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_fit_plot.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fitToAxes_pushButton_2.setIcon(icon2)
        self.fitToAxes_pushButton_2.setIconSize(QtCore.QSize(22, 22))
        self.fitToAxes_pushButton_2.setObjectName("fitToAxes_pushButton_2")
        self.horizontalLayout_4.addWidget(self.fitToAxes_pushButton_2)
        self.save_plot_pushButton_2 = QtWidgets.QToolButton(self.frame)
        self.save_plot_pushButton_2.setStyleSheet("margin: 0px;padding: 0px;")
        self.save_plot_pushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_save_plot_image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_plot_pushButton_2.setIcon(icon3)
        self.save_plot_pushButton_2.setIconSize(QtCore.QSize(22, 22))
        self.save_plot_pushButton_2.setObjectName("save_plot_pushButton_2")
        self.horizontalLayout_4.addWidget(self.save_plot_pushButton_2)
        self.gridLayout_14.addLayout(self.horizontalLayout_4, 3, 3, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("background-color : #656565; color : white")
        self.label_27.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_14.addWidget(self.label_27, 1, 3, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_50 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy)
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_6.addWidget(self.label_50)
        self.colormap_comboBox = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colormap_comboBox.sizePolicy().hasHeightForWidth())
        self.colormap_comboBox.setSizePolicy(sizePolicy)
        self.colormap_comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.colormap_comboBox.setObjectName("colormap_comboBox")
        self.horizontalLayout_6.addWidget(self.colormap_comboBox)
        self.gridLayout_14.addLayout(self.horizontalLayout_6, 2, 3, 1, 1)
        self.value_label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        font.setBold(True)
        font.setWeight(75)
        self.value_label_2.setFont(font)
        self.value_label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.value_label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.value_label_2.setObjectName("value_label_2")
        self.gridLayout_14.addWidget(self.value_label_2, 4, 3, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_14, 9, 0, 1, 1)
        self.gridLayout_40 = QtWidgets.QGridLayout()
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.label_48 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        self.label_48.setObjectName("label_48")
        self.gridLayout_40.addWidget(self.label_48, 0, 0, 1, 1)
        self.bandY_spinBox = QtWidgets.QSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bandY_spinBox.sizePolicy().hasHeightForWidth())
        self.bandY_spinBox.setSizePolicy(sizePolicy)
        self.bandY_spinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.bandY_spinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bandY_spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bandY_spinBox.setMinimum(1)
        self.bandY_spinBox.setMaximum(2000)
        self.bandY_spinBox.setProperty("value", 2)
        self.bandY_spinBox.setObjectName("bandY_spinBox")
        self.gridLayout_40.addWidget(self.bandY_spinBox, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_40, 2, 0, 1, 1)
        self.gridLayout_38 = QtWidgets.QGridLayout()
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.label_46 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy)
        self.label_46.setObjectName("label_46")
        self.gridLayout_38.addWidget(self.label_46, 0, 0, 1, 1)
        self.bandX_spinBox = QtWidgets.QSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bandX_spinBox.sizePolicy().hasHeightForWidth())
        self.bandX_spinBox.setSizePolicy(sizePolicy)
        self.bandX_spinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.bandX_spinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bandX_spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bandX_spinBox.setMinimum(1)
        self.bandX_spinBox.setMaximum(2000)
        self.bandX_spinBox.setProperty("value", 1)
        self.bandX_spinBox.setObjectName("bandX_spinBox")
        self.gridLayout_38.addWidget(self.bandX_spinBox, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_38, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.remove_Signature_Button = QtWidgets.QToolButton(self.frame)
        self.remove_Signature_Button.setStyleSheet("margin: 0px;padding: 0px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_Signature_Button.setIcon(icon4)
        self.remove_Signature_Button.setIconSize(QtCore.QSize(22, 22))
        self.remove_Signature_Button.setObjectName("remove_Signature_Button")
        self.horizontalLayout.addWidget(self.remove_Signature_Button)
        self.plot_temp_ROI_pushButton = QtWidgets.QToolButton(self.frame)
        self.plot_temp_ROI_pushButton.setStyleSheet("margin: 0px;padding: 0px;")
        self.plot_temp_ROI_pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_scatter_raster_temp_ROI.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plot_temp_ROI_pushButton.setIcon(icon5)
        self.plot_temp_ROI_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.plot_temp_ROI_pushButton.setObjectName("plot_temp_ROI_pushButton")
        self.horizontalLayout.addWidget(self.plot_temp_ROI_pushButton)
        self.gridLayout_6.addLayout(self.horizontalLayout, 7, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 1, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_25 = QtWidgets.QLabel(ScatterPlot)
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color : #5a5a5a; color : white; font: bold")
        self.label_25.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_25.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 2)

        self.retranslateUi(ScatterPlot)
        self.precision_comboBox.setCurrentIndex(1)
        self.colormap_comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ScatterPlot)

    def retranslateUi(self, ScatterPlot):
        _translate = QtCore.QCoreApplication.translate
        ScatterPlot.setWindowTitle(_translate("ScatterPlot", "SCP: Scatter Plot"))
        self.scatter_list_plot_tableWidget.setSortingEnabled(True)
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ScatterPlot", "S"))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ScatterPlot", "MC ID"))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ScatterPlot", "MC Name"))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ScatterPlot", "C ID"))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ScatterPlot", "C Name"))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ScatterPlot", "Color"))
        self.label_49.setText(_translate("ScatterPlot", "Calculate"))
        self.scatter_ROI_Button.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Calculate scatter plot</p></body></html>"))
        self.precision_checkBox.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Use custom decimal precision</p></body></html>"))
        self.precision_checkBox.setText(_translate("ScatterPlot", "Precision"))
        self.precision_comboBox.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Select decimal precision:</p><p>4 = 10^<span style=\" vertical-align:super;\">−4</span></p><p>3 = 10^<span style=\" vertical-align:super;\">−3</span></p><p>2 = 10^<span style=\" vertical-align:super;\">−2</span></p><p>1 = 10^<span style=\" vertical-align:super;\">−1</span></p><p>0 = 1</p><p>-1 = 10</p><p>-2 = 10^<span style=\" vertical-align:super;\">2</span></p><p>-3 = 10^<span style=\" vertical-align:super;\">3</span></p></body></html>"))
        self.precision_comboBox.setItemText(0, _translate("ScatterPlot", "4"))
        self.precision_comboBox.setItemText(1, _translate("ScatterPlot", "3"))
        self.precision_comboBox.setItemText(2, _translate("ScatterPlot", "2"))
        self.precision_comboBox.setItemText(3, _translate("ScatterPlot", "1"))
        self.precision_comboBox.setItemText(4, _translate("ScatterPlot", "0"))
        self.precision_comboBox.setItemText(5, _translate("ScatterPlot", "-1"))
        self.precision_comboBox.setItemText(6, _translate("ScatterPlot", "-2"))
        self.precision_comboBox.setItemText(7, _translate("ScatterPlot", "-3"))
        self.fitToAxes_pushButton_2.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Automatically fit the plot to data</p></body></html>"))
        self.save_plot_pushButton_2.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Save the plot to file (jpg, png, pdf)</p></body></html>"))
        self.label_27.setText(_translate("ScatterPlot", " Plot"))
        self.label_50.setText(_translate("ScatterPlot", "Colormap"))
        self.colormap_comboBox.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Select a colormap for selected rows</p></body></html>"))
        self.value_label_2.setText(_translate("ScatterPlot", "x=0.000000 y=0.000000"))
        self.label_48.setText(_translate("ScatterPlot", "Band Y"))
        self.bandY_spinBox.setToolTip(_translate("ScatterPlot", "<html><head/><body><p align=\"justify\">Band Y</p></body></html>"))
        self.label_46.setText(_translate("ScatterPlot", "Band X"))
        self.bandX_spinBox.setToolTip(_translate("ScatterPlot", "<html><head/><body><p align=\"justify\">Band X</p></body></html>"))
        self.remove_Signature_Button.setToolTip(_translate("ScatterPlot", "<html><head/><body><p >Delete row</p></body></html>"))
        self.remove_Signature_Button.setText(_translate("ScatterPlot", "Plot"))
        self.plot_temp_ROI_pushButton.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Calculate scatter plot from temporary ROI</p></body></html>"))
        self.label_25.setText(_translate("ScatterPlot", " Scatter list"))
from .scatterwidget2 import ScatterWidget2
from . import resources_rc
