import sys

from PyQt5.uic.properties import QtCore
from scipy.stats import pearsonr
import statistics as st
from builtins import zip
import  pandas as pa
import numpy as np
import matplotlib.pyplot as pt
from PyQt5.QtWidgets import QMainWindow ,QApplication,QPushButton
from matplotlib.backends.backend_qt5agg import  FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from numpy.distutils.system_info import lapack_atlas_3_10_info
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QWidget,QTableWidget,QTableWidgetItem
from PyQt5.uic import loadUi


from ExcelReader import ExcelReader as E
import  math as ma
class GUI(QDialog):
    excelReader = E()

    def __init__(self):
        super(GUI,self).__init__()
        loadUi('finalGUI.ui',self)
        self.setWindowTitle("Statistics Assistant")
        self.setFixedSize(self.size())
        self.tableOfItems.setRowCount(self.excelReader.get_Ncols());
        self.tableOfItems.setColumnCount(self.excelReader.get_Nrows()-1);

        i=0
        for i in range(len(self.excelReader.get_Xlist())):
            #self.tableOfItems.setItem.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
            self.tableOfItems.setItem(0, i, QTableWidgetItem(str(self.excelReader.get_Xlist()[i])))
            i+=1

        j=0
        for i in range(len(self.excelReader.get_Ylist())):
            self.tableOfItems.setItem(1, j, QTableWidgetItem(str(self.excelReader.get_Ylist()[j])))
            j+=1



        self.barchart.clicked.connect(self.Draw_Bar_Chart)
        self.mode_1_btn.clicked.connect(self.calcXmode)
        self.mode_2_btn.clicked.connect(self.calcYmode)
        self.median_1_btn.clicked.connect(self.calcXmedian)
        self.median_2_btn.clicked.connect(self.calcYmedian)
        self.mean_1_btn.clicked.connect(self.calcXmean)
        self.mean_2_btn.clicked.connect(self.calcYmean)
        self.btn_z_zcore.clicked.connect(self.calcX_zscore)
        self.btn_z_zcore2.clicked.connect(self.calcY_zscore)
        self.standardDeviation_btn.clicked.connect(self.calcX_SD)
        self.standardDeviation_2_btn.clicked.connect(self.calcY_SD)
        self.varience_2_btn.clicked.connect(self.calcY_variance)
        self.varience_1_btn.clicked.connect(self.calcX_variance)
        self.correlationC_btn.clicked.connect(self.calc_R)
        self.histogram_1_btn.clicked.connect(self.Draw_XHistogram)
        self.histogram_2_btn.clicked.connect(self.Draw_YHistogram)
        self.boxPlot_2_btn.clicked.connect(self.Draw_YBoxplot)
        self.boxPlot_1_btn.clicked.connect(self.Draw_XBoxplot)
        self.btn_clear.clicked.connect(self.Cleartext)


    def Cleartext(self):
        self.result.setPlaceholderText("")

    def calc_R(self):
        for i in self.excelReader.get_Xlist():
            print(i)
        R = np.corrcoef(self.excelReader.get_Xlist(),self.excelReader.get_Ylist())[0,1]
        Rvalue = round(abs(R),1)
        print(Rvalue)
        if Rvalue>=0.1 and Rvalue<=0.3:
            self.result.setPlaceholderText("The correlation Coefficient is :("+str(R)+")\n"+"This mean Weak relationship")
        elif Rvalue>=0.4 and Rvalue<=0.6:
            self.result.setPlaceholderText(
                "The correlation Coefficient is :(" + str(R) + ") " + "This mean Moderate relationship")
        elif Rvalue>=0.7 and Rvalue<=0.9:
            self.result.setPlaceholderText(
                "The correlation Coefficient is :(" + str(R) + ")  " + "This mean Strong relationship")
        else:
            self.result.setPlaceholderText(
                "The correlation Coefficient is :(" + str(R) + ")  " + "This mean Perfect relationship")






    def calcX_SD(self):
        sd = (st.stdev(self.excelReader.get_Xlist()))
        self.result.setPlaceholderText(str(sd))

    def calcY_SD(self):
        sd = (st.stdev(self.excelReader.get_Ylist()))
        self.result.setPlaceholderText(str(sd))
    def calcX_variance(self):
        var = (st.variance(self.excelReader.get_Xlist()))
        self.result.setPlaceholderText(str(var))

    def calcY_variance(self):
        var = (st.variance(self.excelReader.get_Ylist()))
        self.result.setPlaceholderText(str(var))

    def set_table(self):
        sd = (st.stdev(self.excelReader.get_Xlist()))
        self.result.setPlaceholderText(str(sd))


    def calcX_zscore(self):
        p = 0
        try:
            valuex = float(self.xVariableInput.text())
            for i in self.excelReader.get_Xlist():

                if float(i) == valuex:
                    print(valuex)
                    meanx = float(st.mean(self.excelReader.get_Xlist()))
                    print(meanx)
                    sd = float(st.stdev(self.excelReader.get_Xlist()))
                    print(sd)
                    z_score = (valuex - meanx) / sd
                    print(z_score)
                    self.result.setPlaceholderText(str(z_score))
                    p = 1
                    break
            if p == 0:
                self.result.setPlaceholderText("value not in list")
        except Exception:
            self.result.setPlaceholderText("Please Enter value must in list")
        p = 0

    def calcY_zscore(self):
        p=0
        try:
            valuey = float(self.yVariableInput.text())
            for i in self.excelReader.get_Ylist():

                if float(i) == valuey:
                    print(valuey)
                    meany = float(st.mean(self.excelReader.get_Ylist()))
                    print(meany)
                    sd = float(st.stdev(self.excelReader.get_Ylist()))
                    print(sd)
                    z_score = (valuey - meany) / sd
                    print(z_score)
                    self.result.setPlaceholderText(str(z_score))
                    p = 1
                    break
            if p == 0:
                self.result.setPlaceholderText("value not in list")
        except Exception:
            self.result.setPlaceholderText("Please Enter value must in list")
        p=0

    def calcYmode(self):
        try:
            mode = str(st.mode(self.excelReader.get_Ylist()))
            self.result.setPlaceholderText(mode)
        except Exception:
            self.result.setPlaceholderText("no mode")

    def calcXmode(self):
        try:
            mode = str(st.mode(self.excelReader.get_Xlist()))
            self.result.setPlaceholderText(mode)
        except Exception:
            self.result.setPlaceholderText("no mode")

    def calcXmedian(self):
        median = str(st.median(self.excelReader.get_Xlist()))
        self.result.setPlaceholderText(median)

    def calcYmedian(self):
        median = str(st.median(self.excelReader.get_Ylist()))
        self.result.setPlaceholderText(median) #median2Output

    def calcXmean(self):
        mean = str(st.mean(self.excelReader.get_Xlist()))
        self.result.setPlaceholderText(mean)

    def calcYmean(self):
        mean = str(st.mean(self.excelReader.get_Ylist()))
        self.result.setPlaceholderText(mean)



    def Draw_Bar_Chart(self):
        pt.bar(self.excelReader.get_Xlist(), self.excelReader.get_Ylist())
        pt.show()


    def Draw_XHistogram(self):
        z = 0
        c = 10000000000000000000

        for i in self.excelReader.get_Xlist():
            if z < i:
                z = i;

            if c > i:
                c = i
            print(i)
        print("ok")
        no = int(1 + (3.3 * ma.log10(len(self.excelReader.get_Xlist())))) + 1
        range = z - c
        length = int(range / no) + 1
        A = []
        w = 0
        print("listx:..........")
        while w < len(self.excelReader.get_Xlist()):
            A.append(w)
            print(w)
            w += length

        pt.hist(self.excelReader.get_Xlist(), bins=A)
        pt.show()


    def Draw_YHistogram(self):
        z = 0
        c = 10000000000000000000
        for i in self.excelReader.get_Ylist():
            if z < i:
                z = i;

            if c > i:
                c = i
        no = int(1 + (3.3 * ma.log10(len(self.excelReader.get_Ylist())))) + 1
        range = z - c
        length = int(range / no) + 1
        A = []
        w = 0
        print("listy:..........")
        while w < len(self.excelReader.get_Ylist()):
            A.append(w)
            w += length
        pt.hist(self.excelReader.get_Ylist(), bins=A)
        pt.show()

    def Draw_XBoxplot(self):
        pt.boxplot(self.excelReader.get_Xlist())
        pt.show()


    def Draw_YBoxplot(self):
        pt.boxplot(self.excelReader.get_Ylist())
        pt.show()


    def Draw_Scatterplot(self):
        pt.scatter(self.excelReader.get_Xlist(), self.excelReader.get_Ylist())
        pt.show()





