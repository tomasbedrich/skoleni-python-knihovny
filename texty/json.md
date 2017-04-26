# JSON

```python
import json
```

## Čtení

```python
with open('zdroj.json', mode='r', encoding='utf-8') as zdroj:
    data = json.load(zdroj)
    # nebo
    data = json.loads(zdroj.read())
```

## Zápis

```python
with open('cil.json', mode='w', encoding='utf-8') as cil:
    json.dump(data, cil)
    # nebo
    json.dump(data, cil, indent=2)
    # nebo
    cil.write(json.dumps(data))
```

## Chyby

```python
try:
    json.loads('{')
except json.JSONDecodeError:
    print('Nevalidní JSON.')
```
