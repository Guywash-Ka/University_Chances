import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('/home/vlad/projects/RodionPy/proekt/ui_3.ui',self)
        self.con = sqlite3.connect("/home/vlad/projects/RodionPy/proekt/Яндекс_проект.db")

        # Кнопка сохранения таблицы
        self.pushButton.clicked.connect(self.save_table)
        # Кнопка добавления строки
        self.pushButton_2.clicked.connect(self.add_row)
        # Кнопка добавления информации
        self.pushButton_3.clicked.connect(self.add_to_exsistent)
        # Изменение таблицы
        self.pushButton_4.clicked.connect(self.change_table)
        

        
        # Названия всех столбцов
        self.titles = ("№", "Дата прохождения УМО", 'Длина тела (см)', 'Длина туловища от 7-го шейного позвонка ', 'Размах рук ', 
                    'Обхват грудной клетки на вдохе ', 'Обхват грудной клетки на выдохе ', 'Экскурсия ', 
                    'Спирометрия ', 'Динамометрия', 'Динамометрия правой кисти ', 'Динамометрия левой кисти',
                    "ЭКГ в покое", 'ЭКГ с нагрузкой', 'Плантометрия', 
                    'TANITA % жировой массы', 'TANITA % мышечной массы ', 'Стабилометрия открытые глаза',
                    "Стабилометрия закрытые глаза", "Стабилометрия Мишень", "PWC150-170 кг мм",
                    "PWC150-170 ЧСС", "PWC150-170 давление", 'PWC150-170 МПК', 
                     "Фукциональные возможности ЦНС", "Уровень работоспособности ЦНС", "ГРВ", "Кардиоинтелография золотое сечение ",
                    'Кардиоинтелография Индекс напряжения', 'Кардиоинтелография Спектральный анализ', 
                    "Кардиоинтелография Интегральный показатель", 'Кардиоинтелография Адаптационные возможности организма',
                    "Кардиоинтелография Функциональные резервы", 'Системный анализ Системный анализ',
                    "Системный анализ Психоэмоциональное состояние")
        self.titles2 = ('№', 'Имя', "Пол", "Дата рождения", "Вес", "Длина тела")

        self.spinBox_2.setMinimum(1)
        self.comboBox.addItems(self.titles2)
        self.comboBox_2.addItems(['Первый_этап', 'Второй_этап', 'Третий_этап'])
        self.comboBox_3.addItems(['Персональные данные', "Результаты обследований"])
        self.change_table()


        # Отображение первой таблицы
        cur = self.con.cursor()
        self.result = cur.execute('SELECT * FROM results').fetchall()
        result = self.result.copy()
        title = result[0]
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.cellClicked[int, int].connect(self.clickedRowColumn)
        self.tableWidget.move(1000, 5000)


        # Отображение второй таблицы
        self.result2 = cur.execute('SELECT * FROM personal_data').fetchall()
        result2 = self.result2.copy()
        title2 = result2[0]
        self.tableWidget_2.setColumnCount(len(title2))
        self.tableWidget_2.setRowCount(0)
        for i, row in enumerate(result2):
            self.tableWidget_2.setRowCount(self.tableWidget_2.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(elem))
        self.tableWidget_2.setHorizontalHeaderLabels(self.titles2)
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.cellClicked[int, int].connect(self.clickedRowColumn)

    
    # Добавление информации в существующие поля
    def add_to_exsistent(self):
        cur = self.con.cursor()
        if self.current_table() == 0:
            self.tableWidget_2.setItem(int(self.spinBox_2.text()) - 1, self.find_column_number(self.comboBox.currentText()), QTableWidgetItem(self.lineEdit_3.text()))
        else:
            self.tableWidget.setItem(int(self.spinBox_2.text()) - 1, self.find_column_number(self.comboBox.currentText()), QTableWidgetItem(self.lineEdit_3.text()))
    
    # Функция, которая ищет номер столбца по его названию
    def find_column_number(self, name):
        if self.current_table():
            titles = self.titles
        else:
            titles = self.titles2
        for i, names in enumerate(titles):
            if names == name:
                return i

    # Добавление новой строки
    def add_row(self):
        cur = self.con.cursor()
        if self.current_table() == 0:
            self.result2.append(['' for i in range(self.tableWidget_2.columnCount())])
            self.tableWidget_2.insertRow(self.tableWidget_2.rowCount())
            a = self.tableWidget_2.rowCount()

            for i in range(self.tableWidget_2.columnCount()):
                self.tableWidget_2.setItem(a - 1, i, QTableWidgetItem(''))
        else:
            self.result.append(['' for i in range(self.tableWidget.columnCount())])
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            a = self.tableWidget.rowCount()

            # Заполнение новой строки пустыми элементами класса QTableWidgetItem
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(a - 1, i, QTableWidgetItem(''))
    
    # Если было нажатие на поле таблицы
    def clickedRowColumn(self):
        if self.current_table():
            self.spinBox_2.setMaximum(-1)
            self.spinBox_2.setMinimum(self.tableWidget.currentRow() + 1)
            self.spinBox_2.setMinimum(1)
            self.spinBox_2.setMaximum(self.tableWidget.rowCount())

            self.comboBox.setCurrentIndex(self.tableWidget.currentColumn())

            self.lineEdit_3.setText(self.tableWidget.currentItem().text())
        else:
            self.spinBox_2.setMaximum(-1)
            self.spinBox_2.setMinimum(self.tableWidget_2.currentRow() + 1)
            self.spinBox_2.setMinimum(1)
            self.spinBox_2.setMaximum(self.tableWidget_2.rowCount())

            self.comboBox.setCurrentIndex(self.tableWidget_2.currentColumn())

            self.lineEdit_3.setText(self.tableWidget_2.currentItem().text())

    # Сохранение таблицы в SQLite в базу данных Яндекс_проект в новую таблицу с именем new_table
    def save_table(self):
        if self.current_table() == 1:
            table = []
            
            # Считывание всех данных таблицы
            for i in range(self.tableWidget.rowCount()):
                table.append([])
                for j in range(self.tableWidget.columnCount()):
                    table[i].append(self.tableWidget.item(i, j).text())
                table[i] = tuple(table[i])

            table = tuple(table)
            
            signs = '?, ' * self.tableWidget.columnCount()
            signs = signs[:-2]

            cur = self.con.cursor()
            # Создание новой таблицы
            cur.execute(f"DROP TABLE IF EXISTS {self.comboBox_2.currentText()}")
            cur.execute(f"CREATE TABLE {self.comboBox_2.currentText()}(№, Дата прохождения УМО, Длина_тела_см, Длина_туловища от седьмого шейного позвонка , Размах рук , "
                    'Обхват_грудной_клетки_на_вдохе , Обхват_грудной_клетки_на_выдохе , Экскурсия , '
                    'Спирометрия , Динамометрия, Динамометрия_правой кисти , Динамометрия_левой кисти,'
                    "ЭКГ_в покое, ЭКГ_с нагрузкой, Плантометрия, Динамометрия_нагрузка, "
                    'TANITA_жировой массы, TANITA_мышечной массы , Стабилометрия_открытые глаза,'
                    "Стабилометрия_закрытые глаза, Стабилометрия_Мишень, PWC150_170_кг мм,"
                    "PWC150_170_ЧСС, PWC150_170_давление, PWC150_170_МПК, "
                    "Фукциональные возможности ЦНС, Уровень работоспособности ЦНС, ГРВ, Кардиоинтелография_золотое сечение ,"
                    'Кардиоинтелография_Индекс напряжения, Кардиоинтелография_Спектральный анализ, '
                    "Кардиоинтелография_Интегральный показатель, Кардиоинтелография_Адаптационные возможности организма,"
                    "Кардиоинтелография_Функциональные резервы, Системный_анализ_Системный анализ,"
                    "Системный_анализ_Психоэмоциональное состояние)")

            self.con.commit()

            cur.executemany(f"INSERT INTO {self.comboBox_2.currentText()} VALUES({signs})", table)

            self.con.commit()
        else:
            table = []
            
            # Считывание всех данных таблицы
            for i in range(self.tableWidget_2.rowCount()):
                table.append([])
                for j in range(self.tableWidget_2.columnCount()):
                    table[i].append(self.tableWidget_2.item(i, j).text())
                table[i] = tuple(table[i])

            table = tuple(table)
            
            signs = '?, ' * self.tableWidget_2.columnCount()
            signs = signs[:-2]

            cur = self.con.cursor()
            # Создание новой таблицы
            cur.execute(f"DROP TABLE IF EXISTS new_personal_data")
            cur.execute(f"CREATE TABLE new_personal_data(№, Имя, Пол, Дата рождения, Вес, Длина тела)")

            self.con.commit()

            cur.executemany(f"INSERT INTO new_personal_data VALUES({signs})", table)

            self.con.commit()

    def current_table(self):
        if self.comboBox_3.currentIndex() == 0:
            return 0
        return 1
    
    def delete_from_comboBox(self):
        for i in range(self.comboBox.count()):
            self.comboBox.removeItem(0)
    
    def change_table(self):
        if self.current_table():
            self.tableWidget_2.move(70021, 81100)
            self.tableWidget.move(0, 210)
            self.label_4.move(840, 15)
            self.comboBox_2.move(960, 15)
            self.delete_from_comboBox()
            self.comboBox.addItems(self.titles)
        else:
            self.tableWidget.move(100001, 100001)
            self.tableWidget_2.move(0, 210)
            self.label_4.move(64000, 20000)
            self.comboBox_2.move(76000, 20000)
            self.delete_from_comboBox()
            self.comboBox.addItems(self.titles2)
        

        


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())