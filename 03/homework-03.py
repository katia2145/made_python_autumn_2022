import json
import time
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
        print("timer")
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
    time.sleep(0.5)


json_str = '{"key1": "word1 word2", "key2": "word2 word3"}'
parse_json(json_str, calculate_statistics, required_fields=["key1"], keywords=["word1"])

json_str = '{"key1": "Word1 word2 word2 word2 word2", "key2": "word2 word3"}'
parse_json(json_str, calculate_statistics, required_fields=["key1"], keywords=["word2"])

# json_str = '\'{'
# required_fields = []
# keywords = []

# for key_number in range(5):
#         required_fields.append('key' + str(key_number))
#         json_str += '"key' + str(key_number) + '": "'
#         for word_number in range(5):
#             if key_number == 0:
#                 keywords.append('word' + str(word_number))
#             json_str += 'word' + str(word_number)
#             json_str += (' ' if word_number != 4 else '')   

#         json_str += ('", ' if key_number != 4 else '"')

# json_str += '}\''
# print(required_fields)
# print(keywords)
# print(json_str)

for test_number in range(50):
    parse_json(json_str, calculate_statistics, required_fields = ["key1"], keywords = ["word1"])
