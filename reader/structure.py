from typing import List, Dict

import numpy as np

from reader.read import Reader
from reader.exceptions import TDSEmptyException, TDSIllegalWeightException


class TanswerDataStruct:
    def __init__(self, reader: Reader):
        self.reader = reader

        self.name: str = reader.name
        self.description: str = reader.description
        self.stages: Dict[str, list] = reader.stages  # TODO: OrderedDict로 바꿀 필요성
        self.stage_list: list = list(reader.stages.keys())
        self.stage_dict: Dict[str, int] = {s: i for i, s in enumerate(self.stage_list)}
        self.stage_element_size: Dict[str, int] = {s: len(self.stages[s]) for s in self.stage_list}
        if self.stage_size == 0:
            raise TDSEmptyException

        self.weight_shape: tuple = (len(self.stage_list), max(self.stage_element_size.values()))

    def sampling(self, wil: int, weight: np.ndarray, stages: [None, List[int]] = None) -> list:
        if not self.valid(weight):
            raise TDSIllegalWeightException

        if stages:
            stages = sorted(stages)
            linear_map = lambda i: (int(stages[i // self.weight_shape[1]]), int(i % self.weight_shape[1]))
            W = weight[stages].copy()
        else:
            linear_map = lambda i: (int(i // self.weight_shape[1]), int(i % self.weight_shape[1]))
            W = weight.copy()
        W = W.flatten()

        return list(map(linear_map, np.random.choice(len(W), wil, p=W / np.sum(W))))

    def make_init_weight(self, default=10):
        T = np.zeros(self.weight_shape)
        for i, k in enumerate(self.stage_list):
            T[i, :self.stage_element_size[k]] = default
        return T

    def valid(self, W: np.ndarray):
        if W.shape == self.weight_shape:
            for i, s in enumerate(self.stage_list):
                l = self.stage_element_size[s]
                if any(W[i][l:] != 0):
                    return False

            return True
        else:
            return False

    def vec2element(self, vec: tuple):
        return self.stages[self.stage_list[vec[0]]][vec[1]]

    def stage_int_str(self, i: int):
        return self.stage_list[i]

    def stage_str_int(self, s: str):
        return self.stage_dict[s]

    @property
    def dict(self):
        return {
            "name": self.name,
            "desc": self.description,
            "stages": self.stages
        }

    @property
    def stage_size(self):
        return len(self.stage_list)

if __name__ == "__main__":
    r = Reader("""

##@ TA ### '##@' must be start of line
B: C; D
##@ TE ### comment
F: G;;;
H: ;J ### valid
W: W1; W2
X: X1; X2; X3;;
Y: Y1; Y2
Z: Z1
##@ TK ### excepted stage

""")

    r.read()
    print("# reader stage")
    print(r.stages)
    tds = TanswerDataStruct(r)
    print("# profile")
    print(tds.name, tds.description, tds.stages)
    print(tds.stage_list, tds.stage_element_size)
    print(tds.weight_shape)

    print("# sampling")
    print(tds.sampling(10, tds.make_init_weight()))
    print(tds.sampling(10, tds.make_init_weight(), [tds.stage_str_int("TA")]))

    print("# default weight")
    W = tds.make_init_weight()
    print(W)

    print("# W valid check")
    validW = np.array([[0, 0, 0, 0, 0, 0], [0, 10, 10, 10, 10, 10]])
    invalidW = np.array([[0, 1, 0, 0, 1, 0], [1, 1, 1, 1, 1, 1]])
    print(f"w -> {tds.valid(W)}")
    print(f"v -> {tds.valid(validW)}")
    print(f"iv -> {tds.valid(invalidW)}")

    print("# dict")
    print(tds.dict)

    print("# convert")
    print(tds.vec2element((1, 0)))
    print(tds.stage_int_str(0))
    print(tds.stage_str_int("TE"))
