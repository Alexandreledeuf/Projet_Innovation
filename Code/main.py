import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import sys
from PyQt5 import QtWidgets
from PyQt5 import *
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from pyqtgraph import PlotWidget, plot
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import os
from PyQt5.QtWidgets import QComboBox
from datetime import datetime
from tkinter import *
from tkcalendar import *
import matplotlib.colors as mcolors
import mysql.connector
import random
from PyQt5.QtGui import QIcon, QPixmap
import pandas as pd
from PyQt5.QtWidgets import QGraphicsScene, QApplication, QGraphicsView, QGraphicsEllipseItem
from PyQt5.Qt import QColor
import sys, random



##---------------------------------------------   
        
class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi(r"C:\Users\ledeu\Desktop\m1\Projet_Innovation\Pyqt_fond\login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        import mysql.connector
        try:
        #connexion db
            con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
            cursor = con.cursor()

            user = email
            mdp= password
            cursor.execute("select * from user WHERE Pseudo = '%s' and mdp = '%s'" % (user, mdp))
            rud = cursor.fetchall()
            if (rud and  user == 'Admin') :
                admin=Admin()
                widget.addWidget(admin)
                widget.setCurrentIndex(widget.currentIndex()+1)
            if (rud and user != 'Admin') :
                lambda_=Lambda()
                widget.addWidget(lambda_)
                widget.setCurrentIndex(widget.currentIndex()+1)
            if not(rud) :
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.showMessage("Wrong Nickname/Password")
                error_dialog.setWindowModality(QtCore.Qt.WindowModal)
                
        except mysql.connector.Error as err:
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage('Une erreur est survenue !')
            error_dialog.setWindowModality(QtCore.Qt.WindowModal)
        finally:
            if(con.is_connected()):
                cursor.close()
                con.close()    
        
    def gotoadmin(self):
        admin=Admin()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotolambda(self):
        Lambda=Lambda()
        widget.addWidget(Lambda)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
##-----------------------------------------------------------------   

class Admin(QDialog):
    def __init__(self):
        super(Admin,self).__init__()
        loadUi(r"C:\Users\ledeu\Desktop\m1\Projet_Innovation\Pyqt_fond\admin.ui",self)  
        
        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(200, 160)
        cal.clicked[QtCore.QDate].connect(self.showDate)
        self.date = 0
        self.lbl = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.setGeometry(355,400,120,25)
        
        self.graphiquebutton_entree.clicked.connect(self.gotographiqueentree)
        self.label_entree = QtGui.QLabel(self)
        self.label_entree.setGeometry(75,520,130,50)
        
        self.graphiquebutton_plat.clicked.connect(self.gotographiqueplat)
        self.label_plat = QtGui.QLabel(self)
        self.label_plat.setGeometry(330,520,130,50)
        
        self.graphiquebutton_dessert.clicked.connect(self.gotographiquedessert)
        self.label_dessert = QtGui.QLabel(self)
        self.label_dessert.setGeometry(580,520,130,50)
        
        self.Menubutton.clicked.connect(self.gotoMenu)
        self.Tableaubutton.clicked.connect(self.gotoTableau)
        self.DisconnectedButton.clicked.connect(self.gotologin)

    def showDate(self, date):
        self.date = date
        self.lbl.setText(date.toString())
        
    
    def gotologin(self):
        log=Login()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotoMenu(self):
        menu=Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotoTableau(self):
        tab=Tableau()
        widget.addWidget(tab)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotographiqueentree(self):
        
        loadUi(r"C:\Users\ledeu\Desktop\m1\Projet_Innovation\Pyqt_fond\admin.ui",self)
        
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        if (self.date==0):
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage('Veuillez choisir une date !')
            error_dialog.setWindowModality(QtCore.Qt.WindowModal)
        else:
            newdate = self.date
            date_in_string = str(newdate.toPyDate())
            cursor.execute("SELECT * FROM choixplatetudiant where Date='%s'"% (date_in_string))
            row = cursor.fetchone()
            liste_entree = []
            while row is not None:
                entree=row[1]
                liste_entree.append(entree)
                row = cursor.fetchone()
            cursor.execute("select Entree1 from menudujour WHERE Date = '%s'" % (date_in_string))
            Entree1 = cursor.fetchone()
            cursor.execute("select Entree2 from menudujour WHERE Date = '%s'" % (date_in_string))
            Entree2 = cursor.fetchone()
            
            if(Entree1==None and Entree2 ==None):
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.showMessage('Cette Date ne contient aucun menu !')
                error_dialog.setWindowModality(QtCore.Qt.WindowModal)
            else:
                #entree

                loadUi(r"C:\Users\ledeu\Desktop\m1\Projet_Innovation\Pyqt_fond\admin.ui",self)
                x_entree_1 = 0
                x_entree_2 = 1
                y_entree_1 = 0
                y_entree_2 = 0
                for i in range(len(liste_entree)):
                    if(liste_entree[i]==Entree1[0]):
                        y_entree_1 += 1
                    else:
                        y_entree_2 += 1
                plot = pg.plot()  
                plot.setWindowTitle("Diagramme Entree") 
                plot.setWindowIcon(QtGui.QIcon(r'C:\Users\ledeu\Desktop\m1\Projet_Innovation\logoefood.png'))
                plot.addLegend()
                r1 = 60 
                b1 = 150
                g1 = 20
                r2 = 222
                b2 = 41
                g2 = 22

                color1 = (r1, g1, b1)
                color2 = (r2, g2, b2)
                bargraph = pg.BarGraphItem(x = [x_entree_1],height=[y_entree_1], width = 0.6,pen=color1,brush=color1,name = Entree1[0])
                bargraph2 = pg.BarGraphItem(x = [x_entree_2],height=[y_entree_2], width = 0.6,pen=color2,brush=color2,name = Entree2[0])
                plot.setGeometry(625,100,625,600)
                plot.setTitle("Choix Entrées")
                plot.addItem(bargraph) 
                plot.addItem(bargraph2)

                cursor.execute("SELECT GachisEntree FROM choixplatetudiant where Date='%s' and ChoixEntree = '%s'"% (date_in_string,Entree1[0]))
                row = cursor.fetchone()
                liste_gachis_entree = []
                while row is not None:
                    result = row[0]
                    liste_gachis_entree.append(result) 
                    row = cursor.fetchone()
                x_faible_entree = 0
                x_moyen_entree = 1
                x_important_entree = 2
                y_faible_entree = 0
                y_moyen_entree = 0
                y_important_entree = 0
                for i in range(len(liste_gachis_entree)):
                    if(liste_gachis_entree[i]=='Gachis Faible'):
                        y_faible_entree+=1
                    elif(liste_gachis_entree[i]=='Gachis Moyen'):
                        y_moyen_entree +=1
                    elif(liste_gachis_entree[i]=='Gachis Important'):
                        y_important_entree +=1
                gachis_entree_1 = y_important_entree+y_moyen_entree+y_faible_entree
                plot = pg.plot()
                plot.setWindowTitle(" Diagramme Gachis Entree 1") 
                plot.setWindowIcon(QtGui.QIcon(r'C:\Users\ledeu\Desktop\m1\Projet_Innovation\logoefood.png'))
                plot.addLegend()
                r1 = 80 
                b1 = 110
                g1 = 70
                
                r2 = 30
                b2 = 40
                g2 = 200
                
                r3 = 150
                b3 = 150
                g3 = 20

                color1 = (r1, g1, b1)
                color2 = (r2, g2, b2)
                color3 = (r3, g3, b3)
                bargraph = pg.BarGraphItem(x = [x_faible_entree],height=[y_faible_entree], width = 0.6,pen=color1,brush=color1,name ='Gachis Faible')
                bargraph2 = pg.BarGraphItem(x = [x_moyen_entree],height=[y_moyen_entree], width = 0.6,pen=color2,brush=color2,name ='Gachis Moyen') 
                bargraph3 = pg.BarGraphItem(x = [x_important_entree],height=[y_important_entree], width = 0.6,pen=color3,brush=color3,name ='Gachis Important') 
                plot.setGeometry(0,100,625,600)
                plot.setTitle("Gachis %s"%Entree1[0])
                plot.addItem(bargraph) 
                plot.addItem(bargraph2) 
                plot.addItem(bargraph3)
                

                cursor.execute("SELECT GachisEntree FROM choixplatetudiant where Date='%s' and ChoixEntree = '%s'"% (date_in_string,Entree2[0]))
                row = cursor.fetchone()
                liste_gachis_entree = []
                while row is not None:
                    result = row[0]
                    liste_gachis_entree.append(result) 
                    row = cursor.fetchone()
                x_faible_entree = 0
                x_moyen_entree = 1
                x_important_entree = 2
                y_faible_entree = 0
                y_moyen_entree = 0
                y_important_entree = 0
                for i in range(len(liste_gachis_entree)):
                    if(liste_gachis_entree[i]=='Gachis Faible'):
                        y_faible_entree+=1
                    elif(liste_gachis_entree[i]=='Gachis Moyen'):
                        y_moyen_entree +=1
                    elif(liste_gachis_entree[i]=='Gachis Important'):
                        y_important_entree +=1
                gachis_entree_2 = y_important_entree*3+y_moyen_entree*2+y_faible_entree
                plot = pg.plot()
                plot.setWindowTitle(" Diagramme Gachis Entree 2") 
                plot.setWindowIcon(QtGui.QIcon(r'C:\Users\ledeu\Desktop\m1\Projet_Innovation\logoefood.png'))
                plot.addLegend()
                r1 = 230 
                b1 = 50
                g1 = 10
                
                r2 = 180
                b2 = 210
                g2 = 100
                
                r3 = 140
                b3 = 0
                g3 = 200

                color1 = (r1, g1, b1)
                color2 = (r2, g2, b2)
                color3 = (r3, g3, b3)
                bargraph = pg.BarGraphItem(x = [x_faible_entree],height=[y_faible_entree], width = 0.6,pen=color1,brush=color1,name ='Gachis Faible')
                bargraph2 = pg.BarGraphItem(x = [x_moyen_entree],height=[y_moyen_entree], width = 0.6,pen=color2,brush=color2,name ='Gachis Moyen') 
                bargraph3 = pg.BarGraphItem(x = [x_important_entree],height=[y_important_entree], width = 0.6,pen=color3,brush=color3,name ='Gachis Important') 
                plot.setGeometry(1250,100,625,600)
                plot.setTitle("Gachis %s"%Entree2[0])
                plot.addItem(bargraph) 
                plot.addItem(bargraph2) 
                plot.addItem(bargraph3)
                if(gachis_entree_1>gachis_entree_2):
                    self.label_entree.setText("%s\nest l'entrée\nqui a le plus de Gachis"%Entree1[0])
                else:
                    self.label_entree.setText("%s\nest l'entrée\nqui a le plus de Gachis"%Entree2[0])
                
    
    def gotographiqueplat(self):
        
        loadUi(r"C:\Users\ledeu\Desktop\m1\Projet_Innovation\Pyqt_fond\admin.ui",self)
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        
        if (self.date==0):
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage('Veuillez choisir une date !')
            error_dialog.setWindowModality(QtCore.Qt.WindowModal)
        else:
            newdate = self.date
            date_in_string = str(newdate.toPyDate())

            cursor.execute("SELECT * FROM choixplatetudiant where Date='%s'"% (date_in_string))
            row = cursor.fetchone()
            liste_plat = []
            while row is not None:
                plat = row[2]
                liste_plat.append(plat)
                row = cursor.fetchone()

            cursor.execute("select Plat1 from menudujour WHERE Date = '%s'" % (date_in_string))
            Plat1 = cursor.fetchone()
            cursor.execute("select Plat2 from menudujour WHERE Date = '%s'" % (date_in_string))
            Plat2 = cursor.fetchone()

            if(Plat1==None and Plat2 ==None):
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.showMessage('Cette Date ne contient aucun menu !')
                error_dialog.setWindowModality(QtCore.Qt.WindowModal)
            else:
                #plat

                x_plat_1 = 0
                x_plat_2 = 1
                y_plat_1 = 0
                y_plat_2 = 0
                for i in range(len(liste_plat)):
                    if(liste_plat[i]==Plat1[0]):
                        y_plat_1+=1
                    else:
                        y_plat_2 +=1
                plot = pg.plot()
                plot.setWindowTitle("Diagramme Plat") 
                plot.setTitle("Choix Plats")
                plot.setWindowIcon(QtGui.QIcon(r'C:\Users\ledeu\Desktop\m1\Projet_Innovation\logoefood.png'))
                plot.addLegend()
                r1 = 60 
                b1 = 150
                g1 = 20
                r2 = 222
                b2 = 41
                g2 = 22

                color1 = (r1, g1, b1)
                color2 = (r2, g2, b2)
                bargraph = pg.BarGraphItem(x = [x_plat_1],height=[y_plat_1], width = 0.6,pen=color1,brush=color1,name = Plat1[0])
                bargraph2 = pg.BarGraphItem(x = [x_plat_2],height=[y_plat_2], width = 0.6,pen=color2,brush=color2,name = Plat2[0])
                plot.setGeometry(625,100,625,600)
                plot.addItem(bargraph) 
                plot.addItem(bargraph2) 

                cursor.execute("SELECT GachisPlat FROM choixplatetudiant where Date='%s' and ChoixPlat = '%s'"% (date_in_string,Plat1[0]))
                row = cursor.fetchone()
                liste_gachis_plat = []
                while row is not None:
                    result = row[0]
                    liste_gachis_plat.append(result) 
                    row = cursor.fetchone()
                x_faible_plat = 0
                x_moyen_plat = 1
                x_important_plat = 2
                y_faible_plat = 0
                y_moyen_plat = 0
                y_important_plat = 0
                for i in range(len(liste_gachis_plat)):
                    if(liste_gachis_plat[i]=='Gachis Faible'):
                        y_faible_plat+=1
                    elif(liste_gachis_plat[i]=='Gachis Moyen'):
                        y_moyen_plat +=1
                    elif(liste_gachis_plat[i]=='Gachis Important'):
                        y_important_plat +=1
                gachis_plat_1 = y_important_plat+y_moyen_plat+y_faible_plat
                plot = pg.plot()
                plot.setWindowTitle(" Diagramme Gachis Plat 1") 
                plot.setWindowIcon(QtGui.QIcon(r'C:\Users\ledeu\Desktop\m1\Projet_Innovation\logoefood.png'))
                plot.addLegend()
                r1 = 80 
                b1 = 110
                g1 = 70

                r2 = 30
                b2 = 40
                g2 = 200

                r3 = 150
                b3 = 150
                g3 = 20

                color1 = (r1, g1, b1)
                color2 = (r2, g2, b2)
                color3 = (r3, g3, b3)
                bargraph = pg.BarGraphItem(x = [x_faible_plat],height=[y_faible_plat], width = 0.6,pen=color1,brush=color1,name ='Gachis Faible')
                bargraph2 = pg.BarGraphItem(x = [x_moyen_plat],height=[y_moyen_plat], width = 0.6,pen=color2,brush=color2,name ='Gachis Moyen') 
                bargraph3 = pg.BarGraphItem(x = [x_important_plat],height=[y_important_plat], width = 0.6,pen=color3,brush=color3,name ='Gachis Important') 
                plot.setGeometry(0,100,625,600)
                plot.setTitle("Gachis %s"%Plat1[0])
                plot.addItem(bargraph) 
                plot.addItem(bargraph2) 
                plot.addItem(bargraph3)

                cursor.execute("SELECT GachisPlat FROM choixplatetudiant where Date='%s' and ChoixPlat = '%s'"% (date_in_string,Plat2[0]))
                row = cursor.fetchone()
                liste_gachis_plat = []
                while row is not None:
                    result = row[0]
                    liste_gachis_plat.append(result) 
                    row = cursor.fetchone()
                x_faible_plat = 0
                x_moyen_plat = 1
                x_important_plat = 2
                y_faible_plat = 0
                y_moyen_plat = 0
                y_important_plat = 0
                for i in range(len(liste_gachis_plat)):
                    if(liste_gachis_plat[i]=='Gachis Faible'):
                        y_faible_plat+=1
                    elif(liste_gachis_plat[i]=='Gachis Moyen'):
                        y_moyen_plat +=1
                    elif(liste_gachis_plat[i]=='Gachis Important'):
                        y_important_plat +=1
                gachis_plat_2 = y_important_plat*3+y_moyen_plat*2+y_faible_plat
                plot = pg.plot()
                plot.setWindowTitle(" Diagramme Gachis Plat 2") 
                plot.setWindowIcon(QtGui.QIcon(r'C:\Users\ledeu\Desktop\m1\Projet_Innovation\logoefood.png'))
                plot.addLegend()
                r1 = 80 
                b1 = 110
                g1 = 70

                r2 = 30
                b2 = 40
                g2 = 200

                r3 = 150
                b3 = 150
                g3 = 20

                color1 = (r1, g1, b1)
                color2 = (r2, g2, b2)
                color3 = (r3, g3, b3)
                bargraph = pg.BarGraphItem(x = [x_faible_plat],height=[y_faible_plat], width = 0.6,pen=color1,brush=color1,name ='Gachis Faible')
                bargraph2 = pg.BarGraphItem(x = [x_moyen_plat],height=[y_moyen_plat], width = 0.6,pen=color2,brush=color2,name ='Gachis Moyen') 
                bargraph3 = pg.BarGraphItem(x = [x_important_plat],height=[y_important_plat], width = 0.6,pen=color3,brush=color3,name ='Gachis Important') 
                plot.setGeometry(1250,100,625,600)
                plot.setTitle("Gachis %s"%Plat2[0])
                plot.addItem(bargraph) 
                plot.addItem(bargraph2) 
                plot.addItem(bargraph3)
                if(gachis_plat_1>gachis_plat_2):
                    self.label_plat.setText("%s\nest le plat\nqui a le plus de Gachis"%Plat1[0])
                else:
                    self.label_plat.setText("%s\nest le plat\nqui a le plus de Gachis"%Plat2[0])

        
    def gotographiquedessert(self):
        
        loadUi(r"C:\Users\ledeu\Desktop\m1\Projet_Innovation\Pyqt_fond\admin.ui",self)
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        
        if (self.date==0):
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage('Veuillez choisir une date !')
            error_dialog.setWindowModality(QtCore.Qt.WindowModal)
        else:
            newdate = self.date
            date_in_string = str(newdate.toPyDate())


            cursor.execute("SELECT * FROM choixplatetudiant where Date='%s'"% (date_in_string))
            row = cursor.fetchone()
            liste_dessert = []
            while row is not None:
                dessert = row[3]
                liste_dessert.append(dessert)
                row = cursor.fetchone()

            cursor.execute("select Dessert1 from menudujour WHERE Date = '%s'" % (date_in_string))
            Dessert1 = cursor.fetchone()
            cursor.execute("select Dessert2 from menudujour WHERE Date = '%s'" % (date_in_string))
            Dessert2 = cursor.fetchone()

            if(Dessert1==None and Dessert2 ==None):
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.showMessage('Cette Date ne contient aucun menu !')
                error_dialog.setWindowModality(QtCore.Qt.WindowModal)
            else:

                #dessert
                loadUi(r"C:\Users\ledeu\Desktop\m1\Projet_Innovation\Pyqt_fond\admin.ui",self)
                x_dessert_1 = 0
                x_dessert_2 = 1
                y_dessert_1 = 0
                y_dessert_2 = 0
                for i in range(len(liste_dessert)):
                    if(liste_dessert[i]==Dessert1[0]):
                        y_dessert_1 += 1
                    else:
                        y_dessert_2 += 1
                plot = pg.plot()   
                plot.setWindowTitle("Diagramme Dessert")
                plot.setTitle("Choix Desserts")
                plot.setWindowIcon(QtGui.QIcon(r'C:\Users\ledeu\Desktop\m1\Projet_Innovation\logoefood.png'))
                plot.addLegend()
                r1 = 60 
                b1 = 150
                g1 = 20
                r2 = 222
                b2 = 41
                g2 = 22

                color1 = (r1, g1, b1)
                color2 = (r2, g2, b2)
                bargraph = pg.BarGraphItem(x = [x_dessert_1],height=[y_dessert_1], width = 0.6,pen=color1,brush=color1,name = Dessert1[0])
                bargraph2 = pg.BarGraphItem(x = [x_dessert_2],height=[y_dessert_2], width = 0.6,pen=color2,brush=color2,name = Dessert2[0])
                plot.setGeometry(625,100,625,600)
                plot.addItem(bargraph) 
                plot.addItem(bargraph2) 

                cursor.execute("SELECT GachisDessert FROM choixplatetudiant where Date='%s' and ChoixDessert = '%s'"% (date_in_string,Dessert1[0]))
                row = cursor.fetchone()
                liste_gachis_dessert = []
                while row is not None:
                    result = row[0]
                    liste_gachis_dessert.append(result) 
                    row = cursor.fetchone()
                x_faible_dessert = 0
                x_moyen_dessert = 1
                x_important_dessert = 2
                y_faible_dessert = 0
                y_moyen_dessert = 0
                y_important_dessert = 0
                for i in range(len(liste_gachis_dessert)):
                    if(liste_gachis_dessert[i]=='Gachis Faible'):
                        y_faible_dessert+=1
                    elif(liste_gachis_dessert[i]=='Gachis Moyen'):
                        y_moyen_dessert +=1
                    elif(liste_gachis_dessert[i]=='Gachis Important'):
                        y_important_dessert +=1
                gachis_dessert_1 = y_important_dessert*3 + y_moyen_dessert*2+y_faible_dessert
                plot = pg.plot()
                plot.setWindowTitle(" Diagramme Gachis Dessert 1") 
                plot.setTitle("Gachis %s"%Dessert1[0])
                plot.setWindowIcon(QtGui.QIcon(r'C:\Users\ledeu\Desktop\m1\Projet_Innovation\logoefood.png'))
                plot.addLegend()
                r1 = 80 
                b1 = 110
                g1 = 70

                r2 = 30
                b2 = 40
                g2 = 200

                r3 = 150
                b3 = 150
                g3 = 20

                color1 = (r1, g1, b1)
                color2 = (r2, g2, b2)
                color3 = (r3, g3, b3)
                bargraph = pg.BarGraphItem(x = [x_faible_dessert],height=[y_faible_dessert], width = 0.6,pen=color1,brush=color1,name ='Gachis Faible')
                bargraph2 = pg.BarGraphItem(x = [x_moyen_dessert],height=[y_moyen_dessert], width = 0.6,pen=color2,brush=color2,name ='Gachis Moyen') 
                bargraph3 = pg.BarGraphItem(x = [x_important_dessert],height=[y_important_dessert], width = 0.6,pen=color3,brush=color3,name ='Gachis Important') 
                plot.setGeometry(0,100,625,600)
                plot.addItem(bargraph) 
                plot.addItem(bargraph2) 
                plot.addItem(bargraph3)

                cursor.execute("SELECT GachisDessert FROM choixplatetudiant where Date='%s' and ChoixDessert = '%s'"% (date_in_string,Dessert2[0]))
                row = cursor.fetchone()
                liste_gachis_dessert = []
                while row is not None:
                    result = row[0]
                    liste_gachis_dessert.append(result) 
                    row = cursor.fetchone()
                x_faible_dessert = 0
                x_moyen_dessert = 1
                x_important_dessert = 2
                y_faible_dessert = 0
                y_moyen_dessert = 0
                y_important_dessert = 0
                for i in range(len(liste_gachis_dessert)):
                    if(liste_gachis_dessert[i]=='Gachis Faible'):
                        y_faible_dessert+=1
                    elif(liste_gachis_dessert[i]=='Gachis Moyen'):
                        y_moyen_dessert +=1
                    elif(liste_gachis_dessert[i]=='Gachis Important'):
                        y_important_dessert +=1
                gachis_dessert_2 = y_important_dessert + y_moyen_dessert+y_faible_dessert
                plot = pg.plot()
                plot.setWindowTitle(" Diagramme Gachis Dessert 2")
                plot.setTitle("Gachis %s"%Dessert2[0])
                plot.setWindowIcon(QtGui.QIcon(r'C:\Users\ledeu\Desktop\m1\Projet_Innovation\logoefood.png'))
                plot.addLegend()
                r1 = 80 
                b1 = 110
                g1 = 70

                r2 = 30
                b2 = 40
                g2 = 200

                r3 = 150
                b3 = 150
                g3 = 20

                color1 = (r1, g1, b1)
                color2 = (r2, g2, b2)
                color3 = (r3, g3, b3)
                bargraph = pg.BarGraphItem(x = [x_faible_dessert],height=[y_faible_dessert], width = 0.6,pen=color1,brush=color1,name ='Gachis Faible')
                bargraph2 = pg.BarGraphItem(x = [x_moyen_dessert],height=[y_moyen_dessert], width = 0.6,pen=color2,brush=color2,name ='Gachis Moyen') 
                bargraph3 = pg.BarGraphItem(x = [x_important_dessert],height=[y_important_dessert], width = 0.6,pen=color3,brush=color3,name ='Gachis Important') 
                plot.setGeometry(1250,100,625,600)
                plot.addItem(bargraph) 
                plot.addItem(bargraph2) 
                plot.addItem(bargraph3) 
                if(gachis_dessert_1>gachis_dessert_2):
                    self.label_dessert.setText("%s\nest le plat\nqui a le plus de Gachis"%Dessert1[0])
                else:
                    self.label_dessert.setText("%s\nest le plat\nqui a le plus de Gachis"%Dessert2[0])
                

        
##-------------------------------------------------      
    
class Menu(QDialog):
    def __init__(self):
        super(Menu,self).__init__()
        loadUi(r"C:\Users\ledeu\Desktop\m1\Projet_Innovation\Pyqt_fond\Menu.ui",self)
        
        self.ajoutButton.clicked.connect(self.ajoutfunction)
        self.modifButton.clicked.connect(self.modiffunction)
        self.DisplayButton.clicked.connect(self.AfficheMenu)
        self.BackButton.clicked.connect(self.gotoadmin)
        
        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(200, 80)
        cal.clicked[QtCore.QDate].connect(self.showDate)
        self.date = 0
        self.lbl = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.setGeometry(355,340,120,25)
        
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        
        cursor.execute("select Entree from choixmenu")
        row = cursor.fetchone()
        Entree = []
        while row is not None:
            Entree.append(row[0])
            row = cursor.fetchone()
        self.comboBoxEntree1 = QComboBox(self)
        self.comboBoxEntree1.setGeometry(20,390,231,22)
        for i in range(len(Entree)):
            self.comboBoxEntree1.addItem(Entree[i])
        
        self.comboBoxEntree2 = QComboBox(self)
        self.comboBoxEntree2.setGeometry(20,420,231,22)
        for i in range(len(Entree)):
            self.comboBoxEntree2.addItem(Entree[i])
        
        cursor.execute("select Plat from choixmenu")
        row = cursor.fetchone()
        Plat = []
        while row is not None:
            Plat.append(row[0])
            row = cursor.fetchone()
        
        self.comboBoxPlat1 = QComboBox(self)
        self.comboBoxPlat1.setGeometry(270,390,261,22)
        for i in range(len(Plat)):
            self.comboBoxPlat1.addItem(Plat[i])
        
        self.comboBoxPlat2 = QComboBox(self)
        self.comboBoxPlat2.setGeometry(270,420,261,22)
        for i in range(len(Plat)):
            self.comboBoxPlat2.addItem(Plat[i])
        
        cursor.execute("select Dessert from choixmenu")
        row = cursor.fetchone()
        Dessert = []
        while row is not None:
            Dessert.append(row[0])
            row = cursor.fetchone()
        
        self.comboBoxDessert1 = QComboBox(self)
        self.comboBoxDessert1.setGeometry(550,390,231,22)
        for i in range(len(Dessert)):
            self.comboBoxDessert1.addItem(Dessert[i])
            
        self.comboBoxDessert2 = QComboBox(self)
        self.comboBoxDessert2.setGeometry(550,420,231,22)
        for i in range(len(Dessert)):
            self.comboBoxDessert2.addItem(Dessert[i])
            
        self.Label_entree_jour_1 = QtGui.QLabel(self)
        self.Label_entree_jour_1.setGeometry(640,140,171,21)
        self.Label_entree_jour_2 = QtGui.QLabel(self)
        self.Label_entree_jour_2.setGeometry(640,160,171,21)
        self.Label_plat_jour_1 = QtGui.QLabel(self)
        self.Label_plat_jour_1.setGeometry(640,180,171,21)
        self.Label_plat_jour_2 = QtGui.QLabel(self)
        self.Label_plat_jour_2.setGeometry(640,200,171,21)
        self.Label_dessert_jour_1 = QtGui.QLabel(self)
        self.Label_dessert_jour_1.setGeometry(640,220,171,21)
        self.Label_dessert_jour_2 = QtGui.QLabel(self)
        self.Label_dessert_jour_2.setGeometry(640,240,171,21)
        self.Label_date_choisi = QtGui.QLabel(self)
        self.Label_date_choisi.setGeometry(640,120,171,21)
        
    def showDate(self, date):
        self.date = date
        self.lbl.setText(date.toString())
    
    def AfficheMenu(self):
        
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        if (self.date==0):
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage('Veuillez choisir une date !')
            error_dialog.setWindowModality(QtCore.Qt.WindowModal)
        else:
            newdate = self.date
            date_in_string = str(newdate.toPyDate())
            self.Label_date_choisi.setText("Date:%s"%date_in_string)
            cursor.execute("select Entree1 from menudujour where Date='%s'"%date_in_string)
            row = cursor.fetchone()
            if(row==None):
                Entree1='  -  '
            else:
                Entree1 = row
            self.Label_entree_jour_1.setText("Entrée 1:%s"%Entree1)
            cursor.execute("select Entree2 from menudujour where Date='%s'"%date_in_string)
            row = cursor.fetchone()
            if(row==None):
                Entree2='  -  '
            else:
                Entree2 = row
            self.Label_entree_jour_2.setText("Entrée 2:%s"%Entree2)

            cursor.execute("select Plat1 from menudujour where Date='%s'"%date_in_string)
            row = cursor.fetchone()
            if(row==None):
                Plat1='  -  '
            else:
                Plat1 = row
            self.Label_plat_jour_1.setText("Plat 1:%s"%Plat1)
            cursor.execute("select Plat2 from menudujour where Date='%s'"%date_in_string)
            row = cursor.fetchone()
            if(row==None):
                Plat2='  -  '
            else:
                Plat2 = row
            self.Label_plat_jour_2.setText("Plat 2:%s"%Plat2)

            cursor.execute("select Dessert1 from menudujour where Date='%s'"%date_in_string)
            row = cursor.fetchone()
            if(row==None):
                Dessert1='  -  '
            else:
                Dessert1 = row
            self.Label_dessert_jour_1.setText("Dessert 1:%s"%Dessert1)
            cursor.execute("select Dessert2 from menudujour where Date='%s'"%date_in_string)
            row = cursor.fetchone()
            if(row==None):
                Dessert2='  -  '
            else:
                Dessert2 = row
            self.Label_dessert_jour_2.setText("Dessert 2:%s"%Dessert2)
        
        
    def ajoutfunction(self):
        
        if (self.date==0):
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage('Veuillez choisir une date !')
            error_dialog.setWindowModality(QtCore.Qt.WindowModal)
        else:
            newdate = self.date
            date_in_string = str(newdate.toPyDate())
            Entree1 = (self.comboBoxEntree1.currentText())
            Entree2 = (self.comboBoxEntree2.currentText())
            Plat1 = (self.comboBoxPlat1.currentText())
            Plat2 = (self.comboBoxPlat2.currentText())
            Dessert1 = (self.comboBoxDessert1.currentText())
            Dessert2 = (self.comboBoxDessert2.currentText())
            import mysql.connector
            try:
            #connexion db
                con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
                cursor = con.cursor()
                if(date_in_string==''):
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.showMessage('Veuillez sélectionner une date valide !')
                    error_dialog.setWindowModality(QtCore.Qt.WindowModal)
                    cursor.close()
                    con.close()
                    menu=Menu()
                    widget.addWidget(self)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                result = 0  
                cursor.execute("SELECT count(*) FROM menudujour where Date='%s'"% (date_in_string))
                result = cursor.fetchone()
                if(Entree1 == Entree2 or Plat1 == Plat2 or Dessert1 == Dessert2):
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.showMessage('Veuillez selectionner différent Choix dans votre menu !')
                    error_dialog.setWindowModality(QtCore.Qt.WindowModal)
                    cursor.close()
                    con.close()
                    menu=Menu()
                    widget.addWidget(self)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                if(result[0]!=0):
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.showMessage('Menu déjà ajouté à cette date !')
                    error_dialog.setWindowModality(QtCore.Qt.WindowModal)
                    cursor.close()
                    con.close()
                    menu=Menu()
                    widget.addWidget(self)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                else:
                    query = ("insert INTO menudujour (Date, Entree1, Entree2, Plat1, Plat2, Dessert1, Dessert2) VALUES (%s,%s,%s,%s,%s,%s,%s)")
                    data =(date_in_string,Entree1,Entree2,Plat1,Plat2,Dessert1,Dessert2)
                    cursor.execute(query, data)
                    con.commit()
                    admin=Admin()
                    widget.addWidget(admin)
                    widget.setCurrentIndex(widget.currentIndex()+1)
            except mysql.connector.Error as err:
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.showMessage('Une erreur est survenue !')
                error_dialog.setWindowModality(QtCore.Qt.WindowModal)
            finally:
                if(con.is_connected()):
                    cursor.close()
                    con.close()
                
    def modiffunction(self):
        if (self.date==0):
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage('Veuillez choisir une date !')
            error_dialog.setWindowModality(QtCore.Qt.WindowModal)
        else:
            newdate = self.date
            date_in_string = str(newdate.toPyDate())
            #Date=self.lineEdit.text()
            Entree1=self.lineEdit_2.text()
            Entree2=self.lineEdit_3.text()
            Plat1=self.lineEdit_4.text()
            Plat2=self.lineEdit_5.text()
            Dessert1=self.lineEdit_6.text()
            Dessert2=self.lineEdit_7.text()
            import mysql.connector
            try:
            #connexion db
                con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
                cursor = con.cursor()
                if(date_in_string==''):
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.showMessage('Veuillez sélectionner une date valide !')
                    error_dialog.setWindowModality(QtCore.Qt.WindowModal)
                    cursor.close()
                    con.close()
                    menu=Menu()
                    widget.addWidget(self)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                result = 0  
                cursor.execute("SELECT count(*) FROM menudujour where Date='%s'"% (date_in_string))
                result = cursor.fetchone()
                if(result[0]==0):
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.showMessage("Aucun Menu à ce jour n'a déjà été entré!")
                    error_dialog.setWindowModality(QtCore.Qt.WindowModal)
                    cursor.close()
                    con.close()
                    menu=Menu()
                    widget.addWidget(self)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                query = ("UPDATE menudujour SET Entree1=%s,Entree2=%s,Plat1=%s,Plat2=%s,Dessert1=%s,Dessert2=%s WHERE Date=%s")
                data =(Entree1,Entree2,Plat1,Plat2,Dessert1,Dessert2,date_in_string)
                cursor.execute(query, data)
                con.commit()
                admin=Admin()
                widget.addWidget(admin)
                widget.setCurrentIndex(widget.currentIndex()+1)
            except mysql.connector.Error as err:
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.showMessage('Une erreur est survenue !')
                error_dialog.setWindowModality(QtCore.Qt.WindowModal)
            finally:
                if(con.is_connected()):
                    cursor.close()
                    con.close()
                
    def gotoadmin(self):
        admin=Admin()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex()+1)

##---------------------------------------------------     
    
class Selection(QDialog):
    
    def __init__(self):
        super(Selection,self).__init__()
        loadUi(r"C:\Users\ledeu\Desktop\m1\Projet_Innovation\Pyqt_fond\Choice.ui",self)
        
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        
        datedujour = datetime.today().strftime('%Y-%m-%d')
        cursor.execute("select Entree1 from menudujour WHERE Date = '%s'" % (datedujour))
        Entree1 = cursor.fetchone()
        if(Entree1==None):
            Entree1 = '-'
        cursor.execute("select Entree2 from menudujour WHERE Date = '%s'" % (datedujour))
        Entree2 = cursor.fetchone()
        if(Entree2==None):
            Entree2 = '-'
        
        cursor.execute("select Dessert1 from menudujour WHERE Date = '%s'" % (datedujour))
        Dessert1 = cursor.fetchone()
        if(Dessert1==None):
            Dessert1 = '-'
        cursor.execute("select Dessert2 from menudujour WHERE Date = '%s'" % (datedujour))
        Dessert2 = cursor.fetchone()
        if(Dessert2==None):
            Dessert2 = '-'
        
        cursor.execute("select Plat1 from menudujour WHERE Date = '%s'" % (datedujour))
        Plat1 = cursor.fetchone()
        if(Plat1==None):
            Plat1 = '-'
        cursor.execute("select Plat2 from menudujour WHERE Date = '%s'" % (datedujour))
        Plat2 = cursor.fetchone()
        if(Plat2==None):
            Plat2 = '-'

        
        self.comboBoxEntree = QComboBox(self)
        self.comboBoxEntree.setGeometry(250,150,100,35)
        self.comboBoxEntree.addItem(Entree1[0])
        self.comboBoxEntree.addItem(Entree2[0])
        
        self.comboBoxPlat = QComboBox(self)
        self.comboBoxPlat.setGeometry(250,200,100,35)
        self.comboBoxPlat.addItem(Plat1[0])
        self.comboBoxPlat.addItem(Plat2[0])
        
        self.comboBoxDessert = QComboBox(self)
        self.comboBoxDessert.setGeometry(250,250,100,35)
        self.comboBoxDessert.addItem(Dessert1[0])
        self.comboBoxDessert.addItem(Dessert2[0])
        
        self.comboBoxGachisentree = QComboBox(self)
        self.comboBoxGachisentree.setGeometry(450,150,100,35)
        self.comboBoxGachisentree.addItem("Gachis Faible")
        self.comboBoxGachisentree.addItem("Gachis Moyen")
        self.comboBoxGachisentree.addItem("Gachis Important")
        
        self.comboBoxGachisplat = QComboBox(self)
        self.comboBoxGachisplat.setGeometry(450,200,100,35)
        self.comboBoxGachisplat.addItem("Gachis Faible")
        self.comboBoxGachisplat.addItem("Gachis Moyen")
        self.comboBoxGachisplat.addItem("Gachis Important")
        
        self.comboBoxGachisdessert = QComboBox(self)
        self.comboBoxGachisdessert.setGeometry(450,250,100,35)
        self.comboBoxGachisdessert.addItem("Gachis Faible")
        self.comboBoxGachisdessert.addItem("Gachis Moyen")
        self.comboBoxGachisdessert.addItem("Gachis Important")
        
        self.EnterButton.setGeometry(350,350,100,35)
        self.EnterButton.clicked.connect(self.getValue)
        
        self.EnterButton_2.setGeometry(350,400,100,35)
        self.EnterButton_2.clicked.connect(self.gotolambda)
    
    def gotolambda(self):
        lambda_=Lambda()
        widget.addWidget(lambda_)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def getValue(self):
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        Date = datetime.today().strftime('%Y-%m-%d')
        query = ("insert INTO choixplatetudiant (Date, ChoixEntree, ChoixPlat, ChoixDessert, GachisEntree, GachisPlat, GachisDessert) VALUES (%s,%s,%s,%s,%s,%s,%s)")
        Entree = (self.comboBoxEntree.currentText())
        Plat = (self.comboBoxPlat.currentText())
        Dessert = (self.comboBoxDessert.currentText())
        cursor.execute("select Entree1 from menudujour WHERE Date = '%s'" % (Date))
        Entree1 = cursor.fetchone()
        cursor.execute("select Entree2 from menudujour WHERE Date = '%s'" % (Date))
        Entree2 = cursor.fetchone()
        cursor.execute("select Plat1 from menudujour WHERE Date = '%s'" % (Date))
        Plat1 = cursor.fetchone()
        cursor.execute("select Plat2 from menudujour WHERE Date = '%s'" % (Date))
        Plat2 = cursor.fetchone()
        cursor.execute("select Dessert1 from menudujour WHERE Date = '%s'" % (Date))
        Dessert1 = cursor.fetchone()
        cursor.execute("select Dessert2 from menudujour WHERE Date = '%s'" % (Date))
        Dessert2 = cursor.fetchone()
        if(Entree == 'Entree1'):
            Entree = Entree1[0]
        elif(Entree == 'Entree2'):
            Entree = Entree2[0]
        if(Plat == 'Plat1'):
            Plat = Plat1[0]
        elif(Plat == 'Plat2'):
            Plat = Plat2[0]
        if(Dessert == 'Dessert1'):
            Dessert = Dessert1[0]
        elif(Dessert == 'Dessert2'):
            Dessert = Dessert2[0]
        GachisEntree = (self.comboBoxGachisentree.currentText())
        GachisPlat = (self.comboBoxGachisplat.currentText())
        GachisDessert = (self.comboBoxGachisdessert.currentText())
        data =(Date,Entree,Plat,Dessert,GachisEntree,GachisPlat,GachisDessert)
        cursor.execute(query, data)
        con.commit()
        select=Selection()
        widget.addWidget(select)
        widget.setCurrentIndex(widget.currentIndex()+1)

##-----------------------------------------------------

class Lambda(QDialog):
    def __init__(self):
        super(Lambda,self).__init__()
        loadUi(r"C:\Users\ledeu\Desktop\m1\Projet_Innovation\Pyqt_fond\Lambda.ui",self)
        
        self.SelectionButton.clicked.connect(self.gotoselection)
        self.DisconnectedButton.clicked.connect(self.gotologin)
        
    def gotologin(self):
        log=Login()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotoselection(self):
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        
        datedujour = datetime.today().strftime('%Y-%m-%d')

        cursor.execute("select Entree1 from menudujour WHERE Date = '%s'" % (datedujour))
        Entree1 = cursor.fetchone()
        cursor.execute("select Entree2 from menudujour WHERE Date = '%s'" % (datedujour))
        Entree2 = cursor.fetchone()
        cursor.execute("select Dessert1 from menudujour WHERE Date = '%s'" % (datedujour))
        Dessert1 = cursor.fetchone()
        cursor.execute("select Dessert2 from menudujour WHERE Date = '%s'" % (datedujour))
        Dessert2 = cursor.fetchone()
        cursor.execute("select Plat1 from menudujour WHERE Date = '%s'" % (datedujour))
        Plat1 = cursor.fetchone()
        cursor.execute("select Plat2 from menudujour WHERE Date = '%s'" % (datedujour))
        Plat2 = cursor.fetchone()
        if(Entree1==None and Entree2==None and Plat1==None and Plat2==None and Dessert1==None and Dessert2==None):
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage("Aucun Menu n'a été ajouté à ce jour !")
            error_dialog.setWindowModality(QtCore.Qt.WindowModal)
        else:
            select=Selection()
            widget.addWidget(select)
            widget.setCurrentIndex(widget.currentIndex()+1)

##--------------------------------------------------------------------------------------

class Tableau(QDialog):
    def __init__(self):
        super(Tableau,self).__init__()
        loadUi(r"C:\Users\ledeu\Desktop\m1\Projet_Innovation\Pyqt_fond\Tableau.ui",self)
        
        self.EnterButton.clicked.connect(self.Affichage)
        self.ReturnButton.clicked.connect(self.gotoAdmin)
        self.PieButton.clicked.connect(self.gotoPie)
        self.DiagramButton.clicked.connect(self.gotodiagentree)
        self.DiagramButton_2.clicked.connect(self.gotodiagplat)
        self.DiagramButton_3.clicked.connect(self.gotodiagdessert)
        
        self.comboBoxMois = QComboBox(self)
        self.comboBoxMois.setGeometry(250,180,141,22)
        self.comboBoxMois.addItem("Janvier")
        self.comboBoxMois.addItem("Fevrier")
        self.comboBoxMois.addItem("Mars")
        self.comboBoxMois.addItem("Avril")
        self.comboBoxMois.addItem("Mai")
        self.comboBoxMois.addItem("Juin")
        self.comboBoxMois.addItem("Juillet")
        self.comboBoxMois.addItem("Août")
        self.comboBoxMois.addItem("Septembre")
        self.comboBoxMois.addItem("Octobre")
        self.comboBoxMois.addItem("Novembre")
        self.comboBoxMois.addItem("Décembre")
        
        self.comboBoxAnnee = QComboBox(self)
        self.comboBoxAnnee.setGeometry(400,180,141,22)
        for i in range(2021,2100):
            self.comboBoxAnnee.addItem("%s"%i)
            
        
        
    def gotoAdmin(self):
        admin=Admin()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotodiagentree(self):    
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        Mois = (self.comboBoxMois.currentText())
        Année = (self.comboBoxAnnee.currentText())
        choixdate = (Mois+Année)
        if(Mois=="Janvier"):
            self.Datedebut = ("%s-01-01"%Année)
            self.Datefin = ("%s-01-31"%Année)
        elif(Mois=="Fevrier"):
            self.Datedebut = ("%s-02-01"%Année)
            if(int(Année)%4==0):
                self.Datefin = ("%s-02-29"%Année)
            else:
                self.Datefin = ("%s-02-28"%Année)
        elif(Mois=="Mars"):
            self.Datedebut = ("%s-03-01"%Année)
            self.Datefin = ("%s-03-31"%Année)
        elif(Mois=="Avril"):
            self.Datedebut = ("%s-04-01"%Année)
            self.Datefin = ("%s-04-30"%Année)
        elif(Mois=="Mai"):
            self.Datedebut = ("%s-05-01"%Année)
            self.Datefin = ("%s-05-31"%Année)
        elif(Mois=="Juin"):
            self.Datedebut = ("%s-06-01"%Année)
            self.Datefin = ("%s-06-30"%Année)
        elif(Mois=="Juillet"):
            self.Datedebut = ("%s-07-01"%Année)
            self.Datefin = ("%s-07-31"%Année)
        elif(Mois=="Août"):
            self.Datedebut = ("%s-08-01"%Année)
            self.Datefin = ("%s-08-31"%Année)
        elif(Mois=="Septembre"):
            self.Datedebut = ("%s-09-01"%Année)
            self.Datefin = ("%s-09-30"%Année)
        elif(Mois=="Octobre"):
            self.Datedebut = ("%s-10-01"%Année)
            self.Datefin = ("%s-10-31"%Année)
        elif(Mois=="Novembre"):
            self.Datedebut = ("%s-11-01"%Année)
            self.Datefin = ("%s-11-30"%Année)
        elif(Mois=="Decembre"):
            self.Datedebut = ("%s-12-01"%Année)
            self.Datefin = ("%s-12-31"%Année)
    
        cursor.execute("SELECT DISTINCT ChoixEntree FROM choixplatetudiant where Date BETWEEN '%s' AND '%s'" % (self.Datedebut,self.Datefin))
        row = cursor.fetchone()
        Liste_Entree = []
        while row is not None:
            Liste_Entree.append(row[0])
            row = cursor.fetchone()  
            
        liste_gachis_entree = []
        for i in range(len(Liste_Entree)):
            cursor.execute("SELECT Gachis_Entree FROM gachis_tableau where Date='%s' and Entree = '%s'"% (choixdate,Liste_Entree[i]))
            row = cursor.fetchone()
            while row is not None:
                liste_gachis_entree.append(row[0]) 
                row = cursor.fetchone()

        plot = pg.plot()   
        plot.setWindowTitle("Diagramme Entrée")
        plot.setTitle("Gachis Entrée")
        plot.setWindowIcon(QtGui.QIcon(r'C:\Users\ledeu\Desktop\m1\Projet_Innovation\logoefood.png'))
        plot.addLegend()
        list_x = []
        colours = []
        
        for i in range(len(liste_gachis_entree)):
            list_x.append(i)
        
        for i in range(len(liste_gachis_entree)):
            color = []
            for count in range(3):
                color.append(random.randrange(0, 255))
            addcolor = (color[0],color[1],color[2])
            plot.addItem(pg.BarGraphItem(x = [list_x[i]],height=[liste_gachis_entree[i]], width = 0.6,pen=addcolor,brush=addcolor,name=Liste_Entree[i])) 
        plot.setGeometry(625,100,625,600)
        
        
    def gotodiagplat(self):    
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        Mois = (self.comboBoxMois.currentText())
        Année = (self.comboBoxAnnee.currentText())
        choixdate = (Mois+Année)
        if(Mois=="Janvier"):
            self.Datedebut = ("%s-01-01"%Année)
            self.Datefin = ("%s-01-31"%Année)
        elif(Mois=="Fevrier"):
            self.Datedebut = ("%s-02-01"%Année)
            if(int(Année)%4==0):
                self.Datefin = ("%s-02-29"%Année)
            else:
                self.Datefin = ("%s-02-28"%Année)
        elif(Mois=="Mars"):
            self.Datedebut = ("%s-03-01"%Année)
            self.Datefin = ("%s-03-31"%Année)
        elif(Mois=="Avril"):
            self.Datedebut = ("%s-04-01"%Année)
            self.Datefin = ("%s-04-30"%Année)
        elif(Mois=="Mai"):
            self.Datedebut = ("%s-05-01"%Année)
            self.Datefin = ("%s-05-31"%Année)
        elif(Mois=="Juin"):
            self.Datedebut = ("%s-06-01"%Année)
            self.Datefin = ("%s-06-30"%Année)
        elif(Mois=="Juillet"):
            self.Datedebut = ("%s-07-01"%Année)
            self.Datefin = ("%s-07-31"%Année)
        elif(Mois=="Août"):
            self.Datedebut = ("%s-08-01"%Année)
            self.Datefin = ("%s-08-31"%Année)
        elif(Mois=="Septembre"):
            self.Datedebut = ("%s-09-01"%Année)
            self.Datefin = ("%s-09-30"%Année)
        elif(Mois=="Octobre"):
            self.Datedebut = ("%s-10-01"%Année)
            self.Datefin = ("%s-10-31"%Année)
        elif(Mois=="Novembre"):
            self.Datedebut = ("%s-11-01"%Année)
            self.Datefin = ("%s-11-30"%Année)
        elif(Mois=="Decembre"):
            self.Datedebut = ("%s-12-01"%Année)
            self.Datefin = ("%s-12-31"%Année)
    
        cursor.execute("SELECT DISTINCT ChoixPlat FROM choixplatetudiant where Date BETWEEN '%s' AND '%s'" % (self.Datedebut,self.Datefin))
        row = cursor.fetchone()
        Liste_Plat = []
        while row is not None:
            Liste_Plat.append(row[0])
            row = cursor.fetchone()  
            
        liste_gachis_plat = []
        for i in range(len(Liste_Plat)):
            cursor.execute("SELECT Gachis_Plat FROM gachis_tableau where Date='%s' and Plat = '%s'"% (choixdate,Liste_Plat[i]))
            row = cursor.fetchone()
            while row is not None:
                liste_gachis_plat.append(row[0]) 
                row = cursor.fetchone()

        plot = pg.plot()   
        plot.setWindowTitle("Diagramme Plat")
        plot.setTitle("Gachis Plat")
        plot.setWindowIcon(QtGui.QIcon(r'C:\Users\ledeu\Desktop\m1\Projet_Innovation\logoefood.png'))
        plot.addLegend()
        list_x = []
        colours = []
        
        for i in range(len(liste_gachis_plat)):
            list_x.append(i)
        
        for i in range(len(liste_gachis_plat)):
            color = []
            for count in range(3):
                color.append(random.randrange(0, 255))
            addcolor = (color[0],color[1],color[2])
            plot.addItem(pg.BarGraphItem(x = [list_x[i]],height=[liste_gachis_plat[i]], width = 0.6,pen=addcolor,brush=addcolor,name=Liste_Plat[i])) 
        plot.setGeometry(625,100,625,600)
        
    def gotodiagdessert(self):   
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        Mois = (self.comboBoxMois.currentText())
        Année = (self.comboBoxAnnee.currentText())
        choixdate = (Mois+Année)
        if(Mois=="Janvier"):
            self.Datedebut = ("%s-01-01"%Année)
            self.Datefin = ("%s-01-31"%Année)
        elif(Mois=="Fevrier"):
            self.Datedebut = ("%s-02-01"%Année)
            if(int(Année)%4==0):
                self.Datefin = ("%s-02-29"%Année)
            else:
                self.Datefin = ("%s-02-28"%Année)
        elif(Mois=="Mars"):
            self.Datedebut = ("%s-03-01"%Année)
            self.Datefin = ("%s-03-31"%Année)
        elif(Mois=="Avril"):
            self.Datedebut = ("%s-04-01"%Année)
            self.Datefin = ("%s-04-30"%Année)
        elif(Mois=="Mai"):
            self.Datedebut = ("%s-05-01"%Année)
            self.Datefin = ("%s-05-31"%Année)
        elif(Mois=="Juin"):
            self.Datedebut = ("%s-06-01"%Année)
            self.Datefin = ("%s-06-30"%Année)
        elif(Mois=="Juillet"):
            self.Datedebut = ("%s-07-01"%Année)
            self.Datefin = ("%s-07-31"%Année)
        elif(Mois=="Août"):
            self.Datedebut = ("%s-08-01"%Année)
            self.Datefin = ("%s-08-31"%Année)
        elif(Mois=="Septembre"):
            self.Datedebut = ("%s-09-01"%Année)
            self.Datefin = ("%s-09-30"%Année)
        elif(Mois=="Octobre"):
            self.Datedebut = ("%s-10-01"%Année)
            self.Datefin = ("%s-10-31"%Année)
        elif(Mois=="Novembre"):
            self.Datedebut = ("%s-11-01"%Année)
            self.Datefin = ("%s-11-30"%Année)
        elif(Mois=="Decembre"):
            self.Datedebut = ("%s-12-01"%Année)
            self.Datefin = ("%s-12-31"%Année)
    
        cursor.execute("SELECT DISTINCT ChoixDessert FROM choixplatetudiant where Date BETWEEN '%s' AND '%s'" % (self.Datedebut,self.Datefin))
        row = cursor.fetchone()
        Liste_Dessert = []
        while row is not None:
            Liste_Dessert.append(row[0])
            row = cursor.fetchone()  
            
        liste_gachis_dessert = []
        for i in range(len(Liste_Dessert)):
            cursor.execute("SELECT Gachis_Dessert FROM gachis_tableau where Date='%s' and Dessert = '%s'"% (choixdate,Liste_Dessert[i]))
            row = cursor.fetchone()
            while row is not None:
                liste_gachis_dessert.append(row[0]) 
                row = cursor.fetchone()

        plot = pg.plot()   
        plot.setWindowTitle("Diagramme Dessert")
        plot.setTitle("Gachis Dessert")
        plot.setWindowIcon(QtGui.QIcon(r'C:\Users\ledeu\Desktop\m1\Projet_Innovation\logoefood.png'))
        plot.addLegend()
        list_x = []
        colours = []
        
        for i in range(len(liste_gachis_dessert)):
            list_x.append(i)
        
        for i in range(len(liste_gachis_dessert)):
            color = []
            for count in range(3):
                color.append(random.randrange(0, 255))
            addcolor = (color[0],color[1],color[2])
            plot.addItem(pg.BarGraphItem(x = [list_x[i]],height=[liste_gachis_dessert[i]], width = 0.6,pen=addcolor,brush=addcolor,name=Liste_Dessert[i])) 
        plot.setGeometry(625,100,625,600)

        
    def gotoPie(self):
        scene = QGraphicsScene()
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        Mois = (self.comboBoxMois.currentText())
        Année = (self.comboBoxAnnee.currentText())
        choixdate = (Mois+Année)
        if(Mois=="Janvier"):
            self.Datedebut = ("%s-01-01"%Année)
            self.Datefin = ("%s-01-31"%Année)
        elif(Mois=="Fevrier"):
            self.Datedebut = ("%s-02-01"%Année)
            if(int(Année)%4==0):
                self.Datefin = ("%s-02-29"%Année)
            else:
                self.Datefin = ("%s-02-28"%Année)
        elif(Mois=="Mars"):
            self.Datedebut = ("%s-03-01"%Année)
            self.Datefin = ("%s-03-31"%Année)
        elif(Mois=="Avril"):
            self.Datedebut = ("%s-04-01"%Année)
            self.Datefin = ("%s-04-30"%Année)
        elif(Mois=="Mai"):
            self.Datedebut = ("%s-05-01"%Année)
            self.Datefin = ("%s-05-31"%Année)
        elif(Mois=="Juin"):
            self.Datedebut = ("%s-06-01"%Année)
            self.Datefin = ("%s-06-30"%Année)
        elif(Mois=="Juillet"):
            self.Datedebut = ("%s-07-01"%Année)
            self.Datefin = ("%s-07-31"%Année)
        elif(Mois=="Août"):
            self.Datedebut = ("%s-08-01"%Année)
            self.Datefin = ("%s-08-31"%Année)
        elif(Mois=="Septembre"):
            self.Datedebut = ("%s-09-01"%Année)
            self.Datefin = ("%s-09-30"%Année)
        elif(Mois=="Octobre"):
            self.Datedebut = ("%s-10-01"%Année)
            self.Datefin = ("%s-10-31"%Année)
        elif(Mois=="Novembre"):
            self.Datedebut = ("%s-11-01"%Année)
            self.Datefin = ("%s-11-30"%Année)
        elif(Mois=="Decembre"):
            self.Datedebut = ("%s-12-01"%Année)
            self.Datefin = ("%s-12-31"%Année)
    
        cursor.execute("SELECT DISTINCT ChoixEntree FROM choixplatetudiant where Date BETWEEN '%s' AND '%s'" % (self.Datedebut,self.Datefin))
        row = cursor.fetchone()
        Liste_Entree = []
        while row is not None:
            Liste_Entree.append(row[0])
            row = cursor.fetchone()  
            
        liste_gachis_entree = []
        for i in range(len(Liste_Entree)):
            cursor.execute("SELECT Gachis_Entree FROM gachis_tableau where Date='%s' and Entree = '%s'"% (choixdate,Liste_Entree[i]))
            row = cursor.fetchone()
            while row is not None:
                liste_gachis_entree.append(row[0]) 
                row = cursor.fetchone()
        total = 0
        set_angle = 0
        count1 = 0
        colours = []
        total = sum(liste_gachis_entree)

        for count in range(len(liste_gachis_entree)):
            number = []
            for count in range(3):
                number.append(random.randrange(0, 255))
            colours.append(QColor(number[0],number[1],number[2]))

        for gachis in liste_gachis_entree:
            # Max span is 5760, so we have to calculate corresponding span angle
            angle = round(float(gachis*5760)/total)
            ellipse = QGraphicsEllipseItem(0,0,500,500)
            ellipse.setPos(0,0)
            ellipse.setStartAngle(set_angle)
            ellipse.setSpanAngle(angle)
            ellipse.setBrush(colours[count1])
            #,Liste_Entree[gachis]
            set_angle += angle
            count1 += 1
            scene.addItem(ellipse)

        self.view = QGraphicsView(scene)
        self.view.show()

        
    def Affichage(self):
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        query = ('DELETE FROM gachis_tableau')
        cursor.execute(query)
        con.commit()
        
        Mois = (self.comboBoxMois.currentText())
        Année = (self.comboBoxAnnee.currentText())
        choixdate = (Mois+Année)
        if(Mois=="Janvier"):
            self.Datedebut = ("%s-01-01"%Année)
            self.Datefin = ("%s-01-31"%Année)
        elif(Mois=="Fevrier"):
            self.Datedebut = ("%s-02-01"%Année)
            if(int(Année)%4==0):
                self.Datefin = ("%s-02-29"%Année)
            else:
                self.Datefin = ("%s-02-28"%Année)
        elif(Mois=="Mars"):
            self.Datedebut = ("%s-03-01"%Année)
            self.Datefin = ("%s-03-31"%Année)
        elif(Mois=="Avril"):
            self.Datedebut = ("%s-04-01"%Année)
            self.Datefin = ("%s-04-30"%Année)
        elif(Mois=="Mai"):
            self.Datedebut = ("%s-05-01"%Année)
            self.Datefin = ("%s-05-31"%Année)
        elif(Mois=="Juin"):
            self.Datedebut = ("%s-06-01"%Année)
            self.Datefin = ("%s-06-30"%Année)
        elif(Mois=="Juillet"):
            self.Datedebut = ("%s-07-01"%Année)
            self.Datefin = ("%s-07-31"%Année)
        elif(Mois=="Août"):
            self.Datedebut = ("%s-08-01"%Année)
            self.Datefin = ("%s-08-31"%Année)
        elif(Mois=="Septembre"):
            self.Datedebut = ("%s-09-01"%Année)
            self.Datefin = ("%s-09-30"%Année)
        elif(Mois=="Octobre"):
            self.Datedebut = ("%s-10-01"%Année)
            self.Datefin = ("%s-10-31"%Année)
        elif(Mois=="Novembre"):
            self.Datedebut = ("%s-11-01"%Année)
            self.Datefin = ("%s-11-30"%Année)
        elif(Mois=="Decembre"):
            self.Datedebut = ("%s-12-01"%Année)
            self.Datefin = ("%s-12-31"%Année)
        
        con = mysql.connector.connect(host='localhost', database='Efood', user='root', password='') 
        cursor = con.cursor()
        

        cursor.execute("SELECT DISTINCT ChoixEntree FROM choixplatetudiant where Date BETWEEN '%s' AND '%s'" % (self.Datedebut,self.Datefin))
        row = cursor.fetchone()
        Liste_Entree = []
        Resultat_analyse_entree = []
        while row is not None:
            Liste_Entree.append(row[0])
            row = cursor.fetchone()
            
        cursor.execute("SELECT DISTINCT ChoixPlat FROM choixplatetudiant where Date BETWEEN '%s' AND '%s'" % (self.Datedebut,self.Datefin))
        row = cursor.fetchone()
        Liste_Plat = []
        Resultat_analyse_plat = []
        while row is not None:
            Liste_Plat.append(row[0])
            row = cursor.fetchone()
            
        cursor.execute("SELECT DISTINCT ChoixDessert FROM choixplatetudiant where Date BETWEEN '%s' AND '%s'" % (self.Datedebut,self.Datefin))
        row = cursor.fetchone()
        Liste_Dessert = []
        Resultat_analyse_dessert = []
        while row is not None:
            Liste_Dessert.append(row[0])
            row = cursor.fetchone()
            
        for i in range(len(Liste_Entree)):
            cursor.execute("SELECT GachisEntree FROM choixplatetudiant where Date BETWEEN '%s' AND '%s' and ChoixEntree = '%s'"% (self.Datedebut,self.Datefin,Liste_Entree[i]))
            row = cursor.fetchone()
            liste_gachis_entree = []
            while row is not None:
                liste_gachis_entree.append(row[0]) 
                row = cursor.fetchone()
            x_faible_entree = 0
            x_moyen_entree = 1
            x_important_entree = 2
            y_faible_entree = 0
            y_moyen_entree = 0
            y_important_entree = 0
            for j in range(len(liste_gachis_entree)):
                if(liste_gachis_entree[j]=='Gachis Faible'):
                    y_faible_entree+=1
                elif(liste_gachis_entree[j]=='Gachis Moyen'):
                    y_moyen_entree +=1
                elif(liste_gachis_entree[j]=='Gachis Important'):
                    y_important_entree +=1
            gachis_entree_max = (1*y_important_entree+0.66*y_moyen_entree+0.33*y_faible_entree)/(y_important_entree+y_moyen_entree+y_faible_entree)*100
            gachis_entree_min = (0.66*y_important_entree+0.33*y_moyen_entree+0.01*y_faible_entree)/(y_important_entree+y_moyen_entree+y_faible_entree)*100
            Resultat_analyse_entree.append(Liste_Entree[i])
            Resultat_analyse_entree.append((gachis_entree_min+gachis_entree_max)/2)
            
        for i in range(len(Liste_Plat)):
            cursor.execute("SELECT GachisPlat FROM choixplatetudiant where Date BETWEEN '%s' AND '%s' and ChoixPlat = '%s'"% (self.Datedebut,self.Datefin,Liste_Plat[i]))
            row = cursor.fetchone()
            liste_gachis_plat = []
            while row is not None:
                liste_gachis_plat.append(row[0]) 
                row = cursor.fetchone()
            x_faible_plat = 0
            x_moyen_plat = 1
            x_important_plat = 2
            y_faible_plat = 0
            y_moyen_plat = 0
            y_important_plat = 0
            for j in range(len(liste_gachis_plat)):
                if(liste_gachis_plat[j]=='Gachis Faible'):
                    y_faible_plat+=1
                elif(liste_gachis_plat[j]=='Gachis Moyen'):
                    y_moyen_plat +=1
                elif(liste_gachis_plat[j]=='Gachis Important'):
                    y_important_plat +=1
            gachis_plat_max = (1*y_important_plat+0.66*y_moyen_plat+0.33*y_faible_plat)/(y_important_plat+y_moyen_plat+y_faible_plat)*100
            gachis_plat_min = (0.66*y_important_plat+0.33*y_moyen_plat+0.01*y_faible_plat)/(y_important_plat+y_moyen_plat+y_faible_plat)*100
        
            Resultat_analyse_plat.append(Liste_Plat[i])
            Resultat_analyse_plat.append((gachis_plat_min+gachis_plat_max)/2)
            
            
        for i in range(len(Liste_Dessert)):
            cursor.execute("SELECT GachisDessert FROM choixplatetudiant where Date BETWEEN '%s' AND '%s' and ChoixDessert = '%s'"% (self.Datedebut,self.Datefin,Liste_Dessert[i]))
            row = cursor.fetchone()
            liste_gachis_dessert = []
            while row is not None:
                liste_gachis_dessert.append(row[0]) 
                row = cursor.fetchone()
            x_faible_dessert = 0
            x_moyen_dessert = 1
            x_important_dessert = 2
            y_faible_dessert = 0
            y_moyen_dessert = 0
            y_important_dessert = 0
            for j in range(len(liste_gachis_dessert)):
                if(liste_gachis_dessert[j]=='Gachis Faible'):
                    y_faible_dessert+=1
                elif(liste_gachis_dessert[j]=='Gachis Moyen'):
                    y_moyen_dessert +=1
                elif(liste_gachis_dessert[j]=='Gachis Important'):
                    y_important_dessert +=1
            gachis_dessert_max = (1*y_important_dessert+0.66*y_moyen_dessert+0.33*y_faible_dessert)/(y_important_dessert+y_moyen_dessert+y_faible_dessert)*100
            gachis_dessert_min = (0.66*y_important_dessert+0.33*y_moyen_dessert+0.01*y_faible_dessert)/(y_important_dessert+y_moyen_dessert+y_faible_dessert)*100
            Resultat_analyse_dessert.append(Liste_Dessert[i])
            Resultat_analyse_dessert.append((gachis_dessert_min+gachis_dessert_max)/2)


        
        for i in range(len(Resultat_analyse_plat)):
            if(i%2==0):
                query = ("insert INTO gachis_tableau (Date,Entree,Gachis_Entree,Plat,Gachis_Plat,Dessert,Gachis_Dessert) VALUES (%s,%s,%s,%s,%s,%s,%s)")
                Date = (Mois+Année)
                data =(Date,Resultat_analyse_entree[i],Resultat_analyse_entree[i+1],Resultat_analyse_plat[i],Resultat_analyse_plat[i+1],Resultat_analyse_dessert[i],Resultat_analyse_dessert[i+1])
                cursor.execute(query, data)
                con.commit()
                
        cursor.execute("select Entree,Gachis_Entree,Plat,Gachis_Plat,Dessert,Gachis_Dessert from gachis_tableau WHERE Date='%s'"%choixdate)
        row = cursor.fetchone()
        Aliment_Entree = []
        Aliment_Plat = []
        Aliment_Dessert = []
        Gachis_Entree = []
        Gachis_Plat = []
        Gachis_Dessert = []
        while row is not None:
            Aliment_Entree.append(row[0])
            Gachis_Entree.append(row[1])
            Aliment_Plat.append(row[2])
            Gachis_Plat.append(row[3])
            Aliment_Dessert.append(row[4])
            Gachis_Dessert.append(row[5])
            row = cursor.fetchone()
        self.tableWidget.setRowCount(len(Aliment_Entree))
        self.tableWidget.setColumnCount(6)
        #newItem = QTableWidgetItem(tr("%s" % ((row+1)*(column+1))))
        for i in range(len(Aliment_Entree)):
            
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(Aliment_Entree[i]))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem('%s'%Gachis_Entree[i]))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(Aliment_Plat[i]))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem('%s'%Gachis_Plat[i]))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(Aliment_Dessert[i]))
            self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem('%s'%Gachis_Dessert[i]))
        

##--------------------------------------------------------------------------------------

app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(620)
widget.setWindowTitle('E-food')
widget.setWindowIcon(QtGui.QIcon(r'C:\Users\ledeu\Desktop\m1\Projet_Innovation\logoefood.png'))
widget.show()
app.exec_()
