# Desafio 001 Item Mais Popular

Bem-vindo ao primeiro desafio do **GruPy-Code-Challenges**!

## 📝 O Problema

Você foi contratado como desenvolvedor(a) júnior em uma grande plataforma de e-commerce. Sua primeira tarefa é ajudar o time de marketing a identificar qual produto está fazendo mais sucesso.

O time de infraestrutura forneceu um log de todas as transações bem-sucedidas do dia, representado como uma longa lista (array) onde cada item é o ID do produto vendido.

Sua tarefa é escrever uma função que receba esta lista de IDs e retorne o **ID do produto que aparece com mais frequência** (ou seja, o produto mais vendido).

### Regras:

1.  A lista pode conter números (IDs de produtos) ou strings (ex: nomes de categorias).
2.  Se a lista de entrada estiver vazia, sua função deve retornar `None`.
3.  Se houver um **empate** (dois ou mais produtos com a mesma contagem máxima de vendas), sua função pode retornar os dois produtos empatados.

---

## 📋 Formato da Função Solução

Sua função deve ser implementada para receber o argumento e retornar o valor como descrito abaixo.

**Formato de Entrada (Parametros da Função)**

* **Nome da Função** `verifica_logs`
* **Nome do Parametro:** `vendas`
* **Tipo do Argumento:** Uma lista de inteiros ou strings.
* **Descrição:** Uma lista representando cada venda individual (ex: `[101, 102, 101]`).

**Formato de Saída (Valor de Retorno)**

* **Tipo do Retorno:** Um inteiro, string, ou `None`.
* **O que Retornar:** O item que mais se repete na lista de entrada. Se a lista for vazia, retorne `None`.

---

## 🚀 Desafios

### Desafio 1: IDs de Produto

O time fornece um log de IDs de produtos vendidos.

* **Entrada:** `vendas = [482, 391, 482, 102, 482, 391, 555, 102, 482]`
* **Saída:** `O valor que mais se repete é: 482`
* **Explicação:** O ID `482` aparece 4 vezes, `391` aparece 2 vezes, `102` aparece 2 vezes e `555` aparece 1 vez. O mais frequente é o `482`.

### Desafio 2: Categorias de Produto

O time de marketing quer saber a categoria de produto mais popular da última campanha.

* **Entrada:** `vendas = ["Eletrônicos", "Casa", "Roupas", "Eletrônicos", "Livros", "Eletrônicos", "Roupas"]`
* **Saída:** `O nome que mais se repete é Eletrônicos`
* **Explicação:** "Eletrônicos" aparece 3 vezes, "Roupas" aparece 2 vezes, e as demais categorias aparecem 1 vez.

### Desafio 3: O Caso de Empate

No fim do dia, dois produtos tiveram exatamente o mesmo número de vendas.

* **Entrada:** `vendas = [1001, 2002, 1001, 4004, 2002]`
* **Saída:** `Os valores que mais se repetiram foram 1001` (ou `2002`)
* **Explicação:** O produto `1001` aparece 2 vezes e o `2002` também aparece 2 vezes. Ambos são a contagem máxima. Retornar `1001` ou `2002` está correto.

### Desafio 4: O Caso de Lista Vazia

Houve uma falha no sistema e o log de vendas veio vazio.

* **Entrada:** `vendas = []`
* **Saída:** `None`
* **Explicação:** A lista está vazia, então não há produto mais vendido.

---

### Explicação final
O objetivo é que seu código execute todos os exemplos, se caso vier string, faça o exemplo de string, se vier int ou vazio a mesma coisa

### Boa sorte!

Não se esqueça de criar sua pasta em `resolucoes/` e adicionar seu `README.md` explicando como você pensou para resolver o problema!
