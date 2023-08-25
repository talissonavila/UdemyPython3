from __future__ import annotations

from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.central_widget = QWidget()
        self.vertical_layout = QVBoxLayout()
        self.central_widget.setLayout(self.vertical_layout)
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle('Calculator')

    def adjust_fixed_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def add_widget_to_vertical_layout(self, widget: QWidget):
        self.vertical_layout.addWidget(widget)

    def make_message_box(self):
        return QMessageBox(self)
