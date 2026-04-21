import sys

def count_frequency(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return freq


def main():
    s = sys.stdin.read().strip()
    freq = count_frequency(s)

    for ch in freq:
        print(ch, freq[ch])


if __name__ == "__main__":
    main()