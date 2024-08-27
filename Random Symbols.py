import random
import string

def generate_random_code():
    code_length = random.randint(50, 100)
    random_code = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=code_length))
    return random_code

random_python_code = generate_random_code()
print(random_python_code)
exec(random_python_code)
