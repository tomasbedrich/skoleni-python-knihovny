# Logging

```python
import logging
```

Základní konfigurace + vytvoření loggeru:

```python
logging.basicConfig()
logger = logging.getLogger('nazev_balicku')
```

## Logování

```python
logger.debug('Dělám operaci X.')
logger.info('Operace X provedena.')
logger.warning('Operace X nemohla být provedena kvůli špatnému vstupu.')
logger.error('Provádění operace X selhalo.')
logger.critical('OMG WTF!')

try:
   raise ValueError('špatná hodnota')
except ValueError:
    log.exception('Nepovedlo se...')
```
