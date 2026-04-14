import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Raspberry Pi App")
        self.setMinimumSize(400, 200)

        self._click_count = 0

        self.label = QLabel("Hello from PySide6!")
        self.label.setStyleSheet("font-size: 18px;")

        self.button = QPushButton("Click me")
        self.button.clicked.connect(self._on_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _on_button_clicked(self):
        self._click_count += 1
        self.label.setText(f"Button clicked {self._click_count} time(s)!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
