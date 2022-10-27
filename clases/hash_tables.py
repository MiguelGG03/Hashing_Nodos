class hashNodo(object):

    info , sig = None , None


class Hash(object):

    def __init__(self):
        self.tabla=[]
        self.tamanio=0

    def bernstein(self,cadena):
        '''Solo Funciona para cadenas de caracteres'''
        h=0
        for caracter in cadena:
            h = h *33 + ord(caracter)
        return h

    def crear_tabla(self,tamanio):
        self.tabla=[None]*tamanio
        self.tamanio=tamanio
        return self.tabla

    def __str__(self):
        return print(self.tabla)
    
    def cantidad_elementos(self):
        return self.tamanio-self.tabla.count(None)

    def funcion_hash(self,dato):
        '''Posicion del dato en la tabla'''
        return self.bernstein(str(dato))% self.tamanio
    
    def agregar(self,tabla,dato):
        '''Agrega un elemento a la tabla'''
        posicion=self.funcion_hash(dato)
        aux=hashNodo()
        aux.info=dato
        naux=aux
        if(tabla[posicion] is None):
            tabla[posicion]=naux
            print(f'{naux.info} instertado con exito a la tabla')
            self.tabla=tabla
        else:
            nodo=hashNodo()
            nodo.info=dato
            naux.sig=nodo
            print(f'{nodo.info} aderido a la cola con exito, su puntero apunta a {nodo.sig}')
            self.tabla=tabla


            
        
    







def main():
    hashing=Hash()
    n=int(input('Introduzca el tamaño de la tabla deseado: '))
    
    tabla_hash=(hashing.crear_tabla(n))
    cadena=input('Cadena: ')
    hashing.agregar(tabla_hash,cadena)
    print(tabla_hash.__str__())
    cadena2=input('Cadena: ')
    hashing.agregar(tabla_hash,cadena2)
    print(tabla_hash.__str__())


if __name__=='__main__':
    main()