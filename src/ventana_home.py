from tkinter import ttk
from tkinter import * 
import tkinter as tk
from tkinter import font
from conecction_DB import *
import mariadb
from PIL import ImageTk, Image
import os

class ventana_hom():
    def __init__(self, window, resultado, cursor, connection):
        self.window = window
        self.resultado = resultado
        self.cursor = cursor
        self.connection = connection

        ##ACCEDE A LA RUTA PRINCIPAL DEL PROYECTO
        self.c_principal = os.path.dirname(__file__)
        print(self.c_principal)
        ##ACCEDE A LA CAPETA IMG
        self.c_img = os.path.join(self.c_principal, "img")
        print(self.c_img)

    def mostrar_ventana(self):
        self.ventana_home = tk.Toplevel(self.window)
        self.ventana_home.title("Home")
        self.ventana_home.geometry("1000x500") #COLOR DE FONDO
        self.ventana_home.resizable(False, False)
        self.ventana_home.configure(bg ="#555275")
        self.datos()
    
    def datos(self):
        self.fuente_pequena = font.Font(family="Arial", size=8,)
        self.fuente_mediana = font.Font(family="Arial", size=10)
        self.fuente_grande = font.Font(family="Arial", size=13)

        # LLamar funcion para crear un LabelFrame
        self.frame_datos_personales = LabelFrame(self.ventana_home, bg = "#323050", fg = "black", borderwidth=0)
        self.frame_datos_personales.place(x = 0, y = 0, width = 300, height = 200)
        
        label_logo_home = ImageTk.PhotoImage(Image.open(os.path.join(self.c_img, "KeyVault_logo_HOME.png")))
        self.label_logo_usuario = Label(self.frame_datos_personales, image= label_logo_home, borderwidth=0)
        self.label_logo_usuario.label_logo_home = label_logo_home
        self.label_logo_usuario.grid(row=1, column=0)

        nombre_apledio_U = (f"{self.resultado[1]}")

        self.label_datos_usuario = Label(self.frame_datos_personales, text = "Bienvenido,", font = self.fuente_grande, bg = "#323050", fg ="#F2A71B")
        self.label_datos_usuario.grid(row=2, column=0)
        self.label_datos_usuario = Label(self.frame_datos_personales, text = nombre_apledio_U, font = self.fuente_mediana, bg = "#323050", fg ="#F2E7DC", pady=3)
        self.label_datos_usuario.grid(row=3, column=0)
        self.buscar_cuenta = Entry(self.frame_datos_personales, bg="#555275", fg="#F2E7DC", borderwidth=0)
        self.buscar_cuenta.grid(row=4, column=0)
        self.label_datos_usuario = Label(self.frame_datos_personales, text = "Ingresa la cuenta", font = self.fuente_pequena, bg = "#323050", fg ="#F2A71B")
        self.label_datos_usuario.grid(row=5, column=0)

        #LABEL FRAME BTN
        self.frame_btn_acction = LabelFrame(self.ventana_home, bg = "#323050", fg = "black", borderwidth=0, padx=1, pady=1)
        self.frame_btn_acction.place(x = 0, y = 200, width = 300, height = 100)

        ##LLAMAR A FUNCION PARA CREAR BOTONES
        icono_btn_buscar = ImageTk.PhotoImage(Image.open(os.path.join(self.c_img, "btn_buscar.png")).resize((50,50)))
        self.crear_btn("btn_listar_cuentas", icono_btn_buscar, self.buscar_s, 1,0)
        icono_btn_listar = ImageTk.PhotoImage(Image.open(os.path.join(self.c_img, "btn_listar.png")).resize((50,50)))
        self.crear_btn("btn_listar_cuentas", icono_btn_listar, self.listar_cuentas, 1,1)
        icono_btn_anadir = ImageTk.PhotoImage(Image.open(os.path.join(self.c_img, "btn_agregar.png")).resize((50,50)))
        self.crear_btn("btn_anadir_cuenta", icono_btn_anadir, NONE, 1,2)
        icono_btn_editar = ImageTk.PhotoImage(Image.open(os.path.join(self.c_img, "btn_editar.png")).resize((50,50)))
        self.crear_btn("btn_edita_cuenta", icono_btn_editar, self.editar_cuenta, 1,3)

        self.frame_validar_pin = LabelFrame(self.ventana_home, bg = "#323050", fg = "black", borderwidth=0)
        self.frame_validar_pin.place(x = 0, y = 280, width = 300, height = 150)
        
        self.opcione_de_perfil()

        
    def buscar_s(self):
            print(f"ID: {self.resultado[0]} - Valor imput: {self.buscar_cuenta.get()}")

            self.sql_user = """ SELECT * FROM Info_data_user WHERE ID_datos_personales = {} AND Name_red_social = "{}" 
            """.format(self.resultado[0], self.buscar_cuenta.get())
            self.cursor.execute(self.sql_user)
            self.resultado_datos = self.cursor.fetchone()

            if self.resultado_datos:

                self.numero_de_cuentas_encontadas_SQLL= """
                SELECT Name_red_social , COUNT(*) as cantidad FROM Info_data_user WHERE ID_datos_personales = {} AND Name_red_social = "{}" GROUP BY Name_red_social
                """.format(self.resultado[0], self.buscar_cuenta.get())
                self.cursor.execute(self.numero_de_cuentas_encontadas_SQLL)
                self.resultado_datos_ = self.cursor.fetchall()

                for i in self.resultado_datos_:
                    n_valores_encontrado = i[1]

                #LLamar funcion para poner la informacion del usuario

                self.label_validar_pin = Label(self.frame_validar_pin, text = "Se encontro {} Cuentas, INGRESE EL PIN".format(n_valores_encontrado), font = self.fuente_pequena, pady = 3, fg ="#012340" , bg = "#04D939")
                self.label_validar_pin.grid(row=1, column=0, pady=10, padx=50)
                
                #label de si existe un resultado se ingresa el pin de la db
                self.valida_pin_cuenta = Entry(self.frame_validar_pin, background="#555275", borderwidth=0)
                self.valida_pin_cuenta.grid(row=2, column=0, pady=10)

                icono_btn_validar_pin = ImageTk.PhotoImage(Image.open(os.path.join(self.c_img, "validarpin.png")).resize((90,30)))
                style = ttk.Style()
                style.configure("style_btn_login.TButton", foreground="#323050",borderwidth=0,background="#323050")
                btn_validar_pin=ttk.Button(self.frame_validar_pin, image=icono_btn_validar_pin, command=self.valida_pin)
                btn_validar_pin.icono_btn_validar_pin =icono_btn_validar_pin 
                btn_validar_pin.config(style="style_btn_login.TButton")
                btn_validar_pin.grid(row=3, column=0, pady=10)

            else:
                self.label_validar_pin = Label(self.frame_datos_personales, text = "NO EXISTEN RESULTADOS", font = self.fuente_mediana, pady = 0, fg ="#A52502" , bg = "#8698D9")
                self.label_validar_pin.grid(row=12, column=1)

    def valida_pin(self):
        validar_pi=self.resultado[6]
        print(f"ID: {self.resultado[0]} - CLAVE PIN: {self.valida_pin_cuenta.get()}")

        if validar_pi == int(self.valida_pin_cuenta.get()):
            self.ire_consulta = (
                 f"Usuario: {self.resultado_datos[3]}\nClave: {self.resultado_datos[4]}"
                 )
            print(f"DATOS DE LA BD : {self.ire_consulta}")
            # LLamar funcion para crear un LabelFrame
            self.impimir_n_cuentas_encontradas = "SELECT * FROM Info_data_user WHERE Name_red_social = '{}'".format(self.buscar_cuenta.get())
            self.cursor.execute(self.impimir_n_cuentas_encontradas)
            self.resultado_datos__ = self.cursor.fetchall()

            contador1 = 10
            contador2 = 10

            for W in self.resultado_datos__:
                print(W)
                self.frame_datos_busqueda_cuenta = LabelFrame(self.ventana_home, text=self.resultado_datos[2],pady = 1, bg = "#323050", fg = "#F2A71B", borderwidth=0, font=self.fuente_grande, padx=10)
                self.frame_datos_busqueda_cuenta.place(x = 320, y = contador1, width = 300, height = 75)
                #LLamar funcion para poner la informacion del usuario
                
                self.label_datos_busqueda_cuenta = Label(self.frame_datos_busqueda_cuenta, text = self.ire_consulta, font = self.fuente_mediana, pady = 0, fg ="#FFFCE7" , bg = "#323050", anchor = "e")
                self.label_datos_busqueda_cuenta.grid(row=contador2, column=0, padx=15, pady=5)
                contador1 +=80
                contador2 +=1

        else:
            self.label_message_pin = Label(self.frame_datos_personales, text = "Pin incorrecto", font = self.fuente_mediana, pady = 0, fg ="red" , bg = "#DFE7F2", anchor = "e", padx = 0)
            self.label_message_pin.grid(row=11, column=1)
            
            print("Pin incorrexto")

    def listar_cuentas(self):
        Id_user_lis = [self.resultado[0]]
        sql_user_lis = """ SELECT * FROM Info_data_user WHERE ID_datos_personales = %s"""

        self.cursor.execute(sql_user_lis, Id_user_lis)

        self.resultado_datos_lia = self.cursor.fetchall()

        self.frame_i = LabelFrame(self.ventana_home, text="Lista de cuentas", padx=1, bg="#323050", fg="#F2A71B",borderwidth=0, font=self.fuente_grande)
        self.frame_i.place(x=630, y=10, width=300, height=480)
        row_counter = 0

        for listar in self.resultado_datos_lia:
            self.label_1 = Label(self.frame_i, text=listar[2], font=self.fuente_pequena, fg="#FFFCE7", bg="#323050", justify="right")
            self.label_1.grid(row=row_counter, column=0)
            row_counter += 1

    def editar_cuenta(self):
            self.frame_E = LabelFrame(self.ventana_home, text="EDITDAR CUENTA " + self.resultado_datos[2], padx=3, bg="#323050", fg="#F2A71B", borderwidth=0)
            self.frame_E.place(x=320, y=320, width=300, height=170)

            self.label_E = Label(self.frame_E, text="Usuario o email", font=self.fuente_mediana, fg="#FFFCE7", bg="#323050")
            self.label_E.grid(row=1, column=1)

            self.editar_U = Entry(self.frame_E, bg="#555275", fg="#FFFCE7", borderwidth=0)
            self.editar_U.config(width=34)
            self.editar_U.insert(0, self.resultado_datos[3])
            self.editar_U.grid(row=2, column=1, padx=28)

            self.label_E = Label(self.frame_E, text="Contraseña", font=self.fuente_mediana, fg="#FFFCE7", bg="#323050")
            self.label_E.grid(row=3, column=1)
            
            self.editar_P = Entry(self.frame_E, bg="#555275", fg="#FFFCE7", borderwidth=0)
            self.editar_P.config(width=34)
            self.editar_P.insert(0, self.resultado_datos[4])
            self.editar_P.grid(row=4, column=1, padx=28)

            self.btn_save_editar=ttk.Button(self.frame_E, text="ACTUALIZAR", command = self.actualizar_datos)
            self.btn_save_editar.config(width=25)
            self.btn_save_editar.grid(row=5, columnspan=2, pady=8)

    def  actualizar_datos(self):
        if self.resultado_datos[3] == self.editar_U.get() and self.resultado_datos[4] == self.editar_P.get():
            self.MESSAGE_AC("LOS DATOS SON LOS MISMOS", "#F2AE30")
            print("LOS DATOS SON LOS MISMOS") 
        else:
            try:
                ID_usuario = self.resultado_datos[0]           
                sql = """
                UPDATE Info_data_user SET Usuario_red_social= '{}', Password_red_social = '{}' WHERE ID_data_user = {}
                """.format(self.editar_U.get(), self.editar_P.get(), ID_usuario)

                self.cursor.execute(sql)
                self.connection.commit()
                self.MESSAGE_AC("DATOS ACTUALIZADOS", "#93D94E")

            except mariadb.Error as e:
                self.MESSAGE_AC("UPS! DATOS NO ACTUALIZADOS", "#BD2A2E")
                print(f"UPS! DATOS NO ACTUALIZADOS\n {e}")

    def MESSAGE_AC(self, type_m, color_m):
        #Función para mostrar el tipo de erro y ademas limpiar los mesajes de los errores 
        if hasattr(self, 'label_NO_SAVE'):
            self.label_NO_SAVE.destroy()

        self.label_NO_SAVE = Label(self.frame_E, text=type_m, font=self.fuente_pequena, fg=color_m, bg="#DFE7F2")
        self.label_NO_SAVE.grid(row=7, column=1)

        self.frame_E.after(5000, self.eliminar_mensaje)

    def eliminar_mensaje(self):
        # Función para eliminar el mensaje de los errores
        if hasattr(self, 'label_NO_SAVE'):
            self.label_NO_SAVE.destroy()

    def salir(self):
        #Cerrar ventana home
        self.ventana_home.destroy()
        
    def opcione_de_perfil(self):
        self.labelFrame_opciones = LabelFrame(self.ventana_home, text=f"-_-_- {self.resultado[4]} -_-_-", bg = "#323050", fg = "#F2A71B", borderwidth=0)
        self.labelFrame_opciones.place(x = 0, y = 430, width = 300, height = 80)


        style = ttk.Style()
        style.configure("style_btn_login_.TButton", borderwidth=0, foreground="#F2E7DC", background="#323050")


        icono_btn_btn_conf_cuenta = ImageTk.PhotoImage(Image.open(os.path.join(self.c_img, "btn_configuracion.png")).resize((40,40)))
        bt_conf_cuenta = ttk.Button(self.labelFrame_opciones, image= icono_btn_btn_conf_cuenta, style="style_btn_login_.TButton")
        bt_conf_cuenta.icono_btn_btn_conf_cuenta = icono_btn_btn_conf_cuenta
        bt_conf_cuenta.grid(row=1, column=0)
  
        icono_btn_btn_salir_cuenta = ImageTk.PhotoImage(Image.open(os.path.join(self.c_img, "btn_salir_cuenta.png")).resize((40,40)))
        bt_salir_cuenta = ttk.Button(self.labelFrame_opciones, image= icono_btn_btn_salir_cuenta, style="style_btn_login_.TButton", command=self.salir)
        bt_salir_cuenta.icono_btn_btn_salir_cuenta = icono_btn_btn_salir_cuenta
        bt_salir_cuenta.grid(row=1, column=1)

        icono_btn_btn_eliminar_cuenta = ImageTk.PhotoImage(Image.open(os.path.join(self.c_img, "btn_eliminar_cuenta.png")).resize((40,40)))
        bt_eliminar_cuenta = ttk.Button(self.labelFrame_opciones, image= icono_btn_btn_eliminar_cuenta, style="style_btn_login_.TButton")
        bt_eliminar_cuenta.icono_btn_btn_eliminar_cuenta = icono_btn_btn_eliminar_cuenta
        bt_eliminar_cuenta.grid(row=1, column=2)


    def crear_btn(self, btn_vari, img, command, row, colum):
        self.command = command
        style = ttk.Style()
        style.configure("style_btn_login_.TButton", borderwidth=0, foreground="#F2E7DC", background="#323050")
        btn_vari=ttk.Button(self.frame_btn_acction, image=img, command=self.command, style="style_btn_login_.TButton")
        btn_vari.img=img
        btn_vari.grid(row=row, column=colum, padx=5, pady=5)
    