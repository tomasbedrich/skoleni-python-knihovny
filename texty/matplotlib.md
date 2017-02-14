# Matplotlib

```python
from matplotlib import pyplot
```

## Základní graf

```python
x_data = [1, 2, 3, 4, 5]
y_data = [1**2, 2**2, 3**2, 4**2, 5**2]
pyplot.plot(x_data, y_data)
pyplot.show()
```

## Popisky

```python
pyplot.title('Nadpis')
pyplot.xlabel('Čísla')
pyplot.ylabel('Druhé mocniny')
```

## Limity os

```python
pyplot.xlim(0, 50)
pyplot.ylim(0, 50)
```

## Barvičky a tvary

```python
pyplot.plot(x_data, y_data, 'ro')
```

## Více datových sad

```python
pyplot.plot(x_data, y_data, 'b-', x_data, y_data, 'r.')
```

## Mřížka a čáry

```python
pyplot.grid()
pyplot.axhline(5)
```

## Jiné grafy

```python
pyplot.bar(x_data, y_data)
```

```python
casy = [
    datetime.time(18, 42),
    datetime.time(18, 43),
    datetime.time(18, 44),
    datetime.time(18, 45),
    datetime.time(18, 46),
]
pyplot.plot_date(casy, y_data)
```

```python
velikosti = [10, 20, 30, 100, 20]
barvy = 'rgbrg'
pyplot.scatter(x_data, y_data, velikosti, barvy)
```
