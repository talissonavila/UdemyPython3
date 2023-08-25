import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from main_window import MainWindow
from display import Display
from information import Information
from styles import setup_theme
from variables import WINDOW_ICON_PATH
from buttons import ButtonsGrid


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup_theme()
    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    information = Information("What do you want to calculate?")
    window.add_widget_to_vertical_layout(information)

    display = Display()
    window.add_widget_to_vertical_layout(display)

    buttons_grid = ButtonsGrid(display, information, window)
    window.vertical_layout.addLayout(buttons_grid)

    window.adjust_fixed_size()
    window.show()
    app.exec()
