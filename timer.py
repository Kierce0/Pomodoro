from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.session_minutes = 25
        self.remaining_time = self.session_minutes * 60
        self.is_paused = False
        self.is_running = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer_label = QLabel("25:00")
        self.timer_label.setStyleSheet("font-size: 64px; font-weight: bold;")
        self.start_pause_button = QPushButton("Start")
        self.reset_button = QPushButton("Reset")
        self.start_pause_button.clicked.connect(self.start_pause_timer)
        self.reset_button.clicked.connect(self.reset_timer)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.timer_label)
        self.button_row = QHBoxLayout()
        self.button_row.addWidget(self.start_pause_button)
        self.button_row.addWidget(self.reset_button)
        self.layout.addLayout(self.button_row)
        self.setLayout(self.layout)

    def start_pause_timer(self):
        if not self.is_running:
            self.timer.start(1000)
            self.is_running = True
            self.is_paused = False
            self.start_pause_button.setText("Pause")

        elif self.is_running and not self.is_paused:
            self.timer.stop()
            self.is_running = True
            self.is_paused = True
            self.start_pause_button.setText("Resume")
        
        elif self.is_running and self.is_paused:
            self.timer.start(1000)
            self.is_running = True
            self.is_paused = False
            self.start_pause_button.setText("Pause")

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_timer_display()
        else:
            self.timer.stop()
            self.is_running, self.is_paused = False, False
    
    def update_timer_display(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.timer_label.setText(f"{minutes:02d}:{seconds:02d}")
    
    def reset_timer(self):
        self.timer.stop()
        self.remaining_time = self.session_minutes * 60
        self.is_running, self.is_paused = False, False
        self.start_pause_button.setText("Start")
        self.update_timer_display()
    
    








    

