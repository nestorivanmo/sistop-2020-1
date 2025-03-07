#!/usr/bin/python3
from time import sleep
from random import randint

from threading import Semaphore, Thread

multi = Semaphore(5)
vivos = []
m_vivos = Semaphore(1)

def a_darle(id):
    global vivos, multi
    print("Hilo %d listo!" % id)
    # El uso de "with" es azucar sintactico
    #
    # El uso de "with multi" es igual a decir, al inicio del bloque,
    # "multi.acquire()", y al final del bloque, "multi.release()"
    with multi:
        with m_vivos:
            vivos.append(id)
            print("Soy %d. Estamos dentro: %s" % (id, vivos))

        sleep(randint(0,5))
        print("%d fuera!" % id)

        with m_vivos:
            vivos.remove(id)

for i in range(20):
    Thread(target=a_darle, args=[i]).start()
