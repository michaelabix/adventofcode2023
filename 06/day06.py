import logging


def read_file(file_path: str) -> list:
    """lazy parsing"""
    file_object = open(file_path, "r", encoding="UTF=8").read().splitlines()
    return file_object


def parse_race(paper: list) -> tuple:
    """parse race card"""
    time = paper[0].split()
    distance = paper[1].split()
    return time[1:], distance[1:]


def part1(time: list, distance: list) -> int:
    """calculate record beating solutions"""
    race_records = []
    result = 1
    for i, t in enumerate(time):
        solutions = 0
        for r in range(1, int(t) - 1):
            d = (int(t) - r) * r
            if d > int(distance[i]):
                solutions += 1
        race_records.append(solutions)
    for r in race_records:
        result = result * int(r)
    return result


#this is inefficient but works
def part2(time: list, distance: list) -> int:
    """one big race"""
    new_time = []
    new_distance = []
    new_time.append(''.join(time))
    new_distance.append(''.join(distance))
    result = part1(new_time, new_distance)
    return result


def main():
    #logging.basicConfig(level=logging.DEBUG)
    input = read_file("input")
    time, distance = parse_race(input)
    print('the answer to part 1 is ' + str(part1(time, distance)))
    print('the answer to part 2 is ' + str(part2(time, distance)))


if __name__ == "__main__":
    main()