# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainXTHHAs.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSlider,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1060, 568)
        MainWindow.setMaximumSize(QSize(1060, 568))
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 661, 501))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 641, 481))
        self.plotLayout = QGridLayout(self.gridLayoutWidget)
        self.plotLayout.setObjectName(u"plotLayout")
        self.plotLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(680, 10, 371, 221))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 351, 210))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.threshold = QLabel(self.verticalLayoutWidget_2)
        self.threshold.setObjectName(u"threshold")
        font = QFont()
        font.setPointSize(12)
        self.threshold.setFont(font)
        self.threshold.setFrameShape(QFrame.Shape.NoFrame)
        self.threshold.setFrameShadow(QFrame.Shadow.Raised)
        self.threshold.setTextFormat(Qt.TextFormat.RichText)
        self.threshold.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.threshold)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bSlider = QSlider(self.verticalLayoutWidget_2)
        self.bSlider.setObjectName(u"bSlider")
        self.bSlider.setEnabled(True)
        self.bSlider.setMaximum(100)
        self.bSlider.setOrientation(Qt.Orientation.Horizontal)
        self.bSlider.setInvertedAppearance(False)
        self.bSlider.setInvertedControls(False)
        self.bSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.bSlider.setTickInterval(100)

        self.horizontalLayout.addWidget(self.bSlider)

        self.bValue = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.bValue.setObjectName(u"bValue")
        self.bValue.setMinimumSize(QSize(110, 25))
        self.bValue.setDecimals(0)
        self.bValue.setMaximum(100.000000000000000)
        self.bValue.setSingleStep(1.000000000000000)

        self.horizontalLayout.addWidget(self.bValue)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.contrast = QLabel(self.verticalLayoutWidget_2)
        self.contrast.setObjectName(u"contrast")
        self.contrast.setFont(font)
        self.contrast.setFrameShape(QFrame.Shape.NoFrame)
        self.contrast.setFrameShadow(QFrame.Shadow.Raised)
        self.contrast.setTextFormat(Qt.TextFormat.RichText)
        self.contrast.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.contrast)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tSlider = QSlider(self.verticalLayoutWidget_2)
        self.tSlider.setObjectName(u"tSlider")
        self.tSlider.setEnabled(True)
        self.tSlider.setMinimum(0)
        self.tSlider.setMaximum(1000000000)
        self.tSlider.setOrientation(Qt.Orientation.Horizontal)
        self.tSlider.setInvertedAppearance(False)
        self.tSlider.setInvertedControls(False)
        self.tSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.tSlider.setTickInterval(100000000)

        self.horizontalLayout_2.addWidget(self.tSlider)

        self.tValue = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.tValue.setObjectName(u"tValue")
        self.tValue.setMinimumSize(QSize(140, 25))
        self.tValue.setDecimals(9)
        self.tValue.setMinimum(0.000000000000000)
        self.tValue.setMaximum(100000.000000000000000)
        self.tValue.setSingleStep(0.000001000000000)
        self.tValue.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.tValue.setValue(0.000000000000000)

        self.horizontalLayout_2.addWidget(self.tValue)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.contrast_2 = QLabel(self.verticalLayoutWidget_2)
        self.contrast_2.setObjectName(u"contrast_2")
        self.contrast_2.setFont(font)
        self.contrast_2.setFrameShape(QFrame.Shape.NoFrame)
        self.contrast_2.setFrameShadow(QFrame.Shadow.Raised)
        self.contrast_2.setTextFormat(Qt.TextFormat.RichText)
        self.contrast_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.contrast_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rSlider = QSlider(self.verticalLayoutWidget_2)
        self.rSlider.setObjectName(u"rSlider")
        self.rSlider.setEnabled(True)
        self.rSlider.setMinimum(0)
        self.rSlider.setMaximum(1000000000)
        self.rSlider.setOrientation(Qt.Orientation.Horizontal)
        self.rSlider.setInvertedAppearance(False)
        self.rSlider.setInvertedControls(False)
        self.rSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.rSlider.setTickInterval(100000000)

        self.horizontalLayout_3.addWidget(self.rSlider)

        self.rValue = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.rValue.setObjectName(u"rValue")
        self.rValue.setMinimumSize(QSize(140, 25))
        self.rValue.setDecimals(9)
        self.rValue.setMinimum(0.000000000000000)
        self.rValue.setMaximum(10000.000000000000000)
        self.rValue.setSingleStep(0.000001000000000)
        self.rValue.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.rValue.setValue(0.000000000000000)

        self.horizontalLayout_3.addWidget(self.rValue)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1060, 33))
        self.menuSave = QMenu(self.menubar)
        self.menuSave.setObjectName(u"menuSave")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSave.menuAction())
        self.menuSave.addAction(self.actionSave)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.threshold.setText(QCoreApplication.translate("MainWindow", u"Percent", None))
        self.contrast.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.contrast_2.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

