import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox


class Crosshair(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.resize(64, 90)
        self.pen = QtGui.QPen(QtGui.QColor(255, 0, 0, 255))
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnTopHint
            | QtCore.Qt.WindowTransparentForInput
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(
            QApplication.desktop().screen().rect().center()
            - self.rect().center()
            + QtCore.QPoint(1, 1)
        )
        self.setWindowFlag(QtCore.Qt.Tool)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.drawEllipse(28, 41, 4, 4)


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Crosshair")
        self.setGeometry(450, 250, 200, 80)

        # CheckBox
        self.checkbox = QCheckBox("Crosshair Enable", self)
        self.checkbox.move(20, 30)

        # checkbox on/off event
        self.checkbox.stateChanged.connect(self.openwindow)
        self.show()

    # Run Crosshiar window
    def openwindow(self):
        if self.checkbox.isChecked():
            self.window = Crosshair()
            self.window.show()
        else:
            self.window.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())
