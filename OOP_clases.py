class Libro:
    def __init__(self, title, author):
        self.title = title,
        self.author = author,
        self.prestado = False

    def prestar(self):
        if self.prestado:
            print(f"Error, {self.title} ya esta prestado")
        else:
            self.prestado = True
            print(f"{self.title} acaba de ser prestado")


    def devolver(self):
        if not self.prestado:
            print(f"Error, {self.title} no estaba prestado")
        else :
            self.prestado = False
            print(f"gracias por devolver {self.title}")



libro_1 = Libro("Cien años de soledad", "Gabriel García Márquez")
print(libro_1)
print(libro_1.author)
libro_1.prestar()
libro_1.devolver()

# ENCAPSULATION 

class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0.0         # PRIVATE/ENCAPSULATED VALUE

    def depositar(self, cantidad):  # ENCAPSULATED VALUE CAN ONLY BE MODIFIED BY THIS METHOD
        if cantidad > 0 :
            self._saldo += cantidad
            print("deposito realizado")
    
    def getter(self):           # PUBLIC METHOD
        return self._saldo
    


# INHERITANCE


class ItemBiblioteca:
    def __init__(self, title):
        self.title = title
        self.esta_prestado = False

    def prestar(self):
        self.esta_prestado = True
        print(f"El item {self.title} ha sido prestado")

    def devolver(self):
        self.esta_prestado = False
        print(f"Gracias por devolver {self.title}")

class Comic(ItemBiblioteca) : # especifico la clase padre en el parentesis
    def __init__(self, title, author): # Libro tiene todo lo k tiene ItemBiblioteca, mas lo especifico
        super().__init__(title) # Llamo al constructor del padre con super().
        self.author = author # atributo especifico del libro

class Revista(ItemBiblioteca):
    def __init__(self, title, number_of_edition):
        super().__init__(title)
        self.number_of_edition = number_of_edition



# POLYMORPHISM  (previous expample cont...)

class DVD(ItemBiblioteca):
    def __init__(self, titulo, director):
        super().__init__(titulo)
        self.director = director

    def prestar (self):
        print(f"Verificando si el DVD {self.title} tiene rayotes...")
        super().prestar() # Llamamos al método original después de nuestra lógica para indical cuál sobreescribo

items = [
    Comic("libro A", "autor A"),
    DVD("pelicula B", "director B")
]

for item in items: # puedo iterar con el mismo método prestar en todas las clases hijas aunk la logica del metodo en cada clase sea diferente.
    item.prestar()
    print("-" * 10)