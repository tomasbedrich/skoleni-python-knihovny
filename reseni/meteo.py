#!/usr/bin/env python3

import requests
import bs4
import datetime

ADRESA = 'https://tbedrich.cz/meteo.html'


def stahni():
    page = requests.get(ADRESA)
    page.encoding = 'utf-8'
    return page.text


def zpracuj(surovy_text, nazev_datasetu):
    soup = bs4.BeautifulSoup(surovy_text, 'html.parser')

    dataset = soup.select_one('#' + nazev_datasetu)

    nadpis = dataset.select_one('h1').text
    jednotky = nadpis.split()[-1]
    hodnoty = []

    for radek in dataset.select('tbody tr'):

        hlavicka_radku = radek.select('th')
        rok = int(hlavicka_radku[0].text)
        mesic = int(hlavicka_radku[1].text)

        for i, sloupec in enumerate(radek.select('td')):
            den = i + 1
            datum = datetime.date(rok, mesic, den)
            velicina = float(sloupec.text)
            vzorek = (datum, velicina)
            hodnoty.append(vzorek)

    return {
        'nadpis': nadpis,
        'jednotky': jednotky,
        'hodnoty': hodnoty,
    }


if __name__ == '__main__':
    print(zpracuj(stahni(), 'prumer-teplota'))
