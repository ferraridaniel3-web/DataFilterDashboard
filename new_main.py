from controller.controlador import Controller 

if __name__ == "__main__":
    # 1. Crear el objeto controlador
    app_controller = Controller()
    
    # 2. Iniciar la aplicación
    # El controlador ya tiene referencias al modelo y la vista, y los gestiona.
    app_controller.run()