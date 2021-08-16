class Node():
    #Creacion del objeto Nodo
    def __init__(self, data = None):
        self.anterior = None
        self.siguiente = None
        self.data = data
    
    def __str__(self):
        return str(self.data)

class List():
    #Creacion del objeto Lista TAD
    def __init__(self):
        self.root = None

    #Funcion para añadir y ordenar a la vez un nombre en forma alfabetica
    def add(self,dato):
        nodo = Node(dato)
        if self.root is None:
            self.root = nodo
        elif self.root.data > nodo.data:
            nodo.siguiente = self.root
            self.root.anterior = nodo
            self.root = nodo
        else:
            prev = self.root
            act = self.root.siguiente
            while act is not None:
                if act.data > nodo.data:
                    prev.siguiente = nodo
                    nodo.anterior = prev
                    nodo.siguiente = act
                    act.anterior = nodo
                    return nodo
                prev = act
                act = act.siguiente
            prev.siguiente = nodo
            nodo.anterior = prev
            return nodo

    #Funcion para buscar un elemento en la lista
    def search(self,item):
        aux = self.root
        while aux is not None:
            if aux.data == item:
                return print(f'El elemento {item} se encontro en la lista')
            else:
                aux = aux.siguiente
        return print(f'El elemento {item} NO se encontro en la lista')

    #Funcion para eliminar un elemento de la lista
    def delete(self, item):
        if self.root.data == item:
            self.root = self.root.siguiente
        else:
            prev = self.root
            act = prev.siguiente
            while act is not None:
                if act.data == item:
                    if act.siguiente is None:
                        prev.siguiente = None
                    else:
                        prev.siguiente = act.siguiente
                        act.siguiente = prev.anterior
                    return print(f'El elemento {item} se borro de la lista exitosamente')
                prev = act
                act = act.siguiente
            return print(f'El elemento {item} NO se encontro en la lista, imposible de borrar algo inexistente! ')

    #Funcion para recorrer la lista y crear un OUTPUT
    def recorrido(self):
        string = '['
        aux = self.root
        while aux != None:
            string += str(aux)
            string += str(', ')
            aux = aux.siguiente
        string += ']'
        return string

if __name__ == 'main':
    l = List()
    while True:
        entrada = input('Ingrese un nombre o 0 para detener el programa: ')
        if entrada == '0':
            break
        l.add(entrada)

    if l.clean():
        print('La lista NO contiene elementos!')
    else:
        print('La lista contiene nodos!')
        print('### Lista antes de borrar un dato ### ')
        print(l.recorrido())
        l.search('esteban')
        l.delete('gabriel')
        print('### Lista despues de borrar un dato ### ')
        print(l.recorrido())
