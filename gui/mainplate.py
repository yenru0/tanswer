import numpy as np
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QListWidgetItem, QTableWidgetItem, QHeaderView
from PySide2.QtCore import Qt

from gui.ui.plate import Ui_MainPlate
from gui.fileinfo import FileInfo
from reader.read import Reader
from reader.exceptions import TReaderException
from reader.structure import TanswerDataStruct
from function.nows import NowProcess
import function.const as const
import function.futil as futil


class MainPlate(QMainWindow):
    def __init__(self, parent=None, ):
        super().__init__(parent, )
        self.ui = Ui_MainPlate()
        self.ui.setupUi(self)
        self.setWindowTitle("Tanswer Dev")

        self.now = NowProcess()
        self._tds: TanswerDataStruct = None
        self._weight: np.ndarray = None

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
        self.ui.fileinfo_sl.launched.connect(self.go_tanswermenu)

        def list_prevent_multiple(item: QListWidgetItem, fileinfo: FileInfo):
            t = [self.ui.list_select.item(i) for i in range(self.ui.list_select.count())
                 if self.ui.list_select.item(i).checkState() == Qt.Checked]
            if len(t) > 1:
                for i in t:
                    if i != item:
                        i.setCheckState(Qt.Unchecked)
            if item.checkState() == Qt.Checked:
                self.fileload(fileinfo, item.data(Qt.UserRole))
            else:
                fileinfo.disable()

        self.ui.list_select.itemChanged.connect(lambda x: list_prevent_multiple(x, self.ui.fileinfo_sl))

        # tanswermenu
        self.ui.btn_tanswermenu_execute.clicked.connect(self.go_tanswering)
        self.ui.btn_tanswermenu_weight_browse.clicked.connect(
            lambda: self.weightbrowse(self.ui.lbl_tanswermenu_weight_browse))
        self.ui.btn_tanswermenu_weight_reset.clicked.connect(
            self.weight_reset
        )
        self.ui.list_tanswermenu_stages.itemClicked.connect(
            lambda item: item.setCheckState(Qt.Unchecked if item.checkState() == Qt.Checked else Qt.Checked)
        )

        # tanswering
        self.ui.btn_tanswering_input.clicked.connect(self.tanswering_submit)
        self.ui.ledit_tanswering_input.returnPressed.connect(lambda: self.ui.btn_tanswering_input.click())

        # result
        self.ui.btn_result_goto_main.clicked.connect(self.go_title)
        self.ui.btn_result_goto_tanswermenu.clicked.connect(self.go_tanswermenu)

        self.ui.btn_save_receipt.setEnabled(False)
        self.ui.btn_save_weight.clicked.connect(self.result_weight_apply)

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
        self.ui.list_select.clear()
        for name, path in futil.get_name_path_from_dataset():
            item = QListWidgetItem(f"{name}")
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            item.setData(Qt.UserRole, path)
            self.ui.list_select.addItem(item)

        self.ui.front.setCurrentIndex(2)

    def go_option(self):
        self.ui.front.setCurrentIndex(3)

    def go_info(self):
        self.ui.front.setCurrentIndex(4)

    def go_tanswermenu(self):
        self._weight = None
        self.ui.list_tanswermenu_stages.clear()
        for i, stg in enumerate(self._tds.stage_list):
            item = QListWidgetItem(f"{stg}")
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Checked)
            item.setData(Qt.UserRole, i)
            self.ui.list_tanswermenu_stages.addItem(item)

        self.ui.front.setCurrentIndex(6)

    def go_tanswering(self):
        # 진행 초기화
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

        if not isinstance(self._tds, TanswerDataStruct):
            print("tds is not prepared")
            return
        else:
            if isinstance(self._weight, np.ndarray):
                if not self._tds.valid(self._weight):
                    reply = QMessageBox.question(
                        self, "옳지 않은 가중치",
                        "이 TDS에 맞지 않는 가중치입니다.\n기본 파일 가중치로 시작하시겠습니까?",
                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                    )
                    if reply == QMessageBox.Yes:
                        self._weight = None
                    else:
                        return
            stgs = [i for i in range(self._tds.stage_size) if
                    self.ui.list_tanswermenu_stages.item(i).checkState() == Qt.Checked]
            self.now.launch(self._tds, self._weight, self.ui.spbox_tanswermenu_wil.value(), stgs)

        self.tanswering_clear()
        self.tanswering_display()
        self.ui.front.setCurrentIndex(5)

    def go_tanswring_resume(self):
        self.ui.front.setCurrentIndex(5)

    def go_result(self):
        self.ui.table_result.clear()
        self.ui.table_result.setRowCount(self.now.wil_max)
        self.ui.table_result.setColumnCount(2)
        self.ui.table_result.setHorizontalHeaderItem(0, QTableWidgetItem("답"))
        self.ui.table_result.setHorizontalHeaderItem(1, QTableWidgetItem("대답"))
        self.ui.table_result.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i, (v, r) in enumerate(zip(self.now.sample, self.now.replies)):
            item1 = QTableWidgetItem(f"{self.now.now_tds.vec2element(v)}")
            item1.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item2 = QTableWidgetItem(f"{r}")
            item2.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
            item2.setCheckState(Qt.Unchecked) # TODO: 일치 과정
            self.ui.table_result.setItem(i, 0, item1)
            self.ui.table_result.setItem(i, 1, item2)
        self.ui.front.setCurrentIndex(7)

    def filebrowse(self, fileinfo: FileInfo):
        fname, _ = QFileDialog.getOpenFileName(self,
                                               caption='tds 찾기',
                                               dir=const.DATASET_ROUTE,
                                               filter="TNW-TDS File (*.tnw)")
        if not fname:
            return

        self.fileload(fileinfo, fname)

    def fileload(self, fileinfo: FileInfo, path: str):
        t = futil.load_tnw(path)
        if t is None:
            QMessageBox.warning(self, "파일 오류", "읽을 수 없는 파일입니다.")
            fileinfo.disable()
        else:
            fileinfo.load_file(path, t)
            self._tds = t

    def weightbrowse(self, label):
        fname, _ = QFileDialog.getOpenFileName(self,
                                               caption=f'{self._tds.name} 적합 가중치 찾기',
                                               dir=const.WEIGHT_PREFERENCE_ROUTE,
                                               filter="Json Weight (*.json)")
        if not fname:
            return

        self._weight = futil.load_weight(fname)
        label.setText(fname)
        return

    def weight_reset(self):
        self._weight = None
        self.ui.lbl_tanswermenu_weight_browse.setText("파일이 없습니다.")

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

    def result_weight_apply(self):
        fname, _ = QFileDialog.getSaveFileName(self,
                                               caption=f'{self.now.now_tds.name}',
                                               dir=const.WEIGHT_PREFERENCE_ROUTE,
                                               filter="Json Weight (*.json)")

        if not fname:
            return
        new_W = self.now.weight_process(
            [self.ui.table_result.item(row, 1).checkState() == Qt.Checked for row in
             range(self.ui.table_result.rowCount())])
        futil.save_weight(fname, new_W)
