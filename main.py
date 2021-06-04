import json
import glob
import pickle
import sys
import os
import random
import hashlib
import uuid
import datetime
from typing import Dict

import numpy as np
from PySide2.QtWidgets import QApplication

from gui.mainplate import MainPlate
import function.const as const

if __name__ == '__main__':
    if not os.path.isdir(const.DATASET_ROUTE):
        os.mkdir(const.DATASET_ROUTE)
    if not os.path.isdir(const.PREFERENCE_ROUTE):
        os.mkdir(const.PREFERENCE_ROUTE)
    if not os.path.isdir(const.WEIGHT_PREFERENCE_ROUTE):
        os.mkdir(const.WEIGHT_PREFERENCE_ROUTE)

    app = QApplication(sys.argv)
    window = MainPlate(None)
    sys.exit(app.exec_())
