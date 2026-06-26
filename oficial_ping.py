from kitsat import Modem
from time import sleep
from queue import Empty

def main():
    m = Modem()
    m.connect("COM5")

    networkid = 1

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

    m.write('ping')
    sleep(0.2)

    try:
        print(m.read())
    except Empty:
        print("Sem resposta ao 'ping' (timeout).")

    m.disconnect()

if __name__ == "__main__":
    main()
