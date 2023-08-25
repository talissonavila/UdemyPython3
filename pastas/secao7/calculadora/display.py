from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt, Signal

from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN
from utils import is_empty, is_number_or_dot


class Display(QLineEdit):
    enter_pressed = Signal()
    delete_pressed = Signal()
    clear_pressed = Signal()
    input_pressed = Signal(str)
    operator_pressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_display_style_configuration()

    def set_display_style_configuration(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def key_pressed_event(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        keys_ = Qt.Key

        is_enter = key in [keys_.Key_Enter, keys_.Key_Return, keys_.Key_Equal]
        is_backspace = key in [keys_.Key_Backspace, keys_.Key_Delete, keys_.Key_D]
        is_esc = key in [keys_.Key_Escape, keys_.Key_C]
        is_operator = key in [keys_.Key_Plus, keys_.Key_Minus, keys_.Key_Slash, keys_.Key_Asterisk, keys_.Key_P]

        if is_enter:
            self.enter_pressed.emit()
            return event.ignore()

        if is_backspace:
            self.delete_pressed.emit()
            return event.ignore()

        if is_esc:
            self.clear_pressed.emit()
            return event.ignore()

        if is_operator:
            if text.lower() == 'p':
                text = '^'
            self.operator_pressed.emit(text)
            return event.ignore()

        if is_empty(text):
            return event.ignore()

        if is_number_or_dot(text):
            self.input_pressed.emit(text)
            return event.ignore()
