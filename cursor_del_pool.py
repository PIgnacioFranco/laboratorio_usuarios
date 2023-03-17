from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._cursor = None
        self._conexion = None

    def __enter__(self):
        log.debug('Ingreso al enter del context manager')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipoExc, valorExc, detalleExc):
        log.debug('Ingreso al exit del context manager')
        if valorExc:
            self._conexion.rollback()
            log.error(f'Error transaccion, rollback: {valorExc} {tipoExc} {detalleExc}')
        else:
            self._conexion.commit()
            log.debug('Se realizo commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)