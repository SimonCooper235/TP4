from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget, QMainWindow
from PyQt6.uic import loadUi


class Simulation_view(QMainWindow):

    def __init__(self):
        super().__init__()

        loadUi("ui/v1.ui", self) # TODO  faire le ui


        self.play_pushButton.clicked.connect(self.play)
        self.pause_pushButton.clicked.connect(self.pause)
        self.stop_pushButton.clicked.connect(self.stop)
        # connection signals



    def set_controller(self, controller):
        self.__controller = controller



    def play(self):
        print("play")
        self.__controller.play()

    def pause(self):
        print("pause")
        self.__controller.pause()

    def stop(self):
        print("stop")
        self.__controller.stop()

    def paintEvent(self, event):
       pass
