"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def cash_converter():
    money_int = eval(input("Input an integer: "))
    print(f"That is ${money_int}.00")



def encode():
    encode_list = []
    msg = input("enter a code: ")
    key = eval(input("input a key integer: "))
    for i in msg:
        i = ord(i) + key
        encode_list.append(i)
    for i in encode_list:
        print(chr(i), end="")
encode()



def sphere_area(radius):
    pass


def sphere_volume(radius):
    pass


def sum_n(number):
    pass


def sum_n_cubes(number):
    pass


def encode_better():
    pass


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass

def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext