from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class Graphe_view(QWidget):

    def __init__(self):
        super().__init__()

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        layout = QVBoxLayout()
        layout2 = QHBoxLayout()

        selectionLabel = QLabel()
        selectionLabel.setText("Selection du corps : ")
        self.selectionLineEdit = QLineEdit()

        layout2.addWidget(selectionLabel)
        layout2.addWidget(self.selectionLineEdit)

        layout.addWidget(self.canvas)
        layout.addLayout(layout2)

        self.setLayout(layout)

        self.ax_position = self.figure.add_subplot(311)
        self.ax_velocity = self.figure.add_subplot(312)
        self.ax_acceleration = self.figure.add_subplot(313)

        self.ax_position.set_title("Position")
        self.ax_velocity.set_title("Velocity")
        self.ax_acceleration.set_title("Acceleration")

    def update_graphe(self, data):
        self.ax_position.cla()
        self.ax_velocity.cla()
        self.ax_acceleration.cla()

        body = next(iter(data))

        self.ax_position.set_title("Position")
        self.ax_velocity.set_title("Velocity")
        self.ax_acceleration.set_title("Acceleration")

        self.ax_position.plot(data[body]["position"], "r")
        self.ax_velocity.plot(data[body]["velocity"], "g")
        self.ax_acceleration.plot(data[body]["acceleration"], "b")

        self.canvas.draw_idle()