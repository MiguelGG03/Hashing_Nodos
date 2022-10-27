class Hash:

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
    
    def cantidad_elementos(self):
        return self.tamanio-self.tabla.count(None)

    def hasher(self,dato):
        return self.bernstein(str(dato))% self.tamanio

    def funcion_hash(self,dato):
        '''Posicion del dato en la tabla'''
        return len(str(dato).strip()) % self.tamanio
    
    def agregar(self,tabla,dato):
        posicion=self.hasher(dato)







def main():
    hashing=Hash()
    n=int(input('Introduzca el tamaño de la tabla deseado: '))
    
    tabla_hash=(hashing.crear_tabla(n))
    cadena=input('Cadena: ')
    print(hashing.bernstein(cadena))
    print(tabla_hash)
    print(hashing.bernstein(cadena))
    


if __name__=='__main__':
    main()