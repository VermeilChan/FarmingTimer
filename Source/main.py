import sys
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

class FarmingTimer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Farming Timer")
        self.setWindowIcon(QIcon('Assets/Icon/icon.ico'))
        self.setGeometry(100, 100, 100, 100)

        self.timer_label = QLabel("00:00:00")
        font = QFont("Arial", 24)
        self.timer_label.setFont(font)

        self.start_button = QPushButton(QIcon('Assets/buttons/start_icon.svg'), "Start",)
        self.pause_button = QPushButton(QIcon('Assets/buttons/pause_icon.svg'), "Pause")
        self.stop_button = QPushButton(QIcon('Assets/buttons/stop_icon.svg'), "Stop")
        self.resume_button = QPushButton(QIcon('Assets/buttons/resume_icon.svg'), "Resume")

        self.start_button.setToolTip("Start the timer")
        self.pause_button.setToolTip("Pause the timer")
        self.stop_button.setToolTip("Stop the timer")
        self.resume_button.setToolTip("Resume the timer")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.timer_label, alignment=Qt.AlignCenter)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.resume_button)

        self.layout.addLayout(button_layout)
        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_elapsed = 0

        self.start_button.clicked.connect(self.start_timer)
        self.pause_button.clicked.connect(self.pause_timer)
        self.stop_button.clicked.connect(self.stop_timer)
        self.resume_button.clicked.connect(self.resume_timer)

        self.pause_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        self.resume_button.setEnabled(False)

        self.timer_running = False
        self.setMaximumSize(self.size())

    def start_timer(self):
        self.timer.start(1000)
        self.start_button.setEnabled(False)
        self.pause_button.setEnabled(True)
        self.stop_button.setEnabled(True)
        self.resume_button.setEnabled(False)
        self.timer_running = True

    def pause_timer(self):
        self.timer.stop()
        self.pause_button.setEnabled(False)
        self.resume_button.setEnabled(True)
        self.timer_running = False

    def stop_timer(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        self.resume_button.setEnabled(False)
        self.time_elapsed = 0
        self.update_timer()
        self.timer_running = False

    def resume_timer(self):
        self.timer.start(1000)
        self.pause_button.setEnabled(True)
        self.resume_button.setEnabled(False)
        self.timer_running = True

    def update_timer(self):
        if self.timer_running:
            self.time_elapsed += 1
            hours = self.time_elapsed // 3600
            minutes = (self.time_elapsed % 3600) // 60
            seconds = self.time_elapsed % 60
            self.timer_label.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    timer_window = FarmingTimer()
    timer_window.show()
    sys.exit(app.exec())
