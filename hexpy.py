import sys
from math import sqrt
from PySide6.QtCore import Qt, QRect, QPoint, QFile
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QPushButton, QGraphicsView
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QIcon, QImage, QFont, QPolygon, QPixmap, QPainterPath, QBrush
#записывать для каждой координаты цвет в словарь
class Window(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("test")
        screen = app.primaryScreen()
        self.size = screen.size()
        self.buttons()
        self.showFullScreen()
        self.color = "black"
        self.setMouseTracking(True)
        #self.hex_x, self.hex_y = 0,0
        self.hexcolor = [] #отдельный класс?
        self.hexpos = [] #posdata
        #self.hex = []
        self.player_color = True

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.painter(qp)
        qp.end()

    def painter(self, qp):
        pen = QPen(Qt.black, 8, Qt.SolidLine)
        #qp.setPen(pen)
        font = QFont("Times", 60, QFont.Bold)
        qp.setFont(font)
        self.setplayground(qp, 11)

    def setplayground(self, qp, size):
        def stepper(x_start, y_start, x_set, y_set, size):
            x, y = 0,0
            for i in range(size):
                for s in range(len(self.hexpos)):
                    if(self.hexpos[s][0] - 60 < x_start+x and self.hexpos[s][0] + 0 > x_start+x
                    and self.hexpos[s][1] - 40 < y_start+y and self.hexpos[s][1] + 10 > y_start+y): #function, and name for constant
                        self.hex_x = i
                        if self.hexcolor[s] == True:
                            self.color = "red"
                        else:
                            self.color = "blue"
                        qp.setBrush(self.brushset())
                        qp.drawPolygon(self.hex(x_start+x, y_start+y))
                qp.setBrush(self.brushset())
                self.hex_x = 0
                self.color = "black"
                qp.drawPolygon(self.hex(x_start+x, y_start+y))
                x+=x_set
                y+=y_set
        x, y = 0, 0
        for i in range(size):
            self.hex_y = i
            stepper(self.size.width()/2.1+x, self.size.height()/50+y, 30,50,size)
            x-=30
            y+=50

    def get_data(self):
        return (self.hex_pos, self.hex_color)
    def brushset(self):
        if self.color == "black":
            return QBrush(Qt.white)
        if self.color == "red":
            return QBrush(Qt.red)
        if self.color == "blue":
            return QBrush(Qt.blue)
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.NoButton:
            pass
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.player_color = not self.player_color
            self.hexcolor.append(self.player_color)
            if self.player_color == True:
                print((event.x(), event.y()))
                self.hexpos.append((event.x(), event.y()))
            else:
                pass
            #вставь ИИ здесь
            self.update()
    
    def hex(self, x, y):
        hexpol = QPolygon()
        # 50 50 80 100 50 100 50 -30
        hexpol << QPoint(x, y) << QPoint(x, y + 30) << QPoint(x+30, y+50) << QPoint(x+60, y+30) << QPoint(x+60, y) << QPoint(x+30, y-20) << QPoint(x, y)
        return hexpol

    def buttons(self):
        print(QFile("D:/programs/hex/hex.png").exists())
        exbut = QPushButton("X", self)
        exbut.setStyleSheet("background-color: red")
        exbut.setFixedSize(50, 50)
        exbut.move(self.size.width()-50, 0)
        exbut.clicked.connect(self.exit)

    def exit(self):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)


    win = Window(app)
    sys.exit(app.exec_())