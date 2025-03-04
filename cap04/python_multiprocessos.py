import datetime
import math
#import threading
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor

def main():
    qtd_cores = multiprocessing.cpu_count()
    #qtd_cores2 = int(qtd_cores/4)
    print(f'Realizando o processamento matemático com {qtd_cores} cores.')

    inicio = datetime.datetime.now()

    #computar(fim=50_000_000)
    #threads = []
    with ProcessPoolExecutor(max_workers=qtd_cores) as executor:
        for n in range(1, qtd_cores+1):
            ini = 50_000_000 *(n-1)/qtd_cores
            fim = 50_000_000 * n/qtd_cores
            print(f'Core {n} processados de {ini} até {fim}')
            executor.submit(computar, inicio=ini, fim=fim)
        
        
    tempo = datetime.datetime.now() - inicio

    print(f'O tempo de execução foi de {tempo.total_seconds():.2f} segundos.')

def computar(fim, inicio=1):
    pos = inicio
    fator = 1000*1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))

if __name__ == '__main__':
    main()


'''
sem threads: 6.36s
com threads: 10.31s
multiprocessos: 0.97s
 
'''   