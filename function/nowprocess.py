import numpy as np

from reader.structure import TanswerDataStruct


class NowProcess:
    def __init__(self):
        self.now_tds: TanswerDataStruct = None
        self.weight: np.ndarray = None
        self.wil_now: int = 0
        self.wil_max: int = 10

        self.sample: list = None
        self.replies: list = None

    def launch(self, tds: TanswerDataStruct, w: [np.ndarray, None], wil=10):
        self.now_tds = tds
        if w is None:
            self.weight = tds.make_init_weight(10)
        else:
            if self.now_tds.valid(w):
                self.weight = w
            else:
                self.weight = tds.make_init_weight(10)
        self.wil_now = 0
        self.sample = self.now_tds.sampling(self.wil_max, self.weight)
        self.replies = []

    def progress(self, reply: str):
        self.replies.append(reply)
        self.wil_now += 1
        if self.wil_now >= self.wil_max:
            return True
        else:
            return False

    def display(self, view, progress, info_name, info_vector):
        view.setText(str(self.now_tds.vec2element(self.sample[self.wil_now])))
        progress.setValue(self.wil_now)
        progress.setMaximum(self.wil_max)
        info_name.setText("")
        info_vector.setText(str(self.sample[self.wil_now]))

    @property
    def is_launched(self):
        if self.now_tds is None:
            return self.now_tds
        else:
            return 0 < self.wil_now < self.wil_max
