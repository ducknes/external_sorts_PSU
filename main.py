import copy
import random
import time
from form import *
import sys


class ExternalSorts(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.quit.clicked.connect(self.quit)
        self.ui.sort.clicked.connect(self.sorts_comparation)


    def quit(self):
        self.ui.quit.clicked.connect(QtWidgets.QApplication.instance().quit)

    def simple_two_phase_sort(self, array):
        array_for_sort = copy.deepcopy(array)

        compares = 0
        appends = 0

        start_time = time.time()
        while len(array_for_sort) > 1:
            decay_b = [] #  серии б
            decay_c = [] #  серии с

            #   разложение
            iteration = 0
            while len(array_for_sort) > 0:
                if iteration % 2 == 0:
                    decay_b.append(array_for_sort[0])
                    appends += 1
                    array_for_sort.pop(0)
                else:
                    decay_c.append(array_for_sort[0])
                    appends =+ 1
                    array_for_sort.pop(0)
                iteration += 1
            
            #   слияние
            for i in range(min(len(decay_b), len(decay_c))):
                temp = []
                while len(decay_b[i]) > 0 and len(decay_c[i]) > 0:
                    if decay_b[i][0] < decay_c[i][0]:
                        temp.append(decay_b[i][0])
                        compares += 1
                        appends += 1
                        decay_b[i].pop(0)
                    else:
                        temp.append(decay_c[i][0])
                        compares += 1
                        appends += 1
                        decay_c[i].pop(0)
                
                if len(decay_b[i]) > 0:
                    temp[len(temp):] = decay_b[i][:] #  добавление оставшихся из б
                    appends += len(decay_b[i])
                    decay_b[i].clear()
                else:
                    temp[len(temp):] = decay_c[i][:] #  добавление оставшихся из с
                    appends += len(decay_c[i])
                    decay_c[i].clear()
                array_for_sort.append(temp) # добавляем серию в массив
                appends += 1
            
            if len(decay_b[-1]) > 0: #  проверяем осталось ли что-то в доп массивах
                array_for_sort.append(decay_b[-1])
                appends += 1
            elif len(decay_c[-1]) > 0:
                array_for_sort.append(decay_c[-1])
                appends += 1
        end_time = time.time()

        self.ui.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(compares)))
        self.ui.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(appends)))
        self.ui.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(float('{:.3f}'.format(end_time - start_time)))))
        return array_for_sort

    def sorts_comparation(self):
        A = [[random.randint(0, self.ui.size.value())] for _ in range(self.ui.size.value())]

        for i in range(5):
            self.ui.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(" "))
            self.ui.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(" "))
            self.ui.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(" "))
            self.ui.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(" "))

        if self.ui.simple2f.isChecked():
            a = self.simple_two_phase_sort(A)
            self.ui.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str(self.isSorted(a[0]))))

    def isSorted(self, array):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                return False
        return True


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = ExternalSorts()
    myapp.show()
    sys.exit(app.exec())
