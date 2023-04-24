#
# Simple Tick Data Collector
#
import zmq
import pandas as pd

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:5555')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

ticks = pd.DataFrame()

while True:
    MSG = socket.recv_pyobj()
    print(MSG)
    df = pd.DataFrame(MSG, index=[0])
    ticks = ticks.append(df)
