from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Slot

from gui.ui.fileinfo import Ui_fileinfo
from reader.structure import TanswerDataStruct


class FileInfo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_fileinfo()
        self.ui.setupUi(self)

        sp_retain = self.sizePolicy()
        sp_retain.setRetainSizeWhenHidden(True)
        self.setSizePolicy(sp_retain)
        self.disable()

        self.launched = self.ui.btn_info.clicked
        self.launched.connect(self.disable)

    def load_file(self, filename: str, tds: TanswerDataStruct):
        self.enable()
        self.ui.lbl_filename.setText(filename)

    def enable(self):
        self.setEnabled(True)
        self.show()

    def disable(self):
        self.setEnabled(False)
        self.hide()
