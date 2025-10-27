vendasNum = [482, 391, 482, 102, 482, 391, 555, 102, 482]
vendasNomes = ["Eletrônicos", "Casa", "Roupas", "Eletrônicos", "Livros", "Eletrônicos", "Roupas"]
vendasNone =[]
vendasRep = [1001, 2002, 1001, 4004, 2002]


def item_mais_popular(vendas):
    
    contador = {}
    max_apareceu = 0
    lista_mais_apareceu = []

    if not vendas:
        return print("Lista vazia")   

    for item in vendas:
        if item in contador:
            contador[item] += 1
        else:
            contador[item] = 1

    max_apareceu = max(contador.values())

    for chave, valor in contador.items():
        if  valor == max_apareceu:
            lista_mais_apareceu.append(chave)
            
    if len(lista_mais_apareceu) > 1:
        return print(f"Os itens que mais apareceram foram: {lista_mais_apareceu}")
    else:
        mais_apareceu = max(contador, key=contador.get)
        return print(f"O item que mais apareceu foi: {mais_apareceu}")
    
   

if __name__ == "__main__":
    item_mais_popular(vendasNum)
    item_mais_popular(vendasNomes)
    item_mais_popular(vendasNone)
    item_mais_popular(vendasRep)
