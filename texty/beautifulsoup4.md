# BeautifulSoup4

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup('<html> ... </html>', 'html.parser')
```

## Hledání elementů

```python
element = soup.select_one('CSS-selektor')
elementy = soup.select('CSS-selektor')
```

### Některé nejpoužívanější CSS selektory

- `#id`
- `.trida`
- `element`
- `element potomek`
- + jejich kombinace

```python
menu = soup.select_one('#hlavicka .menu')
```

## Text prvku

```python
nadpis_stranky = soup.select_one('#hlavicka h1').text
```

## Atributy

```python
cil_formulare = soup.select_one('form.kontakt')['action']
```
