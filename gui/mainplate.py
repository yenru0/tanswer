import numpy as np
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from gui.ui.plate import Ui_MainPlate
from gui.fileinfo import FileInfo
from reader.read import Reader
from reader.exceptions import TReaderException
from reader.structure import TanswerDataStruct
from function.nowprocess import NowProcess


class MainPlate(QMainWindow):
    def __init__(self, parent=None, ):
        super().__init__(parent, )
        self.ui = Ui_MainPlate()
        self.ui.setupUi(self)
        self.setWindowTitle("Tanswer Dev")

        self.now = NowProcess()
        self._tds = None
        self._weight = None

        self.cached = 0

        # title
        self.ui.btn_title_btn1.clicked.connect(self.go_faststart)
        self.ui.btn_title_btn2.clicked.connect(self.go_select)
        self.ui.btn_title_btn3.clicked.connect(self.go_option)
        self.ui.btn_title_btn4.clicked.connect(self.go_info)

        # fast start
        self.ui.fileinfo_fs = FileInfo(self.ui.frame_fs_fileinfo)
        self.ui.frame_fs_fileinfo.layout().addWidget(self.ui.fileinfo_fs)
        self.ui.btn_filebrowse.clicked.connect(lambda: self.filebrowse(self.ui.fileinfo_fs))
        self.ui.fileinfo_fs.launched.connect(self.go_tanswermenu)

        # select
        self.ui.fileinfo_sl = FileInfo(self.ui.frame_sl_fileinfo)
        self.ui.frame_sl_fileinfo.layout().addWidget(self.ui.fileinfo_sl)

        # tanswermenu
        self.ui.btn_tanswermenu_execute.clicked.connect(self.go_tanswering)
        self.ui.btn_tanswermenu_weight_browse.clicked.connect(
            lambda: self.weightbrowse(self.ui.lbl_tanswermenu_weight_browse))

        # tanswering
        self.ui.btn_tanswering_input.clicked.connect(self.tanswering_submit)
        ###

        # side
        self.ui.btn_side_1.clicked.connect(self.go_title)
        # self.ui.btn_side_2.clicked.connect()
        self.ui.btn_side_3.clicked.connect(self.go_info)

        self.show()

    def go_title(self):
        self.ui.front.setCurrentIndex(0)

    def go_faststart(self):
        self.ui.front.setCurrentIndex(1)

    def go_select(self):
        self.ui.front.setCurrentIndex(2)

    def go_option(self):
        self.ui.front.setCurrentIndex(3)

    def go_info(self):
        self.ui.front.setCurrentIndex(4)

    def go_tanswermenu(self):
        self.ui.front.setCurrentIndex(6)

    def go_tanswering(self):
        if self.now.is_launched:
            reply = QMessageBox.question(
                self, "확인",
                "진행 중인 것이 있는 것 같습니다.\n진행 중인 것이 모두 삭제됩니다. 그래도 시작하시겠습니까?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                pass
            else:
                return

        else:
            pass
        if isinstance(self._tds, TanswerDataStruct) and \
                (isinstance(self._weight, np.ndarray) or self._weight is None):
            self.now.launch(self._tds, self._weight)
        else:
            print("error")
            return

        self.tanswering_clear()
        self.tanswering_display()
        self.ui.front.setCurrentIndex(5)

    def go_tanswring_resume(self):
        self.ui.front.setCurrentIndex(5)

    def go_result(self):
        self.ui.lbl_result.setText(str(self.now.replies))
        self.ui.front.setCurrentIndex(7)

    def filebrowse(self, fileinfo: FileInfo):
        fname, _ = QFileDialog.getOpenFileName(self)
        if not fname:
            return
        with open(fname, "r", encoding='utf-8') as f:
            t = self.fileread(f)
        if t is False:
            QMessageBox.warning(self, "파일 오류", "읽을 수 없는 파일입니다.")
            fileinfo.disable()
            return
        else:
            fileinfo.load_file(fname, t)
            self._tds = t
            return

    def fileselect(self, index: int):
        pass

    def fileread(self, f) -> [bool, TanswerDataStruct]:
        """
        False -> failure
        TDS -> Success
        :param f:
        :return:
        """
        read = Reader(f.read())
        try:
            read.read()
        except TReaderException:
            return False

        tds = TanswerDataStruct(read)
        return tds

    def weightbrowse(self, label):
        fname, _ = QFileDialog.getOpenFileName(self)
        if not fname:
            return

        self._weight = None
        label.setText(fname)
        return

    def tanswering_clear(self):
        self.ui.text_tanswering_view.clear()
        self.ui.ledit_tanswering_input.clear()

    def tanswering_submit(self):
        self.tanswering_clear()
        if self.now.progress(self.ui.ledit_tanswering_input.text()):
            self.go_result()
        else:
            self.tanswering_display()

    def tanswering_display(self):
        self.now.display(self.ui.text_tanswering_view, self.ui.progress_tanswering,
                         self.ui.lbl_tanswering_name, self.ui.lbl_tanswering_vec)
