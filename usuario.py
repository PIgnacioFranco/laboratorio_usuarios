class Usuario:
    _id_usuario = None
    _usuario = None
    _contrasenia = None

    def __str__(self):
        return f'''
        id: {self._id_usuario}
        usuario: {self._usuario} contraseña: {self._contrasenia}
        '''
    
    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def contrasenia(self):
        return self._contrasenia

    @contrasenia.setter
    def contrasenia(self, contrasenia):
        self._contrasenia = contrasenia