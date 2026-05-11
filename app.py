import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from timer import Timer
from task_table import TaskTable


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(500, 500)

        layout = QVBoxLayout()
        self.setLayout(layout)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Widget()
    window.show()

    sys.exit(app.exec())    