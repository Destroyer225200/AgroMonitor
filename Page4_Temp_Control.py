from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class Temp_Control(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.alert_label = QLabel("Alerts:")
        self.alert_list = QLabel("No alerts")

        self.layout.addWidget(self.alert_label)
        self.layout.addWidget(self.alert_list)

        self.setLayout(self.layout)