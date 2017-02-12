#!/usr/bin/env python3

import zmq

with zmq.Context() as context:
    with context.socket(zmq.PULL) as socket:

        socket.bind('tcp://*:6633')
        print('posloucham...')

        while True:
            prispevek = socket.recv_string()
            print(prispevek)
