from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSlider, QPushButton, QFormLayout
from PyQt5.QtCore import Qt

class Temp_Control(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        # Heat pumps control
        self.heat_pump_label = QLabel("Heat Pump Power:")
        self.heat_pump_slider = QSlider(Qt.Horizontal)
        self.heat_pump_slider.setRange(0, 100)
        self.heat_pump_slider.setTickPosition(QSlider.TicksBelow)
        self.heat_pump_slider.setTickInterval(10)
        self.form_layout.addRow(self.heat_pump_label, self.heat_pump_slider)

        # Fans control
        self.fan_label = QLabel("Fan Speed:")
        self.fan_slider = QSlider(Qt.Horizontal)
        self.fan_slider.setRange(0, 100)
        self.fan_slider.setTickPosition(QSlider.TicksBelow)
        self.fan_slider.setTickInterval(10)
        self.form_layout.addRow(self.fan_label, self.fan_slider)

        # Air intakes control
        self.air_intake_label = QLabel("Air Intake Control:")
        self.open_air_intake_button = QPushButton("Open Air Intake")
        self.close_air_intake_button = QPushButton("Close Air Intake")
        self.form_layout.addRow(self.air_intake_label)
        self.form_layout.addRow(self.open_air_intake_button, self.close_air_intake_button)

        self.layout.addLayout(self.form_layout)

        self.setLayout(self.layout)

        # Connect buttons to functions
        self.open_air_intake_button.clicked.connect(self.open_air_intake)
        self.close_air_intake_button.clicked.connect(self.close_air_intake)

    def open_air_intake(self):
        print("Opening air intake")

    def close_air_intake(self):
        print("Closing air intake")
