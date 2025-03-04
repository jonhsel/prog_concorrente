import asyncio
import aiofiles

async def exemplo_arq1():
    async with aiofiles.open('texto.txt') as arquivo:
        conteudo = await arquivo.read()
    print(conteudo)

async def exemplo_arq2():
    async with aiofiles.open('texto.txt') as arquivo:
        async for linha in arquivo:
            print(linha)

def main():

    el = asyncio.get_event_loop()

    print('Funcão 1')
    el.run_until_complete(exemplo_arq1())

    print('função 2')
    el.run_until_complete(exemplo_arq2())

    el.close()
    
if __name__ == '__main__':
    main()