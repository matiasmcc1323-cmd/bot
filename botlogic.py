import random
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890"
    password = ""
    
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def flip_a_coin():
    coin = random.randint(1, 2)
    if coin == 1:
        return("The coin landed on heads!")
    elif coin == 2:
        return("The coin landed on tails!")

def random_number(max_number):
    number = random.randint(1,max_number)
    return(number)
