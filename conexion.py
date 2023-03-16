from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _BASEDEDATOS = 'tes-bd'
    _USUARIO = 'posgres'
    _CONTRASENA = '1234'
    _HOST = '127.0.0.1'
    _PUERTO = '3456'
    _MIN = 1
    _MAX = 5
    _conexion = None
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN, cls._MAX,
                    database=cls._BASEDEDATOS,
                    username=cls._USUARIO,
                    password=cls._CONTRASENA,
                    host=cls._HOST,
                    port=cls._PUERTO
                )
                log.debug(f'Se obtuvo el pool: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Error al obtener pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        try:
            cls._conexion = cls.obtenerPool().getconn()
            log.debug(f'Se obtuvo conexion: {cls._conexion}')
            return cls._conexion
        except Exception as e:
            log.error(f'Error al obtener conexion: {e}')
            sys.exit()

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putpool(conexion)
        log.debug(f'Libero conexion al pool: {conexion}')

    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
        log.debug('Se cerro las conexiones')