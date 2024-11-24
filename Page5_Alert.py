from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt5.QtCore import QTimer

class Alert(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.grid_layout = QGridLayout()
        self.pumps = []

        for i in range(1, 6):
            pump_label = QLabel(f"Pump {i}")
            pump_status = QLabel()
            pump_status.setStyleSheet("border: 1px solid black; background-color: green;")
            self.grid_layout.addWidget(pump_label, i-1, 0)
            self.grid_layout.addWidget(pump_status, i-1, 1)
            self.pumps.append(pump_status)

        self.layout.addLayout(self.grid_layout)
        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_pump_status)
        self.timer.start(1000)  # Update every second

    def check_pump_status(self):
        for pump_status in self.pumps:
            # Simulate pump status check
            if self.is_pump_failing():
                pump_status.setStyleSheet("border: 1px solid black; background-color: red;")
                self.parentWidget().parentWidget().btn_page5.setStyleSheet("background-color: orange;")
            else:
                pump_status.setStyleSheet("border: 1px solid black; background-color: green;")
                self.parentWidget().parentWidget().btn_page5.setStyleSheet("")

    def is_pump_failing(self):
        
        import random
        return random.choice([True, False])
