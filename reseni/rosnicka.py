#!/usr/bin/env python3

import click

import meteo
import grafy


def _filtruj_roky(hodnoty, od, do):
    for datum, vzorek in hodnoty:
        if od <= datum.year <= do:
            yield datum, vzorek


@click.group()
def main():
    '''
    Stáhne a zobrazí historická data o počasí.
    '''
    return


@main.command()
@click.option('--od', type=int, default=2000, help='Počáteční rok')
@click.option('--do', type=int, default=2017, help='Konečný rok')
def teploty(od, do):
    '''
    Graf průměrné denní teploty.
    '''
    data = meteo.zpracuj(meteo.stahni(), 'prumer-teplota')
    hodnoty = list(_filtruj_roky(data['hodnoty'], od, do))
    grafy.vykresli_spojnice(hodnoty, data['nadpis'], data['jednotky'])


@main.command()
@click.option('--od', type=int, default=2000, help='Počáteční rok')
@click.option('--do', type=int, default=2017, help='Konečný rok')
def srazky(od, do):
    '''
    Graf denního úhrnu srážek.
    '''
    data = meteo.zpracuj(meteo.stahni(), 'srazky')
    hodnoty = list(_filtruj_roky(data['hodnoty'], od, do))
    grafy.vykresli_sloupce(hodnoty, data['nadpis'], data['jednotky'])


if __name__ == '__main__':
    main()
