"""
AOP2 UVV - Sistema de Avaliação EAD
Autor: Rubens Lyra / Rubinho Lyra Labs
Objetivo: Ler notas de alunos, calcular situação acadêmica e exibir estatísticas finais.

Regras do enunciado:
- AOP1: 0.0 a 1.0
- AOP2: 0.0 a 2.0
- AOP3: 0.0 a 1.0
- Prova Regular: 0.0 a 6.0
- Média do Módulo (MM) = AOP1 + AOP2 + AOP3 + Prova Regular
- Aprovado direto: MM >= 7.0
- Reprovação direta: MM < 3.0, sem recuperação
- Recuperação: 3.0 <= MM < 7.0
- Média Geral com recuperação: (MM + Prova Recuperação) / 2
- Aprovado por recuperação: Média Geral >= 5.0

Modos de execução:
1 - Teste manual com 5 alunos
2 - Seeder automático com 100 alunos
3 - Oficial manual com 100 alunos
"""

from __future__ import annotations

import random
from typing import Any


# ------------------------------
# Constantes do domínio
# ------------------------------
LIMITE_AOP1 = (0.0, 1.0)
LIMITE_AOP2 = (0.0, 2.0)
LIMITE_AOP3 = (0.0, 1.0)
LIMITE_PROVA_REGULAR = (0.0, 6.0)
LIMITE_RECUPERACAO = (0.0, 10.0)

MEDIA_APROVACAO_DIRETA = 7.0
MEDIA_REPROVACAO_DIRETA = 3.0
MEDIA_APROVACAO_RECUPERACAO = 5.0

QTD_TESTE_MANUAL = 5
QTD_OFICIAL = 100


# ------------------------------
# Utilitários de entrada e saída
# ------------------------------
def linha(tamanho: int = 72) -> None:
    """Exibe uma linha separadora simples."""
    print("-" * tamanho)


def titulo(texto: str) -> None:
    # clear terminal (funciona na maioria dos sistemas). Esta linha está fazendo a função de "limpar" o terminal para exibir o título de forma mais destacada.    
    print("\033c", end="")
    # Exibe um título padronizado no terminal. Aqui, o unicode "\033c" é um comando de controle ANSI que limpa a tela do terminal. O argumento "end=''" é usado para evitar que o comando de limpeza seja seguido por uma nova linha, garantindo que o título seja exibido no topo da tela limpa.
    """Exibe um título padronizado no terminal."""
    linha()
    print(texto)
    linha()


def normalizar_decimal(texto: str) -> str:
    """
    Aceita vírgula ou ponto como separador decimal.
    Ex.: '7,5' vira '7.5'.
    """
    return texto.strip().replace(",", ".")


def ler_float_intervalo(rotulo: str, minimo: float, maximo: float) -> float:
    """
    Lê um número decimal validando tipo e faixa.
    Mantém o usuário em loop até informar uma nota válida.
    """
    while True:
        entrada = input(f"{rotulo} [{minimo:.1f} a {maximo:.1f}]: ")
        entrada = normalizar_decimal(entrada)

        try:
            valor = float(entrada)
        except ValueError:
            print("  Erro: digite um número válido. Exemplo: 0.8 ou 0,8.")
            continue

        if valor < minimo or valor > maximo:
            print(f"  Erro: a nota deve estar entre {minimo:.1f} e {maximo:.1f}.")
            continue

        return round(valor, 2)


def ler_texto_obrigatorio(rotulo: str) -> str:
    """Lê um texto obrigatório, impedindo entrada vazia."""
    while True:
        valor = input(f"{rotulo}: ").strip()
        if valor:
            return valor
        print("  Erro: este campo não pode ficar vazio.")


def ler_opcao_menu() -> int:
    """Lê a opção inicial do usuário com validação."""
    while True:
        titulo("AOP2 UVV - Sistema de Avaliação")
        print("Escolha uma forma de execução:")
        print("1 - Testar manualmente com 5 alunos")
        print("2 - Executar seeder automático com 100 alunos")
        print("3 - Executar versão oficial manual com 100 alunos")
        print("0 - Sair")
        linha()

        entrada = input("Opção: ").strip()
        if entrada in {"0", "1", "2", "3"}:
            return int(entrada)

        print("Erro: escolha apenas 0, 1, 2 ou 3.")


# ------------------------------
# Cálculo e regras acadêmicas
# ------------------------------
def calcular_media_modulo(aop1: float, aop2: float, aop3: float, prova_regular: float) -> float:
    """Calcula a Média do Módulo conforme enunciado."""
    return round(aop1 + aop2 + aop3 + prova_regular, 2)


def calcular_media_geral(media_modulo: float, prova_recuperacao: float) -> float:
    """Calcula a Média Geral quando há prova de recuperação."""
    return round((media_modulo + prova_recuperacao) / 2, 2)


def avaliar_aluno(
    nome: str,
    aop1: float,
    aop2: float,
    aop3: float,
    prova_regular: float,
    prova_recuperacao: float | None = None,
) -> dict[str, Any]:
    """
    Aplica as regras do enunciado e retorna um dicionário com o resultado do aluno.

    Observação de interpretação:
    Como o enunciado define reprovação direta apenas para MM < 3.0,
    consideramos que MM = 3.0 ainda tem direito à recuperação.
    """
    media_modulo = calcular_media_modulo(aop1, aop2, aop3, prova_regular)

    resultado: dict[str, Any] = {
        "nome": nome,
        "aop1": aop1,
        "aop2": aop2,
        "aop3": aop3,
        "prova_regular": prova_regular,
        "media_modulo": media_modulo,
        "prova_recuperacao": prova_recuperacao,
        "media_geral": None,
        "status": "",
        "motivo": "",
    }

    if media_modulo >= MEDIA_APROVACAO_DIRETA:
        resultado["status"] = "Aprovado"
        resultado["motivo"] = "Aprovado direto por Média do Módulo >= 7.0"
        return resultado

    if media_modulo < MEDIA_REPROVACAO_DIRETA:
        resultado["status"] = "Reprovado"
        resultado["motivo"] = "Reprovação direta por Média do Módulo < 3.0"
        return resultado

    # Recuperação: 3.0 <= MM < 7.0
    if prova_recuperacao is None:
        raise ValueError("Aluno em recuperação precisa de nota da Prova de Recuperação.")

    media_geral = calcular_media_geral(media_modulo, prova_recuperacao)
    resultado["media_geral"] = media_geral

    if media_geral >= MEDIA_APROVACAO_RECUPERACAO:
        resultado["status"] = "Aprovado"
        resultado["motivo"] = "Aprovado por recuperação com Média Geral >= 5.0"
    else:
        resultado["status"] = "Reprovado"
        resultado["motivo"] = "Reprovado após recuperação com Média Geral < 5.0"

    return resultado


# ------------------------------
# Coleta manual e seeder
# ------------------------------
def coletar_aluno_manual(indice: int) -> dict[str, Any]:
    """Coleta as notas de um aluno com validação de entrada."""
    titulo(f"Aluno {indice}")
    nome = ler_texto_obrigatorio("Nome do aluno")
    aop1 = ler_float_intervalo("Nota AOP1", *LIMITE_AOP1)
    aop2 = ler_float_intervalo("Nota AOP2", *LIMITE_AOP2)
    aop3 = ler_float_intervalo("Nota AOP3", *LIMITE_AOP3)
    prova_regular = ler_float_intervalo("Nota da Prova Regular", *LIMITE_PROVA_REGULAR)

    media_modulo = calcular_media_modulo(aop1, aop2, aop3, prova_regular)
    prova_recuperacao = None

    if MEDIA_REPROVACAO_DIRETA <= media_modulo < MEDIA_APROVACAO_DIRETA:
        print(f"MM = {media_modulo:.2f}. Aluno em recuperação.")
        prova_recuperacao = ler_float_intervalo("Nota da Prova de Recuperação", *LIMITE_RECUPERACAO)
    elif media_modulo < MEDIA_REPROVACAO_DIRETA:
        print(f"MM = {media_modulo:.2f}. Reprovação direta, sem recuperação.")
    else:
        print(f"MM = {media_modulo:.2f}. Aprovação direta.")

    return avaliar_aluno(nome, aop1, aop2, aop3, prova_regular, prova_recuperacao)


def gerar_nota(minimo: float, maximo: float) -> float:
    """Gera nota válida com uma casa decimal."""
    return round(random.uniform(minimo, maximo), 1)


def gerar_aluno_seeder(indice: int) -> dict[str, Any]:
    """Gera um aluno fictício válido para teste com 100 registros."""
    nome = f"Aluno {indice:03d}"
    aop1 = gerar_nota(*LIMITE_AOP1)
    aop2 = gerar_nota(*LIMITE_AOP2)
    aop3 = gerar_nota(*LIMITE_AOP3)
    prova_regular = gerar_nota(*LIMITE_PROVA_REGULAR)

    media_modulo = calcular_media_modulo(aop1, aop2, aop3, prova_regular)
    prova_recuperacao = None

    if MEDIA_REPROVACAO_DIRETA <= media_modulo < MEDIA_APROVACAO_DIRETA:
        prova_recuperacao = gerar_nota(*LIMITE_RECUPERACAO)

    return avaliar_aluno(nome, aop1, aop2, aop3, prova_regular, prova_recuperacao)


def executar_turma_manual(quantidade: int) -> list[dict[str, Any]]:
    """Executa coleta manual em laço controlado."""
    alunos = []
    for indice in range(1, quantidade + 1):
        aluno = coletar_aluno_manual(indice)
        alunos.append(aluno)
        imprimir_resultado_aluno(aluno)
    return alunos


def executar_turma_seeder(quantidade: int = QTD_OFICIAL, semente: int = 2026) -> list[dict[str, Any]]:
    """Executa geração automática de alunos para testes reproduzíveis."""
    random.seed(semente)
    return [gerar_aluno_seeder(indice) for indice in range(1, quantidade + 1)]


# ------------------------------
# Estatísticas e relatório
# ------------------------------
def calcular_estatisticas(alunos: list[dict[str, Any]]) -> dict[str, float | int]:
    """Calcula totais e percentuais de aprovação/reprovação."""
    total = len(alunos)
    aprovados = sum(1 for aluno in alunos if aluno["status"] == "Aprovado")
    reprovados = total - aprovados

    percentual_aprovados = (aprovados / total) * 100 if total else 0.0
    percentual_reprovados = (reprovados / total) * 100 if total else 0.0

    return {
        "total": total,
        "aprovados": aprovados,
        "reprovados": reprovados,
        "percentual_aprovados": round(percentual_aprovados, 2),
        "percentual_reprovados": round(percentual_reprovados, 2),
    }


def imprimir_resultado_aluno(aluno: dict[str, Any]) -> None:
    """Exibe o resultado individual de um aluno."""
    linha()
    print(f"Aluno: {aluno['nome']}")
    print(f"MM: {aluno['media_modulo']:.2f}")

    if aluno["prova_recuperacao"] is not None:
        print(f"Prova de Recuperação: {aluno['prova_recuperacao']:.2f}")
        print(f"Média Geral: {aluno['media_geral']:.2f}")

    print(f"Status: {aluno['status']}")
    print(f"Motivo: {aluno['motivo']}")
    linha()


def imprimir_relatorio(alunos: list[dict[str, Any]], mostrar_lista: bool = True) -> None:
    """Exibe relatório final da turma."""
    titulo("Relatório Final da Turma")

    if mostrar_lista:
        print(f"{'Aluno':<15} {'MM':>6} {'Rec.':>6} {'MG':>6} {'Status':<10}")
        linha()
        for aluno in alunos:
            rec = "-" if aluno["prova_recuperacao"] is None else f"{aluno['prova_recuperacao']:.2f}"
            mg = "-" if aluno["media_geral"] is None else f"{aluno['media_geral']:.2f}"
            print(f"{aluno['nome']:<15} {aluno['media_modulo']:>6.2f} {rec:>6} {mg:>6} {aluno['status']:<10}")
        linha()

    estatisticas = calcular_estatisticas(alunos)
    print(f"Total de alunos: {estatisticas['total']}")
    print(f"Aprovados: {estatisticas['aprovados']} ({estatisticas['percentual_aprovados']:.2f}%)")
    print(f"Reprovados: {estatisticas['reprovados']} ({estatisticas['percentual_reprovados']:.2f}%)")
    linha()


# ------------------------------
# Testes simples
# ------------------------------
def executar_testes() -> None:
    """Executa pequenos testes de regra de negócio com assert."""
    aluno_aprovado_direto = avaliar_aluno("Teste 1", 1.0, 2.0, 1.0, 3.0)
    assert aluno_aprovado_direto["status"] == "Aprovado"
    assert aluno_aprovado_direto["media_modulo"] == 7.0

    aluno_reprovado_direto = avaliar_aluno("Teste 2", 0.0, 0.5, 0.0, 2.0)
    assert aluno_reprovado_direto["status"] == "Reprovado"
    assert aluno_reprovado_direto["media_modulo"] == 2.5

    aluno_aprovado_rec = avaliar_aluno("Teste 3", 1.0, 1.0, 1.0, 2.0, 5.0)
    assert aluno_aprovado_rec["media_modulo"] == 5.0
    assert aluno_aprovado_rec["media_geral"] == 5.0
    assert aluno_aprovado_rec["status"] == "Aprovado"

    aluno_reprovado_rec = avaliar_aluno("Teste 4", 1.0, 1.0, 0.0, 2.0, 4.0)
    assert aluno_reprovado_rec["media_modulo"] == 4.0
    assert aluno_reprovado_rec["media_geral"] == 4.0
    assert aluno_reprovado_rec["status"] == "Reprovado"

    stats = calcular_estatisticas([aluno_aprovado_direto, aluno_reprovado_direto])
    assert stats["total"] == 2
    assert stats["aprovados"] == 1
    assert stats["reprovados"] == 1
    assert stats["percentual_aprovados"] == 50.0

    print("Testes executados com sucesso.")


# ------------------------------
# Função principal
# ------------------------------
def main() -> None:
    """Controla o menu principal e a execução do algoritmo."""
    executar_testes()

    while True:
        opcao = ler_opcao_menu()

        if opcao == 0:
            print("Programa encerrado.")
            break

        if opcao == 1:
            alunos = executar_turma_manual(QTD_TESTE_MANUAL)
            imprimir_relatorio(alunos)
        elif opcao == 2:
            alunos = executar_turma_seeder(QTD_OFICIAL)
            imprimir_relatorio(alunos, mostrar_lista=True)
        elif opcao == 3:
            alunos = executar_turma_manual(QTD_OFICIAL)
            imprimir_relatorio(alunos)

        input("Pressione Enter para voltar ao menu principal...")


if __name__ == "__main__":
    main()
