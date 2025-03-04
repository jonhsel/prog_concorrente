#from concurrent.futures.thread import ThreadPoolExecutor as Executor
from concurrent.futures.process import ProcessPoolExecutor as Executor
import time

def processar():
    print('[', end='', flush=True) #flush é para não esperar, para ir processando
    for _ in range(1,11):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', end='', flush=True)

if __name__ == '__main__':
    
    with Executor() as executor:
        future = executor.submit(processar)