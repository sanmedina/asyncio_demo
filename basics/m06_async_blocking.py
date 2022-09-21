import asyncio


async def greet():
    print('Hello ...')
    await asyncio.sleep(1)  # blocking resource; database query, API call...
    print('... World!')


async def main():
    coroutines = []
    for _ in range(4):
        coroutines.append(greet())
    await asyncio.gather(*coroutines)


if __name__ == '__main__':
    asyncio.run(main())
