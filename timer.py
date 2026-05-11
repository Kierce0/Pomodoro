from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFrame,
    QComboBox,
    QProgressBar,
)


class Timer(QWidget):
    def __init__(self):
        super().__init__()

        # ---------------- TIMER DATA ----------------
        self.session_minutes = 25
        self.total_time = self.session_minutes * 60
        self.remaining_time = self.total_time

        self.is_paused = False
        self.is_running = False

        # Main countdown timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        # ---------------- PANDA ----------------
        self.panda_label = QLabel()
        self.panda_label.setAlignment(Qt.AlignCenter)

        self.panda_open = QPixmap("panda_open.png")
        self.panda_closed = QPixmap("panda_closed.png")

        self.panda_label.setPixmap(
            self.panda_open.scaled(
                120,
                120,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
        )

        # Blink timer
        self.blink_timer = QTimer()
        self.blink_timer.timeout.connect(self.blink_panda)
        self.blink_timer.start(4000)  # panda blinks every 4 seconds

        # ---------------- TIMER DISPLAY ----------------
        self.timer_label = QLabel("25:00")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 64px; font-weight: bold;")

        # ---------------- TASK SELECTOR ----------------
        self.task_selector = QComboBox()
        self.task_selector.setStyleSheet("""
        QComboBox {
        background-color: rgba(20, 20, 20, 180);
        color: white;
        border: 1px solid rgba(255, 255, 255, 120);
        border-radius: 10px;
        padding: 8px;
        font-size: 14px;
    }
""")
        self.task_selector.addItems(
            ["Select Task", "DSA", "Boot.dev", "GMAT"]
        )

        # ---------------- PROGRESS BAR ----------------
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(self.total_time)
        self.progress_bar.setValue(0)

        # ---------------- BUTTONS ----------------
        self.start_pause_button = QPushButton("Start")
        self.reset_button = QPushButton("Reset")

        self.start_pause_button.clicked.connect(self.start_pause_timer)
        self.reset_button.clicked.connect(self.reset_timer)

        # ---------------- TIMER INLAY ----------------
        self.timer_frame = QFrame()
        self.timer_frame.setObjectName("timerFrame")
        self.timer_frame.setStyleSheet("""
            #timerFrame {
                background-color: rgba(0, 0, 0, 100);
                border: 2px solid rgba(255, 255, 255, 180);
                border-radius: 18px;
                padding: 50px;
            }
        """)

        frame_layout = QVBoxLayout()
        frame_layout.addWidget(self.panda_label)
        frame_layout.addWidget(self.timer_label)
        frame_layout.addWidget(self.task_selector)
        frame_layout.addWidget(self.progress_bar)

        self.timer_frame.setLayout(frame_layout)

        # Main layout of Timer widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.timer_frame)
        self.setLayout(self.layout)

    # ---------------- BUTTON LOGIC ----------------
    def start_pause_timer(self):
        if not self.is_running:
            self.timer.start(1000)
            self.is_running = True
            self.is_paused = False
            self.start_pause_button.setText("Pause")

        elif self.is_running and not self.is_paused:
            self.timer.stop()
            self.is_paused = True
            self.start_pause_button.setText("Resume")

        elif self.is_running and self.is_paused:
            self.timer.start(1000)
            self.is_paused = False
            self.start_pause_button.setText("Pause")

    # ---------------- COUNTDOWN LOGIC ----------------
    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_timer_display()
            self.update_progress_bar()
        else:
            self.timer.stop()
            self.is_running = False
            self.is_paused = False
            self.start_pause_button.setText("Start")

    def update_timer_display(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.timer_label.setText(f"{minutes:02d}:{seconds:02d}")

    def update_progress_bar(self):
        elapsed_time = self.total_time - self.remaining_time
        self.progress_bar.setValue(elapsed_time)

    def reset_timer(self):
        self.timer.stop()
        self.remaining_time = self.total_time
        self.is_running = False
        self.is_paused = False
        self.start_pause_button.setText("Start")
        self.update_timer_display()
        self.progress_bar.setValue(0)

    # ---------------- PANDA BLINK LOGIC ----------------
    def blink_panda(self):
        self.panda_label.setPixmap(
            self.panda_closed.scaled(
                120,
                120,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
        )

        QTimer.singleShot(180, self.open_panda_eyes)

    def open_panda_eyes(self):
        self.panda_label.setPixmap(
            self.panda_open.scaled(
                120,
                120,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
        )