import threading
import time

def main():
    threads = [
    threading.Thread(target=contar, args=('elefante', 10)), #2
    threading.Thread(target=contar, args=('zebra', 8)),
    threading.Thread(target=contar, args=('antilope', 12)),
    threading.Thread(target=contar, args=('leopardo', 18))
    ]

    #th.start() # coloco a thread no poll de threads prontas #3
    [th.start() for th in threads] #list compreenstion

    print('Digitando o código')
    print('Jonh Selmo')

    #th.join() #avisa o sistema para ficar aguardando até a thread terminar a execução #4
    [th.join() for th in threads]

    print('Pronto, finalizou!')

def contar(o_que, numero):
    for n in range(1, numero+1):
        print(f'{n}  {o_que}s')
        time.sleep(1)

if __name__ == '__main__':
    main()