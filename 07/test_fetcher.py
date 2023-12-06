import json
import unittest
from unittest.mock import patch, call, mock_open
import aiohttp

from fetcher import process_text, fetch_and_process, main


class TestFetcher(unittest.IsolatedAsyncioTestCase):
    async def test_main(self):
        filename = 'test_urls.txt'
        num_connections = 2
        urls = ['http://example.com', 'http://example.org']

        with patch(
                'builtins.open',
                new=mock_open(read_data='\n'.join(urls)),
                create=True
        ) as _:
            with patch("builtins.print") as mock_print:
                with patch('fetcher.fetch_and_process') as mock_fetch_and_process:
                    mock_fetch_and_process.side_effect = [
                        'http://example.com: a lot of words',
                        'http://example.org: a lot of words'
                    ]

                    await main(filename, num_connections)

        self.assertEqual(mock_fetch_and_process.call_count, 2)

        print_expected_calls = [
            call('http://example.com: a lot of words'),
            call('http://example.org: a lot of words')
        ]
        self.assertEqual(mock_print.mock_calls, print_expected_calls)

    async def test_process_text(self):
        url = 'http://example.com'
        text = '<html><body>Some text</body></html>'
        top_words_count = 3

        result = process_text(url, text, top_words_count=3)
        self.assertEqual(result, f"{url}: {json.dumps({'Some': 1, 'text': 1})}")

        url = "http://example.com"
        async with aiohttp.ClientSession() as session:
            result = await fetch_and_process(url, session, top_words_count)

        expected_result = f"{url}: {json.dumps({'in': 3, 'Example': 2, 'Domain': 2})}"
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
