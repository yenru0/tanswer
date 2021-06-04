import os

from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Slot

from gui.ui.fileinfo import Ui_fileinfo
from reader.structure import TanswerDataStruct
import function.futil as futil


class FileInfo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_fileinfo()
        self.ui.setupUi(self)

        sp_retain = self.sizePolicy()
        sp_retain.setRetainSizeWhenHidden(True)
        self.setSizePolicy(sp_retain)
        self.disable()

        self.launched = self.ui.btn_execute.clicked
        self.launched.connect(self.disable)

        self.ui.btn_save.clicked.connect(lambda: futil.save_tnw_dataset(self.tds))

        self.filepath: str = ""
        self.tds: TanswerDataStruct = None

    def load_file(self, filepath: str, tds: TanswerDataStruct):
        self.tds = tds
        self.filepath = filepath
        if futil.is_tnw_exists_in_dataset(tds.name):
            self.ui.btn_save.setEnabled(False)
        else:
            self.ui.btn_save.setEnabled(True)

        self.ui.lbl_filename.setText(tds.name)
        self.ui.lbl_info_1.setText(f"{self.tds.description if self.tds.description else 'empty description'}")
        self.ui.lbl_info_2.setText(f"글자수: {tds.reader.src_size}\n스테이지 수: {tds.stage_size}\n")

        self.enable()

    def enable(self):
        # self.setEnabled(True)
        self.show()

    def disable(self):
        # self.setEnabled(False)
        self.hide()
