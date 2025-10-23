# Projeto GruPy-Code-Challenges

Bem-vindo ao repositório de desafios do nosso grupo de Python! O objetivo deste projeto é simples: **elevar nosso nível técnico** através da prática consistente, simulando os desafios de lógica, algoritmos e arquitetura que encontramos em entrevistas técnicas e no dia a dia.

## 🎯 O Objetivo

Todos sabemos que o mercado de tecnologia exige mais do que apenas conhecer a sintaxe de uma linguagem. Ele exige a habilidade de resolver problemas complexos. Este repositório é nosso campo de treino.

A ideia surgiu da percepção de que esses desafios são muito comuns em entrevistas técnicas, e o objetivo é que o grupo todo possa se preparar melhor para essas situações.

## 📚 Como Funciona?

Periodicamente, um novo desafio será postado neste repositório, dentro da pasta `desafios/`. Cada desafio terá seu próprio `README.md` explicando o problema, os requisitos e os exemplos de entrada e saída.

Os temas serão variados, incluindo:

* 🧠 **Lógica e Algoritmos:** Problemas clássicos (LeetCode, HackerRank, etc.)
* 🌐 **APIs e Web:** Consumo de APIs públicas, manipulação de JSON e criação de *endpoints*.
* 🗄️ **Banco de Dados:** Scripts que interagem com um banco (leitura, escrita, atualização).

---
## 🧠 Nossa Filosofia: A "Luta" é o Aprendizado

O objetivo principal deste repositório é que **você** fortaleça seu raciocínio lógico. Ferramentas de IA (como ChatGPT, Gemini, Copilot) são incríveis para acelerar o trabalho no dia a dia, mas são péssimas para *aprender* a resolver problemas do zero.

**Nós encorajamos fortemente que você evite usar IAs para obter a resposta direta.**

Tente primeiro por conta própria. Fique "preso" no problema. É nesse momento de frustração e esforço que o cérebro cria as conexões mais fortes.

* Não sabe como começar? **Tente a solução "lenta" ou "óbvia" primeiro.**
* Não sabe uma sintaxe específica? **Consulte a documentação oficial do Python.**
* Recebeu um erro que não entende? **Pesquise em fóruns como o Stack Overflow.**

Use este espaço para praticar a habilidade de *resolver problemas*, não apenas a de copiar e colar. A explicação em vídeo ou texto que você fará depois será muito mais valiosa!

> !Caso use IA, tente escrever o código que ela passou, e compreenda o seu raciocinio 

---
## 🚀 Como Participar e Enviar Sua Resolução

O fluxo de trabalho é baseado no modelo de **Fork e Pull Request (PR)**. Isso nos ajuda a praticar o Git e a manter o repositório organizado.

**Passo 1: Faça o Fork**
* Clique no botão "Fork" no canto superior direito desta página. Isso criará uma cópia do repositório na sua conta do GitHub.

**Passo 2: Clone o Seu Fork**
* Em sua máquina local, clone o *seu* fork (não o repositório original):
    ```bash
    git clone [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)
    cd NOME-DO-REPO
    ```

**Passo 3: Crie uma Branch para o Desafio**
* Sempre crie uma nova *branch* para cada desafio que for resolver.
    ```bash
    git checkout -b solucao-desafio-001-seu-nome
    ```

**Passo 4: Resolva o Desafio**
* Adicione sua solução dentro da pasta correspondente.
* **Estrutura de Pastas:** Para evitar conflitos, crie uma pasta com seu nome de usuário dentro da pasta `resolucao` do desafio específico.
    ```
    desafios/
    └── 001-Panda-Comendo-Bambu/
        ├── README.md           (O enunciado do problema)
        └── resolucoes/
            ├── seu-username-py/
            │   ├── solucao.py
            │   └── README.md       <-- (A SUA EXPLICAÇÃO VEM AQUI)
                └── solucao.js      <-- (Caso tenha feito uma solução em outra linguagem)
    ```

**Passo 5: Faça o Commit e Envie (Push)**
* Adicione seus arquivos e faça o commit da sua solução.
    ```bash
    git add .
    git commit -m "Resolve desafio 001 (Panda) com Python"
    git push origin solucao-desafio-001-seu-nome
    ```

**Passo 6: Abra um Pull Request (PR)**
* Volte para a página do seu fork no GitHub.
* Clique no botão "Compare & pull request".
* Escreva uma breve descrição da sua solução.
* Clique em "Create pull request".

---

## ⭐️ O Passo Extra: Explique Sua Solução!

A parte mais importante do aprendizado é **ensinar**.

1.  **Gravar um Vídeo Curto:** Faça um *loom* ou grave sua tela explicando sua linha de raciocínio. Não precisa ser perfeito! Fale sobre:
    * Como você entendeu o problema.
    * A solução que você pensou.
    * Como você chegou na solução final.
    * Quais dificuldades encontrou.
2.  **Cole o link do vídeo** no seu readme.

Se não quiser gravar um vídeo, escreva um pequeno texto explicando seu raciocpínio. O objetivo é compartilhar o conhecimento e solidificar o seu!

Vamos codar! 🚀
