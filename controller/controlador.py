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
        self.model.cargar_archivos(ruta)
        self.mostrar_data_frame()
    def obtener_columnas(self):
        columnas=self.model.obtener_columnas() 
        return columnas
    def mostrar_data_frame(self):
        print("model")
        matriz_filas= self.model.mostrar_data_frame()
        self.view.mostrar_data_frame(matriz_filas)
