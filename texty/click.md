# Click

## Základ

```python
@click.command()
def stekni():
    '''Štěkne'''
    print('Haf')
```

Pak stačí běžně zavolat:

```python
if __name__ == '__main__':
    stekni()
```

Spuštění:

- `program.py`
- `program.py -h`
- `program.py --help`

## Parametry

```python
@click.command()
@click.option('-p', '--pocet', required=True, type=int, default=1, help='Kolkrát mám štěknout')
def stekni(pocet):
    print('Haf ' * pocet)
```

Spuštění:

- `program.py -p 3`
- `program.py --pocet 3`

## Argumenty

```python
@click.command()
@click.argument('predpona', nargs=1, type=str)
@click.argument('soubory', nargs=-1, type=click.File('r'))
def vypis(predpona, soubory):
    for s in soubory:
        print(predpona, s.read())
```

Spuštění:

- `program.py "vypisuji:" requirements.txt`

## Více příkazů

```python
@click.group()
def main():
    '''Program simuluje farmu'''
    pass

@main.command()
def stekni():
    '''Štěkne'''
    print('Haf')

@main.command()
def mnoukni():
    '''Mňoukne'''
    print('Mňau')

if __name__ == '__main__':
    main()
```

Spuštění:

- `program.py stekni`
- `program.py mnoukni`
- `program.py --help`

## Doplňkové možnosti

### Vstup

```python
click.prompt('Zadejte číslo', type=int)
```

### Potvrzení

```python
click.confirm('Opravdu smazat?', abort=True, default=True)
```

## Otevření aplikace / URL

```python
click.launch('http://root.cz')
```
