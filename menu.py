import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                                QMenu, QAction)
from PyQt5.QtCore import QSize

class CalcWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()
    
    def initWindow(self):
        menubar = self.menuBar()

        natural = menubar.addMenu("Натуральные числа")
        
        n_sum = QAction("Сумма", self)
        n_sum.triggered.connect(self.sum_window)
        n_dif = QAction("Разность", self)
        n_mult = QAction("Умножение", self)
        n_div = QAction("Деление", self)
        n_mod = QAction("Деление с остатком", self)
        n_GCD = QAction("НОД", self)
        n_LCM = QAction("НОК", self)
        
        self.setActions(natural, [n_sum, n_dif, n_mult, n_div,
                                  n_mod, n_GCD, n_LCM])


        whole = menubar.addMenu("Целые числа")

        w_abs = QAction("Абсолютное значение", self)
        w_sum = QAction("Сумма", self)
        w_dif = QAction("Разность", self)
        w_mult = QAction("Умножение", self)
        w_div = QAction("Деление", self)
        w_mod = QAction("Деление с остатком", self)
        w_GCD = QAction("НОД", self)
        w_LCM = QAction("НОК", self)

        # НАДО ЧТО-ТО ДОБАВИТЬ
        self.setActions(whole, [w_abs, w_sum, w_dif, w_mult,
                                  w_div, w_mod, w_GCD, w_LCM])


        rational = menubar.addMenu("Рациональные числа")
        polynoms = menubar.addMenu("Многочлены")

        self.setFixedSize(QSize(650, 550))
        self.move(300, 300)
        self.setWindowTitle("Компьютерная алгебра")
        
        self.show()


    def setActions(self, bar, actions):
        for action in actions:
            bar.addAction(action)

    def sum_window(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = CalcWindow()
    sys.exit(app.exec_())