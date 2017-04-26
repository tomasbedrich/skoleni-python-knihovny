# Pathlib

```python
from pathlib import Path
```

## Základy

### Reprezentace složky / souboru

```python
obrazky = Path('Dokumenty/Obrazky')
```

### Spojování

```python
dovolena_2016 = obrazky / 'Dovolena' / '2016'
velryba = dovolena_2016 / Path('DSC0123192.jpg')
```

### Rozebrání "na součástky"

```python
velryba.parts
velryba.name
velryba.stem
velryba.suffix
```

## Pokročilejší

### Globbing

```python
for fotka in dovolena_2016.glob('*.jpg'):
    print(fotka)
```

### "Absolutizace" cesty

```python
velryba.resolve()
```
