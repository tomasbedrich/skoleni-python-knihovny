#!/usr/bin/env python3

from matplotlib import pyplot
from matplotlib.dates import YearLocator


def vykresli_spojnice(hodnoty, nadpis, jednotky):
    fig, ax = pyplot.subplots()

    pyplot.title(nadpis)
    pyplot.xlabel('datum')
    pyplot.ylabel(jednotky)

    x_hodnoty = [polozka[0] for polozka in hodnoty]
    y_hodnoty = [polozka[1] for polozka in hodnoty]

    pyplot.plot_date(x_hodnoty, y_hodnoty, 'b-', linewidth=0.5)
    pyplot.axhline(0, linewidth=0.2)

    # v jakých intervalech a jak mají vypadat popisky na ose X
    ax.xaxis.set_major_locator(YearLocator())

    pyplot.show()


def vykresli_sloupce(hodnoty, nadpis, jednotky):
    pyplot.title(nadpis)
    pyplot.xlabel('datum')
    pyplot.ylabel(jednotky)

    x_hodnoty = [polozka[0] for polozka in hodnoty]
    y_hodnoty = [polozka[1] for polozka in hodnoty]

    pyplot.bar(x_hodnoty, y_hodnoty, color='b')
    pyplot.show()


if __name__ == '__main__':
    from datetime import date
    hodnoty = [
        (date(2014, 1, 1), 111),
        (date(2015, 1, 1), 123),
        (date(2016, 1, 1), 126),
        (date(2017, 1, 1), 90),
        (date(2018, 1, 1), 80),
    ]
    vykresli_spojnice(hodnoty, 'test', 'm/s')
    # vykresli_sloupce(hodnoty, 'test', 'm/s')
