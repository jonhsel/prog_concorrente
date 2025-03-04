import multiprocessing


def depositar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value + 1

def sacar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value - 1

def realizar_transacoes(saldo):
    p1 = multiprocessing.Process(target=depositar, args=(saldo,))
    p2 = multiprocessing.Process(target=sacar, args=(saldo,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    saldo = multiprocessing.Value('i', 100)

    print(f'Saldo inicial: {saldo.value}')

    for _ in range(10):
        realizar_transacoes(saldo)

    print(f'Saldo final: {saldo.value}')