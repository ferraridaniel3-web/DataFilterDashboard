from modelos.modelo import DataModel
from gui.vista import MainWindow
class Controller:
    def __init__(self):
        self.model = DataModel() # Crea el modelo
        self.view = MainWindow(self) # Crea la vista, pasándose a sí mismo como controlador

    def run(self): # Método para iniciar el bucle principal
        self.view.mainloop()

    def on_closing_ctk(self):
        #plt.close('all') 
        self.view.quit()
        self.view.destroy()

    def cargar_archivo(self,ruta):
        print("10")
        self.df, self.heads_df=self.model.cargar_archivos(ruta)
        data_frame= self.model.mostrar_data_frame()
        self.view.mostrar_data_frame(data_frame)
        return self.df, self.heads_df
    def pantalla_filtrado(self):
        tipos_de_datos=self.model.clasificacion_por_datos()
        self.view.pantalla_filtrado(tipos_de_datos)
        print(tipos_de_datos)
    def obtener_columnas(self):
        columnas=self.model.obtener_columnas() 
        return columnas
    def mostrar_data_frame(self):
        print("model")
        data_frame= self.model.mostrar_data_frame()
        self.view.mostrar_data_frame(data_frame)
    def funciones_genericas_fecha(self,mi,ma):
        min,max=self.model.funciones_genericas_fecha(self,mi,ma)
        return min,max
    def clasificacion_datos(self):
        tipo_de_datos=self.model.clasificacion_por_datos()
        return tipo_de_datos