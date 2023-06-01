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



#VERİTABANI OLUŞTUR

import sqlite3
global curs 
global conn

conn = sqlite3.connect('veritabani.db')
curs=conn.cursor()

tabloolustur = ("CREATE TABLE IF NOT EXISTS ogrenci(ID INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, AdSoyad TEXT , No TEXT)")    
curs.execute(tabloolustur)
conn.commit()


def ekle():
    _AdSoyad=ui.lne_adsoyad.text()
    _Nu=ui.lne_nu.text()
    
    curs.execute("insert into ogrenci (AdSoyad, No) VALUES (?,?)" , (_AdSoyad, _Nu))
    conn.commit()
    listele()

ui.pushButton.clicked.connect(ekle)

def listele():
    ui.tableWidget.clear()
    ui.tableWidget.setHorizontalHeaderLabels(('ID', 'AdSoyad', 'Öğrenci No'))
    
    curs.execute("select * from ogrenci")
    
    for satirindeks, satirveri in enumerate (curs) :
        for sutunindeks, sutunveri in enumerate (satirveri):
            ui.tableWidget.setItem(satirindeks, sutunindeks, QTableWidgetItem(str(sutunveri)))
    conn.commit()
    
listele()

def sil():
    secilen = ui.tableWidget.selectedItems()
    silinecek_id = int(secilen[0].text())
    curs.execute("delete from ogrenci where ID='%s' " %(silinecek_id))
    conn.commit()
    listele()
ui.btn_sil.clicked.connect(sil)

sys.exit(Uygulama.exec_())