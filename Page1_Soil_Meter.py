from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit


class SoilMeter(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()

        for i in range(1, 5):
            self.layout.addRow(QLabel(f"--- Hub{i} ---"))
            self.layout.addRow(QLabel("Umiditatea din sol (%):"), QLineEdit())
            self.layout.addRow(QLabel("Temperatura din sol (°C):"), QLineEdit())
            self.layout.addRow(QLabel("Macronutrienți (N, P, K):"), QLineEdit())
            self.layout.addRow(QLabel("pH Sol:"), QLineEdit())

        self.setLayout(self.layout)