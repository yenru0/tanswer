import os
import json
import glob

import numpy as np

from reader.structure import Reader
from reader.structure import TanswerDataStruct
from reader.exceptions import TReaderException
import function.const as const


def get_name_from_dataset():
    return [os.path.splitext(os.path.basename(f))[0] for f in glob.glob(const.DATASET_ROUTE + "*.tnw")]


def get_path_from_dataset():
    return [f for f in glob.glob(const.DATASET_ROUTE + "*.tnw")]


def get_name_path_from_dataset():
    return [(os.path.splitext(os.path.basename(f))[0], f) for f in glob.glob(const.DATASET_ROUTE + "*.tnw")]


def tnw_path(name: str) -> str:
    return f"{const.DATASET_ROUTE}{name}.tnw"


def is_tnw_exists_in_dataset(name: str) -> bool:
    return os.path.isfile(tnw_path(name))


def save_tnw_dataset(tds) -> bool:
    if is_tnw_exists_in_dataset(tds.name):
        return False
    else:
        with open(tnw_path(tds.name), "w", encoding='utf-8') as f:
            f.write(tds.reader.src)
        return True


def read_tnw(f) -> [None, TanswerDataStruct]:
    read = Reader(f)
    try:
        read.read()
    except TReaderException:
        return None
    return TanswerDataStruct(read)


def load_tnw(path: str) -> [None, TanswerDataStruct]:
    with open(path, "r", encoding='utf-8') as f:
        t = read_tnw(f)
    return t


def save_weight(path: str, w: np.ndarray) -> bool:
    with open(path, "w", encoding='utf-8') as f:
        json.dump(w.tolist(), f, indent=4, )
    return True


def load_weight(path: str) -> np.ndarray:
    with open(path, "r", encoding='utf-8') as f:
        w = json.load(f)
    w = np.array(w)
    return w
