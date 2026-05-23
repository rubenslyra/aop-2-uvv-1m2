# Proposta Oficial — Padrão RLLabs

## Estratégia de Branches

### Estrutura Base

```text
main
develop
```

---

# Prefixos Oficiais de Branch

## Features

```text
feat-rl-nome-da-feature
```

Exemplos:

```text
feat-rl-validacao-entrada
feat-rl-normalizacao-decimal
feat-rl-menu-terminal
feat-rl-progressbar-seeder
feat-rl-relatorio-tabular
feat-rl-captura-aop
feat-rl-base-notas
```

---

## Correções

```text
fix-rl-descricao-curta
```

Exemplos:

```text
fix-rl-validacao-aop2
fix-rl-loop-entrada
fix-rl-tratamento-cancelamento
```

---

## Documentação

```text
docs-rl-descricao-curta
```

Exemplos:

```text
docs-rl-manual-terminal
docs-rl-regras-avaliacao
docs-rl-fluxograma
```

---

## Refatoração

```text
refactor-rl-descricao-curta
```

Exemplos:

```text
refactor-rl-separacao-modulos
refactor-rl-organizacao-validacao
```

---

# Conventional Commits — RLLabs

## Features

```bash
git commit -m "feat(rl): adiciona validacao de notas do raid"
```

---

## Correções

```bash
git commit -m "fix(rl): corrige tratamento de entrada decimal"
```

---

## Documentação

```bash
git commit -m "docs(rl): adiciona roteiro de treino da equipe"
```

---

## Refatoração

```bash
git commit -m "refactor(rl): reorganiza funcoes de entrada"
```

---

# Template Oficial de Pull Request — RLLabs

# RLLabs — Pull Request Template

## Objetivo

Descreva claramente o objetivo técnico desta alteração.

---

## Funcionalidade

* [ ] Nova funcionalidade
* [ ] Correção
* [ ] Refatoração
* [ ] Documentação
* [ ] Ajuste visual
* [ ] Organização arquitetural

---

## Arquivos Alterados

Liste os principais arquivos modificados.

Exemplo:

* src/entrada.py
* src/validacao.py
* docs/testes_manuais.md

---

## Estratégia Aplicada

Explique:

* qual problema estava sendo resolvido;
* qual abordagem foi escolhida;
* por que essa abordagem foi adotada.

---

## Testes Manuais Realizados

Descreva:

### Cenário 1

Entrada:
Resultado esperado:
Resultado obtido:

### Cenário 2

Entrada:
Resultado esperado:
Resultado obtido:

---

## Checklist

* [ ] Branch criada a partir de develop
* [ ] Código executa sem erros
* [ ] Funções possuem responsabilidade clara
* [ ] Entrada inválida foi testada
* [ ] Fluxo de cancelamento foi testado
* [ ] Commit segue conventional commits
* [ ] PR direcionado para develop
* [ ] Não existem prints de debug esquecidos

---

## Observações Técnicas

Espaço livre para:

* riscos;
* melhorias futuras;
* dúvidas arquiteturais;
* sugestões.

# ISSUES de Treino — Filosofia “Um prepara o outro”

## ISSUE 001 — Normalização de Entrada Decimal

### Objetivo

Construir funções responsáveis por:

* remover espaços;
* trocar vírgula por ponto;
* converter string para Decimal.

### Skills treinadas

* tratamento textual;
* funções pequenas;
* responsabilidade única;
* debug simples.

### Branch

```text
feat-rl-normalizacao-decimal
```

### Commit esperado

```bash
git commit -m "feat(rl): adiciona normalizacao decimal de entrada"
```

---

# ISSUE 002 — Sistema de Cancelamento Seguro

### Objetivo

Criar mecanismo que:

* reconheça `0`, `esc`, `exit`, `sair`;
* interrompa operação sem quebrar terminal.

### Skills treinadas

* condicionais;
* tolerância a erro;
* UX de terminal.

### Branch

```text
feat-rl-cancelamento-operacao
```

---

# ISSUE 003 — Validação por RAID

### Objetivo

Garantir que notas só sejam aceitas se existirem na lista oficial.

### Skills treinadas

* listas;
* busca;
* validação lógica;
* integridade de dados.

### Branch

```text
feat-rl-validacao-raid
```

---

# ISSUE 004 — Prompt Dinâmico

### Objetivo

Construir prompts automáticos usando o RAID.

Exemplo:

```text
AOP1 [0.0, 0.2, 0.4, 0.6...]:
```

### Skills treinadas

* composição textual;
* reutilização;
* funções parametrizadas.

### Branch

```text
feat-rl-prompt-dinamico
```

---

# ISSUE 005 — Captura Resiliente de Entrada

### Objetivo

Construir loop seguro usando:

* try/except;
* KeyboardInterrupt;
* reentrada após erro.

### Skills treinadas

* resiliência;
* fluxo contínuo;
* engenharia defensiva.

### Branch

```text
feat-rl-captura-resiliente
```

---

# ISSUE 006 — ProgressBar Ubuntu Style

### Objetivo

Criar barra de progresso inspirada:

* apt;
* apt-get;
* dpkg;
* installers Linux.

### Skills treinadas

* terminal;
* UX textual;
* atualização dinâmica.

### Branch

```text
feat-rl-progressbar-terminal
```

---

# ISSUE 007 — Tabela Tabular de Terminal

### Objetivo

Exibir alunos em formato:

* linhas;
* colunas;
* alinhamento fixo;
* leitura administrativa.

### Skills treinadas

* formatação;
* exibição;
* organização visual.

### Branch

```text
feat-rl-relatorio-tabular
```

---

# ISSUE 008 — Seeder Examinável

### Objetivo

Gerar 100 alunos usando:

* random controlado;
* seed fixa;
* distribuição auditável.

### Skills treinadas

* geração de dados;
* repetibilidade;
* análise estatística básica.

### Branch

```text
feat-rl-seeder-auditavel
```

---

# ISSUE 009 — Ajuda Unix Style

### Objetivo

Preparar futura estrutura:

```bash
python main.py --help
```

Inspirado em:

* Unix;
* Shell Script Profissional;
* ferramentas CLI.

### Skills treinadas

* arquitetura CLI;
* documentação operacional;
* UX técnica.

### Branch

```text
feat-rl-help-terminal
```

---

# ISSUE 010 — Rodapé Operacional

### Objetivo

Criar rodapé persistente contendo:

* notas válidas;
* atalhos;
* comandos;
* alertas.

Inspirado em:

* DOS;
* Lotus;
* instaladores Linux.

### Branch

```text
feat-rl-rodape-operacional
```
