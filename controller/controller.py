from PyQt6.QtCore import QTimer

from model import model
from view import view


class Simulation_controller():
    __model:model.Simulation_model
    __view:view.Simulation_view


    def __init__(self, model, view):
        self.__model = model
        self.__view = view
        self.__view.set_Controller(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.running = False

        self.__view.playPushButton.clicked.connect(self.play)
        self.__view.pausePushButton.clicked.connect(self.pause)
        self.__view.stopPushButton.clicked.connect(self.stop)

        self.__view.get_dock().createPushButton.clicked.connect(self.ajout_object)

        self.__model.data_updated.connect(self.update_graphe)

        self.data = False

    def ajout_object(self):
        self.__model.add_planet(int(self.__view.get_dock().posXLineEdit.text()),
                                int(self.__view.get_dock().posYLineEdit.text()),
                                int(self.__view.get_dock().masseLineEdit.text()),
                                int(self.__view.get_dock().radiusLineEdit.text()),
                                0,
                                0,
                                self.__view.get_dock().couleurComboBox.currentText()
                                )
        self.__view.update()

    def play(self):
        if not self.running:
            self.timer.start(16)
            self.running = True

    def pause(self):
        self.timer.stop()
        self.running = False

    def stop(self):
        self.timer.stop()
        self.running = False
        self.__model.reset()
        self.__view.update()

    def update(self):
        self.__model.step(1 / 60, self.data)
        self.__view.update()

    def get_planets(self):
        return self.__model.planets

    def get_rad(self, i):
        return self.__model.get_rad(i)

    def get_couleurs(self, i):
        return self.__model.get_couleurs(i)

    def p_pressed(self):
        if self.running:
            self.pause()
        else:
            self.play()

    def esc_pressed(self):
        if not self.__view.get_dock().isHidden():
            self.__view.get_dock().hide()
        else:
            self.__view.get_dock().show()

    def g_pressed(self):
        if self.data:
            self.data = False
        else:
            self.data = True

    def update_graphe(self, data):
        self.__view.get_graph().update_graphe(data)