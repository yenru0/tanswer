# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plate.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainPlate(object):
    def setupUi(self, MainPlate):
        if not MainPlate.objectName():
            MainPlate.setObjectName(u"MainPlate")
        MainPlate.resize(737, 588)
        self.centralwidget = QWidget(MainPlate)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.layout_main = QHBoxLayout()
        self.layout_main.setObjectName(u"layout_main")
        self.frame_side = QFrame(self.centralwidget)
        self.frame_side.setObjectName(u"frame_side")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_side.sizePolicy().hasHeightForWidth())
        self.frame_side.setSizePolicy(sizePolicy)
        self.frame_side.setMinimumSize(QSize(100, 0))
        self.frame_side.setMaximumSize(QSize(100, 16777215))
        self.frame_side.setFrameShape(QFrame.StyledPanel)
        self.frame_side.setFrameShadow(QFrame.Sunken)
        self.frame_side.setLineWidth(2)
        self.verticalLayout = QVBoxLayout(self.frame_side)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 10)
        self.layout_side = QVBoxLayout()
        self.layout_side.setObjectName(u"layout_side")
        self.btn_side_1 = QPushButton(self.frame_side)
        self.btn_side_1.setObjectName(u"btn_side_1")
        self.btn_side_1.setMinimumSize(QSize(70, 70))
        self.btn_side_1.setMaximumSize(QSize(70, 70))

        self.layout_side.addWidget(self.btn_side_1, 0, Qt.AlignHCenter)

        self.btn_side_2 = QPushButton(self.frame_side)
        self.btn_side_2.setObjectName(u"btn_side_2")
        self.btn_side_2.setMinimumSize(QSize(70, 70))
        self.btn_side_2.setMaximumSize(QSize(70, 70))

        self.layout_side.addWidget(self.btn_side_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.btn_side_3 = QPushButton(self.frame_side)
        self.btn_side_3.setObjectName(u"btn_side_3")
        self.btn_side_3.setMinimumSize(QSize(70, 70))
        self.btn_side_3.setMaximumSize(QSize(70, 70))

        self.layout_side.addWidget(self.btn_side_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.vspacer_side = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_side.addItem(self.vspacer_side)


        self.verticalLayout.addLayout(self.layout_side)

        self.lbl_side_user = QLabel(self.frame_side)
        self.lbl_side_user.setObjectName(u"lbl_side_user")

        self.verticalLayout.addWidget(self.lbl_side_user)


        self.layout_main.addWidget(self.frame_side)

        self.frame_front = QFrame(self.centralwidget)
        self.frame_front.setObjectName(u"frame_front")
        self.frame_front.setFrameShape(QFrame.StyledPanel)
        self.frame_front.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_front)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.front = QStackedWidget(self.frame_front)
        self.front.setObjectName(u"front")
        self.page_title = QWidget()
        self.page_title.setObjectName(u"page_title")
        self.verticalLayout_4 = QVBoxLayout(self.page_title)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_title = QLabel(self.page_title)
        self.lbl_title.setObjectName(u"lbl_title")
        font = QFont()
        font.setFamily(u"Malgun Gothic")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_title)

        self.frame_title_btns = QFrame(self.page_title)
        self.frame_title_btns.setObjectName(u"frame_title_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_title_btns.sizePolicy().hasHeightForWidth())
        self.frame_title_btns.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Malgun Gothic")
        font1.setPointSize(11)
        self.frame_title_btns.setFont(font1)
        self.frame_title_btns.setFrameShape(QFrame.NoFrame)
        self.frame_title_btns.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_title_btns)
        self.verticalLayout_5.setSpacing(25)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.btn_title_btn1 = QPushButton(self.frame_title_btns)
        self.btn_title_btn1.setObjectName(u"btn_title_btn1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_title_btn1.sizePolicy().hasHeightForWidth())
        self.btn_title_btn1.setSizePolicy(sizePolicy2)
        self.btn_title_btn1.setMinimumSize(QSize(200, 40))
        self.btn_title_btn1.setMaximumSize(QSize(200, 40))

        self.verticalLayout_5.addWidget(self.btn_title_btn1)

        self.btn_title_btn4 = QPushButton(self.frame_title_btns)
        self.btn_title_btn4.setObjectName(u"btn_title_btn4")
        sizePolicy2.setHeightForWidth(self.btn_title_btn4.sizePolicy().hasHeightForWidth())
        self.btn_title_btn4.setSizePolicy(sizePolicy2)
        self.btn_title_btn4.setMinimumSize(QSize(200, 40))
        self.btn_title_btn4.setMaximumSize(QSize(200, 40))

        self.verticalLayout_5.addWidget(self.btn_title_btn4)

        self.btn_title_btn2 = QPushButton(self.frame_title_btns)
        self.btn_title_btn2.setObjectName(u"btn_title_btn2")
        sizePolicy2.setHeightForWidth(self.btn_title_btn2.sizePolicy().hasHeightForWidth())
        self.btn_title_btn2.setSizePolicy(sizePolicy2)
        self.btn_title_btn2.setMinimumSize(QSize(200, 40))
        self.btn_title_btn2.setMaximumSize(QSize(200, 40))

        self.verticalLayout_5.addWidget(self.btn_title_btn2)

        self.btn_title_btn3 = QPushButton(self.frame_title_btns)
        self.btn_title_btn3.setObjectName(u"btn_title_btn3")
        sizePolicy2.setHeightForWidth(self.btn_title_btn3.sizePolicy().hasHeightForWidth())
        self.btn_title_btn3.setSizePolicy(sizePolicy2)
        self.btn_title_btn3.setMinimumSize(QSize(200, 40))
        self.btn_title_btn3.setMaximumSize(QSize(200, 40))

        self.verticalLayout_5.addWidget(self.btn_title_btn3)


        self.verticalLayout_4.addWidget(self.frame_title_btns, 0, Qt.AlignHCenter)

        self.verticalLayout_4.setStretch(0, 3)
        self.front.addWidget(self.page_title)
        self.page_faststart = QWidget()
        self.page_faststart.setObjectName(u"page_faststart")
        self.verticalLayout_7 = QVBoxLayout(self.page_faststart)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lbl_faststart = QLabel(self.page_faststart)
        self.lbl_faststart.setObjectName(u"lbl_faststart")
        font2 = QFont()
        font2.setPointSize(30)
        self.lbl_faststart.setFont(font2)
        self.lbl_faststart.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lbl_faststart)

        self.frame_filebrowse = QFrame(self.page_faststart)
        self.frame_filebrowse.setObjectName(u"frame_filebrowse")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_filebrowse.sizePolicy().hasHeightForWidth())
        self.frame_filebrowse.setSizePolicy(sizePolicy3)
        self.frame_filebrowse.setFrameShape(QFrame.StyledPanel)
        self.frame_filebrowse.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_filebrowse)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_filebrowse = QPushButton(self.frame_filebrowse)
        self.btn_filebrowse.setObjectName(u"btn_filebrowse")

        self.horizontalLayout.addWidget(self.btn_filebrowse, 0, Qt.AlignLeft)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout_7.addWidget(self.frame_filebrowse)

        self.frame_fs_fileinfo = QFrame(self.page_faststart)
        self.frame_fs_fileinfo.setObjectName(u"frame_fs_fileinfo")
        self.frame_fs_fileinfo.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_fs_fileinfo.sizePolicy().hasHeightForWidth())
        self.frame_fs_fileinfo.setSizePolicy(sizePolicy4)
        self.frame_fs_fileinfo.setFrameShape(QFrame.StyledPanel)
        self.frame_fs_fileinfo.setFrameShadow(QFrame.Sunken)
        self.frame_fs_fileinfo.setLineWidth(2)
        self.gridLayout = QGridLayout(self.frame_fs_fileinfo)
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout_7.addWidget(self.frame_fs_fileinfo)

        self.verticalLayout_7.setStretch(0, 5)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_7.setStretch(2, 6)
        self.front.addWidget(self.page_faststart)
        self.page_select = QWidget()
        self.page_select.setObjectName(u"page_select")
        self.verticalLayout_6 = QVBoxLayout(self.page_select)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_select = QFrame(self.page_select)
        self.frame_select.setObjectName(u"frame_select")
        self.frame_select.setFrameShape(QFrame.StyledPanel)
        self.frame_select.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_select)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lbl_select = QLabel(self.frame_select)
        self.lbl_select.setObjectName(u"lbl_select")

        self.verticalLayout_8.addWidget(self.lbl_select)

        self.list_select = QListWidget(self.frame_select)
        self.list_select.setObjectName(u"list_select")

        self.verticalLayout_8.addWidget(self.list_select)


        self.verticalLayout_6.addWidget(self.frame_select)

        self.frame_sl_fileinfo = QFrame(self.page_select)
        self.frame_sl_fileinfo.setObjectName(u"frame_sl_fileinfo")
        self.frame_sl_fileinfo.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_sl_fileinfo.sizePolicy().hasHeightForWidth())
        self.frame_sl_fileinfo.setSizePolicy(sizePolicy5)
        self.frame_sl_fileinfo.setFrameShape(QFrame.StyledPanel)
        self.frame_sl_fileinfo.setFrameShadow(QFrame.Sunken)
        self.frame_sl_fileinfo.setLineWidth(2)
        self.gridLayout_2 = QGridLayout(self.frame_sl_fileinfo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout_6.addWidget(self.frame_sl_fileinfo)

        self.verticalLayout_6.setStretch(0, 6)
        self.verticalLayout_6.setStretch(1, 6)
        self.front.addWidget(self.page_select)
        self.page_option = QWidget()
        self.page_option.setObjectName(u"page_option")
        self.front.addWidget(self.page_option)
        self.page_info = QWidget()
        self.page_info.setObjectName(u"page_info")
        self.verticalLayout_3 = QVBoxLayout(self.page_info)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_info_version = QFrame(self.page_info)
        self.frame_info_version.setObjectName(u"frame_info_version")
        self.frame_info_version.setFrameShape(QFrame.StyledPanel)
        self.frame_info_version.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_info_version)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 16, -1, -1)
        self.lbl_info_version_name = QLabel(self.frame_info_version)
        self.lbl_info_version_name.setObjectName(u"lbl_info_version_name")

        self.gridLayout_3.addWidget(self.lbl_info_version_name, 0, 0, 1, 1)

        self.lbl_info_version_version = QLabel(self.frame_info_version)
        self.lbl_info_version_version.setObjectName(u"lbl_info_version_version")
        self.lbl_info_version_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lbl_info_version_version, 0, 1, 1, 1)

        self.lbl_info_version_by = QLabel(self.frame_info_version)
        self.lbl_info_version_by.setObjectName(u"lbl_info_version_by")
        self.lbl_info_version_by.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lbl_info_version_by, 1, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)

        self.verticalLayout_3.addWidget(self.frame_info_version, 0, Qt.AlignTop)

        self.front.addWidget(self.page_info)
        self.page_tanswering = QWidget()
        self.page_tanswering.setObjectName(u"page_tanswering")
        self.verticalLayout_9 = QVBoxLayout(self.page_tanswering)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.layout_tanswering_info = QHBoxLayout()
        self.layout_tanswering_info.setObjectName(u"layout_tanswering_info")
        self.layout_tanswering_info.setContentsMargins(5, 9, 3, 5)
        self.lbl_tanswering_name = QLabel(self.page_tanswering)
        self.lbl_tanswering_name.setObjectName(u"lbl_tanswering_name")

        self.layout_tanswering_info.addWidget(self.lbl_tanswering_name)

        self.lbl_tanswering_vec = QLabel(self.page_tanswering)
        self.lbl_tanswering_vec.setObjectName(u"lbl_tanswering_vec")
        self.lbl_tanswering_vec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.layout_tanswering_info.addWidget(self.lbl_tanswering_vec)


        self.verticalLayout_9.addLayout(self.layout_tanswering_info)

        self.text_tanswering_view = QTextBrowser(self.page_tanswering)
        self.text_tanswering_view.setObjectName(u"text_tanswering_view")

        self.verticalLayout_9.addWidget(self.text_tanswering_view)

        self.frame_tanswering_input = QFrame(self.page_tanswering)
        self.frame_tanswering_input.setObjectName(u"frame_tanswering_input")
        self.frame_tanswering_input.setFrameShape(QFrame.StyledPanel)
        self.frame_tanswering_input.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_tanswering_input)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, -1, 1, -1)
        self.ledit_tanswering_input = QLineEdit(self.frame_tanswering_input)
        self.ledit_tanswering_input.setObjectName(u"ledit_tanswering_input")
        self.ledit_tanswering_input.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.ledit_tanswering_input)

        self.btn_tanswering_input = QPushButton(self.frame_tanswering_input)
        self.btn_tanswering_input.setObjectName(u"btn_tanswering_input")
        self.btn_tanswering_input.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.btn_tanswering_input)


        self.verticalLayout_9.addWidget(self.frame_tanswering_input)

        self.progress_tanswering = QProgressBar(self.page_tanswering)
        self.progress_tanswering.setObjectName(u"progress_tanswering")
        self.progress_tanswering.setValue(24)

        self.verticalLayout_9.addWidget(self.progress_tanswering)

        self.front.addWidget(self.page_tanswering)
        self.page_tanswermenu = QWidget()
        self.page_tanswermenu.setObjectName(u"page_tanswermenu")
        self.gridLayout_4 = QGridLayout(self.page_tanswermenu)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(24)
        self.gridLayout_4.setVerticalSpacing(9)
        self.lbl_tanswermenu_wil = QLabel(self.page_tanswermenu)
        self.lbl_tanswermenu_wil.setObjectName(u"lbl_tanswermenu_wil")

        self.gridLayout_4.addWidget(self.lbl_tanswermenu_wil, 0, 0, 1, 1)

        self.spbox_tanswermenu_wil = QSpinBox(self.page_tanswermenu)
        self.spbox_tanswermenu_wil.setObjectName(u"spbox_tanswermenu_wil")

        self.gridLayout_4.addWidget(self.spbox_tanswermenu_wil, 0, 1, 1, 1)

        self.lbl_tanswermenu_weight = QLabel(self.page_tanswermenu)
        self.lbl_tanswermenu_weight.setObjectName(u"lbl_tanswermenu_weight")

        self.gridLayout_4.addWidget(self.lbl_tanswermenu_weight, 1, 0, 1, 1)

        self.frame_tanswermenu_weight = QFrame(self.page_tanswermenu)
        self.frame_tanswermenu_weight.setObjectName(u"frame_tanswermenu_weight")
        self.frame_tanswermenu_weight.setFrameShape(QFrame.StyledPanel)
        self.frame_tanswermenu_weight.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_tanswermenu_weight)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_tanswermenu_weight_browse = QPushButton(self.frame_tanswermenu_weight)
        self.btn_tanswermenu_weight_browse.setObjectName(u"btn_tanswermenu_weight_browse")

        self.horizontalLayout_4.addWidget(self.btn_tanswermenu_weight_browse, 0, Qt.AlignLeft)

        self.lbl_tanswermenu_weight_browse = QLabel(self.frame_tanswermenu_weight)
        self.lbl_tanswermenu_weight_browse.setObjectName(u"lbl_tanswermenu_weight_browse")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lbl_tanswermenu_weight_browse.sizePolicy().hasHeightForWidth())
        self.lbl_tanswermenu_weight_browse.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.lbl_tanswermenu_weight_browse)


        self.gridLayout_4.addWidget(self.frame_tanswermenu_weight, 1, 1, 1, 1)

        self.vspacer_tanswermenu = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.vspacer_tanswermenu, 2, 1, 1, 1)

        self.btn_tanswermenu_execute = QPushButton(self.page_tanswermenu)
        self.btn_tanswermenu_execute.setObjectName(u"btn_tanswermenu_execute")
        sizePolicy7 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_tanswermenu_execute.sizePolicy().hasHeightForWidth())
        self.btn_tanswermenu_execute.setSizePolicy(sizePolicy7)
        self.btn_tanswermenu_execute.setMinimumSize(QSize(150, 25))
        self.btn_tanswermenu_execute.setMaximumSize(QSize(150, 25))
        self.btn_tanswermenu_execute.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.btn_tanswermenu_execute, 3, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 10)
        self.front.addWidget(self.page_tanswermenu)
        self.page_result = QWidget()
        self.page_result.setObjectName(u"page_result")
        self.gridLayout_6 = QGridLayout(self.page_result)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lbl_result = QLabel(self.page_result)
        self.lbl_result.setObjectName(u"lbl_result")
        self.lbl_result.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbl_result.setWordWrap(True)

        self.gridLayout_6.addWidget(self.lbl_result, 0, 0, 1, 1)

        self.front.addWidget(self.page_result)

        self.verticalLayout_2.addWidget(self.front)


        self.layout_main.addWidget(self.frame_front)


        self.gridLayout_5.addLayout(self.layout_main, 0, 0, 1, 1)

        MainPlate.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainPlate)

        self.front.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPlate)
    # setupUi

    def retranslateUi(self, MainPlate):
        MainPlate.setWindowTitle(QCoreApplication.translate("MainPlate", u"MainWindow", None))
        self.btn_side_1.setText(QCoreApplication.translate("MainPlate", u"\uba54\uc778", None))
        self.btn_side_2.setText(QCoreApplication.translate("MainPlate", u"\ud0e0\uc11c \uba54\ub274", None))
        self.btn_side_3.setText(QCoreApplication.translate("MainPlate", u"\uc815\ubcf4", None))
        self.lbl_side_user.setText(QCoreApplication.translate("MainPlate", u"user_info", None))
        self.lbl_title.setText(QCoreApplication.translate("MainPlate", u"Tanswer Dev", None))
        self.btn_title_btn1.setText(QCoreApplication.translate("MainPlate", u"\ube60\ub978 \uc2dc\uc791", None))
        self.btn_title_btn4.setText(QCoreApplication.translate("MainPlate", u"\uc2dc\uc791", None))
        self.btn_title_btn2.setText(QCoreApplication.translate("MainPlate", u"\uc635\uc158", None))
        self.btn_title_btn3.setText(QCoreApplication.translate("MainPlate", u"\uc815\ubcf4", None))
        self.lbl_faststart.setText(QCoreApplication.translate("MainPlate", u"\ube60\ub978 \uc2dc\uc791", None))
        self.btn_filebrowse.setText(QCoreApplication.translate("MainPlate", u"\ud30c\uc77c \ubd88\ub7ec\uc624\uae30", None))
        self.lbl_select.setText(QCoreApplication.translate("MainPlate", u"\uc800\uc7a5\ub41c \ud30c\uc77c \uc120\ud0dd", None))
        self.lbl_info_version_name.setText(QCoreApplication.translate("MainPlate", u"Tanswer Dev", None))
        self.lbl_info_version_version.setText(QCoreApplication.translate("MainPlate", u"version", None))
        self.lbl_info_version_by.setText(QCoreApplication.translate("MainPlate", u"by yenru0604@gmail.com", None))
        self.lbl_tanswering_name.setText(QCoreApplication.translate("MainPlate", u"<name>", None))
        self.lbl_tanswering_vec.setText(QCoreApplication.translate("MainPlate", u"TextLabel", None))
        self.ledit_tanswering_input.setText(QCoreApplication.translate("MainPlate", u"$input", None))
        self.btn_tanswering_input.setText(QCoreApplication.translate("MainPlate", u"\uc785\ub825", None))
        self.lbl_tanswermenu_wil.setText(QCoreApplication.translate("MainPlate", u"\uac1c\uc218", None))
        self.lbl_tanswermenu_weight.setText(QCoreApplication.translate("MainPlate", u"\uac00\uc911", None))
        self.btn_tanswermenu_weight_browse.setText(QCoreApplication.translate("MainPlate", u"\uac00\uc911\uce58 \uac80\uc0c9", None))
        self.lbl_tanswermenu_weight_browse.setText(QCoreApplication.translate("MainPlate", u"\ud30c\uc77c\uc774 \uc5c6\uc2b5\ub2c8\ub2e4.", None))
        self.btn_tanswermenu_execute.setText(QCoreApplication.translate("MainPlate", u"\uc2e4\ud589", None))
        self.lbl_result.setText(QCoreApplication.translate("MainPlate", u"TextLabel", None))
    # retranslateUi

