# Datetime

```python
import datetime
```

- `datetime.date` = pouze datum
- `datetime.time` = pouze čas
- `datetime.datetime` = datum a čas
- `datetime.timedelta` = časový interval

## Vytvoření

```python
silvestr = datetime.date(2017, 12, 31)
poledne = datetime.time(12)
ted = datetime.datetime.now()
dve_hodiny = datetime.timedelta(hours=2)
```

## Operátory

```python
silvestr > datetime.date.today()
```

```python
datetime.datetime.now() - dve_hodiny - dve_hodiny
```

## Spojení / rozdělení

```python
datetime.datetime.combine(silvestr, poledne)
```

```python
ted.date()
ted.time()
```

## Výpis

```python
'právě je: {:%d.%m.%Y, %H:%M:%S}'.format(ted)
```
