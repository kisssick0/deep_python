import aiohttp
import asyncio
import argparse
import json
from bs4 import BeautifulSoup
from collections import Counter


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('filename', type=str, default="urls.txt", help='urls filename')
    parser.add_argument('-c', '--connections_count', type=int, default=10, help='number of requests')

    args = parser.parse_args()
    return args.filename, args.connections_count


async def fetch_and_process(url, session, top_words_count=3):
    try:
        async with session.get(url) as response:
            text = await response.text()
            return process_text(url, text, top_words_count)
    except aiohttp.ClientConnectorError:
        return ""


def process_text(url, text, top_words_count):
    filtered_text = BeautifulSoup(text, 'html.parser').get_text()
    words = filtered_text.split()
    most_common_words = Counter(words).most_common(top_words_count)

    if not most_common_words:
        return ""

    result_json = json.dumps({word: count for word, count in most_common_words})
    return f"{url}: {result_json}"


async def process_queue(queue, session, top_words_count=3):
    while True:
        url = await queue.get()
        result = await fetch_and_process(url, session, top_words_count)
        print(result)
        queue.task_done()


async def main(filename, connections_count):
    async with aiohttp.ClientSession() as session:
        queue = asyncio.Queue()

        workers = [
            asyncio.create_task(process_queue(queue, session))
            for _ in range(connections_count)
        ]

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for url in map(str.strip, file):
                    await queue.put(url)

            await queue.join()
        except FileNotFoundError:
            print('File not found')
        finally:
            for worker in workers:
                worker.cancel()

if __name__ == '__main__':
    url_filename, num_connections = parse_arguments()
    asyncio.run(main(url_filename, num_connections))
