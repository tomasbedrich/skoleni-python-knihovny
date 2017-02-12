#!/usr/bin/env python3

import zmq

SERVER = 'tcp://127.0.0.1:6633'


def odesli_na_server(prispevek):
    with zmq.Context() as context:
        with context.socket(zmq.PUSH) as socket:
            socket.connect(SERVER)
            socket.send_string(prispevek)


if __name__ == '__main__':
    odesli_na_server('/ test komunikace /')
