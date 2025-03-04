import multiprocessing
import multiprocessing.pool

#def imprimir_nome_processo():
#    print (f'Iniciando o processo com nome {multiprocessing.current_process().name}')

def calcular(dado):
    return dado**2


def main():
    tamanho_pool = multiprocessing.cpu_count()*2

    print(f'Tamanho do Pool: {tamanho_pool}')

    pool = multiprocessing.Pool(processes=tamanho_pool)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f'Saídas: {saidas}')

    pool.close()
    pool.join()

if __name__ == '__main__':
    main()