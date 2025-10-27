# Apresentação do códido do desafio 001-Item-Mais-Popular

## Declaração dos inputs do desafio
```
vendasNum = [482, 391, 482, 102, 482, 391, 555, 102, 482]
vendasNomes = ["Eletrônicos", "Casa", "Roupas", "Eletrônicos", "Livros", "Eletrônicos", "Roupas"]
vendasNone =[]
vendasRep = [1001, 2002, 1001, 4004, 2002]
```

## Declaração da função e passando o parametro para que atenda todos os inputs
```
def item_mais_popular(vendas):
```

## Declaração de variaveis para controle local
```
contador = {} -> Dicionario criado para alocal os elementos, que se tornarão chaves, e o valor será a quantidade de aparições
max_apareceu = 0 -> Varivel que irá verificar qual(is) elemento(s) mais se repetiu(rão) 
lista_mais_apareceu = [] -> Caso ocorra de mais de um elemento ter o max valor de aparições, será adicionado na lista, para amostragem dos elementos
```

## Verificação da lista nula
```
if not vendas:
  return print("Lista vazia")   
```

## Looping que irá fazer a iteração da lista, e alocar os elementos(Chave) e a quantidade que repetiram (Valor)
```
for item in vendas: -> item é a variavel de iteração e vendas a lista que será pecorrida
  if item in contador: -> Verifica se o item da lista (Chave) já existe no dicionario
      contador[item] += 1 -> Se caso exista, ele pega a chave Ex: contador[482] e adiciona ao seu valor, caso ele tenha aparecido 1 vez, adiciona mais um e fica 482: 2
  else: -> Caso o item não tenha no dicionario
      contador[item] = 1 -> Ele adiciona o item no dicionario e coloca como valor a sua primeira aparição contador[525], ficando da seguinte forma 525: 1
```

## Verificação da ocorrência de mais de um elemento com o maximo valor
```
max_apareceu = max(contador.values())

    for chave, valor in contador.items():
        if  valor == max_apareceu:
            lista_mais_apareceu.append(chave)
            
    if len(lista_mais_apareceu) > 1:
        return print(f"Os itens que mais apareceram foram: {lista_mais_apareceu}")
    else:
        mais_apareceu = max(contador, key=contador.get)
        return print(f"O item que mais apareceu foi: {mais_apareceu}")
```

## Chamadas do metodo e passagem dos inputs do desafio como parametros
```
if __name__ == "__main__":
    item_mais_popular(vendasNum)
    item_mais_popular(vendasNomes)
    item_mais_popular(vendasNone)
    item_mais_popular(vendasRep)
```
