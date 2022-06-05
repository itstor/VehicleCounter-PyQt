# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledrSZAtZ.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import cv2
import numpy as np
import torch


class Ui_MainWindow(object):
    def __init__(self):
        self.image = None
        self.leftCounter = {
            2: 0, # car
            3: 0, # motor
            5: 0, # bus
            7: 0 # truck
        }
        self.rightCounter = {
            2: 0, # car
            3: 0, # motor
            5: 0, # bus
            7: 0 # truck
        }
        self.isPlay = False
        self.videoPath = None
        self.yHeight = 40
        self.isTwoWay = True

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Vehicle Counter")
        MainWindow.resize(863, 614)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(961, 700))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QLabel(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalSlider = QSlider(self.centralwidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setValue(self.yHeight)

        self.verticalLayout_2.addWidget(self.verticalSlider)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 9)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.playButton = QPushButton(self.centralwidget)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setEnabled(False)

        self.verticalLayout_6.addWidget(self.playButton)

        self.loadButton = QPushButton(self.centralwidget)
        self.loadButton.setObjectName(u"loadButton")

        self.verticalLayout_6.addWidget(self.loadButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.twoWayCheckbox = QCheckBox(self.centralwidget)
        self.twoWayCheckbox.setObjectName(u"twoWayCheckbox")
        self.twoWayCheckbox.setChecked(self.isTwoWay)

        self.verticalLayout_5.addWidget(self.twoWayCheckbox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.TruckLeft = QLineEdit(self.centralwidget)
        self.TruckLeft.setObjectName(u"TruckLeft")
        self.TruckLeft.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.TruckLeft)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.BusLeft = QLineEdit(self.centralwidget)
        self.BusLeft.setObjectName(u"BusLeft")
        self.BusLeft.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.BusLeft)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.CarLeft = QLineEdit(self.centralwidget)
        self.CarLeft.setObjectName(u"CarLeft")
        self.CarLeft.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.CarLeft)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.MotorLeft = QLineEdit(self.centralwidget)
        self.MotorLeft.setObjectName(u"MotorLeft")
        self.MotorLeft.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.MotorLeft)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.TruckRight = QLineEdit(self.centralwidget)
        self.TruckRight.setObjectName(u"TruckRight")
        self.TruckRight.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.TruckRight)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.BusRight = QLineEdit(self.centralwidget)
        self.BusRight.setObjectName(u"BusRight")
        self.BusRight.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.BusRight)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.CarRight = QLineEdit(self.centralwidget)
        self.CarRight.setObjectName(u"CarRight")
        self.CarRight.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.CarRight)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.MotorRight = QLineEdit(self.centralwidget)
        self.MotorRight.setObjectName(u"MotorRight")
        self.MotorRight.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.MotorRight)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.TotalField = QLineEdit(self.centralwidget)
        self.TotalField.setObjectName(u"TotalField")
        self.TotalField.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.TotalField)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 7)
        self.verticalLayout.setStretch(1, 2)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.loadButton.clicked.connect(self.getfiles)
        self.playButton.clicked.connect(self.playstop)
        self.verticalSlider.connect(ui.verticalSlider, SIGNAL("valueChanged(int)"), self.heightChanged)
        self.twoWayCheckbox.stateChanged.connect(self.setTwoWay)

    def setTwoWay(self):
        if self.twoWayCheckbox.isChecked():
            self.isTwoWay = True
            self.BusRight.show()
            self.MotorRight.show()
            self.CarRight.show()
            self.TruckRight.show()
            self.label_9.show()
            self.label_10.show()
            self.label_11.show()
            self.label_12.show()
            
        else:
            self.isTwoWay = False
            self.BusRight.hide()
            self.MotorRight.hide()
            self.CarRight.hide()
            self.TruckRight.hide()
            self.label_9.hide()
            self.label_10.hide()
            self.label_11.hide()
            self.label_12.hide()


    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Vehicle Counter", u"Vehicle Counter", None))
        self.frame.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"Load Video", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.twoWayCheckbox.setText(QCoreApplication.translate("MainWindow", u"Two Way?", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Counter", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Truck", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Bus", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Car", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Motorcycle", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Truck", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Bus", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Car", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Motorcycle", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Total", None))
    # retranslateUi

    def getfiles(self):
      dlg = QFileDialog()
      dlg.setFileMode(QFileDialog.AnyFile)
      filenames = []
		
      if dlg.exec_():
         filenames = dlg.selectedFiles()
         self.videoPath = filenames[0]
         print(self.videoPath)
         if self.videoPath is not None:
             self.playButton.setEnabled(True)

    def updateCounter(self):
        self.BusLeft.setText(str(self.leftCounter[5]))
        self.CarLeft.setText(str(self.leftCounter[2]))
        self.MotorLeft.setText(str(self.leftCounter[3]))
        self.TruckLeft.setText(str(self.leftCounter[7]))
        self.BusRight.setText(str(self.rightCounter[5]))
        self.CarRight.setText(str(self.rightCounter[2]))
        self.MotorRight.setText(str(self.rightCounter[3]))
        self.TruckRight.setText(str(self.rightCounter[7]))
        self.TotalField.setText(str(sum(self.leftCounter.values()) + sum(self.rightCounter.values())))

    def playstop(self):
        if self.isPlay == False:
            self.isPlay = True
            self.loadButton.setEnabled(False)
            self.twoWayCheckbox.setEnabled(False)
            self.playButton.setText("Stop")
            self.startYolo()
        else:
            self.isPlay = False
            self.loadButton.setEnabled(True)
            self.twoWayCheckbox.setEnabled(True)
            self.playButton.setText("Play")

    def heightChanged(self, height):
        self.yHeight = height

    def VehicleDetection(self, model, frame):
        results = model(frame)
        resBBox = results.pandas().xyxy[0]
        DetectedBBox = resBBox.values.tolist()
        BBox = []
        pmin = np.array([-1, -1])
        pmax = np.array([-1, -1])
        pmid = (pmin+pmax)/2
        # Inisialisasi BBox
        BBox.append([pmin, pmax, pmid, -1, -1, -1, -1])
        for xmin, ymin, xmax, ymax, conf, cl, nama in DetectedBBox:
            IdPrev = -1
            # Menyimpan Bounding Box
            xmid = (xmin+xmax)/2
            ymid = (ymin+ymax)/2
            BBox.append([xmin, ymin, xmax, ymax, xmid,
                        ymid, conf, cl, nama, IdPrev])
        return BBox


    def VehicleTracking(self, ListBBox):
        # Memastikan sedikitnya terdapat dua frame yang di proses
        # ---Begin  len(ListBBox)>2
        if len(ListBBox) >= 2:
            # Bounding Box yang frame yang terakhir disimpan
            CurrentBBox = ListBBox[-1]
            # Bounding Box dari frame sebelumnya
            PrevBBox = ListBBox[-2]

            # ---Begin for IndexLast = 0 in range(len(LastBBox):
            for IndexLast in range(1, len(CurrentBBox)):

                xminc, yminc, xmaxc, ymaxc, xmidc, ymidc,  confc, clc, namac, IdPrevC = CurrentBBox[
                    IndexLast]
                rCocok = 100000000000
                IndexCocok = -1
                # ********************************************************
                # ***Mencari Obyek yang bersesuaian dari frame sebelumnya
                # ********************************************************
                # ---Begin IndexPrev =0 in range(PrevBBox
                for IndexPrev in range(1, len(PrevBBox)):

                    xminp, yminp, xmaxp, ymaxp, xmidp, ymidp,  confp, clp, namep, IdPrevp = PrevBBox[
                        IndexPrev]
                    # 3. pmax1 dan pmax2
                    v = np.array([xmidc-xmidp, ymidc-ymidp])
                    RTot = np.linalg.norm(v)
                    # ---Begin IndexSave ==-1
                    if IndexCocok == -1:
                        rCocok = RTot
                        IndexCocok = IndexPrev
                    else:
                        if RTot < rCocok:
                            rCocok = RTot
                            IndexCocok = IndexPrev
                    # --- End IndexSave ==-1
                # ---End for IndexPrev =0 in range(PrevBBox)

                # --- Begin if IndexCocok>-1:
                if IndexCocok > -1:
                    # Update

                    ListBBox[-1][IndexLast][9] = IndexCocok
                # --- end if IndexCocok>-1:
            # ---End for IndexLast = 0 in range(len(LastBBox):
        # -- End if len(ListBBox)>2
        return ListBBox


    def VehicleCounting(self, ListBBox, MidLineY):
        # Memastikan sedikitnya terdapat dua frame yang di proses
        # ---Begin  len(ListBBox)>2



        if len(ListBBox) >= 2:
            # Bounding Box yang frame yang terakhir disimpan
            CurrentBBox = ListBBox[-1]
            # Bounding Box dari frame sebelumnya
            PrevBBox = ListBBox[-2]
            # ---Begin for IndexLast = 0 in range(len(LastBBox):
            for IndexLast in range(1, len(CurrentBBox)):
                xminc, yminc, xmaxc, ymaxc, xmidc, ymidc,  confc, clc, namac, IdPrevC = CurrentBBox[
                    IndexLast]

                if IdPrevC > -1:

                    xminm, yminm, xmaxm, ymaxm, xmidm, ymidm = PrevBBox[IdPrevC][0:6]
                    LewatBatas = (ymidc-MidLineY)*(ymidm-MidLineY)
                    if LewatBatas <= 0:
                        # Menentukan apakah arah kendaraan menuju ke atas atau kebawah
                        Arah = ymidc-MidLineY
                        if Arah >= 0:
                            self.rightCounter[clc] += 1
                        else:
                            self.leftCounter[clc] += 1

            self.updateCounter()


    def DrawLastBoundingBox(self, frame, ListBBox):
        # Bounding Box yang frame yang terakhir disimpan
        CurrentBBox = ListBBox[-1]
        # Bounding Box dari frame sebelumnya
        # ---Begin for IndexLast = 0 in range(len(LastBBox):
        for IndexLast in range(1, len(CurrentBBox)):
            xminc, yminc, xmaxc, ymaxc, xmidc, ymidc,  confc, clc, namac, IdPrevC = CurrentBBox[
                IndexLast]
            pc1 = (int(xminc), int(yminc))
            pc2 = (int(xmaxc), int(ymaxc))
            pcc = (int(xmidc), int(ymidc))
            frame = cv2.rectangle(frame, pc1, pc2, (255, 0, 255), 1)
            frame = cv2.circle(frame, pcc, 2, (255, 255, 255), 1)

        return frame


    def DrawVehicleVector(self, frame, ListBBox):
        if len(ListBBox) >= 2:
            # Bounding Box yang frame yang terakhir disimpan
            CurrentBBox = ListBBox[-1]
            # Bounding Box dari frame sebelumnya
            PrevBBox = ListBBox[-2]
            # ---Begin for IndexLast = 0 in range(len(LastBBox):
            for IndexLast in range(1, len(CurrentBBox)):
                xminc, yminc, xmaxc, ymaxc, xmidc, ymidc,  confc, clc, namac, IdPrevC = CurrentBBox[
                    IndexLast]

                if IdPrevC > -1:

                    xminm, yminm, xmaxm, ymaxm, xmidm, ymidm = PrevBBox[IdPrevC][0:6]
                    p1 = (int(xmidc), int(ymidc))
                    p2 = (int(2*xmidc-xmidm), int(2*ymidc-ymidm))

                    frame = cv2.line(frame, p1, p2, (255, 255, 255), 1)
        return frame

    def updateFrame(self):
        frame = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        image = QImage(
            frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.frame.setPixmap(QPixmap.fromImage(image))
        self.frame.setScaledContents(True)
        self.frame.setScaledContents(True)
        

    def startYolo(self):
        cap = cv2.VideoCapture(self.videoPath)

        model = torch.hub.load('ultralytics/yolov5', 'yolov5n', _verbose=False)
        model.classes = [2, 3, 5, 7]
        #model.conf =0.4
        #model.iou=0.2
        if (cap.isOpened()== False): 
            print("Error opening video stream or file")
        #Membuat Daftar Untuk menyimpan Bounding Box yang diperoleh disetiap frame.
        ListBBox=[]
        # Membaca setiap frame sampai selesai
        #---Begin while(cap.isOpened()):

        while(cap.isOpened() and self.isPlay and self.videoPath is not None):
            # Capture frame-by-frame
            QApplication.processEvents()
            ret, self.image = cap.read()
            #Membuat Garis batas untuk perhitungan Kendaraan yang Lewat
            b, c, w = self.image.shape
            MidLineY = b - b*self.yHeight/100

            if ret == True:
                BBox = self.VehicleDetection(model, self.image)
                    #Menambahkan Bounding box ke ListBBox
                ListBBox.append(BBox)
                if len(ListBBox)>2:
                    ListBBox.pop(0)
                ListBBox= self.VehicleTracking(ListBBox)
                self.VehicleCounting(ListBBox,MidLineY)
                    
                self.image = self.DrawLastBoundingBox(self.image, ListBBox)
                self.image = self.DrawVehicleVector(self.image,ListBBox)
                p1 = (0, int(MidLineY))
                p2 = (c, int(MidLineY))
                self.image = cv2.line(self.image, p1, p2, (0,255,0), 2)
                self.updateFrame()
                if self.isPlay == False:
                    break


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())