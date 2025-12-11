import pandas as pd

class DataModel:
    def __init__(self): 
        # ... inicialización simple sin pasar 'controller' ...
        
        pass

    def cargar_archivos(self,ruta):
        self.df = pd.read_excel(ruta, parse_dates=True)
        self.df_actual=self.df.copy()
        self.heads_df=self.df_actual.columns.tolist()#Lista con los encabezados de cada columna
        self.df_filtrado=self.df_actual
        print("modelo")
        print(self.df)
        return self.df,self.heads_df
    
    def obtener_columnas(self):
        columnas_frame= self.df_actual.columns
        return columnas_frame
    
    def mostrar_data_frame(self):
        #verificar si puedo hacerla una funcion que pueda repetir
        data_frame = []
        for _, fila in self.df_actual.iterrows():
            valores = []
            for col in self.heads_df:
                if pd.api.types.is_datetime64_any_dtype(self.df_actual[col]):
                    # Formatea la fecha aquí en el modelo
                    valores.append(fila[col].strftime("%Y-%m-%d"))
                else:
                    valores.append(fila[col])
            data_frame.append(valores)
        return data_frame
    
    def clasificacion_por_datos(self):
        tipo_de_datos={}
        for col in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[col]) or pd.api.types.is_datetime64_any_dtype(self.df[col]):
                tipo_de_datos[col]= ["Numeros"]
            elif pd.api.types.is_object_dtype(self.df[col]):
                tipo_de_datos[col]= ["Categorico"]
            elif pd.api.types.is_datetime64_any_dtype(self.df[col]):
                tipo_de_datos[col]=["Fecha"]
                self.min_[col]= pd.to_datetime(self.ent_min_heads[col].get()) 
                self.maxi[col]= pd.to_datetime(self.ent_max_heads[col].get()) 
                pd.to_datetime(self.min_[col], errors='raise')
                pd.to_datetime(self.maxi[col], errors='raise')

        return tipo_de_datos
    
    def funciones_genericas_fecha(self,min,max):
        pd.to_datetime(min) 
        pd.to_datetime(max)
        pd.to_datetime(min, errors='raise')
        pd.to_datetime(max, errors='raise')
        #no se si tengo que devolver los valores min y max    
        