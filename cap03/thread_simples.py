import threading
import time

def main():
    th = threading.Thread(target=contar, args=('elefante', 10))

    th.start()#adiciona nossa thread num pool de threads, pronto para execução

    print('Podemos fazer outras coisas aqui')
    print('Jonh Selmo' * 2)

    th.join() #avisa para ficar aguardando aqui até a thread terminar a execução

    print('Pronto')

def contar(o_que, numero):
    for n in range(1, numero+1):
        print(f'{n} {o_que}s ...')
        time.sleep(1)

if __name__=='__main__':
    main()