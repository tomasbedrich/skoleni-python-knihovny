# Requests

## Základy

### GET

```python
response = requests.get('http://httpbin.org/get')
response.encoding = 'utf-8'
response.text
response.status_code
response.json()
```

### POST

```python
requests.post('http://httpbin.org/post')
```

### URL parametry

```python
requests.get('http://httpbin.org/get', params={'klic': 'hodnota'})
```

### POST data

```python
requests.post('http://httpbin.org/post', data={'klic': 'hodnota'})
```

## Pokročilejší

### Session

```python
session = requests.Session()
session.get('http://httpbin.org/cookies/set?name=value')
```

### Chyby

```python
try:
    response = requests.post('http://httpbin.org/status/401')
    response.raise_for_status()
except requests.exceptions.RequestException:
    ...
```

### Timeout

```python
requests.get('http://httpbin.org/headers', timeout=3)
```
