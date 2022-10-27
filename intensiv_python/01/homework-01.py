import math
eps = 1e-10

def roots_of_quadratic_equation(a, b, c):
    if (not (isinstance(a, int) or isinstance(a, float)) or
        not (isinstance(b, int) or isinstance(a, float)) or
        not (isinstance(c, int) or isinstance(a, float))):
        return None
    
    if math.isclose(a, 0):
        return None
    
    D = b**2 - 4*a*c
    
    if math.isclose(D, 0):
        x1 = -b / 2*a
        return x1
    
    if D > -eps:
        x1 = (-b + math.sqrt(D)) / 2*a
        x2 = (-b - math.sqrt(D)) / 2*a
        return x1, x2
    
    D *= -1
    x1 = complex(-b, math.sqrt(D)) / 2*a
    x2 = complex(-b, -math.sqrt(D)) / 2*a
    return x1, x2



def divide_list_into_even_odd(lst):
    if not isinstance(lst, list):
        return None
    
    even, odd = [], []

    for elm in lst:
        if not isinstance(elm, int):
            return None 
        even.append(elm) if elm % 2 == 0 else odd.append(elm)
    
    return even, odd



assert roots_of_quadratic_equation(0, 1, 2)   == None
assert roots_of_quadratic_equation('2', 1, 2) == None
assert roots_of_quadratic_equation(2, '1', 2) == None
assert roots_of_quadratic_equation(2, 1, '2') == None
assert roots_of_quadratic_equation(1, -2, -3) == (3.0, -1.0)
assert roots_of_quadratic_equation(1.0, -2.0, -3.0) == (3.0, -1.0)
assert roots_of_quadratic_equation(16, 8, 1)  == -64.0
assert roots_of_quadratic_equation(2, 4, 4)   == ((-4+4j), (-4-4j))



assert divide_list_into_even_odd(1) == None
assert divide_list_into_even_odd(['a', 'b', 'c']) == None

lst = [i for i in range(10)]
assert divide_list_into_even_odd(lst) == ([i for i in range(0, 10, 2)], [i for i in range(1, 10, 2)])

lst = [i for i in range(0, 10, 2)]
assert divide_list_into_even_odd(lst) == (lst, [])

lst = [i for i in range(1, 10, 2)]
assert divide_list_into_even_odd(lst) == ([], lst)

assert divide_list_into_even_odd([]) == ([], [])
