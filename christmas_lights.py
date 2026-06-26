#!/usr/bin/env python

from kitsat import Modem
from time import sleep
from queue import Empty

def main():
    m = Modem()
    m.connect("COM5")

    networkid = 1
    amt_of_cycles = 10

    m.write('ping_local')
    sleep(0.2)

    try:
        resp = m.read()
    except Empty:
        print("Sem resposta ao 'ping_local' (timeout).")
        m.disconnect()
        return

    if len(resp) > 4 and resp[4] == '0':
        m.write(f'gs_set_network {networkid}')

    lights_array = [[1, 4, 2], [2, 1, 4], [4, 2, 1]]

    for _ in range(amt_of_cycles):
        for i in range(3):
            for j in range(3):
                m.write(f'led_on {j+1} {lights_array[j][i]}')
                sleep(0.03)
            sleep(1)

    m.write('led_off 0')
    sleep(0.1)
    m.disconnect()

if __name__ == "__main__":
    main()
