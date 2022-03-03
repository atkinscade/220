def main():
    def weighted_average(in_file):
        open_file = open(in_file)
        read_file = open_file.read()
        lines = read_file.splitlines()
        name_list = []
        num_list = []
        for i in lines:
            parse = i.split(': ')
            name_list.append(parse[:1])
            num_list.append(parse[1:])
        num_dict = {}
        for key in name_list:
            for val in num_list:
                num_dict[str(key)] = val
                num_list.remove(val)
                break
        count = 0
        for values, keys in num_dict.items():
            key_parse = str(keys).split(" ")
            key_length = len(key_parse)
            iter_length = key_length // 2
            for i in range(iter_length):
                for j in key_parse:
                    var_result = j[0 + count]
                    count += (1 * 2)
                    print(key_parse)
                    print(var_result)


    weighted_average('test_file')


main()
