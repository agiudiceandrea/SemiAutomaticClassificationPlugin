# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_semiautomaticclassificationplugin_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SCP_Widget(object):
    def setupUi(self, SCP_Widget):
        SCP_Widget.setObjectName("SCP_Widget")
        SCP_Widget.resize(609, 355)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SCP_Widget.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(SCP_Widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.main_widget = QtWidgets.QWidget(SCP_Widget)
        self.main_widget.setObjectName("main_widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidget = QtWidgets.QListWidget(self.main_widget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_5.addWidget(self.listWidget, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.main_widget, 0, 0, 1, 1)
        self.select_all_toolButton = QtWidgets.QToolButton(SCP_Widget)
        self.select_all_toolButton.setStyleSheet("margin: 0px;padding: 0px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_select_all.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_all_toolButton.setIcon(icon1)
        self.select_all_toolButton.setIconSize(QtCore.QSize(22, 22))
        self.select_all_toolButton.setObjectName("select_all_toolButton")
        self.gridLayout_3.addWidget(self.select_all_toolButton, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(SCP_Widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(SCP_Widget)
        self.buttonBox.accepted.connect(SCP_Widget.accept) # type: ignore
        self.buttonBox.rejected.connect(SCP_Widget.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SCP_Widget)

    def retranslateUi(self, SCP_Widget):
        _translate = QtCore.QCoreApplication.translate
        SCP_Widget.setWindowTitle(_translate("SCP_Widget", "Semi-Automatic Classification Plugin"))
        self.select_all_toolButton.setToolTip(_translate("SCP_Widget", "<html><head/><body><p>Select all</p></body></html>"))
        self.select_all_toolButton.setText(_translate("SCP_Widget", "Plot"))
from . import resources_rc