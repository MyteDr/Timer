from PyQt5.QtWidgets import QWidget, QApplication , QPushButton, QLabel, QComboBox,QFormLayout,QHBoxLayout ,QMessageBox
from PyQt5.QtGui import QIcon
from sys import argv , exit
from os import system

class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 150)
        self.setWindowTitle("Timer")
        self.setWindowIcon(QIcon("Icon.png"))
        self.setStyleSheet(self.setCss())
        self.body()
        self.show()
    def body(self):
        self.l1 = QLabel("Hour:")
        self.l1.setObjectName("l")
        self.l2 = QLabel("Minute:")
        self.l2.setObjectName("l")
        self.cb1 = QComboBox()
        self.cb1.setObjectName("cb")
        self.cb1.addItems([str(number) for number in range(0,24)])
        self.cb2 = QComboBox()
        self.cb2.setObjectName("cb")
        self.cb2.addItems([str(number) for number in range(0,60)])
        self.form = QFormLayout()
        self.btn1 = QPushButton("Start")
        self.btn1.clicked.connect(self.Start)
        self.btn1.setObjectName("btn")
        self.btn2=QPushButton("Cancel")
        self.btn2.clicked.connect(self.Stop)
        self.btn2.setObjectName("btn")
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btn1)
        self.hbox.addWidget(self.btn2)
        self.form.addRow(self.l1, self.cb1)
        self.form.addRow(self.l2, self.cb2)
        self.form.addRow(self.hbox)
        self.setLayout(self.form)
        self.setObjectName("main")
    def setCss (self):
        return """
            #main{
                    background: #001219;
                }
                #l{
                    font-size: 20px;
                    color: #fff;
                }
                #btn{
                    color: white;
                    font-size: 20px;
                    font-weight: 600;
                    background-color: #4CAF50;
                    padding: 10px;
                    border-radius: 4px;
                }
                #cb{
                    color:#fff;
                    font-size: 20px;
                    border-radius: 4;
                    border: 2px solid white;
                    background: transparent;
                }
        """
    def Start(self):
        self.hour = int(self.cb1.currentText())*3600
        self.minute = int(self.cb2.currentText())*60
        system(f"shutdown -s -t {self.hour+self.minute}")
        QMessageBox.information(self, "Information", "Countdown Started Successfully")
    def Stop(self):
        system("shutdown -a")
        QMessageBox.information(self, "Information", "Countdown Successfully Stopped")

if __name__ == "__main__":
    app = QApplication(argv)
    timer = Timer()
    exit(app.exec_())