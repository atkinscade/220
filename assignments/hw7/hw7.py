"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def open_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return lines

def save_file(file_name, results):
    with open(file_name, 'w') as f:
        for name in results:
            f.write(
                "{0}: {1}\n".format(name, results[name])
            )
def number_words(in_file):

    lines = open_file(in_file)
    line_list = []
    count = 1
    for line in lines:
        line = line.strip()
        line = line.split(' ')

    for i in line_list:

        print(count, i)
        count += 1

    return None
number_words('bob.txt')


def hourly_wages(in_file_name, out_file_name):
    pass


def calc_check_sum(isbn):
    count = 11
    num_list = []
    try:
        parse = isbn.split('-')
    except:
        parse = isbn
    for i in isbn:
        count -= 1
        result = i * count
        num_list.append(result)
    return print(sum(num_list))
#calc_check_sum('')

def send_message(file_name, friend_name):
    pass


def encode():
    pass


def send_safe_message(file_name, friend_name, key):
    pass


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
