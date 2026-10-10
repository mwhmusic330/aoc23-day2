limits = {"red": 12, "green": 13, "blue": 14}

with open("inputday2part1", "r") as inputval:
    content = inputval.read()
    lines = content.splitlines()

def parse_numbers(text: str) -> dict[str, int]:
    values = {}
    for part in text.split(","):
        count, color = part.split()
        values[color] = int(count)
    return values
def parse_game(line: str) -> tuple[int, list[dict[str, int]]]:
    head, rest = line.split(":",1)
    game_id = int(head.split()[-1])
    numbers = [parse_numbers(r) for r in rest.split(";")]
    return game_id, numbers

def main():
    print("Hello from aoc23-2!")


if __name__ == "__main__":
    main()
