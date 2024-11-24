import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QHBoxLayout
from Page1_Soil_Meter import SoilMeter
from Page2_Climate_Control import ClimateControl
from Page3_Mix import Mix
from Page4_Temp_Control import Temp_Control
from Page5_Alert import Alert

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Agro Monitor")
        self.setGeometry(100, 100, 500, 400)
        self.showMaximized()

        self.main_layout = QVBoxLayout()
        self.stacked_widget = QStackedWidget()

        self.page1 = SoilMeter()
        self.page2 = ClimateControl()
        self.page3 = Mix()
        self.page4 = Temp_Control()
        self.page5 = Alert()

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        self.stacked_widget.addWidget(self.page4)
        self.stacked_widget.addWidget(self.page5)

        self.nav_layout = QHBoxLayout()
        self.btn_page1 = QPushButton("Soil specs")
        self.btn_page2 = QPushButton("Climate control metrics")
        self.btn_page3 = QPushButton("Mix Nutrient levels")
        self.btn_page4 = QPushButton("Alert Dashboard")
        self.btn_page5 = QPushButton("Heat & Temperature Control")

        self.btn_page1.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page1))
        self.btn_page2.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page2))
        self.btn_page3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page3))
        self.btn_page4.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page4))
        self.btn_page5.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page5))

        self.nav_layout.addWidget(self.btn_page1)
        self.nav_layout.addWidget(self.btn_page2)
        self.nav_layout.addWidget(self.btn_page3)
        self.nav_layout.addWidget(self.btn_page4)
        self.nav_layout.addWidget(self.btn_page5)

        self.main_layout.addLayout(self.nav_layout)
        self.main_layout.addWidget(self.stacked_widget)
        self.setLayout(self.main_layout)

        self.setStyleSheet("""
            QWidget {
                background-color: #333333;
                color: white;
                border: 2px solid #0000FF;
            }
            QPushButton {
                background-color: #555555;
                color: white;
                border: 2px solid #0000FF;
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
                box-shadow: 3px 3px 5px #222222;
            }
            QPushButton:hover {
                background-color: #66FF66;
                box-shadow: 5px 5px 8px #222222;
            }
            QPushButton:pressed {
                background-color: #4285F4;
            }
            QLineEdit {
                background-color: #444444;
                color: white;
                border: 1px solid #555555;
                padding: 10px;
                font-size: 16px;
            }
            QLabel {
                font-size: 18px;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())