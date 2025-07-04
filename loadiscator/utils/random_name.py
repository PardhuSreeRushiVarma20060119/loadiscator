import random
import string

def random_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length)) 