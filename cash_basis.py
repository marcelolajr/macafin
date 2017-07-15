# -*- coding: utf-8 -*-
"""
    ----------
    Macafin basic report module
    ----------

    This module implements basic financial report generation.

    :copyright: (c) 2017 by Aguiar, Vitoriano.
    :license: GNU GPL 3, see LICENSE for more details.
"""
import numpy as np
import pandas as pd
import locale
from os import listdir
import datetime


def color_negative_red(val):
    """
        Takes a scalar and returns a string with
        the css property `'color: red'` for negative
        strings, black otherwise.
    """
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color


def formata_real(val):
    """
        TODO:
    """
    locale.setlocale(locale.LC_ALL, 'pt-BR')
    valor = locale.currency(val)
    locale.setlocale(locale.LC_ALL, '')
    return valor


def category_piece_generation(financeira_df):
    """
        TODO:
    """
    categoria_df = financeira_df.groupby(['Categoria']).agg(
        {'ValorNum': sum}).apply(lambda x: x.sort_values(ascending=False))
    categoria_df.rename(columns={'ValorNum': 'Total'}, inplace=True)
    categoria_df_style = categoria_df.style.applymap(
        color_negative_red).format({"Total": lambda x: formata_real(x)})
    return categoria_df_style.render()


def classify_securities(row):
    """
        TODO:
    """
    if(row['Data'] == ''):
        return 'Previsto'
    else:
        return 'Recebido'


def classify_balance(row):
    """
        TODO:
    """
    if(row['ValorNum'] >= 0):
        return 'Receita'
    else:
        return 'Despesa'


def receipt_debt_generation(financeira_df):
    """
        TODO:
    """
    financeira_df['Recebido'] = financeira_df.apply(
        lambda row: classify_securities(row), axis=1)
    financeira_df['Classificação'] = financeira_df.apply(
        lambda row: classify_balance(row), axis=1)
    receita_despesa = financeira_df.groupby(
        ['Recebido', 'Classificação']).agg({'ValorNum': sum})
    receita_despesa = receita_despesa.apply(
        lambda x: x.sort_values(ascending=False))
    return receita_despesa.style.applymap(color_negative_red).format(
        {"ValorNum": lambda x: formata_real(x)}).render()


def general_report_generation(financeira_df):
    """
        TODO:
    """
    relatorio_geral = financeira_df[[
        'Data', 'Categoria', 'Beneficiário', 'Vencimento', 'ValorNum']]
    relatorio_geral = relatorio_geral.sort_values('Data', ascending=True)
    relatorio_geral = relatorio_geral.style.applymap(
        color_negative_red, subset=['ValorNum'])
    relatorio_geral = relatorio_geral.format(
        {"ValorNum": lambda x: formata_real(x)})
    relatorio_geral = relatorio_geral.format(
        {"Data": lambda x: datetime.datetime.strftime(x, '%d/%m/%Y') if (x != '') else 'Pendente'})
    return relatorio_geral.render()


def total_profit(financeira_df):
    """
        TODO:
    """
    total_periodo_df = financeira_df['ValorNum'].sum()
    return 'O total de apurado no mês foi: ' + formata_real(total_periodo_df)


def cash_basis_generation(start, finish, app):
    """
        TODO:
    """
    if(start == ''):
        start = None
    if(finish == ''):
        finish = None
    allFiles = listdir(app.config['DATA_FOLDER'])
    financeira_df = pd.DataFrame()
    list_ = []
    for file_ in allFiles:
        df = pd.read_csv(
            app.config['DATA_FOLDER'] +
            '\\' +
            file_,
            index_col=None,
            header=0)
        list_.append(df)
        financeira_df = pd.concat(list_)
    financeira_df['ValorNum'] = financeira_df['Valor'].map(
        lambda x: x.replace(
            'R$ ',
            '').replace(
            '.',
            '').replace(
                ',',
            '.'))
    financeira_df['ValorNum'] = pd.to_numeric(
        financeira_df['ValorNum'], errors='coerce')
    financeira_df['Data'] = pd.to_datetime(
        financeira_df['Data'], format='%d/%m/%Y', errors='coerce')
    financeira_df = financeira_df.replace(np.nan, '', regex=True)

    if (start is not None and finish is not None):
        financeira_df = financeira_df[(financeira_df.Data >= datetime.datetime.strptime(start, "%d/%m/%Y").date())
                                      & (financeira_df.Data <= datetime.datetime.strptime(finish, "%d/%m/%Y").date())]

    return {
        "category_piece": category_piece_generation(financeira_df),
        "receipt_debt": receipt_debt_generation(financeira_df),
        "general_report": general_report_generation(financeira_df),
        "total_profit": total_profit(financeira_df),
        "start": start,
        "finish": finish}
