class Balde:
    """Essa classse modela os objetos?"""

    def __init__(self):

        # Atributos simples
        self.marca = ""
        self.durabilidade_em_anos = 0
        self.volume = ""
        self.material = ""

    def __str__(self):
        return self.marca
    
    #comentar alt 3 descomentar alt4

#     def __repr__(self):
#         return self.marca

    # instanciamento


Castelo_1 = Balde()
Castelo_2 = Balde()

print(Castelo_1)
print(Castelo_2)
