import asyncio


async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')


async def main():
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second to let task start
    print('main(): Waiting 1 sec...')
    await asyncio.sleep(1)
    print('main(): Sleep done')

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print('main(): cancel_me is cancelled now')


if __name__ == '__main__':
    asyncio.run(main())
