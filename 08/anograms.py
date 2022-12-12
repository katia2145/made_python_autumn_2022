from typing import List
from collections import defaultdict


def check_pattern(cnt_errors):
    return cnt_errors == 0


def def_value():
    return 0


def find_anagrams(text: str, pattern: str) -> List[int]:
    if text == '' or pattern == '':
        return []
    pos = []
    frequancy_pattern = defaultdict(def_value)
    frequancy_text = defaultdict(def_value)

    for letter in pattern:
        frequancy_pattern[letter] += 1
    begin_window, end_window = 0, 0
    cnt_errors = 0

    while end_window < len(pattern):
        letter = text[end_window]
        frequancy_text[letter] += 1
        if frequancy_text[letter] > frequancy_pattern[letter]:
            cnt_errors += 1
        end_window += 1

    if check_pattern(cnt_errors):
        pos.append(begin_window)

    while end_window < len(text):
        letter = text[begin_window]
        frequancy_text[letter] -= 1
        begin_window += 1

        if frequancy_text[letter] == frequancy_pattern[letter]:
            cnt_errors -= 1

        letter = text[end_window]
        frequancy_text[letter] += 1
        end_window += 1

        if frequancy_text[letter] != frequancy_pattern[letter]:
            cnt_errors += 1

        if check_pattern(cnt_errors):
            pos.append(begin_window)
    return pos
