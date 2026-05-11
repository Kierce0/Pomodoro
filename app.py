import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
)
from timer import Timer
from task_table import TaskTable


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Focus Panda")
        self.setMinimumSize(500, 500)

        self.setObjectName("mainWindow")
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setStyleSheet("""
            #mainWindow {
                border-image: url(background.png) 0 0 0 0 stretch stretch;
            }
        """)

        self.timer = Timer()

        main_layout = QVBoxLayout()

        self.settings_button = QPushButton("Settings")
        self.settings_button.clicked.connect(self.open_settings)

        button_row = QHBoxLayout()
        button_row.addStretch()
        button_row.addWidget(self.timer.start_pause_button)
        button_row.addWidget(self.timer.reset_button)
        button_row.addWidget(self.settings_button)
        button_row.addStretch()

        button_style = """
            QPushButton {
                background-color: rgba(20, 20, 20, 180);
                color: white;
                border: 1px solid rgba(255, 255, 255, 120);
                border-radius: 10px;
                padding: 8px 16px;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: rgba(20, 20, 20, 220);
            }
        """

        self.timer.start_pause_button.setStyleSheet(button_style)
        self.timer.reset_button.setStyleSheet(button_style)
        self.settings_button.setStyleSheet(button_style)
                

        

        main_layout.addLayout(button_row)

        main_layout.addStretch()
        main_layout.addWidget(self.timer, alignment=Qt.AlignCenter)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def open_settings(self):
        self.task_table_window = TaskTable()
        self.task_table_window.setWindowTitle("Settings")
        self.task_table_window.resize(800, 400)
        self.task_table_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Widget()
    window.show()

    sys.exit(app.exec())