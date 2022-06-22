#!/usr/bin/env python
import asyncio
from collections import Counter
import time

from argparse import ArgumentParser, Namespace
import httpx


def _parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("port", type=int)
    parser.add_argument("-n", "--num_clients", type=int, default=4)
    return parser.parse_args()


async def _make_request(id_: int, port: int) -> bool:
    start = time.time()
    try:
        async with httpx.AsyncClient() as client:
            url = f"http://localhost:{port}/resource"
            print(f"#{id_} Requesting {url}...")
            r = await client.get(url, timeout=7.0)
            print(f"#{id_} Response received:{r.json()}")
            return True
    except Exception as ex:
        print(f"#{id_}", type(ex), str(ex))
        return False
    finally:
        request_time = time.time() - start
        print(f"#{id_} Request time:{request_time:.2f}")


async def _run_clients(port: int, num_clients: int) -> None:
    clients = [_make_request(id_, port) for id_ in range(num_clients)]
    results = await asyncio.gather(*clients)
    counter = Counter(results)
    print(f"Successful:{counter[True]} Failed:{counter[False]}")


def main() -> None:
    args = _parse_args()
    asyncio.run(_run_clients(args.port, args.num_clients))


if __name__ == "__main__":
    main()

