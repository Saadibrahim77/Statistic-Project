from PyQt5.QtWidgets import QMainWindow ,QApplication,QPushButton
from matplotlib.backends.backend_qt5agg import  FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import  matplotlib.pyplot as pt
import math as ma

import ExcelReader as ex



class Graphs(object):

    @staticmethod
    def barchart(self):
        pt.bar(ex.get_Xlist(),ex.get_Ylist())
        pt.show()

    @staticmethod
    def Scatterplot(self):
        pt.scatter(ex.get_Xlist(),ex.get_Ylist())
        pt.show()
    @staticmethod
    def XBoxplot(self):
        pt.boxplot(ex.get_Xlist())
        pt.show()
    @staticmethod
    def YBoxplot(self):
        pt.boxplot(ex.get_Ylist())
        pt.show()
    @staticmethod
    def XHistogram(self):
        z=0
        c=10000000000000000000

        for i in GUI.excelReader.get_Xlist():
            if z < i:
                z = i;

            if c > i:
                c = i
            print(i)
        print("ok")
        no = int(1 + (3.3 * ma.log10(len(ex.get_Xlist())))) + 1
        range = z - c
        length = int(range / no) + 1
        A = []
        w = 0
        print("listx:..........")
        while w < len(ex.get_Xlist()):
            A.append(w)
            print(w)
            w += length


        pt.hist(ExcelReader.get_Xlist(), bins=A)
        pt.show()
        print("aaaa")

    @staticmethod
    def YHistogram(self):
        z = 0
        c = 10000000000000000000
        for i in ExcelReader.get_Ylist():
            if z < i:
                z = i;

            if c > i:
                c = i
        no = int(1 + (3.3 * ma.log10(len(ExcelReader.get_Ylist())))) + 1
        range = z - c
        length = int(range / no) + 1
        A = []
        w = 0
        print("listy:..........")
        while w < len(ExcelReader.get_Ylist()):
            A.append(w)
            w += length
        pt.hist(ExcelReader.get_Ylist(), bins=A)
        pt.show()








