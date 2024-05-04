import random
import sys

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
    lines = code.strip().split('\n')
    num_lines = len(lines)
    mutate_index = random.randint(0, num_lines - 1)
    mutation = lines[mutate_index]
    
    # mutating a random line by reversing it
    mutated_line = mutation[::-1]
    lines[mutate_index] = mutated_line
    
    mutated_code = '\n'.join(lines)
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
        print("Merged code works:")
        print(merged_code)
        break
    else:
        print("Merged code failed. Mutating codes...")
        code1 = mutate_code(code1)
        code2 = mutate_code(code2)
        print("Code 1 after mutation:")
        print(code1)
        print("Code 2 after mutation:")
        print(code2)
