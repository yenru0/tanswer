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

if __name__ == '__main__':
    if not os.path.isdir("./dataset"):
        os.mkdir("./dataset")
    if not os.path.isdir("./preference"):
        os.mkdir("./preference")

    app = QApplication(sys.argv)
    window = MainPlate(None)
    sys.exit(app.exec_())
