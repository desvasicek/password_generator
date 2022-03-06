import string, random
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ["-", "_", "$"]
def make(length):
    password = ''
    for i in range(length):
        rand = random.randint(1, 2)
        if rand == 1:
            password += numbers[random.randint(0, len(numbers) -1)]
        elif rand == 2:
            password += letters[random.randint(0, len(letters) -1)]
    return password
def make_int(length):
    password = ''
    for i in range(length):
        password += numbers[random.randint(0, len(numbers) -1)]
    return password
def make_letter(length):
    password = ''
    for i in range(length):
        password += letters[random.randint(0, len(letters) -1)]
    return password
def make_special(length, chars):
    chars_list = list(chars)
    password = ''
    for i in range(length):
        password += chars_list[random.randint(0, len(chars_list) -1)]
    return password
