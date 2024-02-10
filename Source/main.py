import sys
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

class FarmingTimer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Farming Timer")
        self.setWindowIcon(QIcon('Assets/Icon/icon.ico'))
        self.setGeometry(100, 100, 200, 200)

        font = QFont("Minecraft", 8)
        QApplication.setFont(font)

        self.timer_label = QLabel("00:00:00")
        self.timer_label.setFont(QFont("Minecraft", 24))

        self.start_button = QPushButton(QIcon('Assets/buttons/start_icon.svg'), "Start")
        self.pause_button = QPushButton(QIcon('Assets/buttons/pause_icon.svg'), "Pause/Resume")
        self.stop_button = QPushButton(QIcon('Assets/buttons/stop_icon.svg'), "Stop")

        self.start_button.setToolTip("Start the timer")
        self.pause_button.setToolTip("Pause/Resume the timer")
        self.stop_button.setToolTip("Stop the timer")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.timer_label, alignment=Qt.AlignCenter)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.stop_button)

        self.layout.addLayout(button_layout)
        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_elapsed = 0

        self.start_button.clicked.connect(self.start_timer)
        self.pause_button.clicked.connect(self.pause_resume_timer)
        self.stop_button.clicked.connect(self.stop_timer)

        self.pause_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        self.setMaximumSize(self.size())

    def start_timer(self):
        self.timer.start(1000)
        self.start_button.setEnabled(False)
        self.pause_button.setEnabled(True)
        self.stop_button.setEnabled(True)

    def pause_resume_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.pause_button.setText("Resume")
            self.pause_button.setIcon(QIcon('Assets/buttons/resume_icon.svg'))
        else:
            self.timer.start(1000)
            self.pause_button.setText("Pause")
            self.pause_button.setIcon(QIcon('Assets/buttons/pause_icon.svg'))

    def stop_timer(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        self.time_elapsed = -1
        self.update_timer()

    def update_timer(self):
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
