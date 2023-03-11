import logger as log

log.basicConfig(
    level=log.DEBUG,  # Mayor nivel de log
    format=
    '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s %(message)s]',  # define el tiempo, nivel, archivo, linea y mensaje de logg
    datefmt='%d-%m-%Y %I:%M:%S %p',  # Define la feche y hora
    handlers=[
        log.FileHandler(
            'capa_datos.log'
        ),  # Crear el archivo de log con los mensajes de logging
        log.StreamHandler()
    ])
