#!/usr/bin/env python
import asyncio
from collections import Counter
import time
import traceback

from argparse import ArgumentParser, Namespace
import httpx


def _parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("port", type=int)
    parser.add_argument("-n", "--num_clients", type=int, default=4)
    return parser.parse_args()


async def _make_request(port: int) -> bool:
    try:
        async with httpx.AsyncClient() as client:
            url = f"http://localhost:{port}/resource"
            print(f"Requesting {url}...")
            start = time.time()
            r = await client.get(url, timeout=7.0)
            end = time.time()
            request_time = end - start
            print(f"Response received:{r.json()}")
            print(f"Request time:{request_time:.2f}")
            return True
    except Exception:
        traceback.print_exc()
        traceback.print_stack()
        return False


async def _run_clients(port: int, num_clients: int) -> None:
    clients = [_make_request(port) for _ in range(num_clients)]
    results = await asyncio.gather(*clients)
    counter = Counter(results)
    print(f"Successful:{counter[True]} Failed:{counter[False]}")


def main() -> None:
    args = _parse_args()
    asyncio.run(_run_clients(args.port, args.num_clients))


if __name__ == "__main__":
    main()

