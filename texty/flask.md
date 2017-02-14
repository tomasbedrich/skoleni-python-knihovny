# Flask

## Základ

```python
from flask import Flask

app = Flask('moje-aplikace')


@app.route('/')
def pozdrav():
    return 'Ahoj'


if __name__ == '__main__':
    app.run(debug=True)
```

## Vykreslení HTML šablony

```python
from flask import render_template

@app.route('/sablona')
def pozdrav_se_sablonou():
    return render_template('pozdrav.html')
```

### Parametry šablony

```python
render_template('pozdrav.html', pozdrav='Ahoj', jmeno='Franto')
```

### Zpracování dat v šabloně

```html
<html>
<head> ... </head>
<body>
    {{ pozdrav }}! Vítáme Tě, {{ jmeno }}.
</body>
</html>
```

## Přijímání dat od uživatele

### Z části URL

```python
@app.route('/obrazek/<int:cislo>')
def zobraz_obrazek(cislo):
    return render_template('obrazek.html', cislo=cislo)
```

Funguje pro: `/obrazek/12`

### Z URL parametrů

```python
from flask import request

@app.route('/obrazek')
def zobraz_obrazek():
    cislo = request.args['cislo']
    ...
```

Funguje pro: `/obrazek?cislo=12`

### Z odeslaného formuláře

```python
@app.route('/obrazek', methods=['POST'])
def zobraz_obrazek():
    cislo = request.form['cislo']
    ...
```

Funguje pro odeslání formuláře s polem pojmenovaným `cislo`.

## Sessions

```python
from flask import session

@app.route('/')
def prihlaseni():
    session['uzivatel'] = 'franta123'
    ...
```

## Různé pomůcky

### Získání URL dle názvu metody

```python
from flask import url_for

url_for('zobraz_obrazek')
```

### Přesměrování

```python
from flask import redirect

@app.route('/presmeruj_na_root')
def presmeruj_na_root():
    return redirect('http://root.cz')
```

### Chyby a HTTP kódy

```python
@app.errorhandler(404)
def nenalezeno():
    return render_template('nenalezeno.html'), 404
```
