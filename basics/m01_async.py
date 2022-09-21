import asyncio


# This is a corouting
async def greet():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')


if __name__ == '__main__':
    # .run receives a coroutine
    asyncio.run(greet())
    # calling task() won't perform the inner code
