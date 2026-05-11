from PySide6.QtWidgets import (QWidget,QLabel,QLineEdit,QSpinBox,QPushButton,QTableWidget,QTableWidgetItem,QVBoxLayout,QHBoxLayout,)


class TaskTable(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.title_label = QLabel("Tasks")
        self.layout.addWidget(self.title_label)

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Task Name")

        self.goal_input = QLineEdit()
        self.goal_input.setPlaceholderText("Goal")

        self.session_input = QSpinBox()
        self.session_input.setMinimum(1)
        self.session_input.setMaximum(20)
        self.session_input.setValue(1)

        self.add_task_button = QPushButton("Add Task")
        self.add_task_button.clicked.connect(self.add_task)

        self.input_row = QHBoxLayout()
        self.input_row.addWidget(self.task_input)
        self.input_row.addWidget(self.goal_input)
        self.input_row.addWidget(self.session_input)
        self.input_row.addWidget(self.add_task_button)

        self.layout.addLayout(self.input_row)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(

            ["Task", "Goal", "Allocated", "Completed", "Remaining"]

        )

        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def add_task(self):
        task_name = self.task_input.text().strip()
        goal = self.goal_input.text().strip()
        allocated_session = self.session_input.value()

        if task_name == "":
            return

        row = self.table.rowCount()
        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem(task_name))
        self.table.setItem(row, 1, QTableWidgetItem(goal))
        self.table.setItem(row, 2, QTableWidgetItem(str(allocated_session)))
        self.table.setItem(row, 3, QTableWidgetItem("0"))
        self.table.setItem(row, 4, QTableWidgetItem(str(allocated_session)))

        self.task_input.clear()
        self.goal_input.clear()

        self.session_input.setValue(1)



if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = TaskTable()
    window.setWindowTitle("Task Table Test")
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec())
