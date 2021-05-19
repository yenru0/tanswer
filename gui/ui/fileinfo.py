# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileinfo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_fileinfo(object):
    def setupUi(self, fileinfo):
        if not fileinfo.objectName():
            fileinfo.setObjectName(u"fileinfo")
        fileinfo.resize(531, 297)
        self.horizontalLayout = QHBoxLayout(fileinfo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_filename = QLabel(fileinfo)
        self.lbl_filename.setObjectName(u"lbl_filename")
        self.lbl_filename.setAlignment(Qt.AlignCenter)
        self.lbl_filename.setWordWrap(True)

        self.horizontalLayout.addWidget(self.lbl_filename)

        self.frame_info = QFrame(fileinfo)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_info_1 = QLabel(self.frame_info)
        self.lbl_info_1.setObjectName(u"lbl_info_1")

        self.verticalLayout.addWidget(self.lbl_info_1)

        self.lbl_info_2 = QLabel(self.frame_info)
        self.lbl_info_2.setObjectName(u"lbl_info_2")

        self.verticalLayout.addWidget(self.lbl_info_2)

        self.btn_info = QPushButton(self.frame_info)
        self.btn_info.setObjectName(u"btn_info")
        self.btn_info.setMinimumSize(QSize(200, 0))
        self.btn_info.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout.addWidget(self.btn_info, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_info)


        self.retranslateUi(fileinfo)

        QMetaObject.connectSlotsByName(fileinfo)
    # setupUi

    def retranslateUi(self, fileinfo):
        fileinfo.setWindowTitle(QCoreApplication.translate("fileinfo", u"Form", None))
        self.lbl_filename.setText(QCoreApplication.translate("fileinfo", u"\ud30c\uc77c\uc774\ub984", None))
        self.lbl_info_1.setText(QCoreApplication.translate("fileinfo", u"TextLabel", None))
        self.lbl_info_2.setText(QCoreApplication.translate("fileinfo", u"TextLabel", None))
        self.btn_info.setText(QCoreApplication.translate("fileinfo", u"\uc2e4\ud589", None))
    # retranslateUi

