# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:56:58 2023

@author: P558
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from ana_form2 import *

Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)

penAna.show()

sys.exit(Uygulama.exec_())