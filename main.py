limits = {"red": 12, "green": 13, "blue": 14}

with open("inputday2part1", "r") as inputval:
    content = inputval.read()

def game_reader(text: str) -> dict[str, int]:
    values = {}
    for part in text.split(","):
        count, color = part.split()
        values[color] = int(count)
    return values

def main():
    print("Hello from aoc23-2!")


if __name__ == "__main__":
    main()
