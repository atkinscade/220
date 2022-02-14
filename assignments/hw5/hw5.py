"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def name_reverse():
    name = input("Enter name (first last): ")
    name = list(name.partition(" "))
    print(name[2], ', ', name[1])



def company_name():
    domain = input("Domain name: ")
    domain.split(".")
    print(domain[2])

def initials():
    num_names = eval(input("How many students: "))
    for i in range(num_names):
        print("What's student", i+1, "'", "s name: ")
        name = input("")
        name.split(" ")
        print(name[0][:1], name[1][:1])



def names():
    list_names = input("List of students: ")
    for i in list_names:
        list_names.split()
        print(list_names[i][:1], list_names[i+1][:1])



def thirds():
    pass


def word_average():
    enlist = []
    sentence = input("Sentence: ")
    sentence = sentence.split()
    for i in sentence:
        enlist.append(len(i))
    avg = sum(enlist) / len(sentence)
    print(avg)


def pig_latin():
    sentence = input("sentence: ")
    sentence = sentence.split()
    for i in sentence:
        print(i[1:] + i[0] + "ay", end=" ")


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
