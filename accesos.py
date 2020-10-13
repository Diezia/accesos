import sqlite3
conn = sqlite3.connect('project-accesos/accesos.db')
c = conn.cursor()

# Create table
# nombreTabla1 = "nombre_random1"
# c.execute("CREATE TABLE "+nombreTabla1+" (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Nombre TEXT NOT NULL, Clave TEXT NOT NULL)")

# Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
# conn.close()

# Modelo actual




class Categoria:
    def crearCategoria(self, accion):
        print("accedió a crearCategoria")
        self.crearRegistro()
    def consultarCategoria(self, accion):
        print("accedió a consultarCategoria")
        print(accion)
        self.consultarRegistro()

class Registro(Categoria):
    def consultarRegistro(self, categoria_elegida_usuario, nro_acceso_elegido_usuario):
        c.execute("SELECT Clave FROM " + categoria_elegida_usuario + " WHERE ID=?", str(nro_acceso_elegido_usuario))
        contraseña = c.fetchone()
        print(contraseña[0]) # el indicé es para que devuelva el elemento del la tupla (tipo = str) y no la tupla en si
        conn.close()
    def crearRegistro(self):
        print("accedió a crearRegistro")
    def eliminarRegistro(self):
        print("accedió a eliminarRegistro")

class MostrarEnPantalla():
    '''Muestra mensajes en pantalla'''
    OPERACIONES_REGISTRO = "Opciones de registro: \n1. consultar \n2. crear \n3. eliminar \n"
    crea_un_servicio = "Crea un sevicio: \n"
    crea_un_acceso = "Crea un acceso: \n"
    elige_un_acceso = "Elige un acceso: \n"
    def definirMensajeEligeUnServicio(self):
        '''crea el mensaje elige_un_sevicio según los datos que tiene la base de datos'''
        elige_un_sevicio = "Elige un sevicio: \n"
        res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        arreglo_nombres_base = []
        for name in res:
            arreglo_nombres_base.append(name[0])
        i = 0
        # print(arreglo_nombres_base)
        while i < len(arreglo_nombres_base) - 1:
            nro_servicio = str(i + 1)
            elige_un_sevicio += nro_servicio + ". " + arreglo_nombres_base[i] + "\n"
            i += 1
        nro_categoria_elegida_usuario = int(input(elige_un_sevicio)) #la nro_categoria_elegida_usuario corresponde al número de servicio, categoría, tabla elegida por el usuario. Si quiero el nombre de la misma, solo tengo que pedirle al array arreglo_nombres_base el número nro_categoria_elegida_usuario + 1
        categoria_elegida_usuario = arreglo_nombres_base[nro_categoria_elegida_usuario - 1]
        return categoria_elegida_usuario
    def definirMensajeEligeOCreaUnServicio(self):
        elige_o_crea_un_sevicio = "Elige o crea un sevicio: \n0. Crea un servicio \n"
        res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        arreglo_nombres_base = []
        for name in res:
            arreglo_nombres_base.append(name[0])
        i = 0
        print(arreglo_nombres_base)
        while i < len(arreglo_nombres_base)-1:
            nro_servicio = str(i + 1)
            elige_o_crea_un_sevicio += nro_servicio + ". " + arreglo_nombres_base[i] + "\n"
            i += 1
        nro_categoria_elegida_usuario = int(input(elige_o_crea_un_sevicio))
        self.nro_categoria_elegida_usuario = nro_categoria_elegida_usuario
        self.categoria_elegida_usuario = arreglo_nombres_base[nro_categoria_elegida_usuario - 1]
        return nro_categoria_elegida_usuario
    def definirMensajeEligeUnAcceso(self, categoria_elegida_usuario):
        '''Muestra los accesos de una tabla determinada'''
        # opciones: -crea un listado de accesos correspondiente a la tabla que se eligió actualmente
        # por ahora solo se está guardando la nro_categoria_elegida_usuario. Ver que categoría corresponde a nro_categoria_elegida_usuario en arreglo_nombres_base y trabajar con eso para traer los registros correspondientes a la tabla actual
        nombre_id_tabla_actual = []
        for row in c.execute("select ID, Nombre from " + categoria_elegida_usuario):
            nombre_id_tabla_actual.append( str(row[0]) + '. ' +  str(row[1]))
        elige_un_acceso = self.elige_un_acceso
        for elemento in nombre_id_tabla_actual:
            elige_un_acceso += elemento + "\n" # elige_un_acceso es el mensaje que se muestra en pantalla
        nro_acceso_elegido_usuario = int(input(elige_un_acceso))
        return nro_acceso_elegido_usuario
    def valorDeEtapa1(self):
        pass

class Selectores(Registro, MostrarEnPantalla):
    '''Direcciona el flujo del programa según sea la elección del usuario'''
    def seleccionMetodo(self, accion):
        if accion == 1:
            categoria_elegida_usuario = self.definirMensajeEligeUnServicio()
            nro_acceso_elegido_usuario = self.definirMensajeEligeUnAcceso(categoria_elegida_usuario)
            self.consultarRegistro(categoria_elegida_usuario, nro_acceso_elegido_usuario)
        elif accion == 2:
            nro_categoria_elegida_usuario = self.definirMensajeEligeOCreaUnServicio()
            self.seleccionMetodoCategoria(nro_categoria_elegida_usuario)
            self.crearRegistro()
        elif accion == 3:
            self.eliminarRegistro()
            self.nro_categoria_elegida_usuario = self.definirMensajeEligeUnServicio()
            print("esta es la accion nro " + str(self.nro_categoria_elegida_usuario))
    def seleccionMetodoCategoria(self, nro_categoria_elegida_usuario): # problema: no puedo usar muchos if según sea el caso porque nose de antemano cuantas tablas hay. PS:podría almacenar los nombres de las tablas en un array y con un indice de posición e ir mostrándolos con el indice de posición de array +1. Se resolvería en definirMensajeEligeUnServicio
        if nro_categoria_elegida_usuario == 0:
            self.crearCategoria()
        else:
            categoria_elegida_usuario = self.categoria_elegida_usuario
    def seleccionMensaje(self, mensaje):
        pass



class Validaciones():
    pass

mostrarenpantalla = MostrarEnPantalla()
accion = int(input(mostrarenpantalla.OPERACIONES_REGISTRO)) #imprime en pantalla un mensaje y asigna a "accion" el numero para el siguiente paso
selectores = Selectores()
registro = Registro()
selectores.seleccionMetodo(accion)

""" nro_categoria_elegida_usuario = int(input(self.elige_un_sevicio))
self.seleccionMetodo2(nro_categoria_elegida_usuario) """

""" mostrarenpantalla.definirMensajeEligeUnServicio()
mostrarenpantalla.definirMensajeEligeOCreaUnServicio() """

