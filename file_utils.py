
def read_lines(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        data = file.readlines()

    return data


def write_lines(filename: str, lines: list[str]) -> None:
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
    


def count_words(filename: str) -> dict[str, int]:
    word_count: dict[str, int] = {}

    with open(filename, "r") as f:
        for line in f:
            words = line.strip().split()

            for word in words:
                word = word.lower()
                word_count[word] = word_count.get(word, 0) + 1

    return word_count
