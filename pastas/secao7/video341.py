import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout


app = QApplication(sys.argv)

button = QPushButton("Click me")
button.setStyleSheet("font-size: 45px; color: blue;")
button2 = QPushButton("Don't click me")
button2.setStyleSheet("font-size: 20px; color: red;")


central_widget = QWidget()

layout = QVBoxLayout()
central_widget.setLayout(layout)

layout.addWidget(button)
layout.addWidget(button2)

central_widget.show()
app.exec()
