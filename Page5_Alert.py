from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QCheckBox, QSpinBox


class Alert(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()

        self.heat_pump_label = QLabel("Heat Pump Control:")
        self.heat_pump_control = QCheckBox("Turn On/Off")

        self.set_temperature_label = QLabel("Set Temperature (°C):")
        self.set_temperature_input = QSpinBox()
        self.set_temperature_input.setRange(0, 50)

        self.layout.addRow(self.heat_pump_label, self.heat_pump_control)
        self.layout.addRow(self.set_temperature_label, self.set_temperature_input)

        self.setLayout(self.layout)