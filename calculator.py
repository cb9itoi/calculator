from PyQt5 import QtWidgets
from calc import Ui_MainWindow


class CalculatorWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Логика калькулятора
        self.add_functions()
        self.is_equal = False

    def add_functions(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_division.clicked.connect(lambda: self.write_number(self.btn_division.text()))
        self.btn_multiply.clicked.connect(lambda: self.write_number(self.btn_multiply.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))

        self.btn_equal.clicked.connect(self.results)

    def write_number(self, number):
        if self.label_result.text() == "0" or self.is_equal:
            self.label_result.setText(number)
            self.is_equal = False
        else:
            self.label_result.setText(self.label_result.text() + number)

    def results(self):
        res = eval(self.label_result.text())
        self.label_result.setText("Результат: " + str(res))
        self.is_equal = True
