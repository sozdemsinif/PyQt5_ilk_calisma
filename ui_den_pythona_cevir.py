# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:43:50 2023

@author: P558
"""

from PyQt5 import uic

with open('ana_form2.py', 'w', encoding="utf-8") as kodlama:
    uic.compileUi("ana_form2.ui", kodlama)
