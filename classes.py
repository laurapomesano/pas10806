class Carro:
    def __init__(self, marca, modelo, kms):
        self.marca = marca
        self.modelo = modelo
        self.kms = kms

    def __str__(self):
        return f"{self.marca} {self.modelo} com {self.kms} kms"

class livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.ano}"
