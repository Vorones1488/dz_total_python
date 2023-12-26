# from typing import 
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
from interface import *
import sys
from PyQt6 import *
import  logging 


logging.basicConfig(filename='calculator.log', level=logging.INFO, encoding='UTF-8')
logger = logging.getLogger()

class Window(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.my_result =''
        self.result = ''
        self.lineEdit.setText(self.result)
        self.pushButton_multiply.clicked.connect(self.multiply)
        self.pushButto_delimetr.clicked.connect(self.delimetr)
        self.pushButton_point.clicked.connect(self.point)
        self.pushButton_1.clicked.connect(self.add_1)
        self.pushButton_2.clicked.connect(self.add_2)
        self.pushButton_3.clicked.connect(self.add_3)
        self.pushButton_plus.clicked.connect(self.plus)
        self.pushButton_deleter.clicked.connect(self.deleter)
        self.pushButton_4.clicked.connect(self.add_4) 
        self.pushButton_5.clicked.connect(self.add_5)
        self.pushButton_6.clicked.connect(self.add_6)
        self.pushButton_minus.clicked.connect(self.minus)
        self.pushButton_7.clicked.connect(self.add_7)
        self.pushButton_8.clicked.connect(self.add_8)
        self.pushButton_9.clicked.connect(self.add_9)
        self.pushButton_0.clicked.connect(self.add_0)
        self.pushButton_plus_or_minus.clicked.connect(self.add_plus_or_minus)
        self.pushButton_reset.clicked.connect(self.reset)
        self.pushButton_result.clicked.connect(self.result_count)

    def add_0(self):
        logger.info('Ползователь нажал кнопку 1')
        self.result += '0'
        self.lineEdit.setText(self.result)
    
    def add_1(self):
        self.result +='1'
        self.lineEdit.setText(self.result)
        
    
    def add_2(self):
        logger.info('Ползователь нажал кнопку 2')
        self.result += '2'
        self.lineEdit.setText(self.result)


    def add_3(self):
        logger.info('Ползователь нажал кнопку 3')
        self.result += '3'
        self.lineEdit.setText(self.result)

        
    
    def add_4(self):
        logger.info('Ползователь нажал кнопку 4')
        self.result += '4'
        self.lineEdit.setText(self.result)


    def add_5(self):
        logger.info('Ползователь нажал кнопку 5')
        self.result += '5'
        self.lineEdit.setText(self.result)


    def add_6(self):
        logger.info('Ползователь нажал кнопку 6')
        self.result +='6'
        self.lineEdit.setText(self.result)


    def add_7(self):
        logger.info('Ползователь нажал кнопку 7')
        self.result +='7'
        self.lineEdit.setText(self.result)

    
    def add_8(self):
        logger.info('Ползователь нажал кнопку 8')
        self.result +='8'
        self.lineEdit.setText(self.result)

    
    def add_9(self):
        logger.info('Ползователь нажал кнопку 9')
        self.result += '9'
        self.lineEdit.setText(self.result)


    def multiply(self):
        logger.info('Ползователь выбрал действие умножить')
        self.result +='*'
        self.lineEdit.setText(self.result)

    
    def minus(self):
        logger.info('Ползователь выбрал действие вычитание')
        self.result +='-'
        self.lineEdit.setText(self.result)

    
    def plus(self):
        self.result +='+'
        self.lineEdit.setText(self.result)

    
    def point(self):
        logger.info('Ползователь выбрал действие cложение')
        self.result += '.'
        self.lineEdit.setText(self.result)

    
    def delimetr(self):
        logger.info('Ползователь выбрал действие деление')
        self.result += '/'
        self.lineEdit.setText(self.result)


    def add_plus_or_minus(self):
        logger.info('Ползователь выбрал действие изменение знака числа')
        try:
            if self.result[0] !='-':
                logger.info('Преобразование числа в отрицательное')
                self.result = '-' + self.result
                self.lineEdit.setText(self.result)

            else:
                logger.info('Преобразование числа в положительное')
                self.result = self.result.replace(self.result[0],'')
                self.lineEdit.setText(self.result)
        except IndexError:
            logger.info('Ошибка ввода данных')
            self.lineEdit.setText('IndexError')
            
    def reset(self):
        logger.info('Очистка результата')
        self.result = ''
        self.lineEdit.setText(self.result)

    
    def deleter(self):
        logger.info('Посимвольное удаление')
        self.result = self.result[:-1]
        self.lineEdit.setText(self.result)
           


   
    def result_count(self):

        try:
            logger.info('Операция расчета')
            self.my_result = eval(self.result)
            self.lineEdit.setText(str(float(eval(self.result))))
        except ZeroDivisionError:
            logger.info('Ошибка деления на ноль')
            self.lineEdit.setText('ZeroDivisionError')
        except TypeError:
            logger.info('Ошибка ввода данных')
            self.lineEdit.setText('ZeroDivisionError')
        except SyntaxError:
            logger.info('Ошибка ввода данных')
            self.lineEdit.setText('SyntaxError')
        except IndexError:
            logger.info('Ошибка ввода данных')
            self.lineEdit.setText('IndexError')




app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())