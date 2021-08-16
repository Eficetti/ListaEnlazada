class Nodo():

    #Se crea el objeto NODO#

    def __init__(self,info = None,siguiente=None):
        self.siguiente = siguiente
        self.informacion = info

    def __str__(self):
        return str(self.informacion)
    
    def setNext(self,next):
        self.siguiente = next

class lista():

    #Se crea el objeto de LISTA#
    def __init__(self):
        self.cabeza = None
        self.size = 0
    
    #Metodo para agregar elementos a la lista#
    def add(self, info):
        node = Nodo(info)
        act = self.cabeza
        ant = None
        stop = False
        while act != None and not stop:
            if act.informacion > info:
                stop = True
            else:
                ant = act
                act = act.siguiente
        if ant == None:
            node.setNext(self.cabeza)
            self.cabeza = node
        else:
            node.setNext(act)
            ant.setNext(node)
        self.size += 1
        return node

    #Metodo para borrar un elemento en la lista #
    def delete(self,key):
        if self.size == 0:
            raise IndexError('Index out of range')
        else:
            act = self.cabeza
            ant = None
            find = False
            while not find:
                if act.informacion != key:
                    ant = act
                    act = act.siguiente
                    if act.siguiente == None:
                        return print(f'El elemento {key} no existe')
                else:
                    find = True
                    print(f'El elemento {key} se ha borrado con exito!')
            if ant == None:
                self.cabeza = act.siguiente
            else:
                ant.setNext(act.siguiente)
        self.size -= 1


    #Metodo para verificar si la lista esta vacia#
    def vacia(self):
        return self.cabeza == None
    
    #Metodo para usar un buscador#
    def buscar(self,info):
        search = self.cabeza
        find = False
        while search != None and not find:
            if search.informacion == info:
                find = True
            else:
                search = search.siguiente
        if find == True:
            print(f'El nombre {info} se ha encontrado en la lista!')
        else:
            print(f'El nombre {info} no se ha encontrado en la lista!')

    #Metodo para imprimir los nombres#
    def printeo(self):
        string = '['
        node = self.cabeza
        while node != None:
            string += str(node)
            string += str(', ')
            node = node.siguiente
        string += ']'
        return string

if __name__ == 'main':
    s = lista()

    #Entrada de datos del usuario#
    while True:
        entrada = input('Ingrese un nombre o 0 para detener el programa: ')
        if entrada == '0':
            break
        s.add(entrada)

    if s.vacia():
        print('la lista esta vacia!')
    else:
        print('la lista contiene nodos!')
        s.buscar('esteban')
        s.delete('gabriel')
        print(s.cabeza)
        print(s.printeo())

    # INPUTS USADOS EN EL TESTEO #

    #ESTEBAN
    #ANA
    #GABRIEL
    #ABRIL
    #NICOLAS
