class Pilha:
    def __init__(self):
        self.TamMax = 50
        self.itens = [None] * (self.TamMax + 1)
        self.topo: int = -1

    def inicializa_pilha(self):
        self.topo = -1
        
    def pilha_vazia(self) -> bool:
        return self.topo == -1
    
    def pilha_cheia(self) -> bool:
        return self.topo == self.TamMax
    
    def empilha(self, item) -> None:
        if not self.pilha_cheia():
            self.topo = self.topo + 1
            self.itens[self.topo] = item
        
    def desempilha(self):
        if not self.pilha_vazia():
            item = self.itens[self.topo]
            self.topo = self.topo - 1
            return item
        else:
            raise Exception("Pilha Vazia")
        
    def elemento_do_topo(self):
        if not self.pilha_vazia():
            return self.itens[self.topo]
        else:
            raise Exception("Pilha Vazia")
        