import sys

def remove_extra_spaces(s):
    words = s.split()
    return " ".join(words)


def main():
    s = sys.stdin.read()
    result = remove_extra_spaces(s)
    print(result)


if __name__ == "__main__":
    main()
    