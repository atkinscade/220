# def encode(word):
#     enlist = []
#     for letter in word:
#         enlist.append(ord(letter))
#     return enlist
#
# def decode(num):
#     unlist = []
#     for numbers in num:
#         unlist.append(eval(numbers))
#     print(unlist)
#     return unlist
#


halls_food = ['steak', 'fries', 'potatos', 'drinks']
gilroys_food = ['pizza', 'cheese', 'drinks', 'calzone']
five_guys_food = ['burger', 'peanuts', 'fries', 'drink']
resteraunts = {
    'resteraunt': 'food/dishes',
    'halls': halls_food,
    'gilroys': gilroys_food,
    '5 guys': five_guys_food
}


def find_all(val_list, value):
    count = 0
    out_list = []
    for i in val_list:
        count += 1
        if value == i:
            out_list.append(count - 1)
    return out_list



