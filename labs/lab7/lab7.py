def equation(grades, weights):
    items = zip(
        weights, grades
    )
    item_sum = 0
    for item in items:
        item_sum += item[0] * item[1]
    return item_sum / 100


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


def check_weights(weights):
    return sum(weights) == 100


def weighted_average(infile_name, outfile_name):
    lines = open_file(infile_name)
    results = (
        dict()
    )
    overall_grades = (
        []
    )
    for line in lines:
        line = (
            line.strip()
        )
        line = line.split(": ")
        name = line[0]
        grade_info = line[
            1
        ].split()
        weights = []
        grades = []
        for idx, item in enumerate(grade_info):
            if idx % 2 == 0:
                weights.append(int(item))
            else:
                grades.append(int(item))
        if check_weights(
                weights
        ):
            w_average = equation(weights, grades)
            results[name] = w_average
            overall_grades.append(
                w_average
            )
        else:
            results[name] = "Error: Weights did not equal 100."
    results["Overall Avg."] = sum(overall_grades) / len(overall_grades)
    print(results)
    save_file(outfile_name, results)


def main():
    weighted_average("test_file", "out_file")


if __name__ == "__main__":
    main()