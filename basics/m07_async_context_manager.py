import asyncio
from contextlib import asynccontextmanager  # Since Python 3.7


async def greet():
    print('greet(): Hello ...')
    await asyncio.sleep(1)
    print('greet(): ... World!')


class Foo:
    async def __aenter__(self):
        print(f"aenter(): sleeping 1 sec...")
        await asyncio.sleep(1)  # Simulate blocking action
        print(f"aenter(): done")

    async def __aexit__(self, exc_type, exc_value, traceback):
        print(f"aexit(): sleeping 1 sec...")
        await asyncio.sleep(1)  # Simulate blocking action
        print(f"aexit(): done")


@asynccontextmanager
async def bar():
    print(f"bar() before: sleeping 1 sec...")
    await asyncio.sleep(1)  # Simulate blocking action
    print(f"bar() before: done")
    yield
    print(f"bar() after: sleeping 1 sec...")
    await asyncio.sleep(1)  # Simulate blocking action
    print(f"bar() after: done")


async def task():
    greet1 = asyncio.create_task(greet())
    async with Foo():
        pass
    await greet1
    greet2 = asyncio.create_task(greet())
    async with bar():
        pass
    await greet2


def main():
    asyncio.run(task())


if __name__ == "__main__":
    main()
