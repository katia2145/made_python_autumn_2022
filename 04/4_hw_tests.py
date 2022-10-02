from CustomList import CustomList

# проверка сложения, вычитания CustomList с CustomList
l1 = CustomList([1, 2, 3])
l2 = CustomList([2, 3, 4])
assert (l1 + l2) == CustomList([3, 5, 7])
assert (l1 - l2) == CustomList([-1, -1, -1])

l1 = CustomList([1, 2, 3, 4, 5])
l2 = CustomList([2, 3, 4])
assert (l1 + l2) == CustomList([3, 5, 7, 4, 5])
assert l1 == CustomList([1, 2, 3, 4, 5])
assert l2 == CustomList([2, 3, 4])

assert (l2 + l1) == CustomList([3, 5, 7, 4, 5])
assert l1 == CustomList([1, 2, 3, 4, 5])
assert l2 == CustomList([2, 3, 4])

assert (l1 - l2) == CustomList([-1, -1, -1, 4, 5])
assert l1 == CustomList([1, 2, 3, 4, 5])
assert l2 == CustomList([2, 3, 4])

assert (l2 - l1) == CustomList([1, 1, 1, -4, -5])
assert l1 == CustomList([1, 2, 3, 4, 5])
assert l2 == CustomList([2, 3, 4])

assert isinstance((l1 + l2), CustomList)
assert isinstance((l1 - l2), CustomList)

# проверка сложения, вычитания CustomList с list
l1 = CustomList([1, 2, 3])
l2 = [2, 3, 4]
assert (l1 + l2) == CustomList([3, 5, 7])
assert (l2 + l1) == CustomList([3, 5, 7])
assert (l1 - l2) == CustomList([-1, -1, -1])
assert (l2 - l1) == CustomList([1, 1, 1])

l1 = CustomList([1, 2, 3, 4, 5])
l2 = [2, 3, 4]
assert (l1 + l2) == CustomList([3, 5, 7, 4, 5])
assert l1 == CustomList([1, 2, 3, 4, 5])
assert l2 == [2, 3, 4]

assert (l2 + l1) == CustomList([3, 5, 7, 4, 5])
assert l1 == CustomList([1, 2, 3, 4, 5])
assert l2 == [2, 3, 4]

assert (l1 - l2) == CustomList([-1, -1, -1, 4, 5])
assert l1 == CustomList([1, 2, 3, 4, 5])
assert l2 == [2, 3, 4]

assert (l2 - l1) == CustomList([1, 1, 1, -4, -5])
assert l1 == CustomList([1, 2, 3, 4, 5])
assert l2 == [2, 3, 4]

assert isinstance((l1 + l2), CustomList)
assert isinstance((l1 - l2), CustomList)

# проверка на операции не с list CustomList
l1 = CustomList([1, 2, 3, 4, 5])
l2 = 1
try:
    l1 + l2
except TypeError:
    pass

try:
    l2 + l1
except TypeError:
    pass

try:
    l1 - l2
except TypeError:
    pass

try:
    l1 < l2
except TypeError:
    pass

try:
    l1 > l2
except TypeError:
    pass

try:
    l1 <= l2
except TypeError:
    pass

try:
    l1 >= l2
except TypeError:
    pass

try:
    l1 == l2
except TypeError:
    pass

try:
    l1 != l2
except TypeError:
    pass

# проверка операторов сравнения
l1 = CustomList([1, 2, 3])
l2 = CustomList([2, 3, 4])
assert (l1 < l2) is True
assert (l2 < l1) is False

assert (l1 > l2) is False
assert (l2 > l1) is True

assert (l1 <= l2) is True
assert (l2 <= l1) is False

assert (l1 >= l2) is False
assert (l2 >= l1) is True

l1 = CustomList([1, 2, 3])
l2 = CustomList([2, 3, 4])
assert (l1 == l2) is False

l1 = CustomList([1, 2, 3])
l2 = CustomList([2, 2, 2])
assert (l2 == l1) is True

l1 = CustomList([1, 2, 3])
l2 = CustomList([2, 3, 4])
assert (l1 != l2) is True

l1 = CustomList([1, 2, 3])
l2 = CustomList([3, 2, 1])
assert (l2 != l1) is False

assert str(l1) == "CustomList = [1, 2, 3]\nsum = 6"
