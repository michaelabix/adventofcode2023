import logging


def read_file(file_path: str) -> list:
    """lazy parsing"""
    file_object = open(file_path, "r", encoding="UTF=8").read().splitlines()
    return file_object


def part1(calibration_values: list) -> int:
    """find calibration values"""
    total = 0
    for c in calibration_values:
        digits = []
        for i in c:
            if i.isdigit():
                digits.append(i)
        if len(digits) > 1:
            try:
                total += int(digits[0] + digits[-1])
            except ValueError:
                logging.error("digits not converted")
        elif len(digits) == 1:
            try:
                total += int(digits[0] + digits[0])
            except ValueError:
                logging.error("digits not converted")
        else:
            logging.error("SOMETHING IS VERY WRONG")
    return total


def part2(values: list) -> int:
    """find calibration values the harder way"""
    total = 0
    words = {'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9}
    for v in values:
        digits = {}
        for i, j in enumerate(v):
            if j.isdigit():
                digits.update({int(i):int(j)})
        for k in words.keys():
            first_index = v.find(k)
            last_index = v.rfind(k)
            if first_index == -1:
                continue
            elif first_index == last_index:
                digits.update({first_index:words[k]})
            else:
                digits.update({first_index:words[k]})
                digits.update({last_index:words[k]})
        index_list = sorted(digits.keys())
        total += int((str(digits[index_list[0]]) + str(digits[index_list[-1]])))
    return total


def main():
    input = read_file("input")
    print('the answer to part 1 is ' + str(part1(input)))
    print('the answer to part 2 is ' + str(part2(input)))


if __name__ == "__main__":
    main()