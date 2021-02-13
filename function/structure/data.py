from typing import List, Dict

import numpy as np

import function.reader.read
from function.structure.exceptions import TDSEmptyException


class TanswerDataStruct:
    def __init__(self, fs: str, name: str, desc: str, ser=None):
        if ser:
            self.name: str = ser["name"]
            self.desc: str = ser["desc"]
            self.stages: dict = ser["stages"]
            self.stageMap: list = ser["stageMap"]
        else:
            self.name: str = name  # ser
            self.desc: str = desc  # ser
            reader = function.reader.read.Reader(fs)
            reader.read()
            self.stages: dict = reader.structure["stages"]  # ser
            self.stageMap: list = list(self.stages.keys())  # ser

        if len(self.stageMap) == 0:
            raise TDSEmptyException

        self.weightShape: tuple = (len(self.stageMap), max([len(self.stages[k]) for k in self.stageMap]))

        self.samples = None

    @property
    def __next__(self):
        return next(self.samples)

    def sampling(self, wil: int, weight: np.ndarray, stages: [None, List[int]] = None) -> list:
        if weight.shape != self.weightShape:
            raise Exception

        if stages:
            stages = sorted(stages)
            linear_map = lambda i: (int(stages[i // self.weightShape[1]]), int(i % self.weightShape[1]))
            W = weight[stages].copy()
        else:
            linear_map = lambda i: (int(i // self.weightShape[1]), int(i % self.weightShape[1]))
            W = weight.copy()
        W = W.flatten()

        return list(map(linear_map, np.random.choice(len(W), wil, p=W / np.sum(W))))

    def vec2element(self, vec: tuple):
        return self.stages[self.stageMap[vec[0]]][vec[1]]

    def make_init_weight(self):
        T = np.zeros(self.weightShape)
        for i, k in enumerate(self.stageMap):
            T[i, :len(self.stages[k])] = 1
        return T

    @property
    def dict(self):
        return {"name": self.name, "desc": self.desc, "stages": self.stages, "stageMap": self.stageMap}


if __name__ == '__main__':
    TDS = TanswerDataStruct("""
##@ 결단력S
word: 단어; 바이트
##@ 킹단력K
byte: 바이트;
biden: 바이든 주석 각하
trump: 대미천하 투 황상 폐하
##@ 스페시컬<T>
yangang no mat 맛없갱
mingnagang: 밍나갱
jeoleon: 제오레온; 제오런

""", "허경영 추천", "저런")
    print(TDS.stages)
    print(TDS.stageMap)
    print(TDS.weightShape)
    WW = TDS.make_init_weight()
    WW[2, (1, 2)] = 53
    print(WW)
    for v in TDS.sampling(10, WW, [1, 0, 2, 3], ):
        print(TDS.vec2element(v))
