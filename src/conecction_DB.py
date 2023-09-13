import mariadb

######
from tkinter import ttk
from tkinter import * 
import tkinter as tk
from tkinter import font

#####
from ventana_login import *
from ventana_home import *

class DB():
    def __init__(self, window, frame_login, message):
        self.frame_login = frame_login
        self.message=message
        self.window=window
        self.connection = mariadb.connect(
            host="localhost",
            user="root",
            password="CrisBaraja10042",
            database="Password_manager_python"
        )
    def validar_login(self, user, password):

        self.cursor = self.connection.cursor()

        sql = """ SELECT * FROM Datos_personales WHERE User_email= "{}" AND User_password = "{}" """.format(user, password)

        self.cursor.execute(sql)
        self.resultado = self.cursor.fetchone()

        if self.resultado:
            self.ventana_home = ventana_hom(self.window, self.resultado, self.cursor, self.connection)  # Crear una instancia de ventana_hom
            self.ventana_home.mostrar_ventana()

        else:
            #Mensaje de erro de usuario y clave
            self.message("Usuario o clave incorrecta", "#F2C12E", self.frame_login)
