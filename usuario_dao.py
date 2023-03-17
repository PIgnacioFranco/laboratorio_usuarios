from cursor_del_pool import CursorDelPool
from logger_base import log
from usuario import Usuario

class UsuarioDAO:
    _SELECCIONAR='SELECT * FROM usuario ORDER BY id_persona'
    _INSERTAR='INSERT INTO usuario(usuario, contrasenia) VALUES(%s, %s)'
    _ACTUALIZAR='UPDATE usuario SET usuario=%s, contrasenia=%s WHERE id_persona=%s'
    _ELIMINAR='DELETE FROM usuario WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Transaccion select')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuarios.append(Usuario(registro[0], registro[1],registro[2], registro[3]))
            return usuarios
            
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'insertar usuario: {usuario}')
            cursor.execute(cls._INSERTAR, (usuario.usuario, usuario.contrasenia))
            return cursor.rowcount()

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'actualizando usuario: {usuario}')
            cursor.execute(cls._ACTUALIZAR, (usuario.usuario, usuario.contrasenia, usuario.id_usuario))
            return cursor.rowcount()

    @classmethod
    def eliminar (cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'eliminando usario: {usuario}')
            cursor.execute(cls._ELIMINAR, (usuario.id_usuario,))
            return cursor.rowcount()