import random
import sys
import ast
import astor

def merge_code(code1, code2):
    merged_code = ''
    lines1 = code1.strip().split('\n')
    lines2 = code2.strip().split('\n')
    max_lines = max(len(lines1), len(lines2))
    
    for i in range(max_lines):
        if i < len(lines1):
            merged_code += lines1[i] + '\n'
        if i < len(lines2):
            merged_code += lines2[i] + '\n'
    
    return merged_code

def test_code(exec_code):
    try:
        exec(exec_code)
        return True
    except Exception as e:
        return False

def mutate_code(code):
    tree = ast.parse(code)
    elements = [node for node in ast.walk(tree)]
    element_to_mutate = random.choice(elements)
    
    # Стратегии мутации могут быть более сложными, чем эта, но для простоты я просто отменю литералы или заменю на 0
    if isinstance(element_to_mutate, ast.Constant):
        if isinstance(element_to_mutate.value, bool):
            mutated_value = not element_to_mutate.value
        elif isinstance(element_to_mutate.value, int):
            mutated_value = -element_to_mutate.value
        else:
            mutated_value = 0
        element_to_mutate.value = mutated_value
    elif isinstance(element_to_mutate, ast.BinOp):
        if isinstance(element_to_mutate.op, ast.Add):
            element_to_mutate.op = ast.Sub()
        elif isinstance(element_to_mutate.op, ast.Sub):
            element_to_mutate.op = ast.Add()
        elif isinstance(element_to_mutate.op, ast.Mult):
            element_to_mutate.op = ast.Div()
        elif isinstance(element_to_mutate.op, ast.Div):
            element_to_mutate.op = ast.Mult()
    
    mutated_code = astor.to_source(tree)
    return mutated_code

code1 = """class Number:
    def __init__(self, number):
        self.number = number
    
    def __truediv__(self, other):
        if other == 0:
            return "на ноль делить нельзя"
        return self.number / other

num = Number(10)
result1 = num / 2
result2 = num / 0
print(result1)
print(result2)"""

code2 = """def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

a = list(map(int,input().split()))
print(*filter_lst(a))
print(*filter_lst(a,lambda x: x if x < 0 else False))
print(*filter_lst(a,lambda x: x >= 0))
print(*filter_lst(a,lambda x: x >= 3 and x <= 5))"""

while True:
    merged_code = merge_code(code1, code2)
    if test_code(merged_code):
        print("Объединенный код работает:")
        print(merged_code)
        break
    else:
        print("Ошибка в объединенном коде. Изменяющиеся коды...")
        code1 = mutate_code(code1)
        code2 = mutate_code(code2)
        print("Код 1 после мутации:")
        print(code1)
        print("Код 2 после мутации:")
        print(code2)
