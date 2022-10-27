import logging


class LRUCache:
    def __init__(self, limit=42):
        if limit <= 0:
            logging.error('LRUCache limit < 0')
            raise ValueError('LRUCache limit must be > 0')

        logging.info(f'Inicialized LRUCache with limit size={limit}')
        self.cache_size = limit
        self.values = {}
        self.priority = {}
        self.cur_time = 1

    def get(self, key):
        if key not in self.values.keys():
            logging.warning(f'LRUCache don\'t exist key {key}')
            return None

        self.set_priprity(key)
        return self.values[key]

    def set(self, key, value):
        logging.debug(f'Cache size={len(self.values.keys())} ' +
                      f'limit={self.cache_size}')

        if key in self.priority.keys():
            logging.warning(f'key {key} was added in LRUCache befor')

            self.set_priprity(key)

            logging.info(f'for key {key} change value ' +
                         f'{self.values[key]} --> {value}')

            self.values[key] = value

        else:
            if len(self.values) >= self.cache_size:
                key_with_min_priority = self.find_key_with_min_priority()

                logging.info(f'erase key {key_with_min_priority} ' +
                             'from LRUCache')

                self.priority.pop(key_with_min_priority, None)
                self.values.pop(key_with_min_priority, None)

            logging.info(f'for key {key} set value {value}')

            self.values[key] = value
            self.set_priprity(key)

    def set_priprity(self, key):
        logging.info(f'for key {key} set priority {self.cur_time}')

        self.priority[key] = self.cur_time
        self.cur_time += 1

    def find_key_with_min_priority(self):
        logging.debug(f'keys priority: {self.priority}')

        key_with_min_priority = None
        min_priority = 1e9

        for key in self.priority.keys():
            if self.priority[key] < min_priority:
                min_priority = self.priority[key]
                key_with_min_priority = key

        return key_with_min_priority


if __name__ == "__main__":
    logging.basicConfig(
        filename="cache.log",
        level=logging.DEBUG,
        format="%(asctime)s\t%(levelname)s\t%(message)s",
    )

    try:
        cache = LRUCache(-1)
    except ValueError:
        pass

    cache = LRUCache(2)
    cache.set("k1", "val1")
    cache.set("k2", "val2")
    result = cache.get("k3")
    result = cache.get("k2")
    result = cache.get("k1")
    cache.set("k1", "val3")
