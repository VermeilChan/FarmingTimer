import sys
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QIcon, QFont, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QSystemTrayIcon,
    QMenu,
    QMessageBox,
)


class Timer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timer")
        self.setWindowIcon(QIcon("Assets/Icons/Program.ico"))
        self.setGeometry(100, 100, 100, 150)
        self.setMaximumSize(self.size())

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.icon_label = QLabel()
        self.icon_label.setPixmap(
            QPixmap("Assets/Icons/Program.ico").scaled(
                64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.icon_label)

        self.timer_label = QLabel("00:00:00", alignment=Qt.AlignCenter)
        self.timer_label.setFont(QFont("Arial", 24))
        self.layout.addWidget(self.timer_label)

        self.start_button = self.create_button(
            "Start", "Assets/Icons/Start.svg", "Start the timer", self.start_timer
        )
        self.pause_button = self.create_button(
            "Pause/Resume",
            "Assets/Icons/Pause.svg",
            "Pause/Resume the timer",
            self.pause_resume_timer,
            False,
        )
        self.stop_button = self.create_button(
            "Stop", "Assets/Icons/Stop.svg", "Stop the timer", self.stop_timer, False
        )

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.stop_button)
        self.layout.addLayout(button_layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time_elapsed = 0

        self.tray_icon = QSystemTrayIcon(QIcon("Assets/Icons/Program.ico"), self)
        self.tray_icon.activated.connect(self.on_tray_icon_activated)
        self.create_tray_menu()
        self.tray_icon.show()

    def create_button(self, text, icon_path, tooltip, callback, enabled=True):
        button = QPushButton(QIcon(icon_path), text)
        button.setToolTip(tooltip)
        button.setEnabled(enabled)
        button.clicked.connect(callback)
        return button

    def create_tray_menu(self):
        tray_menu = QMenu(self)
        tray_menu.addAction("Open", self.show)
        tray_menu.addAction("Quit", self.exit_application)
        self.tray_icon.setContextMenu(tray_menu)

    def start_timer(self):
        self.timer.start(1000)
        self.start_button.setEnabled(False)
        self.pause_button.setEnabled(True)
        self.stop_button.setEnabled(True)

    def pause_resume_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.pause_button.setText("Resume")
            self.pause_button.setIcon(QIcon("Assets/Icons/Resume.svg"))
        else:
            self.timer.start(1000)
            self.pause_button.setText("Pause")
            self.pause_button.setIcon(QIcon("Assets/Icons/Pause.svg"))

    def stop_timer(self):
        self.timer.stop()
        self.time_elapsed = 0
        self.update_timer()
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.stop_button.setEnabled(False)

    def update_timer(self):
        self.time_elapsed += 1
        hours, remainder = divmod(self.time_elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.timer_label.setText(f"{hours:02}:{minutes:02}:{seconds:02}")

    def exit_application(self):
        self.tray_icon.hide()
        QApplication.quit()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        QMessageBox.information(
            self,
            "Minimized to Tray",
            "The application is still running in the system tray. Right-click the tray icon to open or exit.",
        )

    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    timer_window = Timer()
    timer_window.show()
    sys.exit(app.exec())
