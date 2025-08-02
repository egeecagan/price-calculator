# source/gui/main_window.py

from PyQt6.QtWidgets import QMainWindow, QTabWidget, QApplication
from PyQt6.QtGui import QIcon
import os

from .pages.measurement_page import MeasurementPage
from .pages.fixed_prices_page import PricesPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧮 price calculator")

        current_dir = os.path.dirname(__file__)
        icon_path = os.path.join(current_dir, '..', 'resources', 'icon.png')
        icon_path = os.path.abspath(icon_path)
        self.setWindowIcon(QIcon(icon_path))

        self.resize(520, 390)
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.measurement_page = MeasurementPage()
        self.prices_page = PricesPage()

        self.tabs.addTab(self.measurement_page, "📐 measurements")
        self.tabs.addTab(self.prices_page, "💵 dollar and euro")

