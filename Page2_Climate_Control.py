from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton
from PyQt5.QtCore import QTimer
import random
import csv
from datetime import datetime

class ClimateControl(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.form_layout = QFormLayout()
        self.hubs = []

        for i in range(1, 5):
            hub = {
                "temperature": QLineEdit(),
                "humidity": QLineEdit(),
                "co2": QLineEdit()
            }
            self.form_layout.addRow(QLabel(f"--- Hub {i} ---"))
            self.form_layout.addRow(QLabel("Temperature (°C):"), hub["temperature"])
            self.form_layout.addRow(QLabel("Humidity (%):"), hub["humidity"])
            self.form_layout.addRow(QLabel("CO2 Levels (ppm):"), hub["co2"])
            self.hubs.append(hub)

        self.layout.addLayout(self.form_layout)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Time", "Temperature (°C)", "Humidity (%)", "CO2 Levels (ppm)"])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table_widget)

        self.refresh_button = QPushButton("Refresh Data")
        self.refresh_button.clicked.connect(self.load_historical_data)
        self.layout.addWidget(self.refresh_button)

        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)  # Update every second

    def update_data(self):
        for hub in self.hubs:
            temperature = round(random.uniform(20.0, 30.0), 2)
            humidity = round(random.uniform(40.0, 60.0), 2)
            co2 = round(random.uniform(300, 500), 2)
            hub["temperature"].setText(str(temperature))
            hub["humidity"].setText(str(humidity))
            hub["co2"].setText(str(co2))
            self.store_data(temperature, humidity, co2)

    def store_data(self, temperature, humidity, co2):
        with open('climate_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temperature, humidity, co2])

    def load_historical_data(self):
        self.table_widget.setRowCount(0)
        try:
            with open('climate_data.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row_position = self.table_widget.rowCount()
                    self.table_widget.insertRow(row_position)
                    for column, data in enumerate(row):
                        self.table_widget.setItem(row_position, column, QTableWidgetItem(data))
        except FileNotFoundError:
            pass