import sys
from collections import deque
import logging.config
import logging
import argparse


LOGG_CONFIG = {
    'version': 1,
    'formatters': {
        'command_line': {
            'format': '[%(levelname)s] - %(message)s',
        },
        'log_file': {
            'format': '%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s',
        }
    },
    'handlers': {
        'log_file': {
            'filename': 'cache.log',
            'class': 'logging.FileHandler',
            'formatter': 'log_file',
        },
        'command_line': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'command_line',
        }
    },
    'loggers': {
        'command_line': {
            'level': 'INFO',
            'handlers': ['command_line'],
        },
        'logger_file': {
            'level': 'INFO',
            'handlers': ['log_file'],
        }
    },
}


class LenFilter(logging.Filter):
    def filter(self, record):
        return len(record.getMessage()) < 5


class LRUCache:
    def __init__(self, logger: logging.Logger, limit=42):
        self.limit = limit
        self.deq = deque()
        self.dct = {}
        self.logger = logger

    def get(self, key):
        if key in self.dct:
            last = self.deq.pop()
            if last != key:
                self.deq.remove(key)
                self.deq.append(last)
                self.logger.info(f'key: {key} is not last: {last}')
            self.deq.append(key)
            self.logger.info(f'for key: {key} found value: {self.dct[key]}')
            return self.dct[key]
        self.logger.error(f'key: {key} not in lru')
        return None

    def set(self, key, value):
        if self.get(key) is not None:
            self.dct[key] = value
            return

        if len(self.deq) == self.limit:
            delete_key = self.deq.popleft()
            self.logger.info(f'for set [key: {key} value: {value}] reach limit: {self.limit}; key: {delete_key} remove')
            del self.dct[delete_key]
            self.logger.debug(f'removed in dict (expected False): {delete_key in self.dct}')
        self.deq.append(key)
        self.dct[key] = value
        self.logger.info(f'set [key: {key} value: {value}]: len lru cache: {len(self.deq)}; limit: {self.limit}')


if __name__ == '__main__':
    # Парсер аргументов
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--stdout',
                        action=argparse.BooleanOptionalAction)
    parser.add_argument('-f', '--filter',
                        action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    stdout = args.stdout
    filter_ = args.filter

    # Инициализация логгеров
    logging.config.dictConfig(LOGG_CONFIG)
    logger = logging.getLogger('logger_file')
    if stdout:
        logger.addHandler(
            logging.getLogger('command_line').handlers[0]
        )
    if filter_:
        logger.addFilter(LenFilter())

    # запись в LRUCache
    cache = LRUCache(logger=logger, limit=2)
    cache.set('k1', 'val1')  # set отсутствующего ключа
    cache.set('k2', 'val2')  # set отсутствующего ключа
    cache.set('k3', 'val3')  # set отсутствующего ключа, когда достигнута ёмкость
    k1_value = cache.get('k1')  # get существующего ключа
    k2_value = cache.get('k2')  # get существующего ключа
    not_found_value = cache.get('k5')  # get отсутствующего ключа

