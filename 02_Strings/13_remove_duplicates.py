import sys

def find_duplicates(s):
    freq = {}
    result = []

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in freq:
        if freq[ch] > 1:
            result.append(ch)

    return result


def main():
    s = sys.stdin.read().strip()
    duplicates = find_duplicates(s)

    for ch in duplicates:
        print(ch, end=" ")


if __name__ == "__main__":
    main()