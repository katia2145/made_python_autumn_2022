import json
import time
import math
from functools import wraps

statictics = {}
work_time = []

def get_mean(lst):
    cum_sum = 0
    for elm in lst:
        cum_sum += elm
    
    return cum_sum / len(lst)


def timer(k):
    def _timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            start_timer = time.time()

            res = func(*args, **kwargs)
            
            end_timer = time.time()
            
            work_time.append(end_timer - start_timer)
            cnt = min(0, len(work_time) - k)
            mean_time = get_mean(work_time[cnt:])
            print(f'Mean time work of last {k} = {mean_time}')
            
            return mean_time
        return wrapper
    return _timer


@timer(10)
def parse_json(json_str: str, keyword_callback, required_fields=None, keywords=None):
    json_dict = json.loads(json_str)
    for field in required_fields:
        if field in json_dict.keys():
            for word in json_dict[field].split(' '):
                if word in keywords:
                    keyword_callback(word)
                    

def calculate_statistics(word):
    if word in statictics.keys():
        statictics[word] += 1
    else:
        statictics[word] = 1
    # time.sleep(0.5)


json_str = '{"key1": "word1 word2", "key2": "word2 word3"}'
assert math.isclose(parse_json(json_str, calculate_statistics, required_fields=["key1"], keywords=["word1"]), 0)

json_str = '{"key1": "Word1 word2 word2 word2 word2", "key2": "word2 word3"}'
assert math.isclose(parse_json(json_str, calculate_statistics, required_fields=["key1"], keywords=["word2"]), 0)

json_str = '''{"key0": "word0 word1 word2 word3 word4", 
                "key1": "word0 word1 word2 word3 word4", 
                "key2": "word0 word1 word2 word3 word4", 
                "key3": "word0 word1 word2 word3 word4", 
                "key4": "word0 word1 word2 word3 word4"}'''

required_fields=['key1', 'key2', 'key3', 'key4']
keywords=['word1', 'word2', 'word3', 'word4']

assert math.isclose(parse_json(json_str, calculate_statistics, required_fields, keywords), 0)

required_fields = ['key1', 'key2', 'key3', 'key4']
keywords = ['word1', 'word2', 'word3', 'word4']

for test_number in range(20):
    assert math.isclose(parse_json(json_str, calculate_statistics, required_fields, keywords), 0)
