#!/usr/bin/env python3

import csv
import fileinput
import sys
from collections import defaultdict
from jinja2 import Template


if sys.argv[1] in ('-h', '--help'):
    print('Usage: {} dataset.csv dataset2.csv ...'.format(sys.argv[0]))
    sys.exit(0)


datasets = defaultdict(lambda: {
    'title': None,
    'data': [],
})

with fileinput.input() as f, open('template.html', mode='r', encoding='utf-8') as template:
    reader = csv.reader(f, delimiter='\t')

    for row in reader:

        dataset = datasets[fileinput.filename()]

        if row[0] == 'title':
            dataset['title'] = row[1]
            continue

        rok, mesic, *dny = row
        rok, mesic = int(rok), int(mesic)
        dny = list(map(lambda i: float(i.replace(',', '.')), dny))

        dataset['data'].append({
            'rok': rok,
            'mesic': mesic,
            'dny': dny,
        })

    print(Template(template.read()).render(datasets=datasets))
