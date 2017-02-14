# PyZMQ

```python
import zmq
```

Typy socketů:

- PAIR (1 - 1)
- REQ/REP (1 - 1..N)
- PUB/SUB (M - N)
- PUSH/PULL (producent/konzument) (M - N)

## Odesílání

```python
with zmq.Context() as context:
    with context.socket(zmq.PUB) as socket:

        socket.bind('tcp://*:1234')
        socket.send(b'ahoj')
```

### Co lze posílat

```python
socket.send_string('ahoj česky!')
socket.send_json({'moje': 'data', 'cislo': 1})
```

## Přijímání

```python
with zmq.Context() as context:
    with context.socket(zmq.SUB) as socket:

        socket.connect('tcp://localhost:1234')
        socket.recv()
        socket.recv_string()
        socket.recv_json()
```
