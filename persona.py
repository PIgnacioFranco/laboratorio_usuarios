class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, clave=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._clave = clave

    def __str__(self):
        return f'Id: {self._id_persona} Nombre: {self._nombre} Apellido: {self._apellido} clave: {self._clave}'

    @property
    def id_persona(self):
        return self._id_persona

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def clave(self):
        return self._clave

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
        
    @clave.setter
    def clave(self, clave):
        self._clave = clave