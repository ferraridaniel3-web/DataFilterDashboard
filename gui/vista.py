import customtkinter as ctk
from tkinter import filedialog,ttk
import tkinter as tk
# Importamos typing para usar características avanzadas de type hinting
from typing import TYPE_CHECKING

# Esta importación solo se usa para que las herramientas de análisis de código (VS Code/Pylance)
# sepan de qué estamos hablando. Python la ignora cuando el programa se ejecuta realmente.
if TYPE_CHECKING:
    from controller.controlador import Controller
class MainWindow(ctk.CTk):
    def __init__(self, controller:Controller): # Recibe el controlador
        self.controller = controller 
        super().__init__()
        # Lo guarda como referencia
        self.geometry("900x300")
        self.protocol("WM_DELETE_WINDOW",self.controller.on_closing_ctk)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=6)
        self.grid_rowconfigure(0,weight=1)
        self.frame_izq=ctk.CTkFrame(self,fg_color="lightgreen")
        self.frame_izq.grid(row= 0,column=0,sticky="nsew",padx=5,pady=5)
        self.frame_izq.grid_columnconfigure(0,weight=1)       
        self.frame_izq.grid_propagate(False)
        self.frame_der=ctk.CTkFrame(self,fg_color="blue")
        self.frame_der.grid(row=0,column=1,sticky="nsew",padx=3,pady=10)
        self.frame_der.grid_rowconfigure(0,weight=1)
        self.frame_der.grid_columnconfigure(0,weight=1)
        self.tree=ttk.Treeview(self.frame_der)
        self.tree.grid(row=0,column=0,sticky="nsew")
        self.letras = ttk.Style()
        self.letras.configure("Treeview.Heading", font= ("Consolas", 13,"bold"))
        self.letras.configure("Treeview", font=("Consolas",11))
        self.frame_der.grid_propagate(False)
        self.dashboard()
        
    def dashboard(self):
        self.limpiar_ventana()
        self.label_encabe= ctk.CTkLabel(self.frame_izq,text="Dashboard")
        self.label_encabe.pack()
        self.boton_cargar_archivo=ctk.CTkButton(self.frame_izq,text="Cargar archivo",command=self.cargar_archivo)
        self.boton_cargar_archivo.pack()
        self.boton_filtrar=ctk.CTkButton(self.frame_izq,text="Filtrar",command=self.controller.pantalla_filtrado)
        self.boton_filtrar.pack()
        self.boton_graficar=ctk.CTkButton(self.frame_izq,text="Graficar",command=self.menu_graficar)
        self.boton_graficar.pack()

    def limpiar_ventana(self):
        for widget in self.frame_izq.winfo_children():
            widget.destroy()

    def cargar_archivo(self):
        ruta= filedialog.askopenfilename(title="Selecciona un Archivo Excel")
        print("500000")       
        self.df, self.heads_df=self.controller.cargar_archivo(ruta)
        self.label_col={}
        self.check_y_all={}
        self.check_x_all={}
        self.chek_var_x_all={}
        self.chek_var_y_all={}

    def mostrar_data_frame(self,data_frame):
        columnas=list(self.controller.obtener_columnas())
        colum_sin_lista=self.controller.obtener_columnas()
        self.tree["columns"]=columnas
        self.tree["show"]="headings"
        for col in colum_sin_lista:
            self.tree.heading(col,text=col,command=lambda c=col: self.ordenar_columna(c))
            self.tree.column(col,anchor="center",width=50)
        print("vista")
        for valores in data_frame:
            self.tree.insert("", "end", values=valores)
        print("vista2")
        print("vista2")
        
    def ordenar_columna():
        pass
       
    def pantalla_filtrado(self,tipos_de_datos):
        self.limpiar_ventana()
        self.frame_izq.columnconfigure(0,weight=1)
        self.frame_izq.columnconfigure(1,weight=1)
        self.frame_izq.columnconfigure(2,weight=1)
        self.label_filtros=ctk.CTkLabel(self.frame_izq,text="Filtros")
        self.label_filtros.grid()
        self.label_filtros.grid_configure(column=1,row=0)
        self.i_iteracion=1
        self.boton_heads={}
        self.ent_min_heads={}
        self.ent_max_heads={}
        self.min_={}        
        self.maxi={}
        self.scroll_heads={}
        self.check_boxes_selec={}
        self.valores_unicos={}
        self.cb={}   
        self.boton_confirmar_filtros={}
        self.label_col={}
        self.i_iteracion=1
        for  col in self.heads_df: #Iteramos por cada encabezado de columna para crear los botones y entrys respectivos
            self.boton_heads[col]=ctk.CTkButton(self.frame_izq, text=col,command=lambda head=col: self.funciones_genericas(head),width=95)
            self.boton_heads[col].grid()
            self.boton_heads[col].grid_configure(row=self.i_iteracion,column=1)
                
            
            if tipos_de_datos[col] == ["Numeros"]:
                self.ent_min_heads[col]=ctk.CTkEntry(self. frame_izq,width=80)
                self.ent_min_heads[col].grid()
                self.ent_min_heads[col].grid_configure(row=self.i_iteracion,column=0)
                self.ent_max_heads[col]=ctk.CTkEntry(self.frame_izq, width=80)
                self.ent_max_heads[col].grid()
                self.ent_max_heads[col].grid_configure(row=self.i_iteracion,column=2)
            
            self.i_iteracion += 1
        self.boton_cargar_df_ori=ctk.CTkButton(self.frame_izq, text="Df Original", command=self.cargar_df_original,width=90)
        self.boton_cargar_df_ori.grid()
        self.boton_cargar_df_ori.grid_configure(column=1,row=self.i_iteracion)
        self.boton_volver_al_dashboard=ctk.CTkButton(self.frame_izq, text="Volver", command=self.volver_al_dashboard,width=90)
        self.boton_volver_al_dashboard.grid()
        self.boton_volver_al_dashboard.grid_configure(column=1,row=(self.i_iteracion+1))   

    def menu_graficar(self):
        pass
    
    def cargar_df_original(self):
        pass

    def volver_al_dashboard(self):
        self.dashboard()

    def funciones_genericas(self,head):
        tipos_de_datos=self.controller.clasificacion_datos()
       
        if tipos_de_datos[head]== ["Numeros"]:
            self.min_[head]= int(self.ent_min_heads[head].get()) 
            self.maxi[head]= int(self.ent_max_heads[head].get())    
            self.ent_min_heads[head].delete(0,ctk.END)
            self.ent_max_heads[head].delete(0,ctk.END)
            
        elif tipos_de_datos[head]==["Categorico"]:
            self.new_ventana=ctk.CTkToplevel()
            self.new_ventana.title(head)
            self.new_ventana.geometry("200X400")
            self.new_ventana.lift(self)
            self.new_ventana.transient(self)         
            self.scroll_heads[head]=ctk.CTkScrollableFrame(self.new_ventana)
            self.scroll_heads[head].grid(row=0,column=0,sticky="nsew")
            self.valores_unicos[head]=self.df[head].unique().tolist()
            print(self.valores_unicos[head])
            self.i_ite=1
            self.cb[head]=[]#Lista para almacenar los check box creados
            if head not in self.check_boxes_selec:
                self.check_boxes_selec[head]=[]#Lista para almacenar los check box seleccionados
            
            for cada_unico in self.valores_unicos[head]:#Iteramos por cada valor unico para crear un check box

                self.cb1=ctk.CTkCheckBox(self.scroll_heads[head],text=cada_unico)
                self.cb1.grid(row=self.i_ite,column=0,sticky="nsew")
                self.cb[head].append(self.cb1)
                print(self.cb1.cget("text"))
                
                self.i_ite +=1
                if cada_unico in self.check_boxes_selec[head]:  
                    self.cb1.select()

            self.boton_confirmar_filtros[head]=ctk.CTkButton(self.new_ventana,text="Filtrar",command=lambda h=head: self.confirmar_filtros(h))#Crear la funcion que capture los check box seleccionados
            self.boton_confirmar_filtros[head].grid(row=1,column=0)
            
        elif tipos_de_datos[head]==["Fecha"]:
            self.min_[head]= self.ent_min_heads[head].get()
            self.maxi[head]= self.ent_max_heads[head].get()
            self.controller.funciones_genericas_fecha(self.min_[head,self.maxi[head]])
            
        
        
    