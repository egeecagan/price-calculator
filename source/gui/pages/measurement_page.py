from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QDoubleSpinBox,
    QGridLayout, QComboBox, QHBoxLayout
)
from PyQt6.QtCore import Qt
from gui.widgets.multi_unit_input import MultiUnitInput

class MeasurementPage(QWidget):
    def __init__(self):
        super().__init__()

        title = QLabel("mass & volume calculator")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 13px; font-weight: bold;")

        self.x_input = MultiUnitInput()
        self.y_input = MultiUnitInput()
        self.z_input = MultiUnitInput()

        self._shrink_spinboxes(self.x_input)
        self._shrink_spinboxes(self.y_input)
        self._shrink_spinboxes(self.z_input)

        self.density_input = QDoubleSpinBox()
        self.density_input.setRange(0.001, 100000)
        self.density_input.setValue(1)
        self.density_input.setFixedHeight(36)
        self.density_input.setStyleSheet("font-size: 14px;")

        self.density_unit = QComboBox()
        self.density_unit.addItems(["kg/m³", "g/cm³"])
        self.density_unit.setFixedHeight(36)
        self.density_unit.setStyleSheet("font-size: 14px;")
        
        density_layout = QHBoxLayout()
        density_layout.setSpacing(6)
        density_layout.addWidget(self.density_input)
        density_layout.addWidget(self.density_unit)

        self.calculate_button = QPushButton("calculate")
        self.calculate_button.setFixedHeight(36)
        self.calculate_button.setStyleSheet("font-size: 13px;")
        self.calculate_button.clicked.connect(self.calculate)

        self.result_label = QLabel("volume and mass will be calculated...")
        self.result_label.setStyleSheet("font-size: 11px;")

        grid = QGridLayout()
        grid.setHorizontalSpacing(4)
        grid.setVerticalSpacing(3)
        grid.setContentsMargins(10, 10, 10, 10)

        grid.addWidget(title, 0, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)

        grid.addWidget(QLabel(""), 1, 0)
        grid.addWidget(self._bold_label("meters"), 1, 1)
        grid.addWidget(self._bold_label("centimeters"), 1, 2)
        grid.addWidget(self._bold_label("millimeters"), 1, 3)

        self._add_row(grid, "X:", self.x_input, 2)
        self._add_row(grid, "Y:", self.y_input, 3)
        self._add_row(grid, "Z:", self.z_input, 4)

        grid.addWidget(QLabel("density:"), 5, 0)
        grid.addLayout(density_layout, 5, 1, 1, 3)

        grid.addWidget(self.calculate_button, 6, 0, 1, 4)
        grid.addWidget(self.result_label, 7, 0, 1, 4)
        self.result_label.setStyleSheet("""
            font-size: 16px;

            font-family: Arial;
        """)

        self.setLayout(grid)

    def _add_row(self, grid: QGridLayout, label: str, input_widget: MultiUnitInput, row: int):
        m_box = input_widget.m_input
        cm_box = input_widget.cm_input
        mm_box = input_widget.mm_input

        label_widget = QLabel(label)
        label_widget.setStyleSheet("font-size: 16px;")
        grid.addWidget(label_widget, row, 0)
        grid.addWidget(m_box, row, 1)
        grid.addWidget(cm_box, row, 2)
        grid.addWidget(mm_box, row, 3)

    def _shrink_spinboxes(self, widget: MultiUnitInput):
        for spinbox in [widget.m_input, widget.cm_input, widget.mm_input]:
            spinbox.setFixedHeight(36)
            spinbox.setFixedWidth(90)
            spinbox.setStyleSheet("font-size: 14px;")

    def _bold_label(self, text: str):
        label = QLabel(text)
        label.setStyleSheet("font-size: 11px; font-weight: bold;")
        return label

    def calculate(self):
        x = self.x_input.get_value_in_meters()
        y = self.y_input.get_value_in_meters()
        z = self.z_input.get_value_in_meters()

        density = self.density_input.value()
        selected_unit = self.density_unit.currentText()

        if selected_unit == "g/cm³":
            density *= 1000  # 1 g/cm³ = 1000 kg/m³

        volume = x * y * z
        mass = volume * density

        volume_str = f"{volume:.4f} m³" if volume >= 0.0001 else f"{volume:.2e} m³"
        mass_str = f"{mass:.4f} kg" if mass >= 0.0001 else f"{mass:.2e} kg"

        self.result_label.setText(
            f"volume: {volume_str}\nmass: {mass_str}"
        )
