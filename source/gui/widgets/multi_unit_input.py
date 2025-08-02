from PyQt6.QtWidgets import QWidget, QSpinBox, QHBoxLayout

class MultiUnitInput(QWidget):
    def __init__(self):
        super().__init__()

        self.m_input = QSpinBox()
        self.cm_input = QSpinBox()
        self.mm_input = QSpinBox()

        self.m_input.setRange(0, 999999)
        self.cm_input.setRange(0, 999999)
        self.mm_input.setRange(0, 999999)

        self.m_input.setFixedWidth(60)
        self.cm_input.setFixedWidth(60)
        self.mm_input.setFixedWidth(60)

        layout = QHBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.m_input)
        layout.addWidget(self.cm_input)
        layout.addWidget(self.mm_input)

        self.setLayout(layout)


    def normalize(self):
        total_mm = (
            self.m_input.value() * 1000 +
            self.cm_input.value() * 10 +
            self.mm_input.value()
        )

        meters = total_mm // 1000
        cm = (total_mm % 1000) // 10
        mm = total_mm % 10

        self.m_input.setValue(meters)
        self.cm_input.setValue(cm)
        self.mm_input.setValue(mm)

    def get_value_in_meters(self) -> float:
        self.normalize()
        return (
            self.m_input.value() +
            self.cm_input.value() / 100 +
            self.mm_input.value() / 1000
        )
