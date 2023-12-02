import logging


def read_file(file_path: str) -> list:
    """lazy parsing"""
    file_object = open(file_path, "r", encoding="UTF=8").read().splitlines()
    return file_object


def parse(game: list) -> tuple:
    """separate out the game details"""
    game_title, game_turns = game.split(':')
    game_num = int(game_title.split()[1])
    logging.debug("game number is" + str(game_num))
    temp_turns = game_turns.split(';')
    turns = []
    for t in temp_turns:
        dice = t.split(',')
        colors = {}
        for d in dice:
            num = "".join([char for char in d if char.isnumeric()])
            color = "".join([char for char in d if char.isalpha()])
            colors.update({color: int(num)})
            logging.debug(colors)
        turns.append(colors)
        logging.debug(turns)
    logging.debug(turns)
    return game_num, turns


def part1(games: list) -> int:
    """find out which games are valid"""
    bag = {'red': 12, 'green': 13, 'blue': 14}
    possible = []
    for game in games:
        impossible = 0
        parsed_game = parse(game)
        for turn in parsed_game[1]:
            for key in turn.keys():
                if turn[key] > bag[key]:
                    impossible = 1
        if not impossible:
            possible.append(parsed_game[0])
            logging.debug("possible is: ")
            logging.debug(possible)
    return sum(possible)


def part2(games: list) -> int:
    """find power of the cubes"""
    power = []
    for game in games:
        parsed_game = parse(game)
        highest = {'red': 0, 'green': 0, 'blue': 0}
        for turn in parsed_game[1]:
            for key in turn.keys():
                if turn[key] > highest[key]:
                    highest[key] = turn[key]
        power.append(highest['red'] * highest['green'] * highest['blue'])
    return sum(power)


def main():
    input = read_file("input")
    print('the answer to part 1 is ' + str(part1(input)))
    print('the answer to part 2 is ' + str(part2(input)))


if __name__ == "__main__":
    main()