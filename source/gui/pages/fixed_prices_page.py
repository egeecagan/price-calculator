from PyQt6.QtWidgets import (
    QWidget, QLabel, QGridLayout, QFrame
)
from PyQt6.QtCore import Qt
from core import dollar_tl_price, euro_tl_price

class PricesPage(QWidget):
    def __init__(self):
        super().__init__()

        title = QLabel("Price Information")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 13px; font-weight: bold;")

        self.dollar_dict = dollar_tl_price() 
        self.eur_dict = euro_tl_price()       

        self.usd_buy_label = QLabel(f"USD Buy:  {self.dollar_dict['buy']:.2f} ₺")
        self.usd_sell_label = QLabel(f"USD Sell: {self.dollar_dict['sell']:.2f} ₺")
        self.eur_buy_label = QLabel(f"EUR Buy:  {self.eur_dict['buy']:.2f} ₺")
        self.eur_sell_label = QLabel(f"EUR Sell: {self.eur_dict['sell']:.2f} ₺")

        for label in [self.usd_buy_label, self.usd_sell_label, self.eur_buy_label, self.eur_sell_label]:
            label.setStyleSheet("""
                font-size: 12px;
                font-weight: bold;
                padding: 2px;
            """)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # ⚠️ Uyarı kutusu - QFrame ile şık görünüm
        warning_box = QFrame()
        warning_box.setStyleSheet("""
            QFrame {
                background-color: #fff3cd;
                border: 1px solid #ffeeba;
                border-radius: 4px;
                padding: 6px;
            }
        """)
        warning_label = QLabel("⚠️ Do not rely on these values. They are for informational purposes only.")
        warning_label.setStyleSheet("""
            color: #856404;
            font-size: 10px;
            font-style: italic;
        """)
        warning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        warning_box_layout = QGridLayout()
        warning_box_layout.addWidget(warning_label)
        warning_box.setLayout(warning_box_layout)

        # Layout
        grid = QGridLayout()
        grid.setContentsMargins(10, 10, 10, 10)
        grid.setHorizontalSpacing(4)
        grid.setVerticalSpacing(2)

        grid.addWidget(title, 0, 0, 1, 2)
        grid.addWidget(self.usd_buy_label, 1, 0)
        grid.addWidget(self.usd_sell_label, 1, 1)
        grid.addWidget(self.eur_buy_label, 2, 0)
        grid.addWidget(self.eur_sell_label, 2, 1)

        grid.addWidget(warning_box, 3, 0, 1, 2)

        self.setLayout(grid)
