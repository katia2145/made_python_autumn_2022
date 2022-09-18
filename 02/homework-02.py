import math

eps = 1e-10


def close_to_zero(lst):
    if not (isinstance(lst, list) or isinstance(lst, tuple)):
        return None

    more_close = max(lst)
    more_close_lst = []

    for elm in lst:
        if abs(elm) - more_close < -eps:
            more_close = elm
            more_close_lst = [elm]
            continue

        if math.isclose(abs(elm), abs(more_close)):
            more_close_lst.append(elm)

    return more_close_lst


def merge(lst1, lst2):
    answer = set()
    lst1 = set(lst1)

    for elm in lst2:
        if elm in lst1 and not elm in answer:
            answer.add(elm)

    return list(answer)


def check_answer(correct_answer, answer):
    assert len(correct_answer) == len(answer)

    for i in range(len(answer)):
        assert math.isclose(answer[i], correct_answer[i])


assert close_to_zero([-5, 9, 6, -8]) == [-5]
assert close_to_zero((15, 9, 10, -6, 8, -6)) == [-6, -6]
assert close_to_zero([-1, 2, -5, 1, -1]) == [-1, 1, -1]

correct_answer = [0.3, 0.3, -0.3]
answer = close_to_zero([4, 19, 0.3, 18.6, 0.3, 0.7, -0.3])
check_answer(correct_answer, answer)

correct_answer = [0.3, 0.3, -0.3]
answer = close_to_zero([4, 19, 0.3, 18.6, 0.3, 0.7, -0.3])
check_answer(correct_answer, answer)


lst = [1, 1, 2, 5, 7]
tp = (1, 1, 2, 3, 4, 7)
res = merge(lst, tp)
assert res == [1, 2, 7]

lst = [1, 2, 3, 4]
tp = (6, 7, 8)
res = merge(lst, tp)
assert res == []

lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 3, 4]
res = merge(lst1, lst2)
assert res == [1, 2, 3, 4]

lst1 = [1.3, 2.3, 3.3, 4.3]
lst2 = [1.3, 2.3, 3.3, 4.3]
res = merge(lst1, lst2)
assert res == [1.3, 2.3, 3.3, 4.3]
