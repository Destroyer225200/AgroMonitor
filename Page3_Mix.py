from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QSlider, QSpinBox
from PyQt5.QtCore import Qt


class Mix(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()

        self.nutrient_label = QLabel("Nutrient Mix Ratio (N, P, K):")
        self.nutrient_input = QLineEdit()

        self.water_pump_label = QLabel("Water Pump Control:")
        self.water_pump_control = QSlider()
        self.water_pump_control.setOrientation(Qt.Horizontal)
        self.water_pump_control.setRange(0, 100)

        self.ph_sensor_label = QLabel("PH Sensor Reading:")
        self.ph_sensor_reading = QLineEdit()
        self.ph_sensor_reading.setReadOnly(True)

        self.calcium_label = QLabel("Calcium Mix Ratio:")
        self.calcium_input = QSpinBox()
        self.calcium_input.setRange(0, 100)

        self.layout.addRow(self.nutrient_label, self.nutrient_input)
        self.layout.addRow(self.water_pump_label, self.water_pump_control)
        self.layout.addRow(self.ph_sensor_label, self.ph_sensor_reading)
        self.layout.addRow(self.calcium_label, self.calcium_input)

        self.setLayout(self.layout)