import random

class Moeda:
    def __init__(self, falsa=False):
        self.peso = 1 if not falsa else 0.98
        self.verdadeira = not falsa

class MoedaBag(list):
    def append(self, object):
        if object.__class__.__name__ == 'Moeda':
            super().append(object)

    def contains_falsa(self):
        r = [moeda for moeda in self if not moeda.verdadeira]
        return len(r) >= 1
    
    @property
    def peso(self):
        return sum([moeda.peso for moeda in self])
    

def n_moedas(moedabag, step=0):
    n = len(moedabag)
    steps = step+1
   
    if n%2:
        extra = moedabag.pop()

    left = MoedaBag(moedabag[:int(len(moedabag)/2)])
    right = MoedaBag(moedabag[int(len(moedabag)/2):])

    if left.peso == right.peso:
        return extra, steps
    elif left.peso > right.peso:
        return n_moedas(right, steps)
    else:
        return n_moedas(left, steps)
    
def test_n_moedas(n, quantidades_lista):
    results = []
    
    for q in quantidades_lista:
        for i in range(n):
            bools = [True]
            for _ in range(1, q):
                bools.append(False)
            random.shuffle(bools)
            bag = MoedaBag()
            print(f'#{i}:')
            print(bools)
            for boole in bools:
                bag.append(Moeda(boole))
            moeda, passos = n_moedas(bag)
            results.append(moeda.verdadeira)
    return results

def create_n_bools(n):
    result = []
    for _ in range(n):
        result.append(False)
    return result

def max_steps(quantidade):
    pos_max_step = 0
    pos_min_step = 0
    min_steps = 999999999999999999
    max_steps = 0
    sucessos = []
    
    for i in range(quantidade):
        n_bools = create_n_bools(quantidade)
        n_bools[i] = True
        bag = MoedaBag()
        for bool in n_bools:
            bag.append(Moeda(bool))
        moeda, steps = n_moedas(bag)
        if min_steps > steps:
            min_steps = steps
            pos_min_step = i
        if max_steps < steps:
            max_steps = steps
            pos_max_step = i
        sucessos.append(moeda.verdadeira)
    if sum(sucessos) == 0:
        print('Algoritmo funcionou para todas as posições')
        print('='*10)
        print("""RESULTADOS

        numero máximo de passos: {}, posição da moeda falsa #{}.
        Numero mínimo de passos: {}, posição da moeda falsa #{}
        """.format(max_steps, pos_max_step, min_steps, pos_min_step))
    






            
            


