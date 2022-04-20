from typing import MappingView
import DrawLots
import time
import playsound
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

def PlayingMusic():
    playsound.playsound("Dugudugu_sound.mp3")
UI_class = uic.loadUiType("LottoUI.ui")[0]

class WindowClass(QMainWindow, UI_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.DrawLotsButton.clicked.connect(self.BBobggi)
    def BBobggi(self):
        awnser = DrawLots.MainLot()
        
        PlayingMusic()

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()