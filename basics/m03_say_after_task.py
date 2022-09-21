import asyncio
import time

async def say_after(delay: int, what: str):
    print(f'called say_after("{what}")')
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f'started at {time.strftime("%X")}')

    await task1
    await task2

    print(f'finished at {time.strftime("%X")}')


if __name__ == '__main__':
    asyncio.run(main())

