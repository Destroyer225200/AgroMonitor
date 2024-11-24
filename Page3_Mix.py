from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QSlider, QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer

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

        # Add sliders for N, P, K, and calcium
        self.n_slider = QSlider(Qt.Horizontal)
        self.n_slider.setRange(0, 20)
        self.n_slider.valueChanged.connect(self.update_n_volume)
        self.n_volume = QLabel("20 L")

        self.p_slider = QSlider(Qt.Horizontal)
        self.p_slider.setRange(0, 20)
        self.p_slider.valueChanged.connect(self.update_p_volume)
        self.p_volume = QLabel("20 L")

        self.k_slider = QSlider(Qt.Horizontal)
        self.k_slider.setRange(0, 20)
        self.k_slider.valueChanged.connect(self.update_k_volume)
        self.k_volume = QLabel("20 L")

        self.ca_slider = QSlider(Qt.Horizontal)
        self.ca_slider.setRange(0, 20)
        self.ca_slider.valueChanged.connect(self.update_ca_volume)
        self.ca_volume = QLabel("20 L")

        # Add PH value display
        self.ph_value_label = QLabel("Current PH Value:")
        self.ph_value_display = QLabel("7.0")  # Initial PH value

        # Add pump control buttons
        self.n_pump_button = QPushButton("Start N Pump")
        self.n_pump_button.clicked.connect(lambda: self.start_pump('N'))

        self.p_pump_button = QPushButton("Start P Pump")
        self.p_pump_button.clicked.connect(lambda: self.start_pump('P'))

        self.k_pump_button = QPushButton("Start K Pump")
        self.k_pump_button.clicked.connect(lambda: self.start_pump('K'))

        self.ca_pump_button = QPushButton("Start Ca Pump")
        self.ca_pump_button.clicked.connect(lambda: self.start_pump('Ca'))

        self.layout.addRow(self.nutrient_label, self.nutrient_input)
        self.layout.addRow(self.water_pump_label, self.water_pump_control)
        self.layout.addRow(self.ph_sensor_label, self.ph_sensor_reading)
        self.layout.addRow(self.calcium_label, self.calcium_input)

        # Add rows for the new sliders and volume labels
        self.layout.addRow(QLabel("N Volume:"), self.n_slider)
        self.layout.addRow(QLabel("Current N Volume:"), self.n_volume)
        self.layout.addRow(self.n_pump_button)
        self.layout.addRow(QLabel("P Volume:"), self.p_slider)
        self.layout.addRow(QLabel("Current P Volume:"), self.p_volume)
        self.layout.addRow(self.p_pump_button)
        self.layout.addRow(QLabel("K Volume:"), self.k_slider)
        self.layout.addRow(QLabel("Current K Volume:"), self.k_volume)
        self.layout.addRow(self.k_pump_button)
        self.layout.addRow(QLabel("Calcium Volume:"), self.ca_slider)
        self.layout.addRow(QLabel("Current Calcium Volume:"), self.ca_volume)
        self.layout.addRow(self.ca_pump_button)

        # Add row for PH value display
        self.layout.addRow(self.ph_value_label, self.ph_value_display)

        self.setLayout(self.layout)

        # Timers for pump simulation
        self.pump_timers = {
            'N': QTimer(self),
            'P': QTimer(self),
            'K': QTimer(self),
            'Ca': QTimer(self)
        }

        for element in self.pump_timers:
            self.pump_timers[element].timeout.connect(lambda elem=element: self.simulate_pump(elem))

    # Methods to update the volume labels
    def update_n_volume(self, value):
        self.n_volume.setText(f"{20 - value} L")

    def update_p_volume(self, value):
        self.p_volume.setText(f"{20 - value} L")

    def update_k_volume(self, value):
        self.k_volume.setText(f"{20 - value} L")

    def update_ca_volume(self, value):
        self.ca_volume.setText(f"{20 - value} L")

    # Method to update PH value
    def update_ph_value(self, value):
        self.ph_value_display.setText(f"{value}")

    # Method to start pump
    def start_pump(self, element):
        print(f"Starting {element} pump")
        self.pump_timers[element].start(1000)  # Simulate 1 liter per second for simplicity

    # Method to simulate pump
    def simulate_pump(self, element):
        if element == 'N':
            current_value = self.n_slider.value()
            if current_value < 20:
                self.n_slider.setValue(current_value + 1)
            else:
                self.pump_timers[element].stop()
        elif element == 'P':
            current_value = self.p_slider.value()
            if current_value < 20:
                self.p_slider.setValue(current_value + 1)
            else:
                self.pump_timers[element].stop()
        elif element == 'K':
            current_value = self.k_slider.value()
            if current_value < 20:
                self.k_slider.setValue(current_value + 1)
            else:
                self.pump_timers[element].stop()
        elif element == 'Ca':
            current_value = self.ca_slider.value()
            if current_value < 20:
                self.ca_slider.setValue(current_value + 1)
            else:
                self.pump_timers[element].stop()
