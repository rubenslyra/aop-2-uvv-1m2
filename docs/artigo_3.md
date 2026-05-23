# Guia Instrutivo — Escolha de Figuras em Fluxogramas

O fluxograma não é apenas um desenho. Ele representa o raciocínio lógico antes da programação. Cada figura existe porque ela comunica um tipo específico de operação mental ou computacional.

Quando escolhemos a figura errada, o algoritmo fica confuso, difícil de manter e mais complicado de transformar em código.

---

# 1. Por que usamos fluxogramas?

Antes de programar, precisamos responder:

```text
O que entra?
O que acontece?
O que é calculado?
O que é decidido?
O que sai?
```

O fluxograma transforma isso em:

* visão estrutural;
* sequência lógica;
* rastreamento de decisões;
* prevenção de erros;
* planejamento do código.

---

# 2. Estrutura de pensamento antes da figura

Antes de desenhar qualquer bloco:

## Pergunta 1

```text
Isso é uma ação?
```

Se sim:
→ PROCESSO

---

## Pergunta 2

```text
Isso é uma decisão?
```

Se sim:
→ DECISÃO

---

## Pergunta 3

```text
Isso é entrada ou saída?
```

Se sim:
→ ENTRADA/SAÍDA

---

## Pergunta 4

```text
Isso começa ou termina?
```

Se sim:
→ TERMINADOR

---

# 3. Principais figuras e quando usar

---

# Figura 1 — TERMINADOR

## Forma

```text
oval
```

## Função

Representa:

* início;
* encerramento;
* parada abrupta;
* saída final.

## Quando usar

### Início do algoritmo

```text
INÍCIO
```

### Encerramento

```text
FIM
```

### Cancelamento

```text
ENCERRADO PELO USUÁRIO
```

---

## Exemplo no projeto UVVON

```text
Início do sistema
Fim da execução
Cancelamento da entrada
```

---

# Figura 2 — PROCESSO

## Forma

```text
retângulo
```

## Função

Representa:

* cálculos;
* processamento;
* transformações;
* ações executadas.

## Quando usar

### Cálculo

```text
Calcular Média do Módulo
```

### Organização

```text
Gerar tabela
```

### Conversão

```text
Converter texto para decimal
```

---

## Exemplo UVVON

```text
Somar AOP1 + AOP2 + AOP3 + PR
```

---

# Figura 3 — DECISÃO

## Forma

```text
losango
```

## Função

Representa:

* perguntas;
* bifurcações;
* escolhas;
* condicionais.

## Quando usar

### IF

```text
MM >= 7?
```

### Validação

```text
Nota pertence ao RAID?
```

### Cancelamento

```text
Usuário deseja sair?
```

---

## Saídas da decisão

Toda decisão normalmente possui:

```text
SIM
NÃO
```

ou:

```text
VERDADEIRO
FALSO
```

---

# Figura 4 — ENTRADA / SAÍDA

## Forma

```text
paralelogramo
```

## Função

Representa:

* leitura;
* exibição;
* comunicação com usuário.

## Quando usar

### Entrada

```text
Ler nota AOP1
```

### Saída

```text
Exibir resultado final
```

---

## Exemplo UVVON

```text
Digite a nota:
```

---

# Figura 5 — CONECTOR

## Forma

```text
círculo pequeno
```

## Função

Liga partes distantes do fluxograma.

## Quando usar

Quando:

* o desenho ficou grande;
* existem múltiplas páginas;
* queremos evitar cruzamento de linhas.

---

# Figura 6 — SUBPROCESSO

## Forma

```text
retângulo com bordas laterais duplas
```

## Função

Representa:

* módulo;
* função externa;
* rotina separada.

## Quando usar

### Modularização

```text
Executar validação de entrada
```

### Função externa

```text
Executar cálculo da recuperação
```

---

# 4. Como escolher a figura correta

## Método mental rápido

---

## PASSO 1

Pergunte:

```text
Estou PEDINDO algo?
```

→ Entrada/Saída

---

## PASSO 2

Pergunte:

```text
Estou CALCULANDO algo?
```

→ Processo

---

## PASSO 3

Pergunte:

```text
Estou DECIDINDO algo?
```

→ Decisão

---

## PASSO 4

Pergunte:

```text
Estou COMEÇANDO ou TERMINANDO?
```

→ Terminador

---

## PASSO 5

Pergunte:

```text
Isso virou uma função separada?
```

→ Subprocesso

---

# 5. Aplicando ao projeto UVVON

---

# Etapa 1 — Início

Figura:

```text
Terminador
```

Texto:

```text
INÍCIO
```

---

# Etapa 2 — Ler notas

Figura:

```text
Entrada/Saída
```

Texto:

```text
Ler AOP1
```

---

# Etapa 3 — Validar nota

Figura:

```text
Decisão
```

Texto:

```text
Nota pertence ao RAID?
```

---

# Etapa 4 — Calcular MM

Figura:

```text
Processo
```

Texto:

```text
MM = AOP1 + AOP2 + AOP3 + PR
```

---

# Etapa 5 — Aprovação direta

Figura:

```text
Decisão
```

Texto:

```text
MM >= 7?
```

---

# Etapa 6 — Recuperação

Figura:

```text
Decisão
```

Texto:

```text
3 < MM < 7?
```

---

# Etapa 7 — Calcular MG

Figura:

```text
Processo
```

Texto:

```text
MG = (MM + REC) / 2
```

---

# Etapa 8 — Exibir resultado

Figura:

```text
Entrada/Saída
```

Texto:

```text
Exibir status final
```

---

# Etapa 9 — Encerramento

Figura:

```text
Terminador
```

Texto:

```text
FIM
```

---

# 6. Fluxogramas e relação com Python

| Fluxograma  | Python           |
| ----------- | ---------------- |
| Processo    | cálculo / função |
| Decisão     | if / elif / else |
| Repetição   | while / for      |
| Entrada     | input()          |
| Saída       | print()          |
| Subprocesso | função           |
| Terminador  | início/fim       |

---

# 7. Erros comuns em fluxogramas

## Erro 1

Usar PROCESSO para pergunta.

Errado:

```text
[Calcular] MM >= 7?
```

Correto:

```text
<Decisão> MM >= 7?
```

---

## Erro 2

Misturar entrada com cálculo.

Errado:

```text
Ler e calcular MM
```

Correto:

```text
Ler nota
↓
Calcular MM
```

---

## Erro 3

Múltiplas decisões no mesmo losango.

Errado:

```text
MM >= 7 e usuário quer sair?
```

Cada decisão deve possuir responsabilidade clara.

---

# 8. Filosofia usada pelo time

A equipe adotou a seguinte estrutura:

```text
pensar
→ desenhar
→ testar no papel
→ validar fluxo
→ modularizar
→ programar
→ testar manualmente
→ integrar
```
