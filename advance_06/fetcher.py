import aiohttp
import asyncio
import argparse
import time

WORKERS = 10


async def fetch_url(url, session):
    async with session.get(url) as resp:
        data = await resp.read()
        return len(data)


async def worker(queue, session, num):
    while True:
        url = await queue.get()

        try:
            await fetch_url(url, session)
        finally:
            queue.task_done()


async def fetch_batch_urls(queue, workers):
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(worker(queue, session, i))
            for i in range(workers)
        ]
        await queue.join()

        for task in tasks:
            task.cancel()


async def start(path_to_urls):
    urls_queue = asyncio.Queue()
    with open(path_to_urls) as f:
        urls = f.readlines()

    for url in urls:
        await urls_queue.put(url)

    await fetch_batch_urls(urls_queue, WORKERS)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", dest="count", default=10, type=int)
    parser.add_argument(dest="lst_urls", default='urls.txt', type=str)
    args = parser.parse_args()

    WORKERS = args.count

    t1 = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(start(args.lst_urls))
    print("time", time.time() - t1)
