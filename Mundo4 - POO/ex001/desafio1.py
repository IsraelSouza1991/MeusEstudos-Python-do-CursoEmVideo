class Gafanhoto:
    def __init__(self): # método construtor
        # atributos de instância
        self.nome = ""
        self.idade = 0
    
    #Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de indade"
    
# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 17
print(g1.mensagem())