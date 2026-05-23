# Plano de Execução e Justificativa Técnica — Sistema de Avaliação UVVON

## 1. Justificativa das decisões de código

A aplicação foi planejada com funções pequenas e responsabilidades separadas para facilitar o aprendizado, a revisão e a manutenção. Em vez de criar um único bloco grande de código, a equipe optou por dividir o sistema em partes menores, como entrada de dados, validação, cálculo, classificação, relatórios e exibição no terminal.

Essa decisão permite que cada integrante compreenda uma parte específica do problema antes de participar da integração geral. A separação também reduz erros, facilita testes manuais e aproxima o projeto de práticas profissionais usadas em equipes de desenvolvimento.

## 2. Bases de conhecimento usadas

A construção da aplicação se apoia nos principais tópicos estudados nas aulas de Python:

```text
entrada de dados com input()
conversão de tipos
uso de variáveis
funções
listas
dicionários
condicionais
laços de repetição
tratamento de erros
formatação de strings
organização de arquivos
fluxo de execução
testes manuais
```

Também foram considerados conceitos de organização profissional de repositórios, uso de Git, branches, Pull Requests, conventional commits e documentação técnica.

## 3. O que deve ser treinado

Cada pequeno script tem função pedagógica própria.

## Treino 1 — Entrada de dados

Objetivo:

```text
Entender como o usuário informa dados ao programa.
```

Tópicos treinados:

```text
input()
strings
mensagens de orientação
cancelamento de operação
```

## Treino 2 — Normalização

Objetivo:

```text
Permitir entradas como 0,8 ou 0.8.
```

Tópicos treinados:

```text
replace()
strip()
conversão para Decimal
tratamento de entrada textual
```

## Treino 3 — Validação

Objetivo:

```text
Garantir que apenas notas válidas sejam aceitas.
```

Tópicos treinados:

```text
listas
operador in
condicionais
retorno de mensagens
```

## Treino 4 — Cálculos

Objetivo:

```text
Calcular Média do Módulo e Média Geral.
```

Tópicos treinados:

```text
operações matemáticas
funções com retorno
clareza de fórmula
```

## Treino 5 — Classificação

Objetivo:

```text
Determinar aprovação, reprovação direta ou recuperação.
```

Tópicos treinados:

```text
if
elif
else
ordem lógica das decisões
```

## Treino 6 — Relatórios

Objetivo:

```text
Exibir resultados organizados.
```

Tópicos treinados:

```text
f-strings
alinhamento
tabelas no terminal
listas de dicionários
```

## 4. Por que tratar erros e exceções

O tratamento de erros é importante porque o usuário pode digitar dados inesperados. Um sistema acadêmico, mesmo simples, não deve parar por causa de uma entrada inválida.

Exemplo:

```text
Usuário digita: abc
Sistema não deve quebrar.
Sistema deve orientar o usuário.
```

Por isso, usamos:

```text
try
except
validação antes do cálculo
mensagens de alerta
cancelamento seguro
```

Essa prática ensina resiliência de software: o programa precisa continuar funcionando mesmo quando recebe dados incorretos.

## 5. Estrutura de pensamento antes do código

Antes de codificar, a equipe deve resolver o problema no papel.

A sequência correta é:

```text
1. Ler o enunciado
2. Identificar entradas
3. Identificar saídas
4. Definir fórmulas
5. Criar casos de teste no papel
6. Desenhar o fluxo
7. Escolher tipos de dados
8. Criar funções
9. Testar manualmente
10. Integrar
```

Essa abordagem evita que o aluno apenas “digite código” sem entender o problema.

## 6. Testes no papel

Antes da execução em Python, usamos testes manuais.

Exemplo 1:

```text
AOP1 = 1.0
AOP2 = 2.0
AOP3 = 1.0
Prova Regular = 3.0

MM = 1 + 2 + 1 + 3
MM = 7

Resultado esperado:
Aprovação direta
```

Exemplo 2:

```text
AOP1 = 0.0
AOP2 = 0.2
AOP3 = 0.0
Prova Regular = 2.0

MM = 2.2

Resultado esperado:
Reprovação direta
```

Exemplo 3:

```text
MM = 4.0
Recuperação = 6.0

MG = (4 + 6) / 2
MG = 5

Resultado esperado:
Aprovado após recuperação
```

## 7. Tipos de dados escolhidos

## Listas

Usadas para representar bases válidas de notas:

```python
[0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
```

Justificativa:

```text
A lista permite verificar se uma nota pertence ao conjunto permitido.
```

## Dicionários

Usados para representar um aluno:

```python
{
    "aop_1": 1.0,
    "aop_2": 2.0,
    "aop_3": 1.0,
    "prova_regular": 3.0,
    "media_modulo": 7.0,
    "status": "Aprovação direta"
}
```

Justificativa:

```text
O dicionário organiza informações relacionadas usando nomes claros.
```

## Decimal

Usado para notas com casas decimais.

Justificativa:

```text
Ajuda a evitar problemas de precisão com números decimais em cálculos acadêmicos.
```

## 8. Cálculos matemáticos usados

## Média do Módulo

```text
MM = AOP1 + AOP2 + AOP3 + Prova Regular
```

## Média Geral após recuperação

```text
MG = (MM + Recuperação) / 2
```

## Percentual de aprovados

```text
Percentual = (quantidade_aprovados / total_alunos) * 100
```

## Percentual de reprovados

```text
Percentual = (quantidade_reprovados / total_alunos) * 100
```

## 9. Fluxogramas utilizados

Estamos usando três figuras principais de fluxograma.

## Figura 1 — Fluxo geral do sistema

Mostra:

```text
início
entrada de notas
cálculo da MM
decisão de aprovação
decisão de reprovação direta
recuperação
resultado final
fim
```

Aplicação:

```text
Usada para compreender o problema completo antes do código.
```

## Figura 2 — Fluxo de validação de entrada

Mostra:

```text
usuário digita nota
sistema normaliza
sistema verifica se pertence ao RAID
se válido, aceita
se inválido, solicita novamente
```

Aplicação:

```text
Usada para treinar entrada resiliente.
```

## Figura 3 — Fluxo de recuperação

Mostra:

```text
MM entre corte e aprovação
solicita recuperação
calcula MG
decide aprovado ou reprovado após recuperação
```

Aplicação:

```text
Usada para explicar a extensão do processo após o primeiro cálculo.
```

## 10. Códigos de cores e alertas

As cores são usadas para orientar o usuário no terminal.

```text
Verde:
aprovação, sucesso, operação concluída

Amarelo:
atenção, recuperação, alerta intermediário

Vermelho:
erro de entrada, reprovação direta, falha crítica

Azul/Ciano:
informações institucionais e títulos

Cinza:
rodapé, instruções e informações auxiliares
```

Essa escolha torna a experiência mais clara e reduz confusão durante o uso.

## 11. Uso na tabulação dos resultados

Na tabela final, as cores ajudam a separar visualmente:

```text
Aprovação direta
Reprovação direta
Performance pós-recuperação
```

A ideia é transformar o terminal em uma interface textual legível, quase como um painel administrativo.

## 12. Influência do livro Shell Script Profissional

A referência ao livro **Shell Script Profissional** entra como inspiração para a construção de uma aplicação de terminal mais madura.

A ideia não é transformar o projeto em Shell Script, mas aproveitar princípios como:

```text
clareza de comandos
mensagens objetivas
opção de ajuda
rodapé operacional
saída padronizada
resiliência no terminal
uso futuro de --help
```

Isso prepara o projeto para uma evolução natural:

```bash
python main.py --help
python main.py --seed 2605
python main.py --alunos 100
```

## 13. Conclusão técnica

O projeto não foi construído apenas para resolver um exercício. Ele foi estruturado para treinar uma equipe em pensamento computacional, organização profissional, leitura de enunciado, divisão de responsabilidades, Git, validação, testes manuais e apresentação técnica.

A filosofia adotada é:

```text
um treino prepara o outro;
uma função prepara a próxima;
um módulo prepara o sistema;
um aluno fortalece o time.
```
