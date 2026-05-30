# Paginação em Terminal

Paginar os 100 resultados é uma ótima evolução do projeto, porque evita despejar tudo na tela de uma vez. A ideia é simples: em vez de imprimir os 100 alunos, você guarda todos em uma **lista** e mostra apenas uma “fatia” por vez.

Exemplo: 100 alunos, 10 por página.

```python
pagina_atual = 1
itens_por_pagina = 10

inicio = (pagina_atual - 1) * itens_por_pagina
fim = inicio + itens_por_pagina
```

Na página 1:

```python
inicio = 0
fim = 10
```

Na página 2:

```python
inicio = 10
fim = 20
```

Ou seja, a página é só um recorte da lista:

```python
alunos[inicio:fim]
```

## Função simples para paginar resultados

```python
def exibir_pagina(alunos, pagina_atual, itens_por_pagina):
    total_alunos = len(alunos)
    total_paginas = (total_alunos + itens_por_pagina - 1) // itens_por_pagina

    inicio = (pagina_atual - 1) * itens_por_pagina
    fim = inicio + itens_por_pagina

    alunos_da_pagina = alunos[inicio:fim]

    print("=" * 70)
    print(f"RELATÓRIO DE ALUNOS — Página {pagina_atual} de {total_paginas}")
    print("=" * 70)

    for indice, aluno in enumerate(alunos_da_pagina, start=inicio + 1):
        print(f"{indice:03d} | {aluno['nome']} | MM: {aluno['mm']:.1f} | "
              f"MG: {aluno['mg']:.1f} | Status: {aluno['status']}")

    print("=" * 70)
```

## Navegação entre páginas no terminal

Aqui entra o loop para o usuário avançar, voltar ou sair.

```python
def paginar_resultados(alunos, itens_por_pagina=10):
    if not alunos:
        print("Nenhum aluno cadastrado para exibir.")
        return

    total_paginas = (len(alunos) + itens_por_pagina - 1) // itens_por_pagina
    pagina_atual = 1

    while True:
        exibir_pagina(alunos, pagina_atual, itens_por_pagina)

        print("[N] Próxima página")
        print("[A] Página anterior")
        print("[I] Ir para uma página")
        print("[S] Sair da paginação")

        opcao = input("Escolha uma opção: ").strip().upper()

        if opcao == "N":
            if pagina_atual < total_paginas:
                pagina_atual += 1
            else:
                print("Você já está na última página.")

        elif opcao == "A":
            if pagina_atual > 1:
                pagina_atual -= 1
            else:
                print("Você já está na primeira página.")

        elif opcao == "I":
            try:
                pagina_escolhida = int(input(f"Digite uma página entre 1 e {total_paginas}: "))

                if 1 <= pagina_escolhida <= total_paginas:
                    pagina_atual = pagina_escolhida
                else:
                    print("Página fora do intervalo permitido.")

            except ValueError:
                print("Digite apenas números inteiros para a página.")

        elif opcao == "S":
            print("Saindo da visualização paginada.")
            break

        else:
            print("Opção inválida. Escolha N, A, I ou S.")
```

## Exemplo de estrutura dos alunos

Para essa paginação funcionar bem, cada aluno pode ser armazenado como um dicionário:

```python
alunos = [
    {
        "nome": "Aluno 1",
        "aop1": 0.8,
        "aop2": 1.7,
        "aop3": 0.9,
        "prova_regular": 5.0,
        "mm": 8.4,
        "prova_recuperacao": 0.0,
        "mg": 8.4,
        "status": "Aprovado"
    },
    {
        "nome": "Aluno 2",
        "aop1": 0.5,
        "aop2": 1.0,
        "aop3": 0.5,
        "prova_regular": 2.0,
        "mm": 4.0,
        "prova_recuperacao": 6.0,
        "mg": 5.0,
        "status": "Aprovado"
    }
]
```

Depois, basta chamar:

```python
paginar_resultados(alunos, itens_por_pagina=10)
```

## Onde isso entra no seu projeto

No fluxo completo da AOP2, a paginação deve entrar **depois** de cadastrar, calcular e classificar todos os alunos.

A sequência fica assim:

```text
Início
↓
Escolher modo:
1 - Testar com 5 alunos
2 - Seeder com 100 alunos
3 - Oficial com 100 alunos
↓
Coletar ou gerar alunos
↓
Calcular MM, recuperação, MG e status
↓
Guardar cada aluno em uma lista
↓
Exibir resumo geral da turma
↓
Perguntar se deseja visualizar relatório paginado
↓
Paginar resultados
↓
Fim
```

## Função de teste rápido

Você pode testar a paginação sem depender do algoritmo completo:

```python
def gerar_alunos_teste(quantidade=100):
    alunos = []

    for i in range(1, quantidade + 1):
        aluno = {
            "nome": f"Aluno {i}",
            "mm": 7.0 if i % 2 == 0 else 4.5,
            "mg": 7.0 if i % 2 == 0 else 5.0,
            "status": "Aprovado" if i % 2 == 0 else "Reprovado"
        }

        alunos.append(aluno)

    return alunos


alunos_teste = gerar_alunos_teste(100)
paginar_resultados(alunos_teste, itens_por_pagina=10)
```

A parte mais importante para aprender é esta: **paginação não é uma nova estrutura misteriosa**. Ela combina três coisas que você já está ensinando: **listas**, **laços de repetição** e **cálculo de índices**.
