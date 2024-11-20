import sys
import sqlite3
import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QCheckBox, QLabel
from PyQt6.QtCore import QDate, Qt
from m1 import Ui_Form
from madd import Ui_Addd
from dell import Ui_Dell
from update import Ui_Up
from kal import Ui_kalck
import calendar


class Calendarr(QWidget, Ui_kalck):
    def __init__(self, f):
        super().__init__()
        self.setupUi(self)
        self.f = f
        self.setWindowTitle('Выбор даты')
        global currentYear, currentMonth, currentDay
        currentMonth = datetime.datetime.now().month
        currentYear = datetime.datetime.now().year
        currentDay = int(datetime.datetime.now().day)
        self.calll.setGridVisible(True)
        self.calll.setMinimumDate(QDate(currentYear, currentMonth, currentDay))
        self.calll.setMaximumDate(
            QDate(currentYear, currentMonth + 1, calendar.monthrange(currentYear, currentMonth)[1] + 1))
        self.calll.setSelectedDate(QDate(currentYear, currentMonth, currentDay))
        self.calll.clicked.connect(self.printDateInfo)

    def printDateInfo(self, qDate):
        self.f.dat = '{2}-{0}-{1}'.format(qDate.month(), qDate.day(), qDate.year())
        self.f.date3.setText(self.f.dat)
        con = sqlite3.connect('QTproj')
        cur = con.cursor()
        f = 0
        titl = []
        result = cur.execute(f"""SELECT * FROM date""").fetchall()
        for i in result:
            if (datetime.date(int(self.f.dat.split('-')[0]), int(self.f.dat.split('-')[1]), int(self.f.dat.split('-')[2])).toordinal() - datetime.date(int(i[0].split('-')[0]), int(i[0].split('-')[1]), int(i[0].split('-')[2])).toordinal()) / int(i[2]) % 1 == 0:
                titl.append(i[1])
        if len(titl) > 0:
            result = cur.execute(f'''SELECT * FROM flower WHERE title IN ("{'", "'.join(titl)}")''').fetchall()
            for i in result:
                self.f.table_flower3.setItem(f, 0, QTableWidgetItem(i[1]))
                self.f.table_flower3.setItem(f, 1, QTableWidgetItem(i[3]))
                self.f.table_flower3.setItem(f, 2, QTableWidgetItem(i[4]))
                self.f.table_flower3.setItem(f, 3, QTableWidgetItem(i[5]))
                f += 1
        if f < self.f.kd3:
            for i in range(f, self.f.kd3):
                self.f.table_flower3.setItem(i, 0, QTableWidgetItem(''))
                self.f.table_flower3.setItem(i, 1, QTableWidgetItem(''))
                self.f.table_flower3.setItem(i, 2, QTableWidgetItem(''))
                self.f.table_flower3.setItem(i, 3, QTableWidgetItem(''))
        self.f.kd3 = f
        con.close()
        self.close()


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.kd3 = 0
        self.addfl.clicked.connect(self.dobafit)
        self.pipfl.clicked.connect(self.ubafit)
        self.septfl.clicked.connect(self.sept)
        self.num = 0
        self.n2 = 0
        self.setWindowTitle('Журнал цветов')
        self.table_flower3.hide()
        self.table_flower2.hide()
        self.save.hide()
        self.setdate.clicked.connect(self.btn_setdate)
        self.date3.hide()
        self.setdate.hide()
        self.grpolivki.clicked.connect(self.btn_3)
        self.moifl.clicked.connect(self.btn_1)
        self.segodnia.clicked.connect(self.btn_2)
        con = sqlite3.connect('QTproj')
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM flower""").fetchall()
        for i in result:
            self.table_flower.setItem(self.num, 0, QTableWidgetItem(i[1]))
            self.table_flower.setItem(self.num, 1, QTableWidgetItem('раз в ' + i[2] + ' дней(дня, день)'))
            self.table_flower.setItem(self.num, 2, QTableWidgetItem(i[3]))
            self.table_flower.setItem(self.num, 3, QTableWidgetItem(i[4]))
            self.table_flower.setItem(self.num, 4, QTableWidgetItem(i[5]))
            self.num += 1
        con.close()
        self.save.clicked.connect(self.sv)

    def sv(self):
        for i in range(self.n2):
            if self.table_flower2.cellWidget(i, 0).isChecked():
                con = sqlite3.connect('QTproj')
                cur = con.cursor()
                w = self.table_flower2.cellWidget(i, 0).text()
                res = cur.execute(f'''SELECT * FROM date WHERE flower="{w}"''').fetchall()
                today = datetime.date(int(res[0][0].split('-')[0]), int(res[0][0].split('-')[1]),
                                      int(res[0][0].split('-')[2])) + datetime.timedelta(int(res[0][2]))
                cur.execute(f"""UPDATE date SET datee='{today}' WHERE flower='{w}'""")
                con.commit()
                con.close()
        con = sqlite3.connect('QTproj')
        cur = con.cursor()
        n2 = self.n2
        self.n2 = 0
        result = cur.execute(
            f"""SELECT * FROM flower WHERE title in (SELECT flower FROM date WHERE datee = '{str(datetime.datetime.now().date())}')""").fetchall()
        for j in result:
            chb = QCheckBox(j[1], self)
            chb.setStyleSheet('QCheckBox {background-color: rgb(255, 238, 175); accent-color: #C56FFF;}')
            self.table_flower2.setCellWidget(self.n2, 0, chb)
            self.table_flower2.setItem(self.n2, 2, QTableWidgetItem(j[4]))
            self.table_flower2.setItem(self.n2, 1, QTableWidgetItem(j[3]))
            self.table_flower2.setItem(self.n2, 3, QTableWidgetItem(j[5]))
            self.n2 += 1
        if len(result) < n2:
            for j in range(len(result), n2):
                self.table_flower2.setCellWidget(j, 0, QLabel().setStyleSheet(
                    'QCheckBox {background-color: rgb(255, 238, 175); accent-color: #C56FFF;}'))
                self.table_flower2.setItem(j, 1, QTableWidgetItem(''))
                self.table_flower2.setItem(j, 3, QTableWidgetItem(''))
                self.table_flower2.setItem(j, 2, QTableWidgetItem(''))
        con.close()

    def btn_1(self):
        self.table_flower2.hide()
        self.table_flower.show()
        self.save.hide()
        self.addfl.show()
        self.pipfl.show()
        self.septfl.show()
        self.setdate.hide()
        self.date3.hide()
        self.table_flower3.hide()

    def btn_3(self):
        self.date3.show()
        self.setdate.show()
        self.table_flower.hide()
        self.table_flower2.hide()
        self.table_flower3.show()
        self.save.hide()
        self.addfl.hide()
        self.pipfl.hide()
        self.septfl.hide()
        self.date3.setText('Выберите дату')

    def btn_setdate(self):
        self.dat = str(datetime.datetime.now().date())
        self.nf = Calendarr(self)
        self.nf.show()

    def btn_2(self):
        self.table_flower3.hide()
        self.setdate.hide()
        self.date3.hide()
        self.table_flower.hide()
        self.table_flower2.show()
        self.save.show()
        self.addfl.hide()
        self.pipfl.hide()
        self.septfl.hide()
        con = sqlite3.connect('QTproj')
        cur = con.cursor()
        n2 = self.n2
        self.n2 = 0
        result = cur.execute(
            f"""SELECT * FROM flower WHERE title in (SELECT flower FROM date WHERE datee = '{str(datetime.datetime.now().date())}')""").fetchall()
        for j in result:
            chb = QCheckBox(j[1], self)
            chb.setStyleSheet('QCheckBox {background-color: rgb(255, 238, 175); accent-color: #C56FFF;}')
            self.table_flower2.setCellWidget(self.n2, 0, chb)
            self.table_flower2.setItem(self.n2, 2, QTableWidgetItem(j[4]))
            self.table_flower2.setItem(self.n2, 1, QTableWidgetItem(j[3]))
            self.table_flower2.setItem(self.n2, 3, QTableWidgetItem(j[5]))
            self.n2 += 1
        if len(result) < n2:
            for j in range(len(result), n2):
                self.table_flower2.setItem(j, 0, QTableWidgetItem(''))
                self.table_flower2.setItem(j, 1, QTableWidgetItem(''))
                self.table_flower2.setItem(j, 3, QTableWidgetItem(''))
                self.table_flower2.setItem(j, 2, QTableWidgetItem(''))
        con.close()

    def dobafit(self):
        self.nf = Adddd(self)
        self.nf.show()

    def ubafit(self):
        self.nf = Dell(self)
        self.nf.show()

    def sept(self):
        self.nf = Update(self)
        self.nf.show()


class Adddd(QWidget, Ui_Addd):
    def __init__(self, f):
        super().__init__()
        self.setupUi(self)
        self.f = f
        self.setWindowTitle('Добавление')
        self.dobavit.clicked.connect(self.plus)

    def plus(self):
        if self.lineEdit.text() == '' or self.lineEdit.text() == 'Не указано':
            self.error.setText('Введите название')
        else:
            try:
                if self.lineEdit_5.text() != '' and int(self.lineEdit_5.text()) > 0:
                    con = sqlite3.connect('QTproj')
                    cur = con.cursor()
                    result = cur.execute(f"""SELECT * FROM FLOWER WHERE title='{self.lineEdit.text()}'""").fetchall()
                    if len(result) == 0:
                        cur.execute(f"""INSERT INTO flower (id, title, grap, location, volume, haract, datedob)
                        VALUES ('{self.f.num + 1}', '{self.lineEdit.text()}', '{self.lineEdit_5.text()}', '{self.lineEdit_2.text()}', '{self.lineEdit_3.text()}', '{self.lineEdit_4.text()}', '{str(datetime.datetime.now().date())}');
                        """)
                        con.commit()
                        cur.execute(f'''INSERT INTO date (datee, flower, delta)
                        VALUES ('{str(datetime.datetime.now().date() + datetime.timedelta(int(self.lineEdit_5.text())))}', '{self.lineEdit.text()}', '{self.lineEdit_5.text()}')
                        ''')
                        con.commit()
                        con.close()
                        self.f.table_flower.setItem(self.f.num, 0, QTableWidgetItem(self.lineEdit.text()))
                        self.f.table_flower.setItem(self.f.num, 1,
                                                    QTableWidgetItem('раз в ' + self.lineEdit_5.text() + ' дней(дня, день)'))
                        self.f.table_flower.setItem(self.f.num, 2, QTableWidgetItem(self.lineEdit_2.text()))
                        self.f.table_flower.setItem(self.f.num, 3, QTableWidgetItem(self.lineEdit_3.text()))
                        self.f.table_flower.setItem(self.f.num, 4, QTableWidgetItem(self.lineEdit_4.text()))
                        self.f.num += 1
                        self.close()
                        self.error.setText('')
                    else:
                        self.error.setText('Такой цветок уже есть')
                else:
                    raise Exception
            except Exception:
                self.error.setText('Введите в 5-й ячейке только число большее 0')

class Dell(QWidget, Ui_Dell):
    def __init__(self, f):
        super().__init__()
        self.setupUi(self)
        self.f = f
        self.setWindowTitle('Удаление')
        self.udel.clicked.connect(self.minus)

    def minus(self):
        con = sqlite3.connect('QTproj')
        cur = con.cursor()
        cur.execute(f"""DELETE FROM flower WHERE title='{self.lineEdit.text()}';""")
        con.commit()
        cur.execute(f"""DELETE FROM date WHERE flower='{self.lineEdit.text()}';""")
        con.commit()
        result = cur.execute(f"""SELECT * FROM flower""").fetchall()
        if len(result) < self.f.num:
            self.f.num = 0
            for i in result:
                self.f.table_flower.setItem(self.f.num, 0, QTableWidgetItem(i[1]))
                self.f.table_flower.setItem(self.f.num, 1, QTableWidgetItem('раз в ' + i[2] + ' дней(дня, день)'))
                self.f.table_flower.setItem(self.f.num, 2, QTableWidgetItem(i[3]))
                self.f.table_flower.setItem(self.f.num, 3, QTableWidgetItem(i[4]))
                self.f.table_flower.setItem(self.f.num, 4, QTableWidgetItem(i[5]))
                self.f.num += 1
            con.close()
            self.f.table_flower.setItem(self.f.num, 0, QTableWidgetItem(''))
            self.f.table_flower.setItem(self.f.num, 1, QTableWidgetItem(''))
            self.f.table_flower.setItem(self.f.num, 2, QTableWidgetItem(''))
            self.f.table_flower.setItem(self.f.num, 3, QTableWidgetItem(''))
            self.f.table_flower.setItem(self.f.num, 4, QTableWidgetItem(''))
            self.close()
        else:
            self.lineEdit.setText('Такого цветка нет')


class Update(QWidget, Ui_Up):
    def __init__(self, f):
        super().__init__()
        self.setupUi(self)
        self.f = f
        self.setWindowTitle('Изменение')
        self.label_2.hide()
        self.lineEdit_2.hide()
        self.label_3.hide()
        self.lineEdit_3.hide()
        self.label_4.hide()
        self.lineEdit_4.hide()
        self.label_5.hide()
        self.lineEdit_5.hide()
        self.label_6.hide()
        self.lineEdit_6.hide()
        self.udel_2.hide()
        self.udel_3.hide()
        self.udel.clicked.connect(self.poisk)
        self.udel_3.clicked.connect(self.hidee)
        self.udel_2.clicked.connect(self.sept)

    def poisk(self):
        if self.lineEdit.text() != '':
            self.nn = self.lineEdit.text()
            con = sqlite3.connect('QTproj')
            cur = con.cursor()
            result = cur.execute(f"""SELECT * FROM flower WHERE title='{self.nn}'""").fetchall()
            con.close()
            if len(result) == 0:
                self.lineEdit.setText('Нет такого цветка')
            else:
                result = result[0]
                self.label_2.show()
                self.lineEdit_2.show()
                self.label_3.show()
                self.lineEdit_3.show()
                self.label_4.show()
                self.lineEdit_4.show()
                self.label_5.show()
                self.lineEdit_5.show()
                self.label_6.show()
                self.lineEdit_6.show()
                self.udel_2.show()
                self.udel_3.show()
                self.lineEdit_2.setText(result[1])
                self.lineEdit_3.setText(result[3])
                self.lineEdit_4.setText(result[4])
                self.lineEdit_5.setText(result[5])
                self.lineEdit_6.setText(result[2])

    def hidee(self):
        self.label_2.hide()
        self.lineEdit_2.hide()
        self.label_3.hide()
        self.lineEdit_3.hide()
        self.label_4.hide()
        self.lineEdit_4.hide()
        self.label_5.hide()
        self.lineEdit_5.hide()
        self.label_6.hide()
        self.lineEdit_6.hide()
        self.udel_2.hide()
        self.udel_3.hide()

    def sept(self):
        if self.lineEdit_2.text() == '' or self.lineEdit_2.text() == 'Не указано':
            self.error.setText('Введите название')
        else:
            try:
                if self.lineEdit_6.text() != '' and int(self.lineEdit_6.text()) > 0:
                    self.label_2.hide()
                    self.lineEdit_2.hide()
                    self.label_3.hide()
                    self.lineEdit_3.hide()
                    self.label_4.hide()
                    self.lineEdit_4.hide()
                    self.label_5.hide()
                    self.lineEdit_5.hide()
                    self.label_6.hide()
                    self.lineEdit_6.hide()
                    self.udel_2.hide()
                    self.udel_3.hide()
                    con = sqlite3.connect('QTproj')
                    cur = con.cursor()
                    cur.executescript(f"""UPDATE flower
                    SET title='{self.lineEdit_2.text()}', grap='{self.lineEdit_6.text()}', location='{self.lineEdit_3.text()}', volume='{self.lineEdit_4.text()}', haract='{self.lineEdit_5.text()}'
                    WHERE title='{self.nn}'""")
                    cur.executescript(f"""UPDATE date
                    SET delta={self.lineEdit_6.text()}, datee='{str(datetime.datetime.now().date() + datetime.timedelta(int(self.lineEdit_6.text())))}'
                    WHERE flower='{self.nn}'""")
                    result = cur.execute(f'''SELECT * FROM flower''').fetchall()
                    con.commit()
                    con.close()
                    self.f.num = 0
                    for i in result:
                        self.f.table_flower.setItem(self.f.num, 0, QTableWidgetItem(i[1]))
                        self.f.table_flower.setItem(self.f.num, 1, QTableWidgetItem('раз в ' + i[2] + ' дней(дня, день)'))
                        self.f.table_flower.setItem(self.f.num, 2, QTableWidgetItem(i[3]))
                        self.f.table_flower.setItem(self.f.num, 3, QTableWidgetItem(i[4]))
                        self.f.table_flower.setItem(self.f.num, 4, QTableWidgetItem(i[5]))
                        self.f.num += 1
                    self.close()
                else:
                    raise Exception
            except Exception:
                self.error.setText('Введите в 5-й ячейке только число большее 0')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
