from math import pow
from typing import TYPE_CHECKING

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton

from utils import convert_to_number, is_empty, is_number_or_dot, is_valid_number
from variables import MEDIUM_FONT_SIZE

if TYPE_CHECKING:
    from display import Display
    from information import Information
    from main_window import MainWindow


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style_configuration()

    def style_configuration(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


def _connect_button_is_clicked(button, slot):
    button.clicked.connect(slot)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Information', window: 'MainWindow', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equation_initial_value = 'What do you want to calculate?'
        self._left = None
        self._right = None
        self._operator = None

        self.equation = self._equation_initial_value
        self._make_grid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _make_grid(self):
        self.display.enter_pressed.connect(self._equal)
        self.display.delete_pressed.connect(self._backspace)
        self.display.clear_pressed.connect(self._clear)
        self.display.input_pressed.connect(self._insert_to_diplay)
        self.display.operator_pressed.connect(self._config_left_operator)

        for row_number, row_data in enumerate(self._grid_mask):
            for column_number, button_text in enumerate(row_data):
                button = Button(button_text)

                if not is_number_or_dot(button_text) and not is_empty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._config_special_button(button)

                self.addWidget(button, row_number, column_number)
                slot = self._make_slot(self._insert_to_diplay, button_text)
                self._connect_button_is_clicked(button, slot)

    def _connect_button_is_clicked(self, button, slot):
        button.clicked.connect(slot)

    def _config_special_button(self, button):
        text = button.text()

        if text == 'C':
            self._connect_button_is_clicked(button, self._clear)

        if text == 'D':
            self._connect_button_is_clicked(button, self.display.backspace)

        if text == 'N':
            self._connect_button_is_clicked(button, self._invert_number)

        if text in '+-/*^':
            self._connect_button_is_clicked(button, self._make_slot(self._config_left_operator, text))

        if text == '=':
            self._connect_button_is_clicked(button, self._equal)

    @Slot()
    def _make_slot(self, function, *args, **kwargs):
        @ Slot(bool)
        def real_slot(_):
            function(*args, **kwargs)
        return real_slot

    @Slot()
    def _invert_number(self):
        display_text = self.display.text()

        if not is_valid_number(display_text):
            return

        number = convert_to_number(display_text) * -1
        self.display.setText(str(number))

    @Slot()
    def _insert_to_diplay(self, text):
        new_display_value = self.display.text() + text

        if not is_valid_number(new_display_value):
            return

        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self._equation_initial_value
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _config_left_operator(self, text):
        display_text = self.display.text()
        self.display.clear()
        self.display.setFocus()

        if not is_valid_number(display_text) and self._left is None:
            self._show_error("You didn't digit nothing.")
            return

        if self._left is None:
            self._left = convert_to_number(display_text)

        self._operator = text
        self.equation = f'{self._left} {self._operator} ??'

    @Slot()
    def _equal(self):
        display_text = self.display.text()

        if not is_valid_number(display_text) or self._left is None:
            self._show_error("Incomplete equation.")
            return

        self._right = convert_to_number(display_text)
        self.equation = f'{self._left} {self._operator} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, (float, int)):
                result = pow(self._left, self._right)
                result = convert_to_number(str(result))
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._show_error(f'You  can not divide per zero')
        except OverflowError:
            self._show_error(f"Number too much big")

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
        self.display.setFocus()

        if result == 'error':
            self._left = None

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _make_dialog(self, text):
        message_box = self.window.make_message_box()
        message_box.setText(text)
        return message_box

    def _show_error(self, text):
        message_box = self._make_dialog(text)
        message_box.setIcon(message_box.Icon.Critical)
        message_box.exec()
        self.display.setFocus()

    def _show_info(self, text):
        message_box = self._make_dialog(text)
        message_box.setIcon(message_box.Icon.Information)
        message_box.exec()
        self.display.setFocus()
