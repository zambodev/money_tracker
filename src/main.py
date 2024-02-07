import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QDateEdit, QComboBox, QTextEdit, QPushButton
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtCore import QDate

from json_handler import JsonHadler


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        # Main window settings
        super().__init__()
        self.setGeometry(500, 220, 920, 480)

        self.setWindowTitle("Money Management")

        # Objects
        self.json_handler = JsonHadler("moneydata.json")
        self.json_handler.file_load()

        # Date label
        self.dateLabel = QLabel(self)
        self.dateLabel.setGeometry(10, 10, 50, 20)
        self.dateLabel.setText("Date:")
        # Date input
        self.dateInput = QDateEdit(self)
        self.dateInput.setGeometry(80, 10, 80, 20)
        self.dateInput.setCalendarPopup(True)
        self.dateInput.setDate(QDate.currentDate())

        # Amount input
        self.amountLabel = QLabel(self)
        self.amountLabel.setGeometry(10, 40, 50, 20)
        self.amountLabel.setText("Amount:")
        # Amount input
        self.amountInput = QLineEdit(self)
        self.amountInput.setGeometry(80, 40, 80, 20)
        self.amountInput.setValidator(QDoubleValidator())

        # Type label
        self.typeLabel = QLabel(self)
        self.typeLabel.setGeometry(10, 70, 50, 20)
        self.typeLabel.setText("Type:")
        # Type input
        self.typeInput = QComboBox(self)
        self.typeInput.setGeometry(80, 70, 80, 20)
        self.typeInput.addItems(['Obligatory', 'Normal', 'Extra', 'Income', 'Stocks'])


        # Description label
        self.descriptionLabel = QLabel(self)
        self.descriptionLabel.setGeometry(10, 100, 50, 20)
        self.descriptionLabel.setText("Causal:")
        # Description input
        self.descriptionInput = QTextEdit(self)
        self.descriptionInput.setGeometry(80, 100, 200, 80)

        # Add expense button
        self.expenseButton = QPushButton(self)
        self.expenseButton.setGeometry(10, 130, 30, 20)
        self.expenseButton.setText("Add")
        self.expenseButton.clicked.connect(self.expense_add)

    def expense_add(self):
        expense = {"date":self.dateInput.date().toString(), "amount": float(self.amountInput.text()), "type":self.typeInput.currentText()[0], "description":self.descriptionInput.toPlainText()}
        self.amountInput.clear()
        self.descriptionInput.clear()

        self.json_handler.file_expense_add(expense)

    def closeEvent(self, event):
        self.json_handler.file_save()
        self.json_handler.file_close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
