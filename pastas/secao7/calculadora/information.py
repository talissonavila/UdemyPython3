from __future__ import annotations

from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt

from variables import SMALL_FONT_SIZE


class Information(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None):
        super().__init__(text, parent)
        self.set_style_configuration()

    def set_style_configuration(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
