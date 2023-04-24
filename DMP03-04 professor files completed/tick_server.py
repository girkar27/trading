#
# Simple Tick Data Server
#
import zmq
import time
import random
import datetime

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:5555')

SYM = 'AAPL'
PRICE = 100.

while True:
    PRICE += random.gauss(0, 1) / 2
    TIME = str(datetime.datetime.now())
    MSG = {'time': TIME, 'symbol': SYM, 'price': PRICE}
    socket.send_pyobj(MSG)
    print(f'{TIME} | {PRICE}')
    time.sleep(random.random() * 2)
